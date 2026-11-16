# Episode 001 — Quality Assurance Report

**File:** `09_final_video_1080x1920.mp4` (render v2 plus two-pass loudness normalisation; 20.0 MB, kept out of git)
**Date:** 2026-11-16 · **Tooling:** `tools/qa_video.py`, `hyperframes check`, frame review

## Technical QA (measured) ✅

| Check | Result |
|---|---|
| Resolution / aspect | 1080 × 1920, 9:16 ✅ |
| Frame rate | 30 fps ✅ |
| Codecs | H.264 yuv420p + AAC 48 kHz 192 kb/s, `faststart` ✅ |
| Duration | **80.5 s** (≤ 90 s cap) ✅ |
| Integrated loudness | **−14.0 LUFS** ✅ (raw render was −12.3, normalised without re-encoding the video) |
| True peak | −2.5 dBTP ✅ |
| Black frames / freezes ≥ 4 s | None ✅ |
| Voice vs music | Speech sections about −12.3 LUFS; music-only outro −20.6 LUFS; bed ducked to 0.16 under the voice ✅ |
| Watermarks | None (all assets generated or owned; no third-party watermark) ✅ |
| HyperFrames `check` | 0 errors. Warnings accepted: 6 caption groups slightly under the readability floor (they follow the natural speaking pace); brand bug at y 244 may sit under the Reels/Shorts top bar (decorative only) |

## Visual QA ✅ (frame review, 21 sampled frames + clip seams)

- Mascot: identical in every shot (sprites cut from the approved sheet, no per-shot regeneration). No malformed hands or faces.
- AI inset clips: on-style. H1 face, hair and shirt match the start frame; one hand added, no extra limbs. H2 cat and car match. No AI text.
  - Minor: H1's first frame shows hands on the wheel that our still didn't have, so there is a tiny jump at 1.85 s.
- All on-screen text inside the TikTok ∩ Reels ∩ Shorts clear zone (except the decorative brand bug).
- Measured text contrast ≥ 4.5:1 (text-safe colour tokens).
- Spelling checked against the approved script. Captions show "999" and "Dr. Azren" while the voice reads "sembilan sembilan sembilan" / "Doktor".

## Medical QA ✅ (against `01_research_notes.md`)

- Every narrated claim maps to a source in the fact-check table.
- Red-flag beat present (first time / severe / spreading to arm, neck, jaw → 999), plus on screen "Jangan pandu sendiri ke hospital".
- No drug names or doses, no promise of cure, no implied individual diagnosis.
- On-screen footnotes: the stat source (WMH 2016) and "Ilustrasi" on the curve.
- **Final medical sign-off: Dr. Azren** (watch the final cut once).

## ⚠️ Not verifiable by me — please check by ear

I can measure audio but cannot listen to it.
1. **Voice likeness and Malaysian accent** of the `eleven_v4` take, including how "CBT", "Adrenalin" and "sembilan sembilan sembilan" are pronounced.
2. **Delivery tags** (`[nervous]`, `[serious]`, `[warmly]`, `[happy]`): confirm none were spoken aloud.
3. **Music has no vocals**: confirmed visually from spectrograms only.
4. **Caption sync**: word times come from local pause-based alignment of the exact script. Sentence boundaries are exact; individual words can be off by about ±0.15 s. Each caption group opens on time.

If any sentence is mispronounced, the cheapest fix is to regenerate **only that sentence** (about 60–200 credits) and splice it into the voice track.

## Social QA ✅

- Hook: problem on screen at frame 0 ("TIBA-TIBA DADA KETAT?" plus the car scene); no greeting or logo at the start.
- Visual change every ~2–4 s (19 scenes + sub-beats in 80 s).
- Thumbnail: 1080 × 1920, key elements inside the 4:5 centre crop.
- Copy written separately for TikTok, Facebook and YouTube, with the disclaimer, red-flag line and helplines (FB/YT).
