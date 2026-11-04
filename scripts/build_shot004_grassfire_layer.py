#!/usr/bin/env python3
"""Turn a full-frame grass-fire clip (Seedance first-last-frame) into the shot004 Pass B layer.

The clip is a regenerated copy of the whole plate with the fire in it. This script puts it
back on the 4096x2160 plate and keeps only what the fire changed, in two parts:

- registration: the clip's first frame is matched to the plate frame it started from
  (SIFT + RANSAC affine), so it lands on the plate to about a pixel;
- timing: shot frame -> clip frame by a piecewise-linear map (--map), e.g. Jerry lands on
  shot frame 25 and the clip should catch fire then, faster than it does on its own;
- fire light: the low-frequency brightening around the fire (clip / plate, both blurred,
  in linear light), as a gain on the plate inside a soft zone around the clump. The plate
  keeps its own detail; the clip is softer (480p-1080p against a 4K plate);
- fire: what still differs once the plate is relit (flames, burning blades, embers), ramped
  from --ramp low..high, grown and blurred, times the zone. Taken from the clip.

Outputs per shot frame (f0001.. = Blender comp frame 1 = plate frame 0): `gain/` 32-bit EXR
(linear gain, 1 = unchanged), `rgb/` JPEG (the clip on the plate), `matte/` 8-bit PNG (fire
matte); plus `zone.png` and a JSON report. Frames before the fire are neutral. Needs numpy
and opencv with OpenEXR (/usr/local/bin/python3).

    OPENCV_IO_ENABLE_OPENEXR=1 /usr/local/bin/python3 scripts/build_shot004_grassfire_layer.py \
        --clip outputs/shot004/pass-b_grassfire/seedance-flf_v001/sd03_full169-platebg-timing-480p.mp4 \
        --out-dir assets/elements/by-shot/shot004_fire-jump/scorch-contact/layers/shot004_fire-jump_grassfire-layer-s3_v001 --map 20:25,72:54,96:80
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

os.environ.setdefault("OPENCV_IO_ENABLE_OPENEXR", "1")
import cv2  # noqa: E402
import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SHOT = ROOT / "assets/elements/by-shot/shot004_fire-jump"
PLATE = SHOT / "plates/FW_test_scene.mp4"
KEYFRAME = SHOT / "scorch-contact/keyframes/shot004_grassfire_keyframe-k2_full169_3840x2160_v001.png"
FULL169_X = 128  # the 16:9 keyframes are the plate cropped to x 128..3968
# Pass B burn zone (window pixels, 912x512 at plate x 1838, y 488, scale 2); see
# scripts/build_shot004_grassfire_inputs.py.
BURN_ZONE = [(300, 445), (630, 445), (740, 350), (830, 220), (860, 110), (800, 55), (600, 45),
             (450, 60), (300, 45), (130, 60), (70, 130), (110, 240), (200, 350)]
WINDOW_X, WINDOW_Y = 1838, 488


def read_video(path: Path) -> list[np.ndarray]:
    cap, frames = cv2.VideoCapture(str(path)), []
    while True:
        ok, f = cap.read()
        if not ok:
            return frames
        frames.append(f)


def register(clip0: np.ndarray, plate: np.ndarray) -> tuple[np.ndarray, dict]:
    sift, bf = cv2.SIFT_create(4000), cv2.BFMatcher()
    g1 = cv2.cvtColor(clip0, cv2.COLOR_BGR2GRAY)
    s = 0.25
    g2 = cv2.resize(cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY), None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    k1, d1 = sift.detectAndCompute(g1, None)
    k2, d2 = sift.detectAndCompute(g2, None)
    m = [a for a, b in bf.knnMatch(d1, d2, k=2) if a.distance < 0.75 * b.distance]
    src = np.float32([k1[a.queryIdx].pt for a in m])
    dst = np.float32([k2[a.trainIdx].pt for a in m]) / s
    A, inl = cv2.estimateAffine2D(src, dst, ransacReprojThreshold=6)
    keep = inl[:, 0] > 0
    err = np.hypot(*(cv2.transform(src[keep][None], A)[0] - dst[keep]).T)
    return A, {"inliers": int(keep.sum()), "error_px_median": round(float(np.median(err)), 2),
               "error_px_p90": round(float(np.percentile(err, 90)), 2), "affine": A.round(6).tolist()}


def zone_mask(h: int, w: int, grow: int, feather: float) -> np.ndarray:
    """Soft area the fire may occupy: the keyframe's flames, grown, plus the burn zone."""
    zone = np.zeros((h, w), np.uint8)
    pts = np.array([(WINDOW_X + 2 * x, WINDOW_Y + 2 * y) for x, y in BURN_ZONE], np.int32)
    cv2.fillPoly(zone, [pts], 1)
    if KEYFRAME.exists():
        k = cv2.cvtColor(cv2.imread(str(KEYFRAME)), cv2.COLOR_BGR2RGB).astype(np.int16)
        flames = ((k[..., 0] >= 170) & (k[..., 0] - k[..., 2] >= 50)).astype(np.uint8)
        flames = cv2.morphologyEx(flames, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        zone[:, FULL169_X:FULL169_X + flames.shape[1]] |= flames
    zone = cv2.dilate(zone, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * grow + 1,) * 2))
    return cv2.GaussianBlur(zone.astype(np.float32), (0, 0), feather)


def frame_map(spec: str, n_shot: int, n_clip: int) -> list[int | None]:
    pts = sorted(tuple(int(v) for v in p.split(":"))[::-1] for p in spec.split(","))  # (shot, clip)
    shot = [p[0] for p in pts]
    clip = [p[1] for p in pts]
    out: list[int | None] = []
    for t in range(n_shot):
        if t < shot[0]:
            out.append(None)
        else:
            out.append(int(round(min(n_clip - 1, np.interp(t, shot, clip)))))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--clip", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--map", default="20:25,72:54,96:80",
                    help="clip:shot frame pairs (0-based), linear in between; shot frames before the "
                         "first pair get no fire")
    ap.add_argument("--register-plate-frame", type=int, default=25,
                    help="plate frame the clip's first frame was made from")
    ap.add_argument("--frames", type=int, default=81, help="shot frames to write (the comp's length)")
    ap.add_argument("--ramp", default="30,70", help="remaining change (0-255) after relighting -> fire matte 0..1")
    ap.add_argument("--grow", type=int, default=8, help="fire matte growth in plate px")
    ap.add_argument("--blur", type=float, default=6.0, help="fire matte blur sigma in plate px")
    ap.add_argument("--light-blur", type=float, default=30.0, help="blur sigma (plate px) for the fire light")
    ap.add_argument("--zone-grow", type=int, default=80)
    ap.add_argument("--zone-feather", type=float, default=40.0)
    args = ap.parse_args()

    plate = read_video(PLATE)
    clip = read_video(args.clip)
    h, w = plate[0].shape[:2]
    A, reg = register(clip[0], plate[args.register_plate_frame])
    zone = zone_mask(h, w, args.zone_grow, args.zone_feather)
    lo, hi = (float(v) for v in args.ramp.split(","))
    fmap = frame_map(args.map, args.frames, len(clip))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * args.grow + 1,) * 2)
    lut = ((np.arange(256) / 255.0) ** 2.2).astype(np.float32)  # sRGB-ish -> linear
    gw, gh = w // 4, h // 4  # the light is smooth: store it at quarter size, scale x4 in the comp

    out = args.out_dir
    for sub in ("rgb", "matte", "gain"):
        (out / sub).mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out / "zone.png"), (zone * 255).round().astype(np.uint8))
    coverage, gain_peak = [], []
    neutral = np.ones((gh, gw, 3), np.float32)
    exr = [cv2.IMWRITE_EXR_TYPE, cv2.IMWRITE_EXR_TYPE_HALF]
    for t in range(args.frames):
        name = f"f{t + 1:04d}"
        src = fmap[t]
        if src is None:
            rgb, matte, gain = plate[t], np.zeros((h, w), np.uint8), neutral
        else:
            rgb = cv2.warpAffine(clip[src], A, (w, h), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
            # Fire light: blurred clip / blurred plate in linear light, only inside the zone.
            s_lin = cv2.GaussianBlur(lut[rgb], (0, 0), args.light_blur)
            p_lin = cv2.GaussianBlur(lut[plate[t]], (0, 0), args.light_blur)
            g = np.clip(s_lin / np.maximum(p_lin, 1e-3), 0.5, 6.0)
            g = 1.0 + (g - 1.0) * zone[..., None]
            relit = np.clip((lut[plate[t]] * g) ** (1 / 2.2) * 255, 0, 255)
            # Fire: what still differs after relighting, on lightly blurred images so the
            # clip's softness does not count.
            diff = np.abs(cv2.GaussianBlur(rgb.astype(np.float32), (0, 0), 2)
                          - cv2.GaussianBlur(relit, (0, 0), 2)).max(axis=2)
            m = np.clip((diff - lo) / (hi - lo), 0, 1)
            m = cv2.GaussianBlur(cv2.dilate(m, kernel), (0, 0), args.blur) * zone
            matte = (m * 255).round().astype(np.uint8)
            gain = cv2.resize(g, (gw, gh), interpolation=cv2.INTER_AREA)
        cv2.imwrite(str(out / "rgb" / f"{name}.jpg"), rgb, [cv2.IMWRITE_JPEG_QUALITY, 95])
        cv2.imwrite(str(out / "matte" / f"{name}.png"), matte)
        cv2.imwrite(str(out / "gain" / f"{name}.exr"), gain.astype(np.float32), exr)  # BGR order, like the JPEGs
        coverage.append(round(float(matte.mean() / 255), 4))
        gain_peak.append(round(float(gain.max()), 2))
    report = {"settings": {k: str(v) for k, v in vars(args).items()}, "registration": reg,
              "frame_map": fmap, "fire_matte_coverage": coverage, "gain_peak": gain_peak,
              "zone_coverage": round(float(zone.mean()), 4)}
    (out / "layer_report.json").write_text(json.dumps(report, indent=1))
    print("registration", reg["inliers"], "inliers, median error", reg["error_px_median"], "px")
    print("fire matte coverage at shot frames 30/50/80:", coverage[30], coverage[50], coverage[80])
    print("gain peak at 30/50/80:", gain_peak[30], gain_peak[50], gain_peak[80])


if __name__ == "__main__":
    main()
