# Episode 002: credit usage report (ACTUAL)

Each "actual" figure is what the service returned for the job. Estimates are kept separate.

## Paid generations

| # | Service / model | What | Settings | Estimate (preflight) | **Actual (returned)** | Job / flow |
|---|---|---|---|---|---|---|
| 1 | ElevenLabs `eleven_v4` | Narration, voice "Dr Azren" `lN6exnzhuXDOyNQfsVSR` | **1 take**, 1,367 chars (TTS input incl. tags), 81.6 s | 1,366.86 | **1,367** (`credit_costs` returned; price 1,366.8633 credits / US$0.2485) | flow `n1CxoDELaaXQ2n2zo66L`, gen `cwFWa9Q3zgTTl6DTOV9g`, history `yfj3H5R8o9lh7ELmusHN` |

**Regenerations: 0. Retries: 0. Variations: 0.**

## Higgsfield

| | |
|---|---|
| Generations | **None** (Route A, zero-credit) |
| Balance before | 2,949.01 (checked 18 Nov 2026, pre-production) |
| Balance after | **2,949.01** (checked after build) |
| **Spent this episode** | **0.00** (cap 10) ✅ |

## Free / local

| Item | Cost |
|---|---|
| Sprite cut-outs (`tools/cutout.py`), mouth atlases (`tools/mouth_atlas.py`), skin-tone match, sprite clean-up | 0 (local) |
| Word timings (`tools/align_script.py`), captions + SRT + lip-sync/blink tracks (`tools/build_doodleverse.py`) | 0 (local) |
| HyperFrames check / snapshots / 1080×1920 24 fps render (CLI 0.9.55, local Chrome + FFmpeg) | 0 (local) |
| Music: brand bed A from Ep001 (re-downloaded from ElevenLabs, free) | 0 new |
| SFX: HyperFrames Pixabay pack | 0 |
| Thumbnail (local HTML → PNG) | 0 |
| Preflights: ElevenLabs `estimate_only` ×1, Higgsfield `estimate_image_cost` ×2 | 0 |
| Claude (this session) | Unknown (subscription; not exposed) |

## Totals vs. estimate

| | Estimate | Actual |
|---|---|---|
| ElevenLabs | 1,366.86 | **1,367** |
| Higgsfield | 0 (optional 2.75 not used) | **0** |

ElevenLabs balance before/after: **unknown**. The connector still lacks usage permission (`account_get_usage` refused).
