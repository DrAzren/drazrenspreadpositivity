#!/usr/bin/env python3
"""Technical QA for a delivered episode MP4 (Whiteboard 2.0 spec).

Checks: 1080x1920, 30 fps, H.264 + AAC, duration <= max, integrated loudness
-14 LUFS (+/-1.5), true peak <= -1 dBTP, black frames, frozen spans.
Usage: qa_video.py <video.mp4> [--max 90] [--sheet out.jpg]
"""
import json, re, subprocess, sys


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def main(path, max_dur=90.0, sheet=None):
    pr = json.loads(run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path]).stdout)
    v = next(s for s in pr["streams"] if s["codec_type"] == "video")
    a = next((s for s in pr["streams"] if s["codec_type"] == "audio"), None)
    dur = float(pr["format"]["duration"])
    num, den = map(int, v["r_frame_rate"].split("/"))
    ln = run(["ffmpeg", "-hide_banner", "-i", path, "-af", "loudnorm=print_format=json", "-f", "null", "-"]).stderr
    lj = json.loads(ln[ln.rfind("{"):ln.rfind("}") + 1])
    blk = run(["ffmpeg", "-hide_banner", "-i", path, "-vf", "blackdetect=d=0.1:pic_th=0.98", "-an", "-f", "null", "-"]).stderr
    frz = run(["ffmpeg", "-hide_banner", "-i", path, "-vf", "freezedetect=n=0.001:d=4", "-an", "-f", "null", "-"]).stderr
    checks = [
        ("resolution 1080x1920", v["width"] == 1080 and v["height"] == 1920, f'{v["width"]}x{v["height"]}'),
        ("fps 30", round(num / den, 3) == 30.0, f"{num}/{den}"),
        ("video H.264", v["codec_name"] == "h264", v["codec_name"]),
        ("pixel format yuv420p", v.get("pix_fmt") == "yuv420p", v.get("pix_fmt")),
        ("audio AAC", a is not None and a["codec_name"] == "aac", a and a["codec_name"]),
        (f"duration <= {max_dur:g}s", dur <= max_dur, f"{dur:.2f}s"),
        ("loudness -14 LUFS +/-1.5", abs(float(lj["input_i"]) + 14) <= 1.5, f'{lj["input_i"]} LUFS'),
        ("true peak <= -1 dBTP", float(lj["input_tp"]) <= -1.0, f'{lj["input_tp"]} dBTP'),
        ("no black frames", "black_start" not in blk, ";".join(re.findall(r"black_start:[\d.]+ black_end:[\d.]+", blk)) or "none"),
        ("no frozen span >= 4s", "freeze_start" not in frz, ";".join(re.findall(r"freeze_start: [\d.]+", frz)) or "none"),
    ]
    ok = all(c[1] for c in checks)
    for name, passed, val in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {name:28s} {val}")
    if sheet:
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", path, "-vf",
             "fps=1/4,scale=216:384,tile=7x3", "-frames:v", "1", sheet])
    return 0 if ok else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    mx = float(args[args.index("--max") + 1]) if "--max" in args else 90.0
    sh = args[args.index("--sheet") + 1] if "--sheet" in args else None
    sys.exit(main(args[0], mx, sh))
