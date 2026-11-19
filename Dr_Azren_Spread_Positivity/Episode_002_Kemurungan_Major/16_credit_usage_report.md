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

---

## v2 revision (19 Nov 2026): richer elements, avatar library, no cut-offs, viseme lip-sync

Approved by you before generation: Option A, quoted at 9.25 Higgsfield credits (live quotes 19 Nov). Kavitha was renamed Divya.

| # | Service / model | What | Settings | Quote | **Actual** | Job |
|---|---|---|---|---|---|---|
| 2 | Higgsfield `gpt_image_2_6` | Dr. Azren: 5 new full-body poses + 6 viseme heads | high, 2K, 16:9, refs: poster + full-body frame | 2.75 | **2.75** | `12e84eb8-d367-4a96-a9d7-fc4a5f4140d0` |
| 3 | Higgsfield `gpt_image_2_6` | Avatars: Amir, Mei Ling, Divya (low + relieved) | high, 2K, 16:9, ref: poster | 2.75 | **2.75** | `3ce0f01a-6173-4326-a591-2411969f817b` |
| 4 | Higgsfield `gpt_image_2_6` | Avatars: Pak Rahman, Danish, Kak Ros (low + relieved) | high, 2K, 16:9, ref: poster | 2.75 | **2.75** | `bd251a40-69bf-4b78-95be-7491b1964f19` |
| 5 | Higgsfield `gpt_image_2_6` | Ep002 prop pack (9 props) | medium, 2K, 16:9, ref: poster | 1.00 | **1.00** | `4d2614bf-3d2c-44b6-a068-6eac11200692` |

- Higgsfield balance: **2,948.51 → 2,939.26** (verified with `balance` before and after) = **9.25 spent**, cap 10 ✅. Retries: **0**.
- Reference uploads (`media_upload` ×2): balance unchanged, so **0**.
- ElevenLabs v2: **0**. The approved narration was reused unchanged.
- Everything else (cutting, viseme rigs, composition, edge check, render, thumbnail): local, **0**.

## Episode 002 totals (v1 + v2)

| | ElevenLabs | Higgsfield |
|---|---|---|
| Narration (v1, reused in v2) | 1,367 | — |
| Reusable library (v2) | — | 9.25 |
| **Total** | **1,367** | **9.25** (cap 10 ✅) |

From Ep003 onwards the library (Dr. Azren poses + visemes, 6 avatars) costs **0** to reuse.
