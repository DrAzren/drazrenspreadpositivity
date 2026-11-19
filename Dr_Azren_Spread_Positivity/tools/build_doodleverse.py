#!/usr/bin/env python3
"""Build a DoodleVerse episode: src/index.src.html -> index.html (+ 10_subtitles.srt).

Injects:
  <!--@CAPTIONS-->      caption groups (one line, 3-5 words) on coloured bars that
                        rotate teal/coral/purple/blue, max one yellow keyword per group
  /*@CAPTION_TWEENS*/   pop-in / out tweens
  /*@LIPSYNC*/          const LS = "...": mouth level 0-4 per frame (24 fps), from the
                        narration's loudness, closed outside words
  /*@BLINK*/            const BL = "...": 1 = eyelids closed (seeded, 3-frame blinks)

Episode inputs: 05_voiceover_words.json (aligned words), 05_voiceover.mp3,
optional caption_keywords.txt (one word per line).

Usage: build_doodleverse.py <episode_dir> [--vo-offset 0.3] [--fps 24] [--duration 85.3]
"""
import html, json, os, re, subprocess, sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from build_episode import fmt_srt, groups, merge_short, norm  # noqa: E402


def arg(name, default):
    return type(default)(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


def lipsync(mp3, words, offset, fps, dur):
    sr = 16000
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", mp3, "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
                         capture_output=True).stdout
    x = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
    n = int(round(dur * fps))
    hop = sr / fps
    rms = np.zeros(n)
    for f in range(n):
        a = int((f / fps - offset) * sr)
        b = int(a + hop)
        if b <= 0 or a >= len(x):
            continue
        seg = x[max(a, 0):min(b, len(x))]
        rms[f] = np.sqrt(np.mean(seg ** 2)) if len(seg) else 0
    speaking = np.zeros(n, bool)
    for w in words:
        a = int((w["start"] + offset) * fps); b = int(np.ceil((w["end"] + offset) * fps))
        speaking[max(a, 0):min(b, n)] = True
    ref = np.percentile(rms[speaking], 92) if speaking.any() else 1
    lv = np.clip(rms / ref, 0, 1)
    lev = np.digitize(lv, [0.16, 0.38, 0.6, 0.82])  # 0..4
    lev[~speaking] = 0
    # keep some motion: alternate within long held vowels so the mouth never freezes open
    for f in range(2, n):
        if lev[f] >= 3 and lev[f - 1] == lev[f] and lev[f - 2] == lev[f]:
            lev[f] -= 1
    # median-of-3 to remove single-frame flicker
    out = lev.copy()
    for f in range(1, n - 1):
        out[f] = sorted(lev[f - 1:f + 2])[1]
    return "".join(str(int(v)) for v in out)


SPOKEN = {"15555": "satu lima lima lima lima", "999": "sembilan sembilan sembilan", "dr": "doktor",
          "cbt": "si bi ti", "heal": "hil"}


def visemes(mp3, words, offset, fps, dur):
    """Text-driven visemes from the Malay spelling, timed by the aligned words.
    R rest/closed smile, A open (a), E teeth (e, i), O round (o, u), M lips pressed (m, b, p),
    N relaxed half-open (quiet or between close words). Mouth leads the audio by one frame;
    every shape is held at least two frames."""
    import re as _re
    n = int(round(dur * fps))
    vs = ["R"] * n
    loud = lipsync(mp3, words, offset, fps, dur)  # 0..4 loudness levels, 0 outside words
    for wi, w in enumerate(words):
        key = _re.sub(r"[^\w]", "", w["text"]).lower()
        txt = SPOKEN.get(key, key)
        txt = _re.sub(r"[^a-z ]", "", txt.replace("-", " "))
        syl = _re.findall(r"[^aeiou ]*[aeiou]+", txt) or ["a"]
        f0 = int(round((w["start"] + offset) * fps)); f1 = max(f0 + 1, int(round((w["end"] + offset) * fps)))
        span = (f1 - f0) / len(syl)
        for k, sy in enumerate(syl):
            a = f0 + int(round(k * span)); b = f0 + int(round((k + 1) * span))
            vowel = _re.search(r"[aeiou]", sy).group(0)
            cls = "A" if vowel == "a" else ("E" if vowel in "ei" else "O")
            onset = sy[: sy.index(vowel)]
            m_frames = max(1, int(round(0.3 * (b - a)))) if onset[-1:] in ("m", "b", "p") else 0
            for f in range(a, min(b, n)):
                vs[f] = "M" if f - a < m_frames else cls
        if txt.rstrip()[-1:] in ("m", "b", "p") and f1 - 1 < n:
            vs[f1 - 1] = "M"
        nxt = words[wi + 1] if wi + 1 < len(words) else None
        if nxt is not None and nxt["start"] - w["end"] < 0.12:  # tight word gap: stay relaxed
            for f in range(f1, min(int(round((nxt["start"] + offset) * fps)), n)):
                vs[f] = "N"
    for f in range(n):  # very quiet frames inside words -> relaxed half-open
        if vs[f] in "AEO" and loud[f] == "0":
            vs[f] = "N"
    vs = vs[1:] + ["R"]  # lead the audio by one frame
    for f in range(1, n - 1):  # minimum hold of two frames
        if vs[f] != vs[f - 1] and vs[f] != vs[f + 1]:
            vs[f] = vs[f - 1]
    return "".join(vs)


def blinks(fps, dur, seed=7):
    n = int(round(dur * fps)); s = ["0"] * n
    state = seed
    f = int(1.3 * fps)
    while f < n:
        for k in range(3):
            if f + k < n:
                s[f + k] = "1"
        state = (1103515245 * state + 12345) % 2 ** 31
        f += int((2.6 + 2.2 * (state / 2 ** 31)) * fps)
    return "".join(s)


def main(ep):
    off, fps, dur = arg("--vo-offset", 0.3), arg("--fps", 24), arg("--duration", 85.3)
    hf = os.path.join(ep, "06_hyperframes_source")
    words = json.load(open(os.path.join(ep, "05_voiceover_words.json")))
    kwf = os.path.join(ep, "caption_keywords.txt")
    kws = {norm(l) for l in open(kwf).read().split()} if os.path.exists(kwf) else set()
    gs = merge_short(groups(words, max_words=4, max_chars=21), max_words=5, max_chars=23)
    markup, tweens, srt = [], [], []
    for n, g in enumerate(gs):
        start = max(0.0, g[0]["start"] + off - 0.05)
        end = g[-1]["end"] + off + 0.15
        if n + 1 < len(gs):
            end = min(end, gs[n + 1][0]["start"] + off - 0.06)
        used, spans = False, []
        for w in g:
            t = html.escape(w["text"])
            if not used and norm(w["text"]) in kws:
                spans.append(f'<span class="k">{t}</span>'); used = True
            else:
                spans.append(t)
        cid = f"cap{n:02d}"
        markup.append(f'<div id="{cid}" class="clip cap" data-start="{start:.3f}" data-duration="{end - start:.3f}" '
                      f'data-track-index="10"><div id="{cid}-in" class="cap-in bar{n % 4 + 1}">{" ".join(spans)}</div></div>')
        tweens.append(f'tl.fromTo("#{cid}-in",{{opacity:0,scale:0.86,y:10}},{{opacity:1,scale:1,y:0,duration:0.14,ease:"back.out(2.2)"}},{start:.3f});'
                      f'tl.to("#{cid}-in",{{opacity:0,duration:0.08}},{end - 0.1:.3f});')
        srt.append(f"{n + 1}\n{fmt_srt(start)} --> {fmt_srt(end)}\n{' '.join(w['text'] for w in g)}\n")
    page = open(os.path.join(hf, "src", "index.src.html")).read()
    page = page.replace("<!--@CAPTIONS-->", "\n".join(markup))
    page = page.replace("/*@CAPTION_TWEENS*/", "\n".join(tweens))
    ls = lipsync(os.path.join(ep, "05_voiceover.mp3"), words, off, fps, dur)
    page = page.replace("/*@LIPSYNC*/", f'const LS="{ls}";')
    page = page.replace("/*@BLINK*/", f'const BL="{blinks(fps, dur)}";')
    if "/*@VISEMES*/" in page:
        vs = visemes(os.path.join(ep, "05_voiceover.mp3"), words, off, fps, dur)
        page = page.replace("/*@VISEMES*/", f'const VS="{vs}";')
        print("visemes", {k: vs.count(k) for k in "RAEOMN"})
    open(os.path.join(hf, "index.html"), "w").write(page)
    open(os.path.join(ep, "10_subtitles.srt"), "w").write("\n".join(srt))
    hist = {k: ls.count(str(k)) for k in range(5)}
    print(f"{len(gs)} caption groups; lipsync frames {len(ls)} levels {hist}")


if __name__ == "__main__":
    main(sys.argv[1])
