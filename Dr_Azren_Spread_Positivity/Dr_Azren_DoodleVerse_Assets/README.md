# Dr_Azren_DoodleVerse_Assets: permanent reusable library

Everything here is reused across episodes. **Never regenerate an asset that exists here.** Strategy and rules: `../00_system/06_DOODLEVERSE_asset_and_animation_strategy.md`.

## Sources

| Key | File | Drive ID | Size |
|---|---|---|---|
| `POSTER` | `hf_20261116_091255_90b7f4c1-fdc7-4f66-a6a4-13f29e810aa3.png` (1520 × 2688) | `1PLyCyaLng3kpQWovsc2Qm8vXUkbJF7AR` | 6,024,624 B |
| `REF` | `Panic_Disorder_Ep1_DrAzren_lipsync.mp4` (1080 × 1920, 24 fps) | `1PXLtFf6Dy2RUNjNCUZ-AlCmVVGos2gdW` | 77,472,259 B |

Source files are **not** stored in git (size). Re-fetch them from Drive, then extract a frame with `ffmpeg -ss <t> -i REF.mp4 -frames:v 1 frame.png`.

## Sprites (all cut with `../tools/cutout.py`, 0 credits)

| Sprite | Source | `--box` (x0 y0 x1 y1) and options | Notes |
|---|---|---|---|
| `characters/dr_azren/drazren_bust_pointing.png` | POSTER | `30 1340 740 2350` | Finger up, holding a marker, smiling. Best-resolution doctor |
| `characters/dr_azren/drazren_threequarter_explaining.png` | REF @ 9.0 s | `0 200 1080 1478` | Open-palm explaining, "o" mouth. Cut above the knees (the caption bar sat on the legs) |
| `characters/patient_hijab/patient_bust_worried.png` | POSTER | `820 1420 1500 2350` | Worried, hand on chest, tear drop |
| `characters/patient_hijab/patient_walkaway_headdown.png` | REF @ 46.5 s | `170 560 760 1478` | Head down, walking away. ⚠️ Includes the doctor's hand at right; mask it per scene |
| `scenes/sofa_withdrawn.png` | REF @ 12.5 s | `0 250 1080 1500 --keep all --min-area 3000` | Patient on sofa with mug, eyes closed, TV; doctor standing. ⚠️ Includes a lightning bolt (mask) |
| `scenes/table_consult.png` | REF @ 80.0 s | `0 150 1080 1478 --keep all --min-area 3000` | Doctor + patient at a table, heart between them. ⚠️ The calm bell above is panic-specific (mask for other topics) |
| `scenes/table_relieved.png` | REF @ 86.0 s | `0 150 1080 1478 --keep all --min-area 3000` | Patient standing, smiling; doctor seated |
| `props/heart_ecg.png` | POSTER | `50 940 300 1180 --keep all --min-area 300` | Coral heart with ECG line (small stray specks: crop on use) |

## Templates

- `templates/doodleverse.css`: board surface + frame, marker headline with cyan/yellow offsets, coloured caption bars (teal / coral / purple / blue rotation, yellow keyword), palette tokens.
- `templates/style_test_ep002_scene01.html`: Ep002 Scene 1 style frame (layered composition reference). Its SVG `<symbol>`s (music notes, teh-tarik glass, sparkle, rain drop, grey cloud, dashed arrow) are the start of `props_svg/`.

## Fonts (`fonts/`, local copies of Google Fonts)

Permanent Marker (Apache 2.0): headlines. Poppins 700/800/900 (SIL OFL): captions. Patrick Hand (SIL OFL): small handwritten labels.

## Audio

| File | Source | Cost | Licence |
|---|---|---|---|
| `audio/music/brand_bed_A_ep1.mp3` (90 s, −13.0 LUFS) | ElevenLabs Music `eleven_music_v2_5`, gen `jIpWoipWz0uaSSt6Tp0Q` (Ep1) | Paid once in Ep1 | ⚠️ Commercial terms depend on your ElevenLabs plan, which I can't see (usage scope missing) |
| `audio/music/brand_bed_B_alt.mp3` (90 s, −12.7 LUFS) | gen `7lUDf2ruAfuTT4Ey2iSw` (Ep1) | Paid once in Ep1 | Same |
| SFX | HyperFrames bundle (Pixabay Content License) | 0 | Commercial OK, no attribution required |

MP3s are git-ignored. Re-download them from the ElevenLabs flow `TlpWf0woI5ODbZbJmpos` (`creative_get_generations`, free).

## Still to build (after approval, 0 credits)

- Mouth atlas (closed / small / teeth / round / wide) harvested from REF for both characters, plus eyelid patches.
- `props_svg/` for depression: grey cloud with drizzle, battery (full → low), bed + moon (sleep), plate (appetite), phone with unread messages, brain (no bell), sun + hills colour return, breathing circle, "15555 / 999" helpline card.
- More poses from REF: walking entrance (4–6 s), waving (86–88 s), serious (40–47 s), patient breathing calm (60–65 s), relieved (86 s).
