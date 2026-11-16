# Episode 001 — Credit usage report (ACTUAL)

Every "actual" figure is the credit cost **returned by the service** for that job. Estimates are kept separate.

## Paid generations

| # | Service / model | What | Settings | Estimate (preflight) | **Actual (returned)** | Job / flow |
|---|---|---|---|---|---|---|
| 1 | ElevenLabs `eleven_v4` | Narration, voice Dr Azren `lN6exnzhuXDOyNQfsVSR` | 1 take, 1,309 chars (TTS input incl. tags) | 1,308.87 | **1,308.87** (billed 1,309) | flow `TlpWf0woI5ODbZbJmpos`, gen `TjbyPgyyXQGcgV9mWWjM` |
| 2 | ElevenLabs `eleven_music_v2_5` | Brand music bed **A** (used in Ep1) | 90 s | 1,650 (½ of 3,300) | **899.80** | gen `jIpWoipWz0uaSSt6Tp0Q` |
| 3 | ElevenLabs `eleven_music_v2_5` | Brand music bed **B** (alternate, reusable) | 90 s | 1,650 | **899.80** | gen `7lUDf2ruAfuTT4Ey2iSw` |
| 4 | Higgsfield `gpt_image_2_6` | Dr. Azren character sheet (one-time brand asset) | high, 2K, 16:9, 2 refs | 2.75 | **2.75** | job `f92b8b9e-fbfa-4501-a7b2-0e74329c6863` |
| 5 | Higgsfield `seedance_2_0` | H1: Kawan in car, hand to chest | fast, 720p (960²), 5 s, 1:1, no audio | 12.5 | **12.5** | job `602da41a-01db-43bc-b94d-fb78532a4298` |
| 6 | Higgsfield `seedance_2_0` | H2: cat on bonnet, alarm | fast, 720p (960²), 5 s, 1:1, no audio | 12.5 | **12.5** | job `800da5ac-0322-4748-a56b-69e7b50995dd` |

**Regenerations: 0.** No job was retried.

## Totals

| | ElevenLabs | Higgsfield |
|---|---|---|
| Recurring (this episode) | **1,308.87** (narration) | **25.00** (2 clips) |
| One-time brand assets | **1,799.60** (2 music beds) | **2.75** (character sheet) |
| **Total spent** | **3,108.47** | **27.75** |
| Per-episode cap | 1,500 → recurring ✅ under (191 headroom) | 25 → recurring ✅ exactly on cap |
| Balance before | UNKNOWN | 5,198.52 |
| Balance after | UNKNOWN (usage scope not granted to connector) | **5,170.77** (verified with `balance`) |
| Estimate vs actual | Music came in **1,500.4 under** estimate (preflight priced 2 × 1,650, billed 2 × 899.8) | Exact match |

## Free / local / subscription

| Item | Cost |
|---|---|
| HyperFrames build + 1080×1920 30 fps render | Local (this container), **0 credits** |
| Caption alignment (`tools/align_script.py`) | Local, **0** |
| Sprite cutouts, start-frame plates, thumbnail | Local, **0** |
| SFX (Pixabay licence, bundled with HyperFrames) | **0** |
| `estimate_only` / `get_cost` preflights (7 calls) | **0** (they created empty ElevenLabs flows; nothing charged) |
| Claude (this session) | **UNKNOWN** (subscription; not exposed) |

## Reusable assets now owned (cheaper future episodes)

- 2 brand music beds (A used here; B for variety), so **no music cost** in future episodes
- Character sheet + 10 transparent mascot sprites, so **no mascot cost** in future episodes
- Kawan SVG rig, car/cat/brain/body/calendar SVG library, caption and alignment tools

**Expected recurring cost per future episode:** ≈ 1,300–1,480 ElevenLabs credits (narration) + 0–25 Higgsfield credits.
