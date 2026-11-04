#!/usr/bin/env python3
"""Build the shot004 grass-fire inpainting inputs for the Mick 1.3 graph (Pass B, candidate 2).

Outputs (912x512, 24 fps, --frames frames, a 2x downscale of a 1824x1024 window of the
4096x2160 plate, so the inpaint keeps twice the detail of a full-frame 512p run):

- control: the plate outside the mask; inside it, the plate's Canny edges on black
  (--inside canny, the recipe of Mickmumpitz's OfficeFlood example: blades keep their
  structure), flat mid-gray (--inside gray: the model draws freely), or the edges on
  mid-gray (--inside canny-gray: structure without telling the model to keep black). DRIVING VIDEO.
- mask: white where the model may draw, soft edge. Empty before --start; from there it
  spreads from the ignition point (Jerry's landing contact) through the burn zone
  (the grass clump and the air above it) until --full, then holds. MASK. With --field
  below 1, only the blades inside the spread (strong plate edges grown by --blade-grow px)
  are full white; the rest of the spread is --field (e.g. 0.5), a looser "may change".
  Note the graph's Compose + Match pastes the result with this mask, so a field of 0.5
  also mixes the plate back in at half strength there.
- start: the plate window's first frame as a still (start image / reference).
- a JSON report of the settings and per-frame mask coverage.

The window, ignition point and burn zone are in window pixels (912x512). Placing a result
back on the plate: scale x2 and put its top-left corner at plate (WINDOW_X, WINDOW_Y).

Needs numpy and opencv-python (/usr/local/bin/python3 has both) and ffmpeg.

    /usr/local/bin/python3 shots/shot004_fire-jump/scripts/build_shot004_grassfire_inputs.py --out-dir shots/shot004_fire-jump/outputs/pass-b_grassfire/inpaint_v001
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[3]  # repo root; this file is shots/<shot>/scripts/
PLATE = ROOT / "shots/shot004_fire-jump/plates/FW_test_scene.mp4"
WINDOW_X, WINDOW_Y, WINDOW_W, WINDOW_H = 1838, 488, 1824, 1024  # on the 4096x2160 plate
W, H, FPS = 912, 512, 24

# Grass clump and the air above it, where flames may appear (window pixels).
# Kept MARGIN px inside the window so flames never touch its edges, where the inpaint
# meets the untouched plate around it.
BURN_ZONE = [(300, 445), (630, 445), (740, 350), (830, 220), (860, 110), (800, 55), (600, 45),
             (450, 60), (300, 45), (130, 60), (70, 130), (110, 240), (200, 350)]
MARGIN = 24
IGNITION = (490, 450)  # Jerry's landing contact, frames 26-28


def read_window(frames: int) -> np.ndarray:
    vf = f"crop={WINDOW_W}:{WINDOW_H}:{WINDOW_X}:{WINDOW_Y},scale={W}:{H}:flags=area"
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(PLATE), "-vf", vf, "-frames:v", str(frames),
         "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
        capture_output=True, check=True,
    ).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)


def write_video(frames: list[np.ndarray], path: Path, pix: str) -> None:
    proc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", pix, "-s", f"{W}x{H}",
         "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "12", "-preset", "slow",
         "-pix_fmt", "yuv420p", str(path)],
        stdin=subprocess.PIPE,
    )
    for f in frames:
        proc.stdin.write(np.ascontiguousarray(f).tobytes())
    proc.stdin.close()
    if proc.wait():
        raise SystemExit(f"ffmpeg failed writing {path}")


def smooth_noise(seed: int, scale: int) -> np.ndarray:
    """Low-frequency noise in [-1, 1], used to make the fire front irregular."""
    rng = np.random.default_rng(seed)
    small = rng.standard_normal((H // scale + 2, W // scale + 2)).astype(np.float32)
    big = cv2.resize(small, (W, H), interpolation=cv2.INTER_CUBIC)
    return np.clip(big / 2.0, -1, 1)


def build(args: argparse.Namespace) -> dict:
    plate = read_window(args.frames)
    n = len(plate)
    key, key_groups = None, []
    if args.keyframe:
        key = cv2.cvtColor(cv2.imread(str(args.keyframe)), cv2.COLOR_BGR2RGB)
        if key.shape[:2] != (H, W):
            key = cv2.resize(key, (W, H), interpolation=cv2.INTER_AREA)
        key_groups = [tuple(int(x) for x in g.split("-")) for g in args.key_frames.split(",")]
    poly = np.zeros((H, W), np.float32)
    cv2.fillPoly(poly, [np.array(BURN_ZONE, np.int32)], 1.0)
    if args.zone_from_key:
        # Widen the zone to hold the keyframe's own flames, so the mask does not cut them
        # (test 15: 38% of k2's fire lay outside the burn zone and the cut drew the outline).
        k = key.astype(np.int16)
        flames = ((k[..., 0] >= 170) & (k[..., 0] - k[..., 2] >= 50)).astype(np.uint8)
        flames = cv2.morphologyEx(cv2.dilate(flames, np.ones((21, 21), np.uint8)), cv2.MORPH_CLOSE,
                                  cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (41, 41)))
        poly = np.maximum(poly, flames.astype(np.float32))
    # Organic zone edge: blur the polygon and push its 0.5 contour around with noise.
    zone = (cv2.GaussianBlur(poly, (0, 0), 20) + 0.3 * smooth_noise(args.seed + 1, 40)) > 0.5
    zone[:MARGIN] = zone[-MARGIN:] = False
    zone[:, :MARGIN] = zone[:, -MARGIN:] = False
    zone = zone.astype(np.uint8)

    # Distance from the ignition point, with vertical distance shrunk so fire climbs faster
    # than it spreads sideways. Normalised so the farthest burn-zone pixel is 1.
    ys, xs = np.mgrid[0:H, 0:W].astype(np.float32)
    dist = np.hypot(xs - IGNITION[0], (ys - IGNITION[1]) * args.climb)
    dist /= dist[zone.astype(bool)].max()
    noise = smooth_noise(args.seed, 24)

    controls, masks, coverage, blade_cover = [], [], [], []
    for t in range(n):
        if t < args.start:
            front = -1.0
        elif args.growth == "static":
            front = 10.0  # the whole zone from --start on; the model decides how the fire grows
        else:
            p = min(1.0, (t - args.start + 1) / max(1, args.full - args.start))
            front = p ** args.ease  # ease < 1: fast catch, slower finish
        # The front advances through dist; noise drifts slowly so the edge flickers a little.
        drift = np.roll(noise, shift=int(t * 0.7), axis=0) if t >= args.start else noise
        hard = ((dist + args.ragged * drift * (1 - min(front, 1.0)) * 0.5) <= front) & zone.astype(bool)
        hard_u8 = hard.astype(np.uint8)
        if t >= args.start:
            cv2.circle(hard_u8, IGNITION, 6, 1, -1)
            # Close small gaps so the fire region is one body, not speckles.
            hard_u8 = cv2.morphologyEx(hard_u8, cv2.MORPH_CLOSE,
                                       cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))) & zone
        hard = hard_u8.astype(bool)
        hard_u8 = hard_u8 * 255
        gray = cv2.cvtColor(plate[t], cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(cv2.GaussianBlur(gray, (0, 0), 1.0), args.canny_low, args.canny_high)
        if args.inside == "canny":
            fill = np.repeat(edges[..., None], 3, axis=2)
        elif args.inside == "canny-gray":
            fill = np.full_like(plate[t], 128)
            fill[edges > 0] = 255
        else:  # flat mid-gray: VACE's "generate freely here"
            fill = np.full_like(plate[t], 128)
        control = np.where(hard[..., None], fill, plate[t])
        if args.field < 1.0 and t >= args.start:
            # Full strength on the blades, --field on the space around them.
            strong = cv2.Canny(cv2.GaussianBlur(gray, (0, 0), 1.5), args.blade_low, args.blade_high)
            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * args.blade_grow + 1,) * 2)
            blades = ((cv2.dilate(strong, k) > 0) & hard).astype(np.uint8)
            cv2.circle(blades, IGNITION, 10, 1, -1)
            blades = blades.astype(bool) & hard
            hard_u8 = np.where(blades, 255, np.where(hard, round(255 * args.field), 0)).astype(np.uint8)
            blade_cover.append(round(float(blades.mean()), 4))
            if args.field_fill == "plate":
                # A partial mask keeps that share of the control, so the half-strength area must
                # show the plate (half keep the grass), not gray (test 11: a gray veil).
                control = np.where(blades[..., None], fill, plate[t])
        soft = cv2.GaussianBlur(hard_u8, (0, 0), args.soft) if args.soft > 0 else hard_u8
        if key is not None and any(a0 <= t <= a1 for a0, a1 in key_groups):
            # Keyframe: the still inside the current spread (softened edge), the plate outside
            # it, and mask 0 on the whole frame so the model keeps it. Limited to the current
            # spread, earlier groups show only the part of the fire that has caught so far.
            # The model groups frames by four (latent j holds frames 4j-3..4j and reads the
            # mask at its last frame), so each group should fill one whole latent, e.g. 49-52.
            a = cv2.GaussianBlur(cv2.dilate(hard_u8, np.ones((25, 25), np.uint8)), (0, 0), 12)[..., None] / 255.0
            control = (key * a + plate[t] * (1 - a)).round().astype(np.uint8)
            soft = np.zeros_like(soft)
        controls.append(control)
        masks.append(soft)
        coverage.append(round(float(hard.mean()), 4))

    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)
    tag = f"start{args.start}-full{args.full}" if args.growth == "front" else f"start{args.start}-static"
    tag += "-keyzone" if args.zone_from_key else ""
    stem = f"{W}x{H}_{n}f_{args.version}"
    mask_kind = "soft" if args.field >= 1.0 else f"blades{args.blade_grow}-field{round(args.field * 100):03d}-soft"
    inside_kind = args.inside if args.field >= 1.0 or args.field_fill == "inside" else f"{args.inside}-blades{args.blade_grow}"
    key_kind = "" if key is None else f"-key{args.keyframe_tag}-f" + "-".join(f"{a0:03d}-{a1:03d}" for a0, a1 in key_groups)
    control_path = out / f"shot004_grassfire_control-plate-{inside_kind}{key_kind}-{tag}_{stem}.mp4"
    mask_path = out / f"shot004_grassfire_mask-{tag}-{mask_kind}{key_kind}_{stem}.mp4"
    start_path = out / f"shot004_grassfire_start-frame_{W}x{H}_{args.version}.png"
    write_video(controls, control_path, "rgb24")
    write_video(masks, mask_path, "gray")
    cv2.imwrite(str(start_path), cv2.cvtColor(plate[0], cv2.COLOR_RGB2BGR))
    report = {
        "settings": {k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
        "window_on_plate": {"x": WINDOW_X, "y": WINDOW_Y, "w": WINDOW_W, "h": WINDOW_H, "scale_to_plate": 2.0},
        "burn_zone": BURN_ZONE, "ignition": IGNITION,
        "control": str(control_path), "mask": str(mask_path), "start_image": str(start_path),
        "coverage": coverage, "blade_coverage": blade_cover,
    }
    kind = args.inside if args.field >= 1.0 else f"{args.inside}-{mask_kind}" + ("-platefield" if args.field_fill == "plate" else "")
    kind += key_kind
    (out / f"shot004_grassfire_inputs-{kind}-{tag}_{stem}.json").write_text(json.dumps(report, indent=1))
    return report


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--out-dir", type=Path, required=True)
    p.add_argument("--frames", type=int, default=81)
    p.add_argument("--start", type=int, default=25, help="first frame with fire (Jerry touches down 25-26)")
    p.add_argument("--full", type=int, default=50, help="frame where the mask covers the whole burn zone")
    p.add_argument("--ease", type=float, default=0.7, help="spread curve exponent; below 1 catches fast")
    p.add_argument("--climb", type=float, default=0.6, help="vertical distance weight; below 1 climbs faster")
    p.add_argument("--ragged", type=float, default=0.25, help="how irregular the fire front is")
    p.add_argument("--soft", type=float, default=3.0, help="mask edge Gaussian sigma in px")
    p.add_argument("--inside", choices=["canny", "gray", "canny-gray"], default="canny",
                   help="what the DRIVING VIDEO shows inside the mask: Canny edges on black, flat gray, "
                        "or Canny edges on gray")
    p.add_argument("--canny-low", type=int, default=20)
    p.add_argument("--canny-high", type=int, default=60)
    p.add_argument("--field", type=float, default=1.0,
                   help="mask level around the blades inside the spread; 1 = one solid mask")
    p.add_argument("--blade-grow", type=int, default=4, help="px the blade edges are grown for the full-strength mask")
    p.add_argument("--blade-low", type=int, default=20, help="Canny thresholds that pick the blades for the mask "
                                                              "(on a 1.5 px blur; 20/60 picks about a third of the spread)")
    p.add_argument("--blade-high", type=int, default=60)
    p.add_argument("--field-fill", choices=["inside", "plate"], default="inside",
                   help="with --field below 1, what the DRIVING VIDEO shows in the half-strength area: the "
                        "--inside fill (test 11, which came out as a gray veil) or the plate (only the blades get the fill)")
    p.add_argument("--keyframe", type=Path, help="still of the fire at its height, registered to the window; "
                   "placed in the DRIVING VIDEO over --key-frames with the mask at 0 there")
    p.add_argument("--keyframe-tag", default="", help="short name for file names, e.g. k2")
    p.add_argument("--key-frames", default="49-52",
                   help="first-last frame (0-based) holding the keyframe; several groups separated by commas, "
                        "e.g. 33-36,41-44,49-52")
    p.add_argument("--growth", choices=["front", "static"], default="front",
                   help="front: the mask spreads from the ignition point until --full; static: the whole "
                        "zone from --start on, so the model decides how the fire grows")
    p.add_argument("--zone-from-key", action="store_true",
                   help="widen the burn zone to hold the keyframe's own flames")
    p.add_argument("--seed", type=int, default=4)
    p.add_argument("--version", default="v001")
    r = build(p.parse_args())
    print(r["control"], r["mask"], r["start_image"], sep="\n")
    print("coverage at start/mid/end:", r["coverage"][r["settings"]["start"]], r["coverage"][40], r["coverage"][-1])


if __name__ == "__main__":
    main()
