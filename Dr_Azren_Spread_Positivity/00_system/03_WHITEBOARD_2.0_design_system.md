# DR. AZREN WHITEBOARD 2.0 — Design System v1.0

The reusable look, sound and motion rules for every **Dr. Azren | Spread Positivity** episode.
Engine: **HyperFrames** (HTML + SVG + GSAP rendered locally to MP4). AI video (Higgsfield) only for up to two framed inset shots per episode.

---

## 1. Canvas, frame rate and safe zones

| Item | Spec |
|---|---|
| Canvas | 1080 × 1920 (9:16) |
| Frame rate | 30 fps (the reference was 24) |
| Duration | 60–90 s; the narration sets the clock |
| Export | H.264 MP4 (yuv420p, High profile), AAC 48 kHz 192 kb/s |
| **No-text zone (top)** | y 0–168 px (status bar and search) |
| **Content band** | y 168–1,330 px: every word, diagram and face |
| **Caption lane** | Centre of the caption block at y ≈ 1,180 px, maximum 2 lines, never below 1,300 px |
| **Platform UI zone (bottom)** | y > 1,330 px: texture and decoration only, never text |
| **Right action rail** | x > 950 px between y 900–1,700: no text |
| Side margins | 64 px minimum for text |
| Thumbnail crop-safe | Central 1080 × 1350 box (y 285–1,635) for key elements, since grid previews crop to 4:5/3:4 |

## 2. Colour: semantic, never decorative

| Token | Hex | Meaning (the only allowed use) |
|---|---|---|
| `--ink` | `#16181D` | Hand-drawn outlines (near-black marker) |
| `--navy` | `#142B49` | Typography, captions, UI chrome, brand lockup |
| `--teal` | `#12B8A6` | **Dr. Azren, help, calm, treatment, "safe"**. The scrubs colour |
| `--sky` | `#42A5F5` | **The body**: breath, blood flow, lungs, physiology |
| `--coral` | `#FF6D6D` | **Alarm, danger, symptom, red flag** |
| `--yellow` | `#FFC857` | **Attention**: keyword highlighter, numbers, tips |
| `--lavender` | `#A78BFA` | **The mind**: brain, thoughts, emotions, worry |
| `--board` | `#F9FAFB` | Whiteboard surface |
| `--board-shadow` | `#E6E9EE` | Ghosted marker residue, board texture |

Rules:
1. **One meaning per colour across all episodes.** Coral is never used for a "good" thing, and teal never for danger.
2. At most **3 accent colours in one frame** (ink, navy and board don't count).
3. **Progressive colour:** an object is drawn as ink line first (stroke-dashoffset). Its marker fill wipes in 6–10 frames after the line closes, using a scribble-hatch SVG pattern, not a flat fill.
4. A scene's emotional temperature is set by the dominant accent. Symptom scenes lean coral; resolution scenes lean teal and sky.
5. **Contrast (measured, WCAG):** `--navy` on `--board` = 13.66:1 and `--navy` on `--yellow` = 9.28:1, both pass. **The fill accents fail as text on the board**: coral 2.62, teal 2.38, white-on-teal 2.49. So **text never uses the fill accents.** It uses these text-safe variants:

| Text token | Hex | On board | Use |
|---|---|---|---|
| `--coral-text` | `#C8323A` | 5.06:1 | Danger/symptom words |
| `--teal-text` | `#0B7468` | 5.41:1 | Help/calm words |
| `--sky-text` | `#1F63C2` | 5.55:1 | Body/physiology labels |
| `--lavender-text` | `#6D4FD8` | 5.34:1 | Mind/brain labels |

   On a teal card, text is `--navy` (5.73:1), never white. A word on a yellow marker swipe stays `--navy`, because coloured text on yellow drops to about 3.4:1.

## 3. Line, texture and the board

- **Board:** warm-white `--board` with procedural SVG paper noise (seeded) and 2–3 faint ghost smudges. No photographic aluminium frame in normal scenes. A thin rounded navy frame (16 px radius) appears only in the hook and outro as a brand device.
- **Ink:** 6–8 px strokes for characters and 4–5 px for icons, round caps, slight width variation.
- **Line boil:** outlines are re-jittered 12 times a second with a seed of `Math.floor(t*12)`. That keeps the hand-drawn life without any randomness between renders.
- **The marker hand:** the brand's signature reveal. An original illustrated hand and marker (vector, not photoreal) draws key objects. Used **at most 3× per episode** and **never at frame 0**.

## 4. Characters

### 4.1 Dr. Azren (narrator mascot), consistent by construction
- **Design source:** the existing mascot from earlier episodes. Reference stills are in `mascot_reference/`: messy black hair, round glasses, teal V-neck scrubs, stethoscope around the neck, black smartwatch on the left wrist, white sneakers, friendly young face.
- **Production form:** a **layered SVG rig**, not per-shot AI generation. The same drawing every frame, so no face drift.
  - Layers: head, hair, glasses, eyes, brows, mouth, neck, torso (scrubs + pocket), stethoscope, left arm, right arm, hands, watch, legs, shoes.
  - **Eye states:** `open`, `wide`, `smile-closed`, `worried`, `blink`
  - **Brow states:** `neutral`, `raised`, `worried`, `focused`, `soft`
  - **Mouth states:** `neutral`, `smile`, `talk-A`, `talk-O`, `talk-M`, `worried`, `surprised-O`
  - **Arm poses:** `rest`, `point-up`, `point-side`, `hand-on-chin` (thinking), `open-palms`, `wave`, `thumbs-up`, `hold-clipboard`
  - **Talk:** the mouth is driven by the voiceover's loudness envelope, computed offline into JSON (deterministic and free).
  - **Acting:** every mood change goes anticipation → squash → new face → settle (6–10 frames). Head leads and arms follow. Idle breath and a blink every 2.5–4 s.
- **Mood map** (from the brief): surprised during symptoms, thoughtful for questions, calm for treatment, encouraging at the conclusion, serious and calm (never alarmed) for red flags.
- **Approval gate:** before the rig is final, one **character sheet** (front, ¾, side, 6 expressions) is generated from the reference stills for Dr. Azren to approve. Cost and model are in `04_cost_model.md`. The approved sheet becomes the permanent master.

### 4.2 "Kawan" (the viewer's stand-in)
- An everyday Malaysian adult who *experiences* the topic, so the doctor is never shown as the patient.
- Neutral casual clothes (sky-blue or lavender top); simple, warm, not caricatured.
- Variants across episodes for diversity: male, female, female in a tudung, older adult. One variant per episode, chosen by topic.
- Built as a lighter SVG rig: fewer mouth states, since Kawan rarely "speaks".

## 5. Typography

| Use | Font | Size (1080 w) | Style |
|---|---|---|---|
| Kinetic headline | **Poppins 900** | 110–150 px, ≤ 3 words/line | Uppercase, `--navy` or `--coral-text`, slam/scale-in |
| Section title | Poppins 800 | 72–90 px | Uppercase, yellow highlighter swipe behind |
| Captions | **Poppins 700** | 64–72 px (auto-fit, minimum 52) | Sentence case, `--navy`, keyword in `--coral`/`--teal` with a yellow marker swipe |
| Diagram labels | **Nunito 800** | 40–52 px | Sit on the part they name, with a leader line |
| Source/footnote | Inter 400 | 28–30 px | `--navy` at 70% opacity, inside the content band |

Poppins, Nunito and Inter are bundled with HyperFrames (Latin text). Malay needs no extra glyphs.
Spelling: Bahasa Melayu (DBP) standard spelling in captions, even when the narration uses spoken contractions. For example, the narrator says "tak" and the caption shows "tak": casual spelling is accepted on social, but **no Indonesian spellings** ("tidak apa-apa" not "enggak", "anda" not "kamu").

## 6. Motion language

| Element | Motion | Timing |
|---|---|---|
| Entrance (cards, icons) | `power3.out` from scale 0.85 + 30 px rise | 0.35–0.45 s |
| Pop (badges, numbers, checkmarks) | `back.out(1.7)` from scale 0 | 0.25 s |
| Kinetic slam | Scale 1.25 → 1, 2-frame white flash on the word | 0.18 s |
| Line draw | `stroke-dashoffset`, `power1.inOut` | 0.4–1.2 s by length |
| Colour fill | Hatch-pattern wipe along the main axis | 0.25–0.35 s |
| Camera push-in (within a beat) | Scale 1.00 → 1.06 | Over the whole beat, `sine.inOut` |
| Punch-in (emphasis word) | 1.0 → 1.12 in 4 frames, hold | On the anchor word |
| Scene transition A | **Zoom-through-icon** (an object becomes the next scene's window) | 0.5 s |
| Scene transition B | **Push** (whole board slides, next board in) | 0.4 s |
| Scene transition C | **Marker wipe** (thick teal stroke sweeps and reveals) | 0.45 s |
| Idle (characters) | Breath 1.5% scale-Y over 3 s, offset blink | Continuous |

- **A new visual beat every 2–4 s**: a growth step, label, punch-in, character reaction or cut. No holds over 4 s without change.
- **One diagram that grows**: start from the simplest true picture and add one part when the narrator names it. Never drop a finished diagram on screen.
- **Banned:** spinning text, bounce loops on titles, rainbow gradients, emoji as icons, three cards in a row, bullet-point slides, the same transition twice in a row.

## 7. Sound identity

- **Brand music bed:** one original instrumental. Upbeat educational light electronic pop, about 112 BPM, warm synths, soft plucked 4-note motif, soft percussion, no vocals. Generated once, approved once, **reused every episode** (cost in `04_cost_model.md`). Each episode can re-cut it; there is no new generation per episode.
- **Mix (per episode):**
  - 0–1.5 s: music at full energy (the hook), then ducks to about −20 dB under the voice (volume ≈ 0.12–0.14).
  - Accents: +3–6 dB swells on scene transitions, a short riser into the episode's one key reveal.
  - Outro: music returns to about −8 dB under the sign-off, ends on a bar line with the motif.
  - Master: **−14 LUFS integrated, true peak ≤ −1 dBTP**. Voice peaks at about −6 dBFS before the master.
- **SFX palette** (a cause on screen for every sound; 2–3 rotated takes):

| Sound | Only on | Source |
|---|---|---|
| Marker squeak/draw | Signature marker-hand draws | To source (ElevenLabs SFX or CC0) |
| Soft whoosh | Scene push / zoom-through | Bundled (Pixabay licence) |
| Pop | Badge, number, checkmark landing | Bundled |
| Light heartbeat | Heart/ECG on screen | To source |
| Sparkle | Treatment/hope reveal (≤ 1×) | Bundled |
| Click-soft | UI card toggles | Bundled |
| Notification | Phone/message shown | Bundled |
| Soft impact | Red-flag overlay landing | Bundled (`impact-bass`) |
| Riser | Into the single key reveal | Bundled |

The bundled HyperFrames SFX are under the Pixabay Content License: commercial use, no attribution required.

## 8. Captions

- Word timings come from the **final ElevenLabs narration** (forced alignment by local transcription with `--model small --language ms`, then corrected word-by-word against the approved script). They are never estimated from script length.
- Groups of 3–5 words; break at sentence ends, pauses ≥ 150 ms, or the word limit. One group visible at a time.
- Style: Poppins 700, `--navy`, sentence case, centre of the caption block at y ≈ 1,180. At most one keyword per group, emphasised **either** in `--coral-text`/`--teal-text` (no swipe) **or** in `--navy` on a yellow marker swipe. Never coloured text on yellow (contrast, §2).
- A group fades in over 0.12 s with a 12 px rise and hard-kills after its last word.
- Captions never cover a face or the active diagram part. If they would, the diagram sits higher or the caption lifts.
- An SRT is exported from the same word-timing JSON.

## 9. Reusable component library (HyperFrames)

| # | Component | Variables |
|---|---|---|
| 1 | `whiteboard-bg` | Seed, smudge count, frame on/off |
| 2 | `doctor-rig` | Pose/expression keyframes, talk envelope JSON |
| 3 | `kawan-rig` | Variant, pose/expression keyframes |
| 4 | `draw-reveal` | SVG path set, marker-hand on/off, fill colour |
| 5 | `icon-morph` | From-icon, to-icon |
| 6 | `symptom-checklist` | Items (≤ 4), timings, colour |
| 7 | `kinetic-text` | Words, colour, style (slam/type/highlight) |
| 8 | `keyword-highlight` | Word, colour |
| 9 | `myth-vs-fact` | Myth text, fact text |
| 10 | `timeline-curve` | Points, labels, "illustrative" tag |
| 11 | `red-flag-overlay` | Items, action line ("Hubungi 999") |
| 12 | `caption-track` | Word JSON, group size, keyword list |
| 13 | `stat-pictogram` | N of M icons, label, source footnote |
| 14 | `body-map` | Organs on/off, labels, pulse rates |
| 15 | `brand-outro` | CTA icons, lockup draw-on, motif sting |
| 16 | `ai-inset-card` | Video src, drawn frame, caption |

The episode files only set variables and timings; the components are shared.

## 10. Branding

- **0–3 s:** no logo and no name. Just the problem.
- **From about 4 s:** a small corner bug, top-left at y ≈ 190: a teal stethoscope glyph + "Dr. Azren" in Poppins 700, 34 px, 80% opacity.
- **Outro (last 5–8 s):** Dr. Azren waves, Save and Share icons pop, and the lockup **"Dr. Azren | Spread Positivity"** draws on, ending on the 4-note music motif.
- Disclaimer card (in the description, plus one 1.5 s on-screen line in the outro): *"Untuk pendidikan sahaja, bukan pengganti nasihat doktor."*

## 11. Thumbnail / cover

- 1080 × 1920 PNG, with the key elements inside the central 1080 × 1350 crop box.
- Dr. Azren (rig, strong expression) plus one central medical visual plus a 3–6 word headline in Poppins 900 (≤ 2 lines, 120–150 px), with high contrast against `--board`. The red-flag colour is used only if the topic is about danger.
- Built as a HyperFrames still composition (`data-no-timeline`), so it stays editable.

## 12. Higgsfield usage rules

- Maximum two clips, about 5 s each, per episode, only where SVG would be slow or unconvincing: organic motion, an animal, a character acting.
- **The start frame is our own rendered HyperFrames frame** (free). The AI only animates our drawing, which keeps style and character consistent.
- Always shown **inside an `ai-inset-card`** (a drawn frame on the board), never full-bleed, so a 720p source is never upscaled 1.5× to full screen.
- No AI-generated text inside clips; all text is HyperFrames.
- If a clip fails QA (face drift, hand artefacts, wrong anatomy), **replace it with the native SVG fallback**. Do not regenerate without a written reason.
