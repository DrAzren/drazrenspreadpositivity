# Episode 002: Kemurungan Major. Time-coded storyboard v1

**Format:** 1080 × 1920, **24 fps**, ~84 s. **Engine:** HyperFrames (local). **Higgsfield: 0 credits** (Route A).
Times are estimates from the script length (calibrated on Ep001's real voice). After the narration is generated, every beat snaps to its anchor word from the real word timings.

**Visual spine (one metaphor): colour = joy.** The world drains to grey (Scenes 1–4), small sparks of colour return with self-care (Scene 6), help is teal (7–8), and full colour sweeps back at the end (9). Pure CSS/SVG, no AI needed.

**Layout rules (every scene):** headline zone y 150–450; faces y 450–1,300; caption lane centred at y ≈ 1,440 (never below 1,520); bottom 1,560–1,920 = decoration only; no text at x > 950 for y 900–1,700 (right action rail).

**Asset legend:** 🟢 exists in `Dr_Azren_DoodleVerse_Assets` · 🔵 local SVG to draw (0 credits) · 🟠 local edit of an existing sprite (mask/recolour, 0 credits) · 🟣 only with Route B (optional 2.75-credit pose sheet)

---

### Scene 1 · 0.0–4.0 s · HOOK. "Benda yang dulu buat anda gembira… sekarang rasa kosong?"
- **Main:** patient worried bust, big and bleeding off the bottom 🟢 (`patient_bust_worried`). **Supporting:** DULU column (music notes, teh-tarik glass) in colour; KINI column in grey 🔵 (already drawn in the style test).
- **Title:** "DULU SUKA, / KINI **KOSONG?**". The word KOSONG is in grey ink. **Accents:** grey rain cloud with drizzle 🔵, sparkles on the DULU side, "?" on the KINI side, dashed arrow DULU → KINI.
- **Motion:** frame 0 already shows the full colour composition (no blank board). 0.0–0.6: headline pops (scale 0.9 → 1, overshoot). 1.2–2.6: the arrow draws on, and a grey scribble wipe drains the KINI icons to grey. 2.4: cloud slides in; drops loop every 0.7 s. Patient: slow blink at 1.8 s, brows tilt up, tiny head droop.
- **Camera:** push-in 100 → 104 %. **SFX:** soft music sting at 0.0 (bed A intro), marker scratch on the arrow, low "deflate" whoosh on the drain.
- **Caption:** "dulu buat anda **gembira**…" → "sekarang rasa **kosong?**"
- Style frame: `style_test_scene01.png` ✅

### Scene 2 · 4.0–12.0 s · RELATABLE EXPERIENCE. "Bangun pagi… letih. Selera makan berubah, tidur terganggu. Mesej kawan pun dibiarkan… hari demi hari."
- **4.0–6.0:** patient on the sofa, eyes closed, mug in hand 🟢🟠 (`sofa_withdrawn`, lightning masked, doctor cropped out). Battery icon 🔵 drains 60 → 10 % over her head. Sun-up doodle in the window corner. **Caption:** "Bangun pagi pun dah **letih**."
- **6.0–8.6:** three symptom icons pop in an arc around her, each with a marker circle: 🍽️ plate with a "?" (appetite) 🔵, 🌙 moon + zigzag Zzz (sleep) 🔵. Each pops on its word.
- **8.6–10.4:** phone icon 🔵 with a red badge counting up 3 → 12 unread messages; message bubbles stack up and fade grey.
- **10.4–12.0:** a calendar strip 🔵 slides along the top; days flip grey one by one ("hari demi hari").
- **Camera:** slow pan left → right following the icons. **SFX:** pop per icon, phone buzz (soft), page flips.

### Scene 3 · 12.0–26.0 s · DOCTOR EXPLAINS. "Sedih sekali-sekala itu normal. Tapi kalau… hampir setiap hari, sekurang-kurangnya dua minggu… mungkin kemurungan major. Hanya doktor boleh sahkan."
- **12.0–15.0:** **Dr. Azren enters** from the right 🟢 (`drazren_threequarter_explaining`; slide-in with a 2-step bob plus motion lines, or the walking-entrance sprite from REF 4–6 s 🟠). Lip-sync starts. Left: small "normal sad" weather icon, a cloud with a sun peeking out (passes quickly) 🔵. **Caption:** "Sedih sekali-sekala itu **normal**."
- **15.0–21.0:** a big **14-day calendar** 🔵 draws on beside him; days fill with grey scribble one by one (14 ticks, accelerating). Callout bubble: "**HAMPIR SETIAP HARI**". Big marker number "**2 MINGGU+**" with cyan/yellow offsets pops on "dua minggu".
- **21.0–24.0:** three mini-icons draw under the calendar: briefcase, home, heart-people (work, home, relationships), each with a crack line, for "mengganggu kehidupan". Headline: "**KEMURUNGAN MAJOR?**" with a question mark that wiggles.
- **24.0–26.0:** a teal stethoscope-stamp stamps "**HANYA DOKTOR BOLEH SAHKAN**" 🔵 (thunk). Doctor: serious nod.
- **Camera:** reframe to a two-element layout, 3 % push on "kemurungan major". **SFX:** marker squeaks on the calendar ticks (quiet), stamp thunk.

### Scene 4 · 26.0–35.2 s · METAPHOR. "Bayangkan dunia anda yang penuh warna, perlahan-lahan jadi kelabu. Susah nak fokus. Ada yang rasa diri tak berguna, atau rasa bersalah yang melampau."
- **26.0–30.0:** a **full-colour doodle world** 🔵🟢: hills, sun, flowers, stars, heart, the patient in the centre (`patient_walkaway_headdown`, hand masked 🟠). A **grey scribble wave** sweeps left → right, and everything it passes turns grey (CSS grayscale through an animated scribble mask). This is the signature moment.
- **30.0–31.6:** "Susah nak fokus": swirly scribbles 🔵 spin above her head and text blurs ("fo… kus").
- **31.6–35.2:** two thought bubbles 🔵 pop: "**Aku tak berguna**" and "**Semua salah aku**" (hand-lettered, grey ink), each crossed through with a soft teal line as the doctor's voice continues. They are labelled as *thoughts*, not truths.
- **Camera:** slow pull-out 104 → 100 % so the drain reads as "the whole world". **SFX:** a long soft "vinyl slow-down" pitch-drop as colour drains (gentle, under the voice).
- 🟣 With Route B, the walk-away pose is replaced by "hugging knees on the bed", which is more emotionally accurate.

### Scene 5 · 35.2–44.0 s · NOT WEAKNESS. "Ini bukan malas, dan bukan tanda anda lemah. Kemurungan ialah masalah kesihatan sebenar, hasil gabungan faktor biologi, psikologi dan sosial."
- **35.2–38.4:** Dr. Azren pointing bust 🟢 (`drazren_bust_pointing`). Two stickers, "MALAS" and "LEMAH", slap onto the board 🔵, then big red marker Xs strike through each one on the words "bukan" (two beats).
- **38.4–44.0:** **3-circle Venn** 🔵 draws on: **BIOLOGI** (brain icon, pink), **PSIKOLOGI** (thought cloud, purple), **SOSIAL** (people icons, yellow). The overlap glows with a small heart ("masalah kesihatan sebenar"). Each circle draws on its word.
- **Footnote** (if you approve, small, 3 s): "Doktor juga akan periksa punca fizikal lain (cth. tiroid)."
- **Camera:** push toward the Venn. **SFX:** slap ×2, marker X squeak ×2, three soft pops for the circles.

### Scene 6 · 44.0–51.5 s · PRACTICAL COPING (complement, not cure). "Mula dengan langkah kecil. Bergerak sedikit… Jaga waktu tidur dan makan. Luahkan pada orang yang anda percaya."
- **Layout:** a **staircase of 3 small steps** 🔵 drawn on the board. Patient sprite (calm, eyes closed 🟠 from REF 60–65 s) stands at the bottom and moves up one step per tip:
  - Step 1 "**Gerak sikit**" (sneaker + footprints 🔵)
  - Step 2 "**Tidur & makan ikut waktu**" (clock with moon + plate 🔵)
  - Step 3 "**Luahkan**" (two speech bubbles with a heart 🔵)
- **Colour returns in small sparks:** each step lands with a small burst of colour dots, so part of the grey world becomes colour again (only ~20 %, to stay honest that this alone isn't treatment).
- **Camera:** gentle tilt up the stairs. **SFX:** soft footsteps/ticks, a sparkle on each step.

### Scene 7 · 51.5–59.7 s · TREATMENT. "Tapi langkah ini bukan pengganti rawatan. Jumpa doktor, kerana terapi psikologi seperti CBT, dan ubat bila perlu, terbukti berkesan."
- **51.5–54.0:** a banner draws on: "**BUKAN PENGGANTI RAWATAN**" (teal bar, white text).
- **54.0–59.7:** **table consult scene** 🟢🟠 (`table_consult`, panic bell masked, replaced by a 🔵 teal clipboard "CBT" icon). Two icons rise on their words: 🧠💬 "**Terapi psikologi (CBT)**" and 💊 "**Ubat — bila perlu**" (generic capsule, no brand or name). A check-mark sticker "**Terbukti berkesan**" stamps between them. Lip-sync on the doctor; patient listening (blinks, small nods).
- **Camera:** push into the two-shot. **SFX:** soft chime on "terbukti berkesan".

### Scene 8 · 59.7–71.5 s · RED FLAG & HELP. "Dan jika terlintas fikiran untuk mencederakan diri, jangan tunggu. Hubungi Talian HEAL… atau Befrienders. Jika dalam bahaya… 999."
- **Tone:** calm and serious, not alarming. Music ducks to its lowest; board stays light; **teal = help** (no red alarm imagery).
- **59.7–63.0:** Dr. Azren, serious face 🟢🟠 (REF 40–47 s concerned pose), close-up, direct to camera. Caption: "jika terlintas fikiran untuk **mencederakan diri**, jangan tunggu."
- **63.0–71.5:** **helpline card** 🔵 slides up (hand-drawn index card, teal border, phone doodle), on screen ≥ 8 s:
  - **Talian HEAL 15555** · 8 pagi–12 malam
  - **Befrienders 03-7627 2929** · 24 jam
  - **Kecemasan 999**
  Each line highlights (yellow marker swipe) as it's spoken. Optional small line: "Rasa tak boleh berfungsi langsung? Jumpa doktor segera." (your decision)
- **Camera:** static (stillness = seriousness). **SFX:** none except a soft paper slide.

### Scene 9a · 71.5–75.3 s · HOPE. "Warna dalam hidup anda boleh kembali. Anda tak keseorangan."
- **Signature payoff:** the grey world from Scene 4 returns, and a **colour scribble wave** sweeps right → left, refilling everything: sun 🟠 (REF ~56 s sun over hills), sparkles, hearts. Patient relieved and smiling 🟢 (`table_relieved` crop / REF 86 s); Dr. Azren beside her.
- **Camera:** pull-out to reveal the whole colourful board. **SFX:** rising sparkle shimmer; music lifts (bed energy +3 dB).

### Scene 9b · 75.3–84.0 s · BRAND OUTRO. "Share video ni dengan orang yang anda sayang. Saya Doktor Azren. Spread positivity!"
- Dr. Azren pointing bust 🟢 waves/points; sparkle confetti 🔵; marker headline lockup "**Dr. Azren | Spread Positivity**" with cyan/yellow offsets draws on at ~78 s.
- CTA sticker: "**Share dengan orang tersayang**" + hand-drawn heart (no emoji font needed).
- 80.4–84.0: music logo (the last 3.5 s of bed A with a button ending), final frame holds the lockup (works as an auto-thumbnail).

---

## Cut-count & pacing check

- Distinct visual beats: **~32** across 84 s (one new beat every 2.6 s on average; none longer than 4 s without a new element).
- Characters: only Dr. Azren + the pink-hijab patient (no new designs in this episode).
- Faces never sit under captions: captions are fixed at y ≈ 1,440, and faces are framed above 1,300.

## Sound plan

- Music: **bed A** (reuse), ducked to −22 LUFS under the voice (−26 in Scene 8), up to −18 in the music-only outro.
- SFX: HyperFrames' Pixabay pack (pop, whoosh, sparkle, chime, click) plus pitch/volume shaping. No alarm sounds in this episode.
- Mix target: −14 LUFS integrated, ≤ −1 dBTP true peak (the reference was −9.1 LUFS / +0.4 dBTP).
