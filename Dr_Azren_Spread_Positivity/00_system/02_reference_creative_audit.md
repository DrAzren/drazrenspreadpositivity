# Reference Creative Audit — `Panic_Disorder_Ep1_DrAzrin.mp4`

**Status:** Analysed 2026-11-16 from the file on Google Drive (byte-exact download, 50,513,440 bytes).
**Method:** `ffprobe` and `ffmpeg` (specs, scene-cut detection, EBU R128 loudness), 1 fps contact sheets (`reference_audit/contact_sheet_0[1-3].jpg`), and full-resolution frame inspection.
**Limits:** I cannot listen to audio. Voice quality, accent and the music/voice balance are judged only from loudness measurements and the burned-in captions. The narration below is rebuilt from those captions, sampled at 1 fps, so a few words may be missing.

---

## 1. Technical specs (measured)

| Property | Value | Comment |
|---|---|---|
| Duration | 90.0 s | At the top of the 60–90 s target |
| Resolution / aspect | 1080 × 1920, 9:16 | Correct |
| Frame rate | **24 fps** | Upgrade to 30 fps for smoother motion graphics and kinetic type |
| Video | H.264, ~4.3 Mb/s | Fine |
| Audio | AAC, 48 kHz stereo, ~188 kb/s | Fine |
| Integrated loudness | **−9.6 LUFS** | About 4–5 LU hotter than the −14 LUFS social target. Platforms will turn it down, and dense audio at this level is fatiguing |
| True peak | **+0.1 dBTP** | **Clipping.** Target ≤ −1 dBTP |
| Momentary loudness | Peaks near −5 LUFS around t = 10 s | Heavily limited/compressed mix |
| Hard cuts | **8 cuts → 9 shots, about 10 s each** | Short-form pacing wants a new visual beat every 2–4 s |

## 2. What the video looks like

- **Technique:** AI-generated "hand drawing on a real whiteboard" footage. A photoreal hand with a black marker draws on a photographed whiteboard (aluminium frame, ceiling-light reflections, ghosted marker residue). The line art then gets a single-colour teal marker fill.
- **Character:** A young Malaysian doctor with messy black hair, round glasses, teal scrubs, a stethoscope, a black smartwatch on the left wrist and white sneakers. Thick black ink outlines with teal marker hatching.
- **Palette:** Effectively monochrome: black ink, white board and **one accent (teal)**. No colour encodes meaning, so danger, calm and body systems all look the same.
- **Shots, in order (t ≈ seconds):**
  1. 0–11 — The hand draws a heart and an ECG line, then the doctor clutching his chest, then an ECG monitor.
  2. 11–19 — The doctor on a sofa watching TV, then a lightning bolt (attack "comes suddenly").
  3. 19–28 — A brain with a bell/alarm and a crossed-out fire ("alarm with no fire"). The doctor holds the board.
  4. 28–39 — The doctor sweating, with a heart, lungs, dizzy swirls and a stopwatch ("peaks in 10 minutes").
  5. 39–48 — The doctor from behind, a calendar filling with X marks ("living in fear of the next attack").
  6. 48–58 — The doctor walking away, head down, with a bell in a thought bubble ("that's panic disorder"), then the doctor pointing at a shield-heart ("not dangerous to a healthy heart").
  7. 58–68 — The doctor breathing in a 4-7-8 cycle, with a pie timer.
  8. 68–77 — A breath stream and a ring timer. The bell goes quiet ("zzz") as "the nervous system gets the signal you're safe".
  9. 77–90 — The doctor and a patient at a table ("get professional help, cognitive therapy works"), a sleeping bell plus heart, then the doctor waving.
- **Transitions:** Hard cuts plus a slow continuous push-in inside each shot. Almost no motion graphics; the only in-shot motion is drawing-on and slight camera drift.
- **Captions:** One line of lowercase, 3–4 words, white Poppins-style bold with a thin black outline, about **44 px cap height**. Baseline sits at about **y ≈ 1,570 px**, inside the bottom zone that TikTok, Reels and Shorts cover with the post caption, handle and buttons (everything below about 1,330 px). On a white board, white text relies on a thin outline, which is weak on phones.

## 3. Narration (rebuilt from captions; for reference only, never reused)

> Jantung berdegup laju, dada sesak, tangan menggigil, dan anda yakin sedang kena serangan jantung, tapi doktor kata jantung anda normal. Inilah serangan panik. Ia boleh datang tiba-tiba tanpa sebarang amaran walaupun anda sedang duduk santai menonton televisyen. Bayangkan penggera kebakaran dalam otak anda berbunyi kuat walaupun tiada api, lalu badan terus masuk mod lawan atau lari. Adrenalin membanjiri badan, jantung mengepam laju, nafas jadi pendek, kepala pening, dan kebanyakan serangan ini memuncak dalam masa sepuluh minit sahaja. Bila serangan berulang dan anda mula hidup dalam ketakutan menanti serangan seterusnya sehingga mengelak […], itulah tanda gangguan panik. Tapi ramai tak tahu, serangan panik memang menakutkan, namun ia tidak berbahaya kepada jantung yang sihat dan ia pasti [berlalu]. Jadi bila penggera itu berbunyi, cuba teknik pernafasan empat-tujuh-lapan: sedut melalui hidung selama empat saat, kemudian tahan nafas tujuh saat. Hembus perlahan melalui mulut selama lapan saat dan ulang empat kali, supaya sistem saraf anda menerima isyarat bahawa anda selamat. Jika serangan kerap berlaku, dapatkan bantuan profesional kerana terapi kognitif terbukti berkesan, dan ingat, penggera dalam diri anda boleh ditenangkan.

## 4. Strengths to keep

1. **A recognisable mascot**: teal scrubs, round glasses, stethoscope. Strong brand equity; keep the silhouette and the teal.
2. **The "alarm with no danger" metaphor** is clinically sound and easy to grasp.
3. **Good narrative order**: symptoms → what it is → why → when it becomes a disorder → reassurance → coping → get help.
4. **Natural Malaysian Malay register** in the captions: "kena serangan", "tak tahu", "lawan atau lari".
5. **Qualified safety language**: "tidak berbahaya kepada **jantung yang sihat**" is correctly hedged.
6. **The marker-drawing reveal** is satisfying and on-brand.

## 5. Weaknesses to fix in Whiteboard 2.0

| # | Weakness | Fix in Whiteboard 2.0 |
|---|---|---|
| 1 | **Frame 0 is a blank board and a hand.** No hook in the first second; the thumbnail frame is empty. | Frame 0 already shows the problem: character, symptom and one bold line. |
| 2 | **About 10 s per shot.** Retention drops on long holds in vertical feeds. | A new beat every 2–4 s: diagram growth, punch-ins, kinetic words, cut-aways. |
| 3 | **Monochrome palette.** Colour carries no meaning. | Semantic colour: coral = alarm/danger, teal = calm/help, sky blue = body, lavender = brain, yellow = highlight. |
| 4 | **Captions in the platform-UI zone** (y ≈ 1,570) and small. | Captions inside the 168–1,330 px band, 64–72 px, navy on board with a highlighted keyword. |
| 5 | **The doctor mascot is also the patient.** Confusing: is the doctor having panic attacks? | Two roles: **Dr. Azren** explains; **"Kawan"**, an everyday Malaysian character, has the experience. |
| 6 | **Mascot drift** between shots (face shape, proportions, board frame on/off), typical of per-shot AI video. | The mascot becomes a **vector rig in HyperFrames**: the same drawing every frame, with expressions as keyed states. |
| 7 | **AI artefacts**: a ghosted doctor overlay at about 82 s, photoreal hands next to cartoon hands. | Vector rig; AI video only for 1–2 inset shots, checked frame by frame. |
| 8 | **Audio clips** (+0.1 dBTP) and is over-loud (−9.6 LUFS). | Mix to −14 LUFS integrated, ≤ −1 dBTP; music ducks under the voice. |
| 9 | **No red-flag guidance.** It says "doctor says your heart is normal" but never says *get chest pain checked first*. | Explicit red-flag beat: first episode, severe pain, or pain spreading to arm/neck/jaw → emergency / 999. |
| 10 | **The 4-7-8 breathing protocol** is presented as the coping tool, with "sistem saraf menerima isyarat bahawa anda selamat". The specific evidence for 4-7-8 is limited, and the mechanism is simplified. | Use the guideline-aligned "slow, deep breathing; remind yourself it will pass" (NHS), framed as a coping step *after* medical assessment. |
| 11 | **Treatment line** mentions only cognitive therapy. | CBT **and** appropriate medication (both first-line, per NICE CG113), "discuss with your doctor". |
| 12 | **24 fps**, minimal motion design, no kinetic typography. | 30 fps, kinetic type on key phrases, animated diagrams. |
| 13 | **No sound design is visible** (no cues tied to on-screen events). | A small SFX palette tied to visible actions (§7 of the design system). |

## 6. Reusable lessons

- Keep the **marker-draw reveal** as the brand's signature transition, but always over a frame that already has content.
- Keep the **teal mascot**, re-drawn as a consistent vector rig. Approval is needed; see `03_WHITEBOARD_2.0_design_system.md` §4.
- Keep **one metaphor per episode** and develop it, as the alarm was developed here.
- **Do not reuse the reference's wording, shots or arrangements.** Episode 1 v2 uses a new script, a new metaphor vehicle (car alarm instead of fire alarm) and new compositions.
