#!/usr/bin/env python3
"""Split a white-background character/prop sheet into transparent sprites. 0 credits.

Cells are found by XY-cut (empty columns, then empty rows inside each column band);
inside each cell the white background is flood-filled from the border. Enclosed
background pockets (e.g. the gap between an arm and the body) are removed only when
they are flat pure white, so hatched white clothing (school shirts, sneakers) stays.

Usage:
  sheet_cut.py SHEET OUT_DIR --names a,b,c [--layout row|grid] [--rows R]
               [--x0 X] [--x1 X]   (limit the sheet region, e.g. the left 70 %)
Writes OUT_DIR/<name>.png and OUT_DIR/<name>.json (origin in the sheet).
"""
import argparse, json, os

import cv2
import numpy as np
from PIL import Image
from scipy import ndimage as ndi


POCKET_MIN = 2500
REMOVE_POCKETS = False


def bgmask(rgb):
    mn = rgb.min(2).astype(int); mx = rgb.max(2).astype(int)
    return (mn > 228) & (mx - mn < 22)


def segments(proj, min_gap=14, thresh=2):
    on = proj > thresh
    segs, start, gap = [], None, 0
    for i, v in enumerate(on):
        if v:
            if start is None:
                start = i
            gap = 0
        elif start is not None:
            gap += 1
            if gap >= min_gap:
                segs.append([start, i - gap + 1]); start = None; gap = 0
    if start is not None:
        segs.append([start, len(on)])
    return segs


def top_n(segs, proj, n):
    mass = [proj[a:b].sum() for a, b in segs]
    keep = sorted(np.argsort(mass)[::-1][:n])
    return [segs[i] for i in keep]


def cut_cell(rgb, box, own=None):
    x0, y0, x1, y1 = box
    c = rgb[y0:y1, x0:x1]
    bg = bgmask(c)
    lab, _ = ndi.label(bg)
    border = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    outside = np.isin(lab, border[border != 0])
    fg = ~outside
    if own is not None:  # component mode: only this figure (neighbours' hands excluded)
        fg = ndi.binary_fill_holes(own[y0:y1, x0:x1])
    fg = ndi.binary_opening(fg, iterations=1)
    lab2, n = ndi.label(fg)
    if not n:
        return None, None
    sizes = ndi.sum(fg, lab2, range(1, n + 1))
    big = int(np.argmax(sizes)) + 1
    ys, xs = np.where(lab2 == big)
    bx0, bx1, by0, by1 = xs.min(), xs.max(), ys.min(), ys.max()
    keep = [big]
    for i, s in enumerate(sizes, 1):  # detached parts that sit inside the main figure's box
        if i == big or s < 0.01 * sizes[big - 1]:
            continue
        yy, xx = np.where(lab2 == i)
        cx, cy = xx.mean(), yy.mean()
        if bx0 <= cx <= bx1 and by0 <= cy <= by1:
            keep.append(i)
    fg = np.isin(lab2, keep)
    # enclosed flat-white pockets -> transparent
    grey = cv2.cvtColor(c, cv2.COLOR_RGB2GRAY).astype(float)
    lab3, n3 = ndi.label(bg & fg)
    pockets = []
    for i in range(1, n3 + 1):
        m = lab3 == i
        a = m.sum()
        if a > POCKET_MIN and grey[m].mean() > 246 and grey[m].std() < 5:
            yy, xx = np.where(m)
            pockets.append((int(a), x0 + int(xx.mean()), y0 + int(yy.mean())))
            if REMOVE_POCKETS:
                fg &= ~m
    if pockets:
        print("   pockets (area, cx, cy):", sorted(pockets, reverse=True)[:6])
    alpha = cv2.GaussianBlur(fg.astype(np.float32), (0, 0), 0.9)
    alpha = np.clip((alpha - 0.15) / 0.7, 0, 1)
    rgba = np.dstack([c, (alpha * 255).astype(np.uint8)])
    ys, xs = np.where(alpha > 0.03)
    tx, ty = xs.min(), ys.min()
    return rgba[ty:ys.max() + 1, tx:xs.max() + 1], (x0 + int(tx), y0 + int(ty))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sheet"); ap.add_argument("out")
    ap.add_argument("--names", required=True)
    ap.add_argument("--layout", choices=["row", "grid", "comp"], default="row")
    ap.add_argument("--rows", type=int, default=1)
    ap.add_argument("--x0", type=int, default=0); ap.add_argument("--x1", type=int, default=0)
    ap.add_argument("--min-gap", type=int, default=14)
    ap.add_argument("--pocket", nargs=2, type=int, action="append", default=[],
                    help="x y (sheet coords) inside a background pocket to make transparent")
    a = ap.parse_args()
    names = a.names.split(",")
    rgb = np.array(Image.open(a.sheet).convert("RGB"))
    H, W = rgb.shape[:2]
    X0, X1 = a.x0, (a.x1 or W)
    fgm = ~bgmask(rgb)
    fgm[:, :X0] = False; fgm[:, X1:] = False
    boxes, owns = [], []
    if a.layout == "comp":
        lab, n = ndi.label(fgm)
        sizes = ndi.sum(fgm, lab, range(1, n + 1))
        ids = [int(i) + 1 for i in np.argsort(sizes)[::-1][:len(names)]]
        ids.sort(key=lambda i: np.where(lab == i)[1].min())
        for i in ids:
            m = lab == i
            ys, xs = np.where(m)
            boxes.append((int(max(xs.min() - 6, 0)), int(max(ys.min() - 6, 0)), int(min(xs.max() + 7, W)), int(min(ys.max() + 7, H))))
            owns.append(m)
    elif a.layout == "row":
        cols = top_n(segments(fgm.sum(0), min_gap=a.min_gap), fgm.sum(0), len(names))
        for cx0, cx1 in cols:
            rp = fgm[:, cx0:cx1].sum(1)
            rs = top_n(segments(rp, min_gap=30), rp, 1)[0]
            boxes.append((max(cx0 - 6, 0), max(rs[0] - 6, 0), min(cx1 + 6, W), min(rs[1] + 6, H)))
    else:
        ncol = len(names) // a.rows
        rp = fgm.sum(1)
        rows = top_n(segments(rp, min_gap=10), rp, a.rows)
        for ry0, ry1 in rows:
            band = fgm[ry0:ry1]
            cp = band.sum(0)
            cols = top_n(segments(cp, min_gap=10), cp, ncol)
            for cx0, cx1 in cols:
                boxes.append((max(cx0 - 6, 0), max(ry0 - 6, 0), min(cx1 + 6, W), min(ry1 + 6, H)))
    os.makedirs(a.out, exist_ok=True)
    for k, (name, box) in enumerate(zip(names, boxes)):
        own = owns[k] if owns else None
        spr, org = cut_cell(rgb, box, own)
        if spr is None:
            print("empty cell", name); continue
        # explicit background pockets (flood from the given sheet point within white pixels)
        for px, py in a.pocket:
            ox, oy = org
            if 0 <= px - ox < spr.shape[1] and 0 <= py - oy < spr.shape[0]:
                wm = bgmask(spr[..., :3])
                lab, _ = ndi.label(wm)
                li = lab[py - oy, px - ox]
                if li:
                    spr[..., 3][lab == li] = 0
                    print(f"   pocket cleared at {px},{py} in {name}")
        if spr is None:
            print("empty cell", name); continue
        Image.fromarray(spr).save(os.path.join(a.out, f"{name}.png"), optimize=True)
        json.dump({"source": os.path.basename(a.sheet), "cell": box, "origin": org,
                   "size": [spr.shape[1], spr.shape[0]]}, open(os.path.join(a.out, f"{name}.json"), "w"))
        print(f"{name}: {spr.shape[1]}x{spr.shape[0]} at {org}")


if __name__ == "__main__":
    main()
