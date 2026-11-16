# Episode 001 — Credit estimate (BEFORE any paid generation)

**Nothing has been generated or charged.** Every figure is an estimate. The actual usage report (`16_credit_usage_report.md`) gets written only after generation, using the credits each service returns.

## Production cost report

| Service | Usage | Unit price (verified 2026-11-16) | Estimated credits | Basis |
|---|---|---|---|---|
| ElevenLabs `eleven_v4` | Narration, voice **Dr Azren** (`lN6exnzhuXDOyNQfsVSR`), **1 take**, script v1: **1,283 billable characters** (184 words, tags included) | ≈ 1.0 credit/char (preflight: 1,464 chars → 1,463.85 cr) | **≈ 1,283** (≈ US$0.23) | Preflight on an earlier 1,464-char draft; **the final script will be re-preflighted after medical approval** |
| ElevenLabs Music `eleven_music_v2_5` | Brand music bed, 2 variations, **one-time**, reused every episode | Preflight: 3,300 cr / 2 variations | **3,300 (one-time)** | `estimate_only` preflight. ⚠️ Commercial licence depends on your ElevenLabs plan (UNKNOWN) |
| Higgsfield `seedance_2_0` fast 720p 5 s | H1 + H2 = 2 clips | 12.5 cr/clip (`get_cost`) | **25** | Preflight |
| Higgsfield `gpt_image_2_6` high 2K | Dr. Azren character sheet, **one-time** (approval image) | 2.75 cr/image (`get_cost`) | **2.75 (one-time)**, or 5.5 for 2 options | Preflight |
| HyperFrames | Local render, 1080 × 1920, 30 fps | — | **0** (local/free) | CLI on this machine |
| SFX | Bundled Pixabay set + about 3 sourced sounds (marker, heartbeat, car chirp) | ElevenLabs SFX price not yet preflighted | **UNKNOWN**, to preflight; or 0 via CC0 sources | — |
| Claude | This session | — | **UNKNOWN** (subscription; not exposed) | — |

## Totals

| | ElevenLabs | Higgsfield |
|---|---|---|
| Episode 1 recurring | ≈ 1,283 | 25 |
| One-time brand assets | 3,300 (music) | 2.75–5.5 (character sheet) |
| **Episode 1 total incl. one-time** | **≈ 4,583** | **27.75–30.5** |
| Per-episode cap (brief) | 1,500 → ✅ recurring OK | 25 → ✅ recurring OK; one-time sheet above cap, **needs approval** |
| Current balance | **UNKNOWN** | 5,198.52 |
| Projected after Ep. 1 | UNKNOWN | ≈ 5,168–5,171 |
| Retry allowance | ≈ 217 credits (one sentence-level fix) | 0 (fallback to SVG instead) |

## Approvals needed before Step 8

1. ✅ / ❌ **Script v1**, medical sign-off (`03_script_BM_v1_DRAFT.txt` + `01_research_notes.md` §3).
2. ✅ / ❌ **ElevenLabs narration**: about 1,283 credits, 1 take, `eleven_v4`.
3. ✅ / ❌ **Brand music bed**: 3,300 ElevenLabs credits one-time. Alternatives: (a) your own licensed track, (b) the free HeyGen music catalog via `npx hyperframes auth login` (licence terms to check).
4. ✅ / ❌ **Higgsfield H1 + H2**: 25 credits total (or 0: all-native SVG).
5. ✅ / ❌ **Character sheet**: 2.75 credits, or skip if you'd rather I build the vector rig straight from the reference stills in `00_system/mascot_reference/`.
