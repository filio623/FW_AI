"""Render frames headless with Cycles on the Apple GPU (Metal).

    /Applications/Blender.app/Contents/MacOS/Blender -b FILE.blend \
        --python scripts/blender/render_frames.py -- OUTDIR 25-120 [64 88 ...] \
        [--samples 64] [--percent 50]

Writes OUTDIR/f####.png. Frames are single numbers or inclusive A-B ranges.
Encode a preview with:
    ffmpeg -framerate 24 -start_number 25 -i OUTDIR/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 16 OUT.mp4
"""

import argparse
import os
import sys
import time

import bpy


def parse_frames(tokens):
    frames = []
    for tok in tokens:
        if "-" in tok:
            first, last = (int(x) for x in tok.split("-", 1))
            frames.extend(range(first, last + 1))
        else:
            frames.append(int(tok))
    return frames


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    p = argparse.ArgumentParser(description="Render frames headless.")
    p.add_argument("outdir")
    p.add_argument("frames", nargs="+")
    p.add_argument("--samples", type=int)
    p.add_argument("--percent", type=int, help="resolution percentage")
    args = p.parse_args(argv)

    scn = bpy.context.scene
    prefs = bpy.context.preferences.addons["cycles"].preferences
    prefs.compute_device_type = "METAL"
    prefs.get_devices()
    for dev in prefs.devices:
        dev.use = dev.type == "METAL"
    scn.cycles.device = "GPU"
    if args.samples:
        scn.cycles.samples = args.samples
    if args.percent:
        scn.render.resolution_percentage = args.percent
    scn.render.image_settings.file_format = "PNG"

    os.makedirs(args.outdir, exist_ok=True)
    for frame in parse_frames(args.frames):
        start = time.time()
        scn.frame_set(frame)
        scn.render.filepath = os.path.join(os.path.abspath(args.outdir), "f%04d.png" % frame)
        bpy.ops.render.render(write_still=True)
        print("RENDERED", frame, round(time.time() - start, 1), "s")


main()
