# Cost Model & Budget Controls

All "verified" prices come from the service's own preflight on **2026-11-16** (no job submitted). Re-check before every paid call; prices change.

## 1. Verified unit prices

| Service | Item | Preflight result | Notes |
|---|---|---|---|
| ElevenLabs `eleven_v4` TTS | Episode 1 script, 1,464 billable chars, **1 take** | **1,463.85 credits**, US$0.266 | ≈ **1.0 credit per character**. Audio tags such as `[warmly]` count as characters. |
| ElevenLabs `eleven_v4` TTS | Same script, **2 takes** (the tool's default) | 2,927.71 credits, US$0.532 | ❌ Breaks the 1,500/episode cap, so **always set `generations_count = 1`**. |
| ElevenLabs Music `eleven_music_v2_5` | Brand music bed, 2 variations | **3,300 credits**, US$0.60 | **One-time brand asset**, reused every episode. Commercial licence depends on your ElevenLabs plan, which is **UNKNOWN** (usage scope missing). |
| Higgsfield `seedance_2_0` (fast, 720p, 5 s, 9:16, no audio) | 1 clip | **12.5 credits** | Default choice: 2 clips = 25 = the per-episode cap. |
| Higgsfield `seedance_2_5` (720p, 5 s) | 1 clip | 35 credits | Over budget; not used by default. |
| Higgsfield `seedance_2_0` (std, 1080p, 5 s) | 1 clip | 60 credits | Premium; needs your approval. |
| Higgsfield `gpt_image_2_6` (high, 2K) | 1 image | **2.75 credits** | Character sheet (one-time). |
| Higgsfield `gpt_image_2_6` (default settings) | 1 image | 0.25 credits | Drafts/thumbnails if ever needed. |
| HyperFrames | Local render (CLI + local Chrome + FFmpeg) | **0 (free/local)** | No HeyGen cloud render used. |
| Bundled SFX | Pixabay-licensed set | 0 | Commercial use OK, no attribution needed. |
| Claude | This session | **UNKNOWN** | Subscription session; token use isn't exposed to me. |

## 2. Account balances

| Service | Balance | Source |
|---|---|---|
| Higgsfield | **5,198.52 credits** (Ultra) | `balance` tool |
| ElevenLabs | **UNKNOWN** | `account_get_usage` needs the connector reconnected with more permission |

## 3. Per-episode budget (defaults from the brief)

| Line | Cap | Default plan | Headroom |
|---|---|---|---|
| ElevenLabs narration | 1,500 | 1 take ≈ 1,350–1,480 (scripts kept to ≤ 1,480 billable characters) | ~20–150 credits. A full retake is **not** in budget; fix single sentences instead (~60–200 credits each) |
| Higgsfield | 25 | 2 × `seedance_2_0` fast 720p 5 s = 25 | 0. Retry allowance: **none without your approval** |
| HyperFrames | — | Local | — |

### Episodes affordable

- **Higgsfield:** 5,198.52 ÷ 25 ≈ **207 episodes** at full AI-clip use, or unlimited at 0 clips.
- **ElevenLabs:** UNKNOWN until the balance is visible. Formula: `episodes ≈ balance ÷ 1,470`.

## 4. Rules (enforced every episode)

1. The script is locked and medically approved **before** any audio is generated.
2. Always run a **preflight** (`estimate_only` / `get_cost`) and show it before generating.
3. ElevenLabs: `generations_count = 1`, model `eleven_v4`, voice `lN6exnzhuXDOyNQfsVSR`. Never `eleven_v4_turbo` without your approval.
4. Never regenerate narration for a visual change. For a single bad word, try a pronunciation fix (IPA) on that sentence only.
5. Higgsfield: start frames are our own HyperFrames renders (free). No image generation per episode.
6. Never resubmit a job after a timeout until its outcome is known.
7. Log every paid call in the episode's `16_credit_usage_report.md` with the **actual** credits returned, kept separate from estimates.
8. Anything over cap, any premium model and any retry needs written approval in chat first.
