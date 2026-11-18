# Dr. Azren DoodleVerse: Reference Analysis & Visual Identity (V2)

**Date:** 2026-11-18. This replaces `02_reference_creative_audit.md` as the style reference. That file analysed an older, monochrome cut (`Panic_Disorder_Ep1_DrAzrin.mp4`); the new reference is a different, much richer video.

## 0. What was actually inspected

| Asset | Drive ID | How | Verified |
|---|---|---|---|
| `Panic_Disorder_Ep1_DrAzren_lipsync.mp4` | `1PXLtFf6Dy2RUNjNCUZ-AlCmVVGos2gdW` | Downloaded via its existing link (no sharing change). 77,472,259 bytes, matching Drive's size. | ✅ ffprobe, scene-cut detection, EBU R128 loudness, 90 frames at 1 fps (3 contact sheets), 12 full-res frames, mouth crops |
| `hf_20261116_091255_90b7f4c1-….png` (poster) | `1PLyCyaLng3kpQWovsc2Qm8vXUkbJF7AR` | Same; 6,024,624 bytes, 1520 × 2688 | ✅ Full-res inspection, colour sampling, sprite extraction |

**Not inspected:** the soundtrack and narration *by ear*. I can't listen to audio. Narration content is rebuilt from the burned-in captions, and music balance comes from loudness measurements only.

## 1. Technical specs (measured)

| Property | Value | Note |
|---|---|---|
| Duration | 90.0 s | At the absolute cap |
| Resolution | 1080 × 1920 | ✅ |
| Frame rate | 24 fps | Keep 24 fps for DoodleVerse, as you asked (hand-drawn motion reads naturally at 24) |
| Video | H.264, 6.7 Mb/s | ✅ |
| Audio | AAC 48 kHz stereo, 195 kb/s | ✅ |
| Integrated loudness | **−9.1 LUFS** | ~5 LU louder than the −14 LUFS social target |
| True peak | **+0.4 dBTP** | **Clipping.** Target ≤ −1 dBTP |
| Loudness range | 3.2 LU | Heavily compressed |
| Hard cuts | 9 (at 10.2, 16.6, 19.8, 28.7, 39.2, 48.7, 57.9, 68.4, 77.2 s) | 10 shots, ~9 s each. In-shot motion (lip-sync, slow push, reveals) carries the pacing between cuts |

## 2. The look: what makes it "DoodleVerse"

Observed in every frame of the reference and the poster:

1. **Alcohol-marker illustration, not vector.** Thick black outlines (~6–10 px at 1080 w) with slight wobble. Fills are **hatched marker strokes**: diagonal strokes ~35–40°, darker strokes for shadow, and white "gel pen" highlight strokes on hair, glasses, heart and bell.
2. **Rich, saturated multi-colour palette**, unlike the old monochrome-teal cut. Sampled values:

| Element | Hex (sampled) | Use |
|---|---|---|
| Ink outline | `#17161A` | All outlines |
| Board | `#F7F6F2` → `#E7E6E2` edges, soft ceiling-light reflections | Every scene |
| Dr. Azren scrubs | `#2FB3A1` (poster), `#3A9C8F` (video, hatched) | Doctor only |
| Doctor skin | `#FCCDA3` | |
| Patient hijab | pink/mauve, `#E58FA6` (poster) → `#C98A95` (video) | |
| Patient blouse | mustard `#FDBC17` | |
| Patient trousers | navy `#3E4962` | |
| Patient skin | **`#EFA36C` (poster) vs `#B0744E` (video)** | ⚠️ inconsistent, see §6 |
| Brain | pink `#F08CB4` with lavender shadow `#9B6BC8` | |
| Alarm bell | red `#E2382F` | |
| Doodle accents | yellow `#FFD43B`, cyan `#3CC4E6`, coral `#FF6B5E`, purple `#8F6CF0`, orange `#FF9F2E` | Sparkles, stars, motion lines |

3. **Offset colour outlines on titles.** The poster headline "PANIC DISORDER" is black marker with a cyan offset left and a yellow offset right/below.
4. **Doodle confetti around the subject**: 4-point sparkles (yellow), 5-point stars (coral, purple), motion arcs (cyan, purple, yellow), dots, zig-zag "shock" lines, lightning bolts.
5. **Semantic props**: heart + ECG, brain + bell, crossed-out fire, stopwatch, calendar with red Xs, shield bubble around a heart, sun over hills, calm smiling bell.
6. **Captions** (burned in): one line of 3–5 words, white bold sans (Poppins-like) with a dark outline, sitting on a **solid coloured bar** that rotates teal → coral → purple → blue. One **keyword in yellow** (sometimes another colour). Bar centre is at y ≈ 1,560, inside the zone TikTok/Reels/Shorts cover with UI, so **V2 moves it up** (see design rules).
7. **Framing**: medium shots and big close-ups. Faces often fill 40–60 % of frame width. Two-shots: the doctor explains, the patient reacts. Cut-ins: brain, heart bubble, breathing timers.

## 3. Characters (the canon to keep stable)

**Dr. Azren (mascot):** young Malaysian man; messy black hair with blue/yellow highlight strokes; round black glasses; big brown eyes; rosy cheeks; teal V-neck scrubs with chest pocket and pocket sparkle; black stethoscope with red-ringed diaphragm; **black smartwatch on left wrist**; dark teal trousers; white sneakers. Poses seen: entering/walking, open-palm explaining, pointing up (poster), hand on chest, holding a marker, seated at table, waving.

**Patient (pink hijab):** young Malaysian woman; pink/mauve hijab; mustard long-sleeve button blouse; navy trousers; white flats; expressive brows. Expressions seen: frightened (hand on chest, sweat drop, tear), anxious, eyes closed (sofa), calm breathing (eyes closed), listening, relieved smile.

**Separation of roles is already right** in this reference: the doctor explains and the patient experiences. Keep it.

## 4. Motion & editing observed

- Lip-sync on whoever speaks (AI lip-sync: mouth shapes closed/smile/teeth/round/wide clearly visible frame to frame).
- Slow push-ins and drifts within shots. Brain, heart and bell "breathe" or vibrate. Calendar Xs appear one by one. A breath stream flows. A pie timer fills.
- Hard cuts between shots; no draw-on reveals in this cut (they were in the older one).
- Small artefacts: a frame at ~68–77 s shows a black floor band (letterbox-like), and hands vary in size between shots.

## 5. Strengths to keep / weaknesses to fix

| Keep | Fix in V2 |
|---|---|
| Rich hatched-marker illustration and multi-colour doodle confetti | Loudness (−9.1 LUFS, +0.4 dBTP clipping) → −14 LUFS, ≤ −1 dBTP |
| Two-character storytelling (doctor + patient) | Caption bar in the UI zone (y ≈ 1,560) → caption lane centred at y ≈ 1,440, and never below 1,520 |
| Coloured caption bars with a yellow keyword | Shots of ~9–10 s → a new visual beat every 2–4 s via local motion (reveals, props, push-ins) |
| Big expressive faces, readable at phone size | Character drift between AI shots → one locked sprite set, so the same drawing appears every time |
| Semantic props (brain, heart, bell) | Floor-band artefact and inconsistent hand sizes → no per-shot AI video |
| Poster-style title with cyan/yellow offsets | Patient skin tone differs between poster and video → lock one (your decision, §6) |

## 6. Decisions for you

1. **Patient skin tone**: the poster's tan (`#EFA36C`) or the video's deeper brown (`#B0744E`)? Video-frame sprites keep the deeper tone and poster sprites keep the tan. A light colour-match can unify them at no cost, but I'd rather you pick the canon.
2. **Caption position**: I recommend moving it up out of the platform UI zone (above). Say if you'd rather keep the reference's lower position.
