#!/usr/bin/env python3
"""Free, local forced alignment of a KNOWN script to its narration.

Splits the narration at detected pauses, assigns script phrases to the
speech segments by dynamic programming (consistent speaking rate), then
spreads each segment's words by Malay syllable count.

Usage: align_script.py <tts_input.txt> <voiceover audio> <out_words.json>
Display substitutions (spoken -> caption) are applied at the end.
"""
import json, re, subprocess, sys

TAG = re.compile(r"\[[^\]]+\]")
# spoken form -> caption form (multi-word spoken tokens collapse into one caption word)
DISPLAY = [("sembilan sembilan sembilan.", "999."), ("Doktor Azren.", "Dr. Azren.")]


def pauses(audio, noise="-38dB", d="0.18"):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", audio, "-af",
                          f"silencedetect=noise={noise}:d={d}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", out)]
    en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", out)]
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                "-of", "csv=p=0", audio], capture_output=True, text=True).stdout)
    return list(zip(st, en)), dur


def syl(w):
    w = w.lower()
    if w.isupper() or w == "cbt":
        return 3
    return max(1, len(re.findall(r"[aeiouy]+", w)))


def main(script_path, audio, out_path):
    text = TAG.sub("", open(script_path).read())
    words = re.findall(r"\S+", text)
    # phrase boundaries: after any word ending in punctuation
    phrases, cur = [], []
    for w in words:
        cur.append(w)
        if re.search(r"[.,?!:…]$|\.\.\.$", w):
            phrases.append(cur); cur = []
    if cur:
        phrases.append(cur)
    pw = [sum(syl(re.sub(r"[^\w-]", "", w)) for w in p) for p in phrases]

    sil, total = pauses(audio)
    segs, t = [], 0.0
    for s, e in sil:
        if s - t > 0.05:
            segs.append((t, s))
        t = e
    if total - t > 0.05:
        segs.append((t, total))
    n, m = len(phrases), len(segs)
    rate = sum(e - s for s, e in segs) / sum(pw)

    # DP: assign contiguous phrase groups to segments, every segment >= 1 phrase
    INF = float("inf")
    cost = [[INF] * (n + 1) for _ in range(m + 1)]
    back = [[0] * (n + 1) for _ in range(m + 1)]
    cost[0][0] = 0
    for k in range(1, m + 1):
        d = segs[k - 1][1] - segs[k - 1][0]
        for j in range(k, n + 1):
            acc = 0
            for i in range(j - 1, k - 2, -1):
                acc += pw[i]
                c = cost[k - 1][i] + ((d - rate * acc) / max(d, 0.3)) ** 2
                if c < cost[k][j]:
                    cost[k][j], back[k][j] = c, i
    groups, j = [], n
    for k in range(m, 0, -1):
        i = back[k][j]; groups.append((i, j)); j = i
    groups.reverse()

    out = []
    for (i, j), (s, e) in zip(groups, segs):
        ws = [w for p in phrases[i:j] for w in p]
        weights = [syl(re.sub(r"[^\w-]", "", w)) + 0.35 for w in ws]
        tot, t = sum(weights), s
        for w, wt in zip(ws, weights):
            d = (e - s) * wt / tot
            out.append({"text": w, "start": round(t, 3), "end": round(t + d, 3)})
            t += d

    # display substitutions
    joined = " ".join(o["text"] for o in out)
    for spoken, shown in DISPLAY:
        sp = spoken.split()
        for k in range(len(out) - len(sp) + 1):
            if [o["text"] for o in out[k:k + len(sp)]] == sp:
                out[k:k + len(sp)] = [{"text": shown.split()[0] if len(shown.split()) == 1 else None,
                                       "start": out[k]["start"], "end": out[k + len(sp) - 1]["end"]}]
                if len(shown.split()) > 1:  # e.g. "Dr. Azren." keeps two words
                    a, b = shown.split()
                    mid = (out[k]["start"] + out[k]["end"]) / 2
                    out[k:k + 1] = [{"text": a, "start": out[k]["start"], "end": round(mid, 3)},
                                    {"text": b, "start": round(mid, 3), "end": out[k]["end"]}]
                break
    for idx, o in enumerate(out):
        o["id"] = f"w{idx}"
    json.dump(out, open(out_path, "w"), ensure_ascii=False, indent=1)
    print(f"{len(segs)} segments, {n} phrases, {len(out)} words, rate {1/rate:.2f} syl/s")
    for (i, j), (s, e) in zip(groups, segs):
        print(f"{s:6.2f}-{e:6.2f}  {' '.join(w for p in phrases[i:j] for w in p)}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
