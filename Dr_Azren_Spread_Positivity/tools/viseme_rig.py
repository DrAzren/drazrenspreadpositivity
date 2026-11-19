#!/usr/bin/env python3
"""Build lip-sync mouth patches for full-body Dr. Azren poses from a head/viseme sheet. 0 credits.

Inputs: six head close-ups of the same face (rest, A, E, O, M, neutral) cut by sheet_cut.py,
and full-body pose sprites. For each pose:
  1. find both pupils in the close-up and in the pose (dark round blobs ringed by eye white),
  2. build the similarity transform (scale + rotation + shift) close-up -> pose from the pupils,
  3. find the mouth box from where the six close-ups differ,
  4. warp each viseme's mouth into the pose, colour-match it to the pose skin, feather it,
  5. store pupil positions, eye radius, head angle and eyelid skin colour for blink lids.
Writes OUT/<pose>/mouth_<viseme>.png, OUT/<pose>/check.jpg and OUT/rigs.json.

Usage: viseme_rig.py HEADS_DIR POSES_DIR OUT_DIR pose1 pose2 ...
"""
import json, math, os, sys

import cv2
import numpy as np
from PIL import Image

VIS = ["rest", "A", "E", "O", "M", "neutral"]


def load(p):
    return np.array(Image.open(p).convert("RGBA"))


def flat(rgba, bg=247):
    a = rgba[..., 3:4] / 255.0
    return (rgba[..., :3] * a + bg * (1 - a)).astype(np.uint8)


def pupils(rgba, frac):
    h = rgba.shape[0]; top = int(frac * h)
    rgb = rgba[..., :3].astype(float)
    g = (0.3 * rgb[..., 0] + 0.59 * rgb[..., 1] + 0.11 * rgb[..., 2])[:top]
    m = ((g < 70) & (rgba[:top, :, 3] > 200)).astype(np.uint8)
    n, lab, st, cen = cv2.connectedComponentsWithStats(m)
    cands = []
    for i in range(1, n):
        x, y, ww, hh, ar = st[i]
        if 30 < ar < 1500 and 0.5 < ww / max(hh, 1) < 2.0 and ar / (ww * hh) > 0.45:
            cx, cy = cen[i]; r = int(max(ww, hh))
            ring = g[max(int(cy) - 2 * r, 0):int(cy) + 2 * r, max(int(cx) - 2 * r, 0):int(cx) + 2 * r]
            cands.append(((ring > 200).mean(), cx, cy, ar))
    cands.sort(reverse=True)
    if len(cands) < 2:
        raise SystemExit("pupils not found")
    a, b = sorted(cands[:2], key=lambda c: c[1])
    return np.array([a[1], a[2]]), np.array([b[1], b[2]]), (a[3] + b[3]) / 2


def similarity(src_a, src_b, dst_a, dst_b):
    vs, vd = src_b - src_a, dst_b - dst_a
    s = np.linalg.norm(vd) / np.linalg.norm(vs)
    th = math.atan2(vd[1], vd[0]) - math.atan2(vs[1], vs[0])
    c, si = s * math.cos(th), s * math.sin(th)
    R = np.array([[c, -si], [si, c]])
    t = dst_a - R @ src_a
    return np.hstack([R, t[:, None]]).astype(np.float32), s, math.degrees(th)


def main(heads_dir, poses_dir, out_dir, poses):
    heads = {v: load(os.path.join(heads_dir, f"head_{v}.png")) for v in VIS}
    H0 = min(h.shape[0] for h in heads.values()); W0 = min(h.shape[1] for h in heads.values())
    heads = {k: v[:H0, :W0] for k, v in heads.items()}
    g = {k: cv2.cvtColor(flat(v), cv2.COLOR_RGB2GRAY).astype(np.float32) for k, v in heads.items()}
    up = slice(int(.25 * H0), int(.6 * H0))
    al = {}
    for k in VIS:  # align the six close-ups on the upper face
        (dx, dy), _ = cv2.phaseCorrelate(g["rest"][up], g[k][up])
        M = np.float32([[1, 0, -dx], [0, 1, -dy]])
        al[k] = cv2.warpAffine(heads[k], M, (W0, H0), borderMode=cv2.BORDER_REPLICATE)
    # mouth box = union of lip pixels (dark line / red lips & tongue) over all visemes,
    # inside the lower-face band (the close-ups include shoulders, so the band is 52-70 % of height)
    union = np.zeros((H0, W0), bool)
    for k in VIS:
        c = al[k].astype(int)
        lum = 0.3 * c[..., 0] + 0.59 * c[..., 1] + 0.11 * c[..., 2]
        m = (lum < 110) | ((c[..., 0] > 150) & (c[..., 1] < 120) & (c[..., 2] < 130))
        m &= c[..., 3] > 200
        m[:int(.52 * H0)] = False; m[int(.70 * H0):] = False
        m[:, :int(.30 * W0)] = False; m[:, int(.70 * W0):] = False
        union |= m
    ys, xs = np.where(union)
    mx0, mx1 = int(xs.min()) - 12, int(xs.max()) + 12
    my0, my1 = int(ys.min()) - 9, int(ys.max()) + 9
    bw0, bh0 = mx1 - mx0, my1 - my0
    yy, xx = np.mgrid[0:bh0, 0:bw0]
    rr = np.sqrt(((xx - (bw0 - 1) / 2) / (bw0 / 2)) ** 2 + ((yy - (bh0 - 1) / 2) / (bh0 / 2)) ** 2)
    feather = (np.clip((1 - rr) / 0.32, 0, 1) * 255).astype(np.uint8)
    hl, hr, harea = pupils(al["rest"], 0.8)
    eye_r0 = math.sqrt(harea / math.pi) * 1.9  # eye-white radius from the pupil size
    os.makedirs(out_dir, exist_ok=True)
    report = {}
    for pose in poses:
        P = load(os.path.join(poses_dir, f"{pose}.png"))
        pl, pr, _ = pupils(P, 0.22)
        M, s, ang = similarity(hl, hr, pl, pr)
        Hp, Wp = P.shape[:2]
        # mouth box corners -> pose bbox
        corners = np.array([[mx0, my0], [mx1, my0], [mx0, my1], [mx1, my1]], np.float32)
        pc = cv2.transform(corners[None], M)[0]
        bx0, by0 = np.floor(pc.min(0)).astype(int); bx1, by1 = np.ceil(pc.max(0)).astype(int)
        # colour gain: skin ring around the mouth, pose vs close-up
        def skin_med(img, x0, y0, x1, y1):
            r = img[max(y0, 0):y1, max(x0, 0):x1, :3].reshape(-1, 3).astype(float)
            r = r[(r.sum(1) > 330) & (r.sum(1) < 720)]
            return np.median(r, 0) if len(r) else None
        tgt = skin_med(P, bx0 - 8, by0 - 8, bx1 + 8, by1 + 8)
        src = skin_med(al["rest"], mx0 - 10, my0 - 10, mx1 + 10, my1 + 10)
        gain = np.clip(tgt / np.maximum(src, 1), 0.8, 1.25) if tgt is not None else np.ones(3)
        pd = os.path.join(out_dir, pose); os.makedirs(pd, exist_ok=True)
        for v in VIS:
            canvas = np.zeros((H0, W0, 4), np.uint8)
            crop = np.clip(al[v][my0:my1, mx0:mx1, :3].astype(float) * gain, 0, 255).astype(np.uint8)
            canvas[my0:my1, mx0:mx1] = np.dstack([crop, feather])
            warped = cv2.warpAffine(canvas, M, (Wp, Hp), flags=cv2.INTER_LINEAR, borderValue=(0, 0, 0, 0))
            Image.fromarray(warped[by0:by1, bx0:bx1]).save(os.path.join(pd, f"mouth_{v}.png"))
        # eyelid colour: cheek below each pupil
        eyes = []
        for p in (pl, pr):
            col = skin_med(P, int(p[0] - 14 * s), int(p[1] + 42 * s), int(p[0] + 14 * s), int(p[1] + 62 * s))
            col = col if col is not None else (tgt if tgt is not None else np.array([240, 190, 150]))
            eyes.append({"x": round(float(p[0]), 1), "y": round(float(p[1]), 1), "skin": "#%02x%02x%02x" % tuple(int(c) for c in col)})
        report[pose] = {"scale": round(s, 3), "angle": round(ang, 1), "eye_r": round(eye_r0 * s, 1),
                        "mouth": {"x": int(bx0), "y": int(by0), "w": int(bx1 - bx0), "h": int(by1 - by0)},
                        "eyes": eyes, "size": [int(Wp), int(Hp)]}
        tiles = []
        for v in VIS:
            im = Image.fromarray(flat(P)).convert("RGBA")
            im.alpha_composite(Image.open(os.path.join(pd, f"mouth_{v}.png")), (int(bx0), int(by0)))
            cx, cy = (bx0 + bx1) // 2, (by0 + by1) // 2
            tiles.append(im.crop((cx - 110, cy - 150, cx + 110, cy + 70)).resize((220, 220)))
        sheet = Image.new("RGB", (220 * 6, 220), "white")
        for i, t in enumerate(tiles):
            sheet.paste(t, (220 * i, 0))
        sheet.save(os.path.join(pd, "check.jpg"))
        print(pose, report[pose])
    json.dump(report, open(os.path.join(out_dir, "rigs.json"), "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
