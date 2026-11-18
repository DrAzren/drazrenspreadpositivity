# Episode 002: credit estimate (PRE-GENERATION)

Checked live on **18 Nov 2026**. Nothing paid has been generated.

## Balances

| Service | Balance | Status |
|---|---|---|
| Higgsfield | **2,949.01 credits** (Ultra) | Confirmed (`balance`) |
| ElevenLabs | **Unknown**. `account_get_usage` still refused ("connector requires additional permissions") | Unknown. Fix: reconnect the ElevenLabs connector with account/usage access |

## Estimate

| Item | Detail | Credits | Status |
|---|---|---|---|
| **ElevenLabs `eleven_v4` narration** | Voice "Dr Azren" `lN6exnzhuXDOyNQfsVSR`, **1 take**, `03b_tts_input_DRAFT.txt` (1,367 chars incl. tags) | **1,366.86** (US$0.25) | **Confirmed** by the `estimate_only` preflight for this exact text. Any wording change moves it ≈ 1 credit per character |
| ElevenLabs single-sentence fix | Only if a word is mispronounced; never a full retake | 0 planned (≈ 60–200 each if needed) | Estimated; **needs your approval** |
| Music | Reuse brand bed A (bed B as alternate) from Ep001 | **0** | Confirmed (both files re-downloaded at no cost) |
| SFX | HyperFrames Pixabay pack | **0** | Confirmed |
| **Higgsfield (default, Route A)** | No generations | **0** | Confirmed |
| Higgsfield optional, Route B | 1 × `gpt_image_2_6`, high, 2K, 16:9: patient pose sheet (sad, tired in bed, hugging knees, small smile) referencing the poster | **2.75** | **Confirmed live quote**; ≤ 10/generation and ≤ 10/episode. **Needs your approval** |
| Higgsfield optional, later | New male patient character sheet (same model/settings) | 2.75 | Confirmed live quote. **Not proposed for Ep002**; defer until needed |
| HyperFrames | Local CLI render (Chrome + FFmpeg in this container); no HeyGen cloud render | **0** | Confirmed (Ep001 rendered the same way) |
| Word timings / captions / SRT | Local alignment (`tools/align_script.py`) | **0** | Confirmed |
| Sprites, thumbnail, QA | Local | **0** | Confirmed |
| Metricool scheduling | Your existing subscription; no per-post charge seen via the API | 0 extra | Estimated |
| Claude (this session) | Subscription; token use isn't exposed to me | — | Unknown |

## Totals

| | Route A (recommended default) | Route A + B |
|---|---|---|
| ElevenLabs | **1,366.86** | 1,366.86 |
| Higgsfield | **0** | **2.75** (cap 10 ✅) |

**Higgsfield episode cap check:** maximum possible spend = 2.75 ≤ 10 ✅. No video generation is planned. No retries.

## Side effects of today's free preflights

- ElevenLabs `estimate_only` created one **empty** flow, `n1CxoDELaaXQ2n2zo66L` (nothing generated or charged). It can be deleted from the ElevenLabs Flows page, or I'll reuse it for the real narration so the take lands in a known place.
- Higgsfield `estimate_image_cost` ×2: quotes only, no job submitted.
