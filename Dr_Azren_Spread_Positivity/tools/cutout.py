#!/usr/bin/env python3
"""Cut a transparent sprite out of a whiteboard illustration (zero credits, local).

The DoodleVerse art has closed black marker outlines on a near-white board, so the
background can be found by flood-filling "board-like" pixels (bright, low saturation)
from the crop border. Anything the fill can't reach (inside an outline) is kept.

Usage:
  cutout.py IN.png OUT.png --box x0 y0 x1 y1 [--erase x0 y0 x1 y1 ...]
            [--keep largest|all] [--min-area 400] [--sat 40] [--val 170] [--feather 1.2]

--erase   rectangles (in source-image coordinates) forced to background, e.g. a
          burned-in caption bar.
--keep    'largest' keeps only the biggest connected subject (drops stray doodles),
          'all' keeps every island above --min-area.
"""
import argparse

import cv2
import numpy as np
from PIL import Image
from scipy import ndimage as ndi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--box", nargs=4, type=int, required=True)
    ap.add_argument("--erase", nargs=4, type=int, action="append", default=[])
    ap.add_argument("--keep", choices=["largest", "all"], default="largest")
    ap.add_argument("--min-area", type=int, default=400)
    ap.add_argument("--sat", type=int, default=40, help="max saturation (0-255) of board pixels")
    ap.add_argument("--val", type=int, default=170, help="min brightness (0-255) of board pixels")
    ap.add_argument("--feather", type=float, default=1.2)
    ap.add_argument("--hole-min", type=int, default=6000,
                    help="enclosed board gaps at least this many px become transparent")
    a = ap.parse_args()

    img = np.array(Image.open(a.inp).convert("RGB"))
    for x0, y0, x1, y1 in a.erase:
        img[y0:y1, x0:x1] = 245  # paint the region as board so it floods away
    x0, y0, x1, y1 = a.box
    img = img[y0:y1, x0:x1].copy()

    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    boardlike = (hsv[..., 1] <= a.sat) & (hsv[..., 2] >= a.val)
    # flood from the border: label board-like regions and keep those touching an edge
    lab, _ = ndi.label(boardlike)
    edge_ids = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    edge_ids = edge_ids[edge_ids != 0]
    bg = np.isin(lab, edge_ids)

    fg = ~bg
    fg = ndi.binary_opening(fg, iterations=1)
    lab2, n = ndi.label(fg)
    if n:
        sizes = ndi.sum(fg, lab2, range(1, n + 1))
        if a.keep == "largest":
            fg = lab2 == (int(np.argmax(sizes)) + 1)
        else:
            keep = [i + 1 for i, s in enumerate(sizes) if s >= a.min_area]
            fg = np.isin(lab2, keep)
    # Board showing through enclosed gaps (between an arm and the body) is still
    # board: drop enclosed board-like regions larger than --hole-min. Small ones
    # (eye whites, shoe highlights) stay opaque.
    lab3, n3 = ndi.label(boardlike & fg)
    if n3:
        sizes3 = ndi.sum(np.ones_like(lab3), lab3, range(1, n3 + 1))
        big = [i + 1 for i, s in enumerate(sizes3) if s >= a.hole_min]
        fg &= ~np.isin(lab3, big)

    alpha = fg.astype(np.float32)
    if a.feather > 0:
        alpha = cv2.GaussianBlur(alpha, (0, 0), a.feather)
        alpha = np.clip((alpha - 0.15) / 0.7, 0, 1)
    rgba = np.dstack([img, (alpha * 255).astype(np.uint8)])
    # trim to content
    ys, xs = np.where(rgba[..., 3] > 8)
    tx = ty = 0
    if len(xs):
        tx, ty = int(xs.min()), int(ys.min())
        rgba = rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    Image.fromarray(rgba).save(a.out, optimize=True)
    # sidecar: where the sprite's (0,0) sits in the source image (for mouth/eye patches)
    import json
    json.dump({"source": a.inp.split("/")[-1], "box": a.box, "origin": [x0 + tx, y0 + ty],
               "size": [rgba.shape[1], rgba.shape[0]]}, open(a.out.rsplit(".", 1)[0] + ".json", "w"))
    print(f"{a.out}: {rgba.shape[1]}x{rgba.shape[0]} origin=({x0 + tx},{y0 + ty})")


if __name__ == "__main__":
    main()
