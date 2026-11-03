#!/usr/bin/env python3
"""Build the shot004 gray-in-mask VACE guide and mask from the Houdini fire proxy.

Outputs two 832x448, 24 fps clips with the same frame count as the source proxy,
plus a JSON report of the settings and per-frame sizes:

- guide: flat RGB 128 inside the body shape, black outside (Mick 1.3 DRIVING VIDEO)
- mask:  the same shape in white on black with a soft edge (Mick 1.3 MASK)

Per frame:

1. Body: the fire's red channel above --threshold, holes filled.
2. Rounded top: a morphological opening with a disk of --round px removes flame
   tongues and the pointed tip narrower than the disk. The largest piece is kept
   and replaced by its convex hull, so the outline has no lumps or notches.
   After scaling (step 3), a second opening with a disk of --round-frac times the
   body's smaller side rounds the corners the hull leaves, so the top is domed.
3. Size: up to --landing the body keeps the Houdini fire's size. After it, the
   fire's own growth is damped. Width and height each follow the fire's growth
   raised to one exponent, chosen so the body's linear size (square root of its
   bounding box's width times height) reaches --post-scale times its landing size
   at --grow-end. The body keeps the fire's timing and grows a little taller
   than wide, as the fire does, but far less. After --grow-end the size holds.
   Scaling is anchored at the bottom centre, so the body stays on the ground.
4. Growth: dilation by --grow px. --post-scale applies before this growth.

Needs numpy and opencv-python (python.org Python 3.11 at /usr/local/bin/python3
has both) and ffmpeg on PATH.

Example:
    /usr/local/bin/python3 scripts/build_shot004_guide.py --out-dir outputs/shot004/pass-a_jerry/guide_v002 \\
        --grow 6 --round 14 --post-scale 1.25
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_control_832x448_81f_v001.mp4"
W, H, FPS = 832, 448, 24


def read_rgb(path: Path) -> np.ndarray:
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
        capture_output=True, check=True,
    ).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)


def write_gray_video(frames: list[np.ndarray], path: Path) -> None:
    proc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "gray", "-s", f"{W}x{H}",
         "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "10", "-preset", "slow",
         "-pix_fmt", "yuv420p", str(path)],
        stdin=subprocess.PIPE,
    )
    for f in frames:
        proc.stdin.write(f.tobytes())
    proc.stdin.close()
    if proc.wait():
        raise SystemExit(f"ffmpeg failed writing {path}")


def disk(radius: int) -> np.ndarray:
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * radius + 1, 2 * radius + 1))


def fill_holes(mask: np.ndarray) -> np.ndarray:
    pad = np.pad(mask, 1).astype(np.uint8) * 255
    cv2.floodFill(pad, None, (0, 0), 128)
    return pad[1:-1, 1:-1] != 128


def hull_of_largest(mask: np.ndarray) -> np.ndarray:
    contours, _ = cv2.findContours(mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if not contours:
        return mask
    out = np.zeros((H, W), np.uint8)
    cv2.fillPoly(out, [cv2.convexHull(max(contours, key=cv2.contourArea))], 1)
    return out.astype(bool)


def body(frame: np.ndarray, threshold: int, round_px: int) -> np.ndarray:
    m = fill_holes(frame[..., 0] > threshold).astype(np.uint8)
    if round_px > 0:
        m = cv2.morphologyEx(m, cv2.MORPH_OPEN, disk(round_px))
    return hull_of_largest(m)


def measure(m: np.ndarray) -> dict[str, float]:
    ys, xs = np.nonzero(m)
    return {
        "area": float(len(xs)), "w": float(xs.max() - xs.min() + 1), "h": float(ys.max() - ys.min() + 1),
        "cx": float(xs.mean()), "bottom": float(ys.max()),
    }


def smooth(values: np.ndarray, radius: int = 2) -> np.ndarray:
    padded = np.pad(values, radius, mode="edge")
    return np.convolve(padded, np.ones(2 * radius + 1) / (2 * radius + 1), mode="valid")


def scale_about(m: np.ndarray, sx: float, sy: float, ax: float, ay: float) -> np.ndarray:
    mat = np.float32([[sx, 0, ax - sx * ax], [0, sy, ay - sy * ay]])
    return cv2.warpAffine(m.astype(np.float32), mat, (W, H), flags=cv2.INTER_LINEAR) > 0.5


def build(args: argparse.Namespace) -> dict:
    src = read_rgb(args.source)
    n = len(src)
    landing = args.landing
    grow_end = n - 1 if args.grow_end is None else args.grow_end
    if not 0 <= landing < grow_end < n:
        raise SystemExit(f"need 0 <= landing ({landing}) < grow-end ({grow_end}) < frames ({n})")

    bodies = [body(f, args.threshold, args.round) for f in src]
    meas = [measure(b) for b in bodies]
    width = smooth(np.array([m["w"] for m in meas]))
    height = smooth(np.array([m["h"] for m in meas]))

    # Linear size = sqrt(width * height) of the body's bounding box.
    fire_growth = math.sqrt(width[grow_end] * height[grow_end] / (width[landing] * height[landing]))
    if fire_growth <= 1.0:
        raise SystemExit(f"the fire does not grow between frames {landing} and {grow_end}")
    alpha = math.log(args.post_scale) / math.log(fire_growth)

    guides, masks, rows = [], [], []
    grow_k = disk(args.grow) if args.grow > 0 else None
    for t, (b, m) in enumerate(zip(bodies, meas)):
        sx = sy = 1.0
        if t > landing:
            ref = min(t, grow_end)
            sx = width[landing] * (width[ref] / width[landing]) ** alpha / width[t]
            sy = height[landing] * (height[ref] / height[landing]) ** alpha / height[t]
            b = scale_about(b, sx, sy, m["cx"], m["bottom"])
        if args.round_frac > 0:
            ys, xs = np.nonzero(b)
            r = int(args.round_frac * min(np.ptp(xs) + 1, np.ptp(ys) + 1))
            b = cv2.morphologyEx(b.astype(np.uint8), cv2.MORPH_OPEN, disk(r)).astype(bool)
        pre = measure(b)
        if grow_k is not None:
            b = cv2.dilate(b.astype(np.uint8), grow_k).astype(bool)
        hard = np.where(b, 255, 0).astype(np.uint8)
        guides.append(np.where(b, 128, 0).astype(np.uint8))
        masks.append(cv2.GaussianBlur(hard, (0, 0), args.soft) if args.soft > 0 else hard)
        out = measure(b)
        rows.append({
            "frame": t, "scale_x": round(sx, 4), "scale_y": round(sy, 4),
            "fire_w": m["w"], "fire_h": m["h"], "fire_area": m["area"],
            "body_w": pre["w"], "body_h": pre["h"], "body_area": pre["area"],
            "guide_w": out["w"], "guide_h": out["h"], "guide_area": out["area"], "guide_bottom": out["bottom"],
        })

    args.out_dir.mkdir(parents=True, exist_ok=True)
    tag = f"grow{args.grow}-round{args.round}-{round(args.round_frac * 100)}-post{round(args.post_scale * 100)}"
    if grow_end != n - 1:
        tag += f"-end{grow_end}"
    stem = f"{W}x{H}_{n}f_{args.version}"
    guide_path = args.out_dir / f"shot004_ren-small-fire6_control-graymask-{tag}_{stem}.mp4"
    mask_path = args.out_dir / f"shot004_ren-small-fire6_mask-{tag}-soft_{stem}.mp4"
    write_gray_video(guides, guide_path)
    write_gray_video(masks, mask_path)
    def linear(row: dict) -> float:
        return math.sqrt(row["body_w"] * row["body_h"])

    body_growth = linear(rows[grow_end]) / linear(rows[landing])
    report = {
        "settings": {k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()} | {"grow_end": grow_end},
        "fire_linear_growth": round(fire_growth, 3), "exponent": round(alpha, 3),
        "body_linear_growth": round(body_growth, 3),
        "guide": str(guide_path), "mask": str(mask_path), "frames": rows,
    }
    (args.out_dir / f"shot004_ren-small-fire6_guide-{tag}_{stem}.json").write_text(json.dumps(report, indent=1))
    return report


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--source", type=Path, default=SOURCE, help="832x448 Houdini fire proxy")
    p.add_argument("--out-dir", type=Path, required=True)
    p.add_argument("--threshold", type=int, default=20, help="red-channel threshold for the fire body")
    p.add_argument("--round", type=int, default=14, help="first opening disk radius in px; removes tongues and the tip")
    p.add_argument("--round-frac", type=float, default=0.3, help="second opening radius as a fraction of the body's smaller side")
    p.add_argument("--grow", type=int, default=6, help="dilation in px after rounding and scaling")
    p.add_argument("--landing", type=int, default=28, help="last frame at the Houdini fire's size")
    p.add_argument("--post-scale", type=float, default=1.25, help="body linear size at --grow-end relative to landing")
    p.add_argument("--grow-end", type=int, default=None, help="frame where growth reaches --post-scale (default: last)")
    p.add_argument("--soft", type=float, default=3.0, help="mask edge Gaussian sigma in px")
    p.add_argument("--version", default="v001")
    report = build(p.parse_args())
    print(report["guide"], report["mask"], sep="\n")
    print(f"fire linear growth {report['fire_linear_growth']}, exponent {report['exponent']}, "
          f"body linear growth {report['body_linear_growth']}")


if __name__ == "__main__":
    main()
