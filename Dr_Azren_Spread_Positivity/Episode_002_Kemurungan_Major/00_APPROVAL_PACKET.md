# Episode 002 · Kemurungan Major: approval packet

**Stage:** pre-production complete. **Spent so far: 0 credits** (Higgsfield 0, ElevenLabs 0). Nothing billable runs until you approve below.

| Step (brief "START NOW") | Where | Status |
|---|---|---|
| 1. Inspect reference video + poster | `../00_system/05_DOODLEVERSE_reference_analysis.md` | ✅ Both downloaded byte-exact and analysed (audio not judged by ear) |
| 2. Visual identity breakdown | same file, §2–§4 | ✅ |
| 3. Reusable assets | `../00_system/06_…strategy.md` §4, `../Dr_Azren_DoodleVerse_Assets/README.md` | ✅ 8 sprites already cut from your art (0 credits) |
| 4. Zero-Higgsfield animation strategy | `../00_system/06_…strategy.md` §1–§3 | ✅ Includes the lip-sync method (mouth atlas from your lipsync video, verified feasible) |
| 5. Three hooks | `03a_hooks.md` | ✅ Picked **B: "Benda yang dulu buat anda gembira… sekarang rasa kosong?"** |
| 6. BM narration (≤ 90 s) | `03_script_BM_FOR_APPROVAL.md`, exact TTS text `03b_tts_input_DRAFT.txt` | ✅ 190 words, ~80 s voice, ~84 s video |
| 7. Storyboard | `04_storyboard.md` | ✅ 9 scenes, ~32 beats, colour-drain → colour-return metaphor |
| 8. Credit estimate | `16_credit_estimate_PRE_GENERATION.md` | ✅ ElevenLabs **1,366.86** (confirmed preflight), Higgsfield **0** (optional 2.75) |
| 9. Medical fact-check + sources | `01_medical_factcheck_and_sources.md` | ✅ WHO (Sep 2026), MOH Malaysia CPG MDD 2nd ed., helplines verified today |
| Style proof | `style_test_scene01.png` | ✅ Scene 1 rendered locally from your art + SVG doodles |

## Decisions I need from you

1. **Clinical approval of the script** (`03_script_BM_FOR_APPROVAL.md`), with any wording edits.
2. **ElevenLabs narration, 1,366.86 credits, 1 take.** Approve? (Your ElevenLabs balance is not visible to me.)
3. **Route A (0 Higgsfield credits)** using existing poses, **or Route B (+2.75 credits)**: one patient pose sheet (sad, in bed, hugging knees, small smile) that stays in the library for future episodes?
4. **Patient skin tone canon:** the poster's tan, or the video's deeper brown?
5. **Optional on-screen lines** (no narration change): the "punca fizikal lain (cth. tiroid)" footnote (Scene 5) and "tak boleh berfungsi → jumpa doktor segera" (Scene 8)?
6. **Caption position:** move it up out of the platform-UI zone (recommended), or keep the reference's low position?

## After approval, I will (in this order)

1. Generate the narration once, then download, measure and transcribe it locally for word timings.
2. Build the remaining sprites, mouth atlas and SVG props, then the HyperFrames project (24 fps).
3. Render locally, then QA (specs, ≤ 90 s, −14 LUFS / ≤ −1 dBTP, frame check, caption sync).
4. Thumbnail PNG, SRT, platform captions, credit-usage report (actual vs estimate) and QA report.
5. Prepare the Metricool drafts. **Nothing is published or scheduled without your separate approval.**

---

## Production result (18 Nov 2026, after your "proceed")

Decisions I took on your behalf (my recommended defaults; tell me to change any):
1. Script approved as written.
2. Narration generated once: **1,367 ElevenLabs credits**.
3. **Route A: 0 Higgsfield credits** (balance still 2,949.01).
4. Patient skin tone: **the video's deeper brown** (poster bust colour-matched).
5. Both optional on-screen lines included (thyroid footnote, "tak boleh berfungsi" line).
6. Captions moved up out of the platform-UI zone.

| Deliverable | File | Status |
|---|---|---|
| Final video | `09_final_video_1080x1920.mp4` (85.4 s, −14.1 LUFS) | ✅ (git-ignored; sent to you) |
| Subtitles | `10_subtitles.srt` | ✅ |
| Thumbnail | `11_thumbnail_1080x1920.png` (+ `11_thumbnail_source/`) | ✅ |
| Captions | `12_tiktok_…`, `13_instagram_…`, `14_facebook_…`, `15_youtube_…` | ✅ |
| Voiceover | `05_voiceover.mp3` (git-ignored; also in ElevenLabs history `yfj3H5R8o9lh7ELmusHN`) + `05_voiceover_words.json` | ✅ |
| HyperFrames source | `06_hyperframes_source/` (`src/index.src.html` + `tools/build_doodleverse.py`) | ✅ |
| Credit report | `16_credit_usage_report.md` | ✅ |
| Metricool proposal | `17_metricool_schedule.md` | ⏸ Needs your publishing approval |
| QA report | `18_quality_assurance_report.md` | ✅ |

Storyboard note: scene times in `04_storyboard.md` were estimates. The build snaps every beat to the real word times (narration 81.6 s, starting at 0.3 s).

---

## v2 (19 Nov 2026): revision you requested ("lebih rich, elak elemen lama, avatar, tiada terpotong, kemaskan lip-sync")
Plan + live quotes: `20_V2_PELAN_PENAMBAHBAIKAN.md` → you chose **Option A** (rename Kavitha → **Divya**).
Spent: **Higgsfield 9.25** (exact quote, 0 retries), ElevenLabs 0. Final: `09_final_video_1080x1920.mp4` v2, 85.4 s. QA: `18_quality_assurance_report.md`.
