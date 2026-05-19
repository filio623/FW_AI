#!/usr/bin/env python3
"""Build source-derived Jerry character creator candidate stills."""

from __future__ import annotations

import csv
import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path("/Users/robbiefilios/Documents/FW_AI_Workflow")
OUT = ROOT / "assets/characters/jerry/training-candidates/source-derived-v001"
MANIFEST = OUT / "manifest.tsv"
TMP = Path("/private/tmp/jerry_training_candidates")


CG_SOURCES = [
    {
        "slug": "shot12u_jerry5",
        "source": "/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_12U/jerry5/Proxy/jerry5..mov",
        "frames": [0, 13, 27, 40, 54, 68, 81, 95, 109, 122, 136, 149],
        "folder": "cgi-renders",
        "threshold": 18,
    },
    {
        "slug": "shot12tt_jerry5",
        "source": "/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_12TT_anim_v05/jerry5/Proxy/jerry5..mov",
        "frames": [0, 9, 18, 27, 36, 45, 54, 63, 72],
        "folder": "cgi-renders",
        "threshold": 18,
    },
    {
        "slug": "shot4_ren_small_fire6",
        "source": "/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6/Proxy/ren_small_fire6..mov",
        "frames": [0, 10, 20, 30, 40, 50, 60, 70, 80, 86],
        "folder": "cgi-renders",
        "threshold": 22,
    },
    {
        "slug": "shot4_small_fire_extracted",
        "source": "/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/Small Fire_ extracted/Proxy/ren_small_fire6..mov",
        "frames": [0, 12, 24, 36, 48, 60, 72, 84, 96, 111],
        "folder": "cgi-renders",
        "threshold": 22,
    },
    {
        "slug": "scene4a_2d_animation",
        "source": "/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Scene 4a_v05.mp4",
        "frames": [8, 16, 24, 32, 40, 48, 56, 64, 69],
        "folder": "animation",
        "threshold": 80,
        "orange_only": True,
        "square": False,
        "pad_ratio": 0.12,
    },
]


SHEET_SOURCES = [
    (
        "/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Jerry01.png",
        "x_sheet_jerry01_expression-sheet.png",
    ),
    (
        "/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Jerry02.png",
        "x_sheet_jerry02_expression-sheet.png",
    ),
]


def run(args: list[str], *, capture: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        args,
        check=True,
        text=False,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )


def ffprobe_dims(path: Path) -> tuple[int, int]:
    result = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height",
            "-of",
            "json",
            str(path),
        ],
        capture=True,
    )
    stream = json.loads(result.stdout)["streams"][0]
    return int(stream["width"]), int(stream["height"])


def extract_frame(source: Path, frame: int, dest: Path) -> None:
    if dest.exists():
        dest.unlink()
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(source),
            "-vf",
            f"select=eq(n\\,{frame})",
            "-frames:v",
            "1",
            str(dest),
        ]
    )


def raw_rgb(path: Path, width: int, height: int) -> bytes:
    result = run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(path),
            "-f",
            "rawvideo",
            "-pix_fmt",
            "rgb24",
            "-",
        ],
        capture=True,
    )
    expected = width * height * 3
    if len(result.stdout) != expected:
        raise RuntimeError(f"Unexpected raw frame size for {path}: {len(result.stdout)} != {expected}")
    return result.stdout


def detect_bbox(
    data: bytes,
    width: int,
    height: int,
    *,
    threshold: int,
    orange_only: bool = False,
) -> tuple[int, int, int, int] | None:
    min_x, min_y = width, height
    max_x, max_y = -1, -1
    for y in range(height):
        row = y * width * 3
        for x in range(width):
            i = row + x * 3
            r, g, b = data[i], data[i + 1], data[i + 2]
            if orange_only:
                hit = r >= 150 and g >= 70 and (r + g) >= 260 and r > b + 50 and g > b + 20
            else:
                hit = max(r, g, b) >= threshold and (r + g + b) >= threshold * 2
            if hit:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    if max_x < 0:
        return None
    return min_x, min_y, max_x + 1, max_y + 1


def padded_square(bbox: tuple[int, int, int, int], width: int, height: int) -> tuple[int, int, int]:
    x0, y0, x1, y1 = bbox
    bw, bh = x1 - x0, y1 - y0
    pad = max(48, int(max(bw, bh) * 0.28))
    cx = (x0 + x1) // 2
    cy = (y0 + y1) // 2
    size = max(bw, bh) + pad * 2
    size = min(size, width, height)
    x = max(0, min(width - size, cx - size // 2))
    y = max(0, min(height - size, cy - size // 2))
    return x, y, size


def padded_rect(
    bbox: tuple[int, int, int, int],
    width: int,
    height: int,
    *,
    pad_ratio: float,
) -> tuple[int, int, int, int]:
    x0, y0, x1, y1 = bbox
    bw, bh = x1 - x0, y1 - y0
    pad = max(24, int(max(bw, bh) * pad_ratio))
    x = max(0, x0 - pad)
    y = max(0, y0 - pad)
    right = min(width, x1 + pad)
    bottom = min(height, y1 + pad)
    return x, y, right - x, bottom - y


def crop_frame(src: Path, dest: Path, crop: tuple[int, int, int, int]) -> None:
    x, y, w, h = crop
    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(src),
            "-vf",
            f"crop={w}:{h}:{x}:{y},scale='if(lt(iw,900),900,iw)':-2:flags=lanczos",
            str(dest),
        ]
    )


def copy_storyboard_crops(rows: list[dict[str, str]]) -> None:
    index_path = ROOT / "outputs/review/jerry_asset-triage_v001/storyboard-crops_index.tsv"
    with index_path.open(newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            if row["priority"] == "C":
                continue
            src = ROOT / row["crop_file"]
            out_name = f"storyboard_{row['sheet']}_{row['order']}_{Path(row['crop_file']).stem}.jpg"
            dest = OUT / "storyboards" / out_name
            shutil.copy2(src, dest)
            rows.append(
                {
                    "file": str(dest.relative_to(ROOT)),
                    "category": "storyboard",
                    "source_path": row["source_path"],
                    "source_frame": "",
                    "crop": "existing source-derived crop",
                    "notes": row["notes"],
                }
            )


def copy_sheets(rows: list[dict[str, str]]) -> None:
    for source, name in SHEET_SOURCES:
        src = Path(source)
        if not src.exists():
            continue
        dest = OUT / "sheets" / name
        shutil.copy2(src, dest)
        rows.append(
            {
                "file": str(dest.relative_to(ROOT)),
                "category": "sheet",
                "source_path": source,
                "source_frame": "",
                "crop": "full source sheet copy",
                "notes": "Expression sheet source reference; not split into individual face parts.",
            }
        )


def extract_cg(rows: list[dict[str, str]]) -> None:
    for item in CG_SOURCES:
        source = Path(item["source"])
        if not source.exists():
            continue
        for frame in item["frames"]:
            tmp_frame = TMP / f"{item['slug']}_f{frame:04d}.png"
            extract_frame(source, frame, tmp_frame)
            if not tmp_frame.exists() or tmp_frame.stat().st_size == 0:
                continue
            width, height = ffprobe_dims(tmp_frame)
            data = raw_rgb(tmp_frame, width, height)
            bbox = detect_bbox(
                data,
                width,
                height,
                threshold=item["threshold"],
                orange_only=item.get("orange_only", False),
            )
            if bbox is None:
                continue
            if item.get("square", True):
                x, y, size = padded_square(bbox, width, height)
                crop = (x, y, size, size)
            else:
                crop = padded_rect(
                    bbox,
                    width,
                    height,
                    pad_ratio=float(item.get("pad_ratio", 0.2)),
                )
            dest = OUT / item["folder"] / f"{item['slug']}_f{frame:04d}_jerry-focused.png"
            crop_frame(tmp_frame, dest, crop)
            rows.append(
                {
                    "file": str(dest.relative_to(ROOT)),
                    "category": item["folder"],
                    "source_path": item["source"],
                    "source_frame": str(frame),
                    "crop": f"{crop[2]}x{crop[3]}+{crop[0]}+{crop[1]}",
                    "notes": "Extracted from source movie frame and auto-cropped around Jerry/fire.",
                }
            )


def write_manifest(rows: list[dict[str, str]]) -> None:
    fields = ["file", "category", "source_path", "source_frame", "crop", "notes"]
    with MANIFEST.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    for folder in ["storyboards", "cgi-renders", "animation", "sheets"]:
        shutil.rmtree(OUT / folder, ignore_errors=True)
        (OUT / folder).mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str]] = []
    copy_storyboard_crops(rows)
    extract_cg(rows)
    copy_sheets(rows)
    write_manifest(rows)


if __name__ == "__main__":
    main()
