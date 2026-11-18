# Dr. Azren | Spread Positivity — Daily Health Explainer Production System

One medically responsible, scroll-stopping 60–90 s vertical explainer per day, in Bahasa Melayu Malaysia.

## Pipeline

```
Topic → Research + fact-check → Hooks (3) → Script BM → ★ Dr. Azren medical approval
      → Preflight costs → ★ Budget approval → ElevenLabs v4 narration (1 take)
      → Word timings → HyperFrames build (SVG rigs, diagrams, captions, music mix)
      → [≤ 2 Higgsfield inset clips, start frame = our own render] → QA → Render (local)
      → Thumbnail + captions per platform → ★ Publishing approval → Metricool schedule
      → Cost reconciliation → Analytics feed the next week's plan
```
★ = human approval gate. Nothing is published or scheduled without it.

## Folder layout

```
Dr_Azren_Spread_Positivity/
  00_system/                         ← shared across all episodes
    01_integration_audit.md          what is connected (verified)
    02_reference_creative_audit.md   analysis of the reference episode
    03_WHITEBOARD_2.0_design_system.md
    04_cost_model.md                 verified prices, caps, rules
    mascot_reference/                stills of the existing mascot (approval input)
    reference_audit/                 1 fps contact sheets of the reference
  Episode_NNN_Topic/
    01_research_notes.md  02_sources.md  03_script_BM_*.txt  03a_hooks.md
    04_storyboard.md  05_voiceover.wav  06_hyperframes_source/
    07_higgsfield_assets/  08_background_music/  09_final_video_1080x1920.mp4
    10_subtitles.srt  11_thumbnail_1080x1920.png  12–15 platform captions
    16_credit_usage_report.md  17_metricool_schedule.md  18_quality_assurance_report.md
```
Large binaries (WAV/MP4/PNG renders) are kept on Google Drive and listed in each episode's manifest. They are not committed to git.

## Daily runbook (reusable template)

1. **Pick the topic** from the 30-day calendar. Check it isn't close to the last 3 episodes.
2. **Research**: guideline or systematic review first, Malaysian sources where they exist. Write `01`/`02`, with each source's "read" status stated honestly.
3. **Fact-check table** (claim → verdict → source) and safety checklist (red flags, no diagnosis implied, medication wording).
4. **3 hooks** (curiosity / relatable / fact), scored; pick one and say why.
5. **Script**: 160–190 words, ≤ 1,480 billable characters (v4 tags count), narration starts on the hook (never "Assalamualaikum, saya…"), and red flags are never cut.
6. ★ **Dr. Azren approves** the script and the fact-check.
7. **Preflight** ElevenLabs (`estimate_only`, `generations_count=1`) and Higgsfield (`get_cost`), then fill `16_credit_estimate`. ★ **Budget approval.**
8. **Narration**: `eleven_v4`, voice `lN6exnzhuXDOyNQfsVSR`, 1 take. Download to `05_voiceover.wav`.
9. **Word timings** from the narration (local transcription, corrected against the script), then build the caption JSON and SRT.
10. **Build in HyperFrames** from the master template: set variables and beats, snap beats to anchor words.
11. **AI inset clips** (if approved): render our start frame → Higgsfield → QA → keep or use the SVG fallback.
12. **Mix**: brand bed, ducking, SFX on visible actions, −14 LUFS / ≤ −1 dBTP.
13. `npx hyperframes check` → snapshot review → **render locally** → technical QA (`ffprobe`, loudness, frame check).
14. **Thumbnail** (HyperFrames still) and **platform captions** (TikTok / IG / FB / YT, each written separately).
15. ★ **Publishing approval** → Metricool `brandId 7812551` → verify the scheduled post → log it in `17`.
16. **Reconcile** estimated vs actual credits in `16_credit_usage_report.md`.

## Status — first production task (Part S)

| Step | Status |
|---|---|
| 1. Reference creative audit | ✅ `00_system/02_reference_creative_audit.md` |
| 2. Whiteboard 2.0 design system | ✅ `00_system/03_WHITEBOARD_2.0_design_system.md` |
| 3. HyperFrames master template | ✅ `Episode_001_Serangan_Panik/06_hyperframes_source/src/index.src.html` + `tools/build_episode.py` (copy the folder for each new episode) |
| 4–6. Concept, hooks, script, storyboard | ✅ Episode 001 |
| 7. Credit estimate | ✅ `16_credit_estimate_PRE_GENERATION.md` |
| 8. ElevenLabs v4 narration | ✅ 1 take, 77.1 s, 1,308.87 credits |
| 9. Visuals (HyperFrames + 2 Higgsfield clips) | ✅ 25 credits + 2.75 for the character sheet |
| 10. Final assembly | ✅ `09_final_video_1080x1920.mp4`, 80.5 s, −14 LUFS (MP4 kept out of git) |
| 11. Thumbnail + platform copy | ✅ `11_…png`, `12/14/15_…txt` (Instagram skipped, per your instruction) |
| 12. Metricool | ⏸ Proposal ready (`17_metricool_schedule.md`); **needs your publishing approval** |
| 13. Credit report + reusable template | ✅ `16_credit_usage_report.md`; this runbook |
| 14. 30-day calendar | ⏳ Next |

## V2: DoodleVerse (from Episode 002)

The master brief V2 replaces "Whiteboard 2.0" with **DoodleVerse**, the rich hatched-marker look of the lipsync reference, built almost entirely locally.

| Change | V1 (Ep001) | V2 (Ep002 →) |
|---|---|---|
| Look | Clean vector whiteboard, semantic colours | Hatched alcohol-marker illustration, multi-colour doodle confetti, coloured caption bars |
| Characters | SVG rig + AI sprites | **Sprites cut from your own approved art** (`tools/cutout.py`) + SVG doodles |
| Higgsfield | ≤ 25/episode (2 video clips) | **0 by default; ≤ 10 per generation and ≤ 10 per episode** |
| Frame rate | 30 fps | 24 fps |
| Lip-sync | — | Mouth atlas harvested from the lipsync reference |

Docs: `00_system/05_DOODLEVERSE_reference_analysis.md`, `00_system/06_DOODLEVERSE_asset_and_animation_strategy.md`. Library: `Dr_Azren_DoodleVerse_Assets/`.

### Episode 002: Kemurungan Major (Major Depressive Disorder)
✅ Produced (see `Episode_002_Kemurungan_Major/18_quality_assurance_report.md`). Spend: ElevenLabs 1,367 (narration, 1 take), Higgsfield **0**.
⏸ Needs: your watch-through sign-off, then publishing approval (`17_metricool_schedule.md`).

### DoodleVerse daily runbook (from Ep002)
1. Copy `Episode_002_…/06_hyperframes_source` as the new episode's project; keep `src/index.src.html` as the scene template.
2. Write `03b_tts_input_*.txt`; preflight `estimate_only` (1 take); after approval generate with `eleven_v4`, voice `lN6exnzhuXDOyNQfsVSR`.
3. `python3 tools/align_script.py <tts.txt> 05_voiceover.mp3 05_voiceover_words.json`
4. Add `caption_keywords.txt`; edit scenes (sprites come from `Dr_Azren_DoodleVerse_Assets/`; new poses via `tools/cutout.py`, mouths via `tools/mouth_atlas.py`).
5. `cd 06_hyperframes_source && python3 ../../tools/build_doodleverse.py .. --duration <s>` → captions, SRT, lip-sync + blink tracks.
6. `npx -y hyperframes@0.9.55 check` → `snapshot --at …` → `render -o renders/raw.mp4 --fps 24 --quality delivery`.
7. Loudness-normalise to −14 LUFS / ≤ −1 dBTP (see Ep002 QA report), then `python3 tools/qa_video.py <mp4> --max 90 --fps 24`.

## Tools

| Script | Does |
|---|---|
| `tools/align_script.py <tts.txt> <vo.mp3> <words.json>` | Free local word timing for a known script (pause-based DP alignment) |
| `tools/build_episode.py <episode_dir> [--no-captions]` | Template → `index.html` + caption track + `10_subtitles.srt`; drops AI clips that don't exist yet |
| `tools/qa_video.py <mp4> --max 90` | Technical QA (specs, duration, LUFS/peak, black/frozen frames) |
| `tools/cutout.py IN OUT --box x0 y0 x1 y1 [--erase …] [--keep all]` | Transparent sprite from whiteboard art (border flood-fill) + origin sidecar JSON, 0 credits |
| `tools/mouth_atlas.py VIDEO OUT --tref t --range t0 t1 --face … --mouth …` | Harvest 5 mouth states from the lipsync reference for one pose |
| `tools/build_doodleverse.py <episode_dir>` | DoodleVerse build: captions (coloured bars), SRT, lip-sync + blink tracks |

Render: `cd <episode>/06_hyperframes_source && npx -y hyperframes@0.9.55 render -o renders/out.mp4 --fps 30 --quality delivery`, then loudness-normalise to −14 LUFS (see the QA report).
