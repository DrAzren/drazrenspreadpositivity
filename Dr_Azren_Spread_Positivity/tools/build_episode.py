#!/usr/bin/env python3
"""Build an episode's HyperFrames index.html from index.src.html.

- Generates the caption track from the aligned word timings
  (phrase groups of 2-5 words, broken at punctuation and pauses).
- Highlights at most one keyword per group (Whiteboard 2.0 §8).
- Drops AI inset <video> tags whose clip file does not exist yet.
- Writes 10_subtitles.srt from the same timings.

Usage: build_episode.py <episode_dir> [--vo-offset 0.3]
"""
import html, json, os, re, sys

KW = {  # word (lowercase, stripped) -> css class
    "coral": {"ketat", "laju", "mati", "bahaya", "jangan", "menjalar", "teruk", "999"},
    "teal": {"doktor", "nafas", "berlalu", "dirawat", "cbt", "ubat", "baik", "positivity"},
    "swipe": {"lapan", "minit", "sensitif", "gangguan", "alarm"},
}
CLS = {"coral": "kw-c", "teal": "kw-t", "swipe": "kw-y"}


def norm(w):
    return re.sub(r"[^\w]", "", w).lower()


def groups(words, max_words=5, max_chars=30):
    out, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        nxt = words[i + 1] if i + 1 < len(words) else None
        txt = " ".join(x["text"] for x in cur)
        end_sent = re.search(r"[.?!:]$|\.\.\.$|…$", w["text"])
        comma = w["text"].endswith(",") and len(cur) >= 2
        gap = nxt is not None and nxt["start"] - w["end"] >= 0.15
        too_long = len(cur) >= max_words or len(txt) >= max_chars
        if nxt is None or end_sent or comma or (gap and len(cur) >= 2) or too_long:
            out.append(cur); cur = []
    return out


def merge_short(gs, max_words=6, max_chars=34):
    """Merge a group into its neighbour when it is on screen too briefly to read
    (floor: 0.5 s + 0.3 s per word, HyperFrames motion.md), if the result still fits."""
    changed = True
    while changed:
        changed = False
        for i, g in enumerate(gs):
            dur = g[-1]["end"] - g[0]["start"]
            if dur >= 0.35 + 0.25 * len(g):
                continue
            for j in (i + 1, i - 1):
                if 0 <= j < len(gs):
                    a, b = (g, gs[j]) if j > i else (gs[j], g)
                    txt = " ".join(x["text"] for x in a + b)
                    if len(a) + len(b) <= max_words and len(txt) <= max_chars:
                        k = min(i, j); gs[k:k + 2] = [a + b]; changed = True
                        break
            if changed:
                break
    return gs


def fmt_srt(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)):03d}".replace(",1000", ",999")


def main(ep, offset=0.3):
    src = os.path.join(ep, "06_hyperframes_source", "src", "index.src.html")
    dst = os.path.join(ep, "06_hyperframes_source", "index.html")
    words = json.load(open(os.path.join(ep, "05_voiceover_words.json")))
    gs = merge_short(groups(words))
    markup, tweens, srt = [], [], []
    for n, g in enumerate(gs):
        start = max(0.0, g[0]["start"] + offset - 0.06)
        end = g[-1]["end"] + offset + 0.12
        if n + 1 < len(gs):
            end = min(end, gs[n + 1][0]["start"] + offset - 0.07)
        used = False
        spans = []
        for w in g:
            t = html.escape(w["text"])
            k = norm(w["text"])
            cls = next((CLS[c] for c, s in KW.items() if k in s), None)
            if cls and not used:
                spans.append(f'<span class="{cls}">{t}</span>'); used = True
            else:
                spans.append(t)
        cid = f"cap{n:02d}"
        markup.append(f'<div id="{cid}" class="clip cap" data-start="{start:.3f}" data-duration="{end - start:.3f}" '
                      f'data-track-index="10"><div id="{cid}-in" class="cap-in">{" ".join(spans)}</div></div>')
        tweens.append(f'tl.fromTo("#{cid}-in",{{opacity:0,y:12}},{{opacity:1,y:0,duration:0.12,ease:"power2.out"}},{start:.3f});'
                      f'tl.to("#{cid}-in",{{opacity:0,duration:0.1,ease:"power2.in"}},{end - 0.13:.3f});'
                      f'tl.set("#{cid}-in",{{opacity:0,visibility:"hidden"}},{end - 0.02:.3f});')
        srt.append(f"{n + 1}\n{fmt_srt(start)} --> {fmt_srt(end)}\n{' '.join(w['text'] for w in g)}\n")
    page = open(src).read()
    if "--no-captions" in sys.argv:  # clean plates for AI start frames
        markup, tweens = [], []
    page = page.replace("<!--@CAPTIONS-->", "\n".join(markup))
    page = page.replace("/*@CAPTION_TWEENS*/", "\n".join(tweens))
    for vid in ("h1", "h2"):
        if not os.path.exists(os.path.join(ep, "06_hyperframes_source", "assets", "clips", f"{vid}.mp4")):
            page = re.sub(rf'<video id="{vid}".*?</video>\n?', "", page, flags=re.S)
            print(f"note: {vid}.mp4 missing -> using native SVG fallback")
    open(dst, "w").write(page)
    open(os.path.join(ep, "10_subtitles.srt"), "w").write("\n".join(srt))
    print(f"{len(gs)} caption groups -> {dst}")


if __name__ == "__main__":
    off = 0.3
    if "--vo-offset" in sys.argv:
        off = float(sys.argv[sys.argv.index("--vo-offset") + 1])
    main(sys.argv[1], off)
