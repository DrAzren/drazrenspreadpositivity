#!/usr/bin/env python3
"""Harvest a lip-sync mouth atlas from the (AI-lipsynced) reference video. 0 credits.

The reference keeps each pose still while only the mouth moves, so for one pose we:
  1. take every frame in [t0, t1],
  2. align it to the reference frame (t_ref) with template matching on the upper face,
  3. crop the mouth box, measure how "open" it is (pixels that are not skin),
  4. keep N states spread from closed to wide, saved as feathered PNG patches.

The patches are placed on the sprite cut from the t_ref frame at
(mouth_x0 - sprite_x0, mouth_y0 - sprite_y0).

Usage:
  mouth_atlas.py VIDEO OUT_DIR --tref 9.0 --range 7.0 10.5 \
      --face x0 y0 x1 y1 --mouth x0 y0 x1 y1 [--states 5] [--min-score 0.85]
Writes OUT_DIR/mouth_0..N-1.png, atlas.json and atlas_sheet.png.
"""
import argparse, json, os, subprocess

import cv2
import numpy as np


def frames(video, t0, t1, fps=24):
    w, h = 1080, 1920
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{t0}", "-i", video, "-t", f"{t1 - t0}",
           "-vf", f"fps={fps}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    n = len(raw) // (w * h * 3)
    for i in range(n):
        yield t0 + i / fps, np.frombuffer(raw, np.uint8, w * h * 3, i * w * h * 3).reshape(h, w, 3)


def grab(video, t):
    return next(frames(video, t, t + 0.05))[1]


def openness(crop):
    hsv = cv2.cvtColor(crop, cv2.COLOR_RGB2HSV).astype(int)
    h, w = crop.shape[:2]
    border = np.concatenate([hsv[0], hsv[-1], hsv[:, 0], hsv[:, -1]])
    skin = np.median(border, 0)
    d = np.abs(hsv - skin)
    d[..., 0] = np.minimum(d[..., 0], 180 - d[..., 0])
    yy, xx = np.mgrid[0:h, 0:w]
    inner = ((xx - w / 2) / (w * 0.42)) ** 2 + ((yy - h / 2) / (h * 0.42)) ** 2 <= 1
    non_skin = ((d[..., 0] > 12) | (d[..., 1] > 55) | (d[..., 2] > 70)) & inner
    return int(non_skin.sum())


def feather(crop):
    h, w = crop.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - (w - 1) / 2) / (w / 2)) ** 2 + ((yy - (h - 1) / 2) / (h / 2)) ** 2)
    a = np.clip((1.0 - r) / 0.28, 0, 1)
    return np.dstack([crop, (a * 255).astype(np.uint8)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("out")
    ap.add_argument("--tref", type=float, required=True)
    ap.add_argument("--range", nargs=2, type=float, required=True)
    ap.add_argument("--face", nargs=4, type=int, required=True, help="upper-face box used for alignment")
    ap.add_argument("--mouth", nargs=4, type=int, required=True)
    ap.add_argument("--states", type=int, default=5)
    ap.add_argument("--min-score", type=float, default=0.85)
    ap.add_argument("--search", type=int, default=40)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    ref = grab(a.video, a.tref)
    fx0, fy0, fx1, fy1 = a.face
    tmpl = cv2.cvtColor(ref[fy0:fy1, fx0:fx1], cv2.COLOR_RGB2GRAY)
    mx0, my0, mx1, my1 = a.mouth
    S = a.search
    cands = []
    for t, fr in frames(a.video, *a.range):
        g = cv2.cvtColor(fr, cv2.COLOR_RGB2GRAY)
        win = g[max(0, fy0 - S):fy1 + S, max(0, fx0 - S):fx1 + S]
        res = cv2.matchTemplate(win, tmpl, cv2.TM_CCOEFF_NORMED)
        _, score, _, loc = cv2.minMaxLoc(res)
        if score < a.min_score:
            continue
        dx = loc[0] - (fx0 - max(0, fx0 - S)); dy = loc[1] - (fy0 - max(0, fy0 - S))
        crop = fr[my0 + dy:my1 + dy, mx0 + dx:mx1 + dx]
        if crop.shape[:2] != (my1 - my0, mx1 - mx0):
            continue
        cands.append((openness(crop), t, round(score, 3), crop))
    if len(cands) < a.states:
        raise SystemExit(f"only {len(cands)} aligned frames; widen --range or lower --min-score")
    cands.sort(key=lambda c: c[0])
    picks = [cands[round(q * (len(cands) - 1))] for q in np.linspace(0, 1, a.states)]
    meta = {"tref": a.tref, "mouth_box": a.mouth, "aligned_frames": len(cands), "states": []}
    for i, (o, t, sc, crop) in enumerate(picks):
        cv2.imwrite(os.path.join(a.out, f"mouth_{i}.png"), cv2.cvtColor(feather(crop), cv2.COLOR_RGBA2BGRA))
        meta["states"].append({"i": i, "open": o, "t": round(t, 3), "score": sc})
    json.dump(meta, open(os.path.join(a.out, "atlas.json"), "w"), indent=1)
    sheet = np.concatenate([cv2.resize(p[3], (240, int(240 * p[3].shape[0] / p[3].shape[1]))) for p in picks], 1)
    cv2.imwrite(os.path.join(a.out, "atlas_sheet.png"), cv2.cvtColor(sheet, cv2.COLOR_RGB2BGR))
    print(f"{len(cands)} aligned frames -> states open={[p[0] for p in picks]} at t={[round(p[1], 2) for p in picks]}")


if __name__ == "__main__":
    main()
