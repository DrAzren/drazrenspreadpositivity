# Episode 002: Quality Assurance Report

**File:** `09_final_video_1080x1920.mp4` (64.6 MB; git-ignored, delivered to you directly; copy it to Drive)
**Date:** 2026-11-18 · **Tooling:** `tools/qa_video.py --fps 24`, `hyperframes check`, snapshot + frame review

## Technical QA (measured) ✅

| Check | Result |
|---|---|
| Resolution / aspect | 1080 × 1920, 9:16 ✅ |
| Frame rate | 24 fps ✅ (as briefed; matches the reference) |
| Codecs | H.264 yuv420p + AAC 48 kHz 192 kb/s, `faststart` ✅ |
| Duration | **85.4 s** (target 75–85, cap 90) ✅ |
| Integrated loudness | **−14.1 LUFS** ✅ (raw render −13.8, two-pass linear loudnorm, video stream copied) |
| True peak | **−1.37 dBTP** ✅ (the reference was +0.4 dBTP, clipping) |
| Segments | Hook 0–3 s −12.4 · explanation −13.5/−14.4 · red-flag scene −13.9 · music-only outro −18.5 LUFS |
| Music vs voice | Bed at ×0.20 under the voice (≈10 LU below), ×0.11 in the red-flag scene, opening bars reused as the outro sting |
| Black frames / freezes ≥ 4 s | None ✅ |
| Watermarks / black borders | None ✅ |
| `hyperframes check` | **0 errors** in lint, runtime, layout, motion, contrast, craft, audio |

### Accepted warnings (reviewed)
- **Safe-zone (layout):** the checker's TikTok box is stricter than HyperFrames' own vertical guideline. All text sits inside y 168–1,330 and clear of the right action rail (x > 950 for y 900–1,700). Captions sit at y 1,238–1,323, above the platform caption/handle area.
- **Contrast (5):** yellow keywords on teal/blue caption bars measure 2.0–2.2:1 by WCAG maths, but each glyph has a 2 px black outline, as in your reference. Readable on phones.
- **Craft (13):** a few caption groups are on screen for 1.0–1.4 s, slightly under the reading floor. They follow natural speech pace; shortening the speech would be the only fix.
- **Lint (83):** structural notes (single-file composition, 65 caption clips on one track, nested scene groups), the same pattern as Ep001. No render impact.

## Visual QA ✅ (snapshot review of ~35 frames + final contact sheet)

- **Characters are consistent:** every Dr. Azren and patient image is a sprite cut from your approved reference art; no per-shot regeneration. One skin tone for the patient (the video's deeper brown; poster bust colour-matched).
- **Lip-sync:** mouth states harvested from your lipsync reference (explaining pose: 5 states; table pose: 5 states), driven per frame by the narration's loudness and closed between words. The red-flag close-up uses only neutral talking shapes (no grin).
- **Blinks:** seeded 3-frame blinks every 2.6–4.8 s on every visible character; none on the final second (clean last frame).
- **Every scene has 3–5 layers** (character + concept prop + headline + doodle accents + motion). A new visual beat every ~2.5 s.
- **Signature metaphor works:** colour drains to grey (Scenes 1–4), colour sparks return on each coping step (6), full colour sweeps back at "Warna dalam hidup anda boleh kembali" (9a).
- **Captions:** coloured bars rotate teal/coral/purple/blue with one yellow keyword, as in the reference. SRT text = aligned script words (184/184 match). Captions show "15555", "999", "Dr. Azren" where the voice reads the words.
- **Fixed during QA:** sofa sprite leaked a lightning bolt and the doctor's hand (clipped). The walking patient had the doctor's arm on her back (removed, outline redrawn). The panic-episode bell above the table scene (masked). The colour-return wipe ran backwards (fixed). Disclaimer wrapping over the doctor (shortened). The outro music faded with the bed's own ending (replaced with the brand intro bars).
- **Known cosmetic item (not fixed):** a thin blue sliver from the reference's caption bar is visible at the bottom edge of the table sprite (S7, 53–62 s, y ≈ 1,700, inside the platform-UI zone). Next render: crop that sprite 1 % at the bottom.

## Medical / safety QA ✅ (against `01_medical_factcheck_and_sources.md`)

- Narration is word-for-word the approved script (`03b_tts_input_DRAFT.txt`). No visual adds a clinical claim beyond it.
- On-screen additions approved by default: "Doktor juga akan periksa punca fizikal lain (cth. tiroid)" (S5), and "Rasa tak boleh berfungsi langsung? Jumpa doktor segera" (S8 card).
- Help card on screen 62.3–73.5 s (≥ 11 s): **Talian HEAL 15555** (8 pagi–12 malam), **Befrienders 03-7627 2929** (24 jam), **Kecemasan 999**. Teal "help" styling, no alarm imagery or sound, music ducked lowest.
- The thought bubbles "Aku tak berguna…" / "Semua salah aku…" are shown as thoughts (grey, in bubbles), illustrating the symptom the narration names.
- No drug names or doses, no cure promise, no diagnosis of the viewer ("mungkin", "hanya doktor boleh sahkan").
- Final frame: "Pendidikan kesihatan umum, bukan diagnosis."

## ⚠️ Not verifiable by me: please check by ear and eye

1. **Voice likeness, Malaysian pronunciation and delivery tags** (not spoken aloud?). Check especially "CBT", "Befrienders", "Talian HEAL", "satu lima lima lima lima".
2. **Lip-sync feel** at real-time speed (I reviewed stills and the per-frame track, not playback).
3. **Music/voice balance by ear.** Measurements look right (above).
4. **Caption timing:** sentence boundaries come from pause detection (exact). Words inside long sentences are spread by syllables (±0.15 s).

If a single word is mispronounced, fix only that sentence (~60–200 ElevenLabs credits) and splice it, rather than redoing the whole take.
