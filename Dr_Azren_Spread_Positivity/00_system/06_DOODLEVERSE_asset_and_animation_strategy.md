# DoodleVerse: Reusable Assets & Zero-Higgsfield Animation Strategy (V2)

**Goal:** match the reference's rich hatched-marker look while making almost all motion locally in HyperFrames (HTML + SVG + CSS/GSAP rendered by local Chrome + FFmpeg). **Default Higgsfield spend: 0.** Hard caps: **10 credits per generation, 10 credits per episode in total**, each paid call quoted live and approved first.

---

## 1. The core idea: "cut, don't generate"

The reference poster and video are **your own approved art**. They already contain the exact characters, palette and props. Instead of asking an AI to redraw them every episode (cost, drift), we:

1. **Cut** each character pose and prop out of the reference into a transparent PNG sprite (`tools/cutout.py`: border flood-fill of board-coloured pixels, so the black marker outlines act as the cut line). ✅ Tested; see §3.
2. **Layer** sprites on the shared whiteboard background, with locally drawn **SVG marker doodles** (wobble filter + hatch patterns) for everything simple: sparkles, stars, arrows, clouds, drops, icons, ECG, breathing circles.
3. **Animate** with HyperFrames: reveals, gestures, camera, lip-sync, captions.
4. **Re-colour / re-mood** without new art: CSS filters (grayscale for the depression "colour drain", hue for props), masks, and overlay doodles.

Only if a needed pose truly doesn't exist do we consider one Higgsfield image (≤ 2.75 credits, quoted live), and it then becomes a permanent library asset.

## 2. Technique map (brief §4 → how it's built, cost 0)

| Required technique | Local implementation |
|---|---|
| Marker draw-on reveal | SVG doodles: `stroke-dashoffset` animation along each path. Raster sprites: an animated SVG **mask** of thick scribble strokes that "draws" the sprite in (8–14 frames), plus marker-scratch SFX |
| Scribble fill | Hatch-pattern layer revealed by an animated mask after the outline. Colour-drain/return: animate `filter: grayscale()` with a scribble-shaped mask sweeping across |
| 2D character rigging | Sprites split into layers where the art allows: body, head, forearm (for gestures), mouth patch, eyelid patch. Head = small rotation about the neck pivot; arms = rotation about the shoulder. Pose changes = cut to another sprite of the same character on a beat (hidden by a swoosh/sparkle) |
| Budget lip-sync | **Mouth atlas harvested from your lipsync video** (verified: clear closed / small-open / teeth / rounded / wide-open shapes exist for the doctor). Patches are aligned to each face sprite and swapped by an amplitude + phoneme-class track from the narration (vowels a/e → wide, o/u → round, m/b/p → closed, pauses → closed-smile). Fallback: SVG mouth shapes drawn in the same marker style |
| Blinking | Eyelid patch (skin-coloured, outlined) over the eyes for 3 frames every 2.5–5 s (randomised, seeded) |
| Eyebrows / micro-expressions | Small brow patches nudged ±4 px; head tilt ±2°; breathing = 1.5 % scale on the torso every ~3.5 s |
| Medical metaphors | SVG props with looping motion: cloud drizzle, battery level drop, ECG line scroll, heart pulse, breathing circle (expand 4 s / contract 6 s), thought bubbles popping, arrows drawing |
| Camera | One GSAP-driven `transform` on the stage: push-in 3–6 %, gentle pans, reframes between beats, light parallax (background 0.5×, props 1×, foreground doodles 1.2×). Max zoom speed ≈ 4 %/s to avoid motion sickness |
| Transitions | Marker swipe (a thick scribble mask wiping across), sparkle burst cover, whip-pan with motion lines. All local |
| Captions | Native HTML text, word timings from the narration; the reference's coloured-bar style, a yellow keyword, a 120 ms pop-in |

## 3. Proof of concept (done, 0 credits)

- `tools/cutout.py` produced clean sprites from the poster and video frames: Dr. Azren pointing bust, Dr. Azren ¾ explaining, patient worried bust, patient walking away, sofa scene, table consult, table relieved, heart-ECG.
- `Dr_Azren_DoodleVerse_Assets/templates/style_test_ep002_scene01.html` is an Ep002 Scene 1 style frame: cut-out patient + SVG marker doodles + marker headline with cyan/yellow offsets + coloured caption bar. Rendered locally to `Episode_002_Kemurungan_Major/style_test_scene01.png`.
- **Known limits of cut-outs** (handled per scene): a few contain neighbouring bits of the original frame (e.g. the doctor's hand in the walk-away pose, the panic bell above the table scene). These are masked or covered by props. Characters cut from video frames are 1080-px-wide sources, so the largest close-ups should prefer the poster (1520 px) or stay ≤ 1.3× scale.

## 4. Library: `Dr_Azren_DoodleVerse_Assets/`

```
characters/dr_azren/        sprites per pose (+ mouth/eyelid patches, later)
characters/patient_hijab/   sprites per pose/emotion
characters/male_patient/    (future) second patient character, after approval
props/                      raster props cut from your art (heart-ECG, …)
props_svg/                  marker-style SVG props drawn locally (cloud, drops, battery, …)
scenes/                     multi-character set-ups (sofa, table)
templates/                  doodleverse.css (board, headline, captions), style tests, caption templates
fonts/                      Permanent Marker (Apache 2.0), Poppins 700–900 (OFL), Patrick Hand (OFL)
audio/music/                brand beds A + B (ElevenLabs Music, Ep1; reused, 0 new cost)
audio/sfx/                  Pixabay-licensed SFX (HyperFrames bundle)
source_reference/           provenance notes for every source frame used
```
Each sprite's source (file, time code / crop box) is recorded in `Dr_Azren_DoodleVerse_Assets/README.md`, so any asset can be rebuilt.

### Character inventory vs. what the brief asks for

| Dr. Azren pose (brief) | Available from your art? | Source |
|---|---|---|
| Neutral / explaining | ✅ | video 9 s (¾ body, open palm) |
| Pointing | ✅ | poster (bust, finger up, holding marker) |
| Thinking | ⚠️ partial | concerned face at 40–47 s; no true "hand on chin" pose exists |
| Reassuring | ✅ | video 80–88 s (seated, open hand), waving 86–88 s |
| Surprised | ✅ | video 79–80 s ("o" mouth) |
| Serious clinical | ✅ | video 40–47 s |
| Walking entrance | ✅ | video 4–6 s (stride) |

| Patient emotion (brief) | Available? | Source |
|---|---|---|
| Anxious / frightened | ✅ | poster; video 0–3 s, 12–16 s |
| Confused | ⚠️ partial | video 49–52 s (unsure look at the heart bubble) |
| Listening | ✅ | video 76–82 s (table) |
| Calming down | ✅ | video 58–71 s (eyes closed, breathing) |
| Relieved | ✅ | video 84–88 s |
| **Sad / low / withdrawn (needed for depression)** | ⚠️ **partial** | walking away head down (46 s); sofa eyes closed (12 s); worried face + grey "colour drain" treatment |

**Gap for Ep002:** a genuinely *sad/flat* (not frightened) patient expression and a "lying in bed / curled up" pose. Two routes:
- **Route A (0 credits, default):** use the closest existing poses + colour-drain + grey cloud + drooped-brow overlay patch. Lower expressiveness, zero cost.
- **Route B (optional, 2.75 credits, needs your approval):** one `gpt_image_2_6` high/2K image of a pose sheet of the same patient (sad, tired in bed, hugging knees, small smile) using the poster as the reference image. It becomes a permanent library asset for every future mood/sleep/grief episode.

**New male character (brief §3, future episodes):** optional `gpt_image_2_6` character sheet, 2.75 credits, one-time. Not needed for Ep002, so I'd defer it until an episode needs it.

## 5. Cost rules V2 (replace §3–4 of `04_cost_model.md` where they differ)

| Rule | V1 (Ep001) | **V2 (from Ep002)** |
|---|---|---|
| Higgsfield per episode | ≤ 25 (2 video clips) | **0 by default; ≤ 10 total, hard cap** |
| Higgsfield per generation | — | **≤ 10**; anything priced above → rejected, built locally |
| Higgsfield video clips | 2 per episode | **None.** No AI video for anything in the brief's "do not use" list |
| Unknown price | — | Never generate |
| Retries/variations | Approval needed | **None** without a fresh quote and approval |
| Splitting a costly shot into cheap ones to dodge caps | — | **Forbidden** |
| ElevenLabs narration | 1 take, ≤ 1,500 | 1 take, `generations_count = 1`, script locked + clinically approved first |
| Music | One-time beds | **Reuse beds A/B**; no new music without approval |
