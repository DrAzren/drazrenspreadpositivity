# Integration Audit — 2026-11-16

Every row below comes from a real tool call made in this session. Nothing is assumed.

| Service | Status | What was verified | Gaps / actions |
|---|---|---|---|
| **ElevenLabs** (MCP connector) | ✅ Connected | Voice **"Dr Azren"**, `voice_id = lN6exnzhuXDOyNQfsVSR`, cloned, labelled male / `ms-malaysian` / `ms`. `eleven_v4` is available (and is the workspace default TTS model). The free `estimate_only` preflight works (see cost model). | ❌ `account_get_usage` refused: *"This connector requires additional permissions."* **Credit balance, plan tier and the commercial-licence status of Music are UNKNOWN.** Fix: reconnect the ElevenLabs connector with usage/account scope, or tell me the plan and balance. |
| **Higgsfield** (MCP connector) | ✅ Connected | Balance **5,198.52 credits**, plan **Ultra**. Free `get_cost` preflights work. | None. Prices are re-checked live before every generation. |
| **HyperFrames** | ✅ Installed locally | CLI `hyperframes@0.9.55` via `npx` runs in this container. Skills installed to `~/.claude/skills/` (`hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`, …). `doctor`: Chrome, FFmpeg/FFprobe, 15.7 GB RAM and 29.8 GB disk all OK. **Rendering is local and free.** | Optional, not installed: `whisper-cpp` (local word timing for captions; free to build), Kokoro TTS and MusicGen (both unused: your voice is ElevenLabs, and MusicGen weights are non-commercial). The HeyGen-hosted HyperFrames MCP (`compose`/`render_video`) is disabled for Claude Code by design; the local CLI is the intended route. Not signed in to HeyGen (needed only for the free HeyGen music catalog; optional). |
| **Metricool** (MCP connector) | ✅ Connected | Brand **"Dr Azren \| Spread Positivity"**, `brandId 7812551`, timezone **Asia/Kuala_Lumpur**. Connected networks: **Facebook** (page 1338015042738178), **TikTok** (`drazrennotes`), **YouTube** (channel UCNqHuSxAWbQXQG7z3tdPm8Q), **Threads** (`fakrulazren`). Best-time-to-post data returned for TikTok and Facebook. | ❌ **Instagram is not connected to this brand**, so Instagram Reels can't be scheduled through Metricool until it's connected in Metricool. The account also holds two other brands ("The Curious Affan", "Klinik Nissa"); every scheduling call must use `brandId 7812551`. Media hosting for Metricool uploads will be checked at Step 12. |
| **Google Drive** (MCP connector) | ✅ Connected | Found and downloaded the reference video (see below). The account owns earlier episodes and a `DR AZREN THUMBNAIL.png`. | Can't stream files over a few MB (it returns base64). Large files go through a temporary link-shared copy. |
| **GitHub** | ✅ | The repo `drazren/drazrenspreadpositivity` is empty except for this work; branch `claude/youthful-mccarthy-9eu8jc`. | Large media (MP4/WAV) should not be committed; they will be listed in the manifest and stored on Drive. |

## How the reference video was fetched

1. `Panic_Disorder_Ep1_DrAzrin.mp4` (id `1pYFVENh…`, 50.5 MB) was found on Drive.
2. With your approval, I made a **copy** named `TEMP_claude_download_Panic_Ep1 (delete me).mp4`, set the copy to "anyone with the link: viewer", downloaded it (byte count matched), then **moved the copy to Trash**. **The original file's sharing was never changed.**
3. ⚠️ The connector has no "remove permission" or "delete forever" action. Google Drive keeps a trashed file's link working for people it was shared with until the trash is emptied. **Please permanently delete `TEMP_claude_download_Panic_Ep1 (delete me).mp4` from Drive → Trash** to fully close that link.

## Side effects of this session's checks

- ElevenLabs: three **empty** flows were created by `estimate_only` preflights (`m1EvVzpq…`, `S45yIZD7…`, `tsS63iWo…`). Nothing was generated or charged. They can be deleted from the ElevenLabs Flows page.
- No paid generation was made on any service.

## Persistence note

This cloud container is temporary. The HyperFrames CLI is fetched on demand by `npx`, but the skills in `~/.claude/skills/` are not kept between sessions. Run this at the start of each production session:

```bash
npx -y hyperframes@0.9.55 skills
```
