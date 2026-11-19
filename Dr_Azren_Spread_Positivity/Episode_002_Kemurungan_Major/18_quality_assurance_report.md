# Episode 002: Quality Assurance Report (v2)

**File:** `09_final_video_1080x1920.mp4` (v2, 19 Nov 2026; git-ignored, delivered to you directly). v1 (18 Nov) is superseded.
**Source:** `06_hyperframes_source/compose_v2.py` → `src/index.src.html` → `tools/build_doodleverse.py` → `index.html` (v1 kept as `src/index_v1.src.html`).

## What changed from v1 (your four requests)

| Request | v2 result |
|---|---|
| Richer elements | Every scene has a set (bedroom, park, clinic, notice board…), confetti doodle layer, props with cyan/yellow offset marker shadows, sticky notes with washi tape, speech bubbles, draw-on arrows, marker swipes between scenes, drifting rain, rotating gears |
| No elements from the previous video | No sofa/TV, table-and-heart, heart bubble, calendar, bell or hijab patient. New: Amir, Mei Ling, guitar with cobwebs, messy bed, rain window, 3 a.m. clock, unread chats, sun/moon timeline, life sticky notes, wilting → blooming plant, park bench, label tags, three gears, stepping stones, clinic desk, cork notice board, avatar family outro |
| Reusable avatars | 6 avatars × 2 states + 5 Dr. Azren poses + 6 viseme heads in `Dr_Azren_DoodleVerse_Assets` (see its README) |
| No cut-off images | All characters are full body with feet on a drawn floor; the doctor stands behind a fully drawn desk in the clinic. **Automated check `tools/sprite_edge_check.js`: PASS** (every 0.25 s, no character or prop leaves the canvas). Slide-in entrances were changed to short in-frame moves |
| Tidier lip-sync | Text-driven visemes from the Malay spelling (a → open, e/i → teeth, o/u → round, m/b/p → closed, relaxed between close words), mouth leads audio by 1 frame, ≥ 2-frame holds, patches warped to each pose with pupil-based scale/rotation and skin colour-matched. Verified on consecutive frames (S3, S5): clean shapes, no seams |

## Technical QA (measured) ✅

| Check | Result |
|---|---|
| Resolution / fps / codecs | 1080 × 1920 · 24 fps · H.264 yuv420p + AAC 48 kHz 192 kb/s · faststart ✅ |
| Duration | **85.4 s** ✅ (≤ 90) |
| Loudness / true peak | **−14.1 LUFS / −1.44 dBTP** ✅ |
| Segments | Hook −12.4 · explanation −13.5/−14.3 · help scene −13.8 · music-only outro −18.4 LUFS |
| Black frames / freezes ≥ 4 s | None ✅ |
| `hyperframes check` | **0 errors** in all 7 categories (warnings reviewed, same accepted classes as v1) |
| Sprite edge check | **PASS** |
| File size | 97 MB (detail-rich art at delivery quality). Fine for TikTok/Reels/Shorts uploads |

## Medical / safety QA ✅

The narration is unchanged (approved script). The help card shows HEAL 15555 (8 pagi–12 malam), Befrienders 03-7627 2929 (24 jam) and 999, on screen from 62.3 s for over 11 s. It also carries the "tak boleh berfungsi" line. The thyroid footnote is in S5 and the disclaimer on the last frame. No drug names or doses, and no diagnosis of the viewer.

## Known items

- Amir's sad sprite: AI-drawn under-eye shadows were purple (looked like bruises); recoloured locally to tired brown.
- Lint warnings (single-file composition, 65 caption clips on one track) carry over from v1, with no render impact.
- **Please check by ear:** voice/pronunciation (unchanged from v1), and the lip-sync feel at full speed.
