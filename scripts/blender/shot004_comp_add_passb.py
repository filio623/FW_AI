"""Add a Pass B grass-fire layer to an existing shot004 Blender comp and save it as a new file.

    /Applications/Blender.app/Contents/MacOS/Blender -b IN.blend \
        --python scripts/blender/shot004_comp_add_passb.py -- OUT.blend --layer LAYER_DIR [--label TEXT]

LAYER_DIR is the output of scripts/build_shot004_grassfire_layer.py: `gain/f####.exr`
(quarter-size linear fire light), `rgb/f####.jpg` (the fire clip on the plate) and
`matte/f####.png` (fire matte), one frame per comp frame starting at f0001.

The layer goes into the comp's Pass B slot, between "plate + glow" and Jerry:

    plate + glow -> x fire light (gain, scaled x4) -> fire over (matte) -> Pass B in

so Jerry, his glow and the ridge holdout sit on top of the burning grass. The input file is
not changed (frozen _vNNN comps keep their path); OUT.blend is written with relative paths.
"""

import argparse
import os
import sys

import bpy

FRAMES = 81


def sequence(path, colorspace):
    img = bpy.data.images.load(path, check_existing=True)
    img.source = "SEQUENCE"
    img.colorspace_settings.name = colorspace
    return img


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    ap = argparse.ArgumentParser()
    ap.add_argument("blend")
    ap.add_argument("--layer", required=True)
    ap.add_argument("--label", default="")
    args = ap.parse_args(argv)
    layer = os.path.abspath(args.layer)

    s = bpy.context.scene
    ng = s.compositing_node_group
    nodes, links = ng.nodes, ng.links
    slot = nodes["Pass B in"]
    plate_lit = nodes["plate + glow"]
    for old in [l for l in links if l.to_node == slot]:
        links.remove(old)

    frame = nodes.new("NodeFrame")
    frame.label = frame.name = "PASS B  grass fire: x fire light, then fire over" + (f"  ({args.label})" if args.label else "")
    frame.use_custom_color, frame.color, frame.label_size = True, (0.2, 0.3, 0.2), 28

    def node(kind, label, loc):
        n = nodes.new(kind)
        n.label = n.name = label
        n.location = loc
        n.parent = frame
        return n

    def image_node(label, loc, path, colorspace):
        n = node("CompositorNodeImage", label, loc)
        n.image = sequence(path, colorspace)
        n.frame_duration, n.frame_start, n.frame_offset = FRAMES, 1, 0
        return n

    def mix(label, loc, blend):
        n = node("ShaderNodeMix", label, loc)
        n.data_type, n.blend_type = "RGBA", blend
        n.clamp_factor = n.clamp_result = False
        n.inputs[0].default_value = 1.0
        return n

    gain = image_node("Pass B fire light (gain EXR, quarter size)", (-200, 1250), os.path.join(layer, "gain", "f0001.exr"), "Non-Color")
    up = node("CompositorNodeScale", "fire light x4 to plate size", (60, 1250))
    up.inputs["X"].default_value = up.inputs["Y"].default_value = 4.0
    up.inputs["Interpolation"].default_value = "Bicubic"
    links.new(gain.outputs["Image"], up.inputs["Image"])
    relit = mix("CTRL plate x fire light", (300, 1100), "MULTIPLY")
    links.new(plate_lit.outputs[2], relit.inputs[6])
    links.new(up.outputs["Image"], relit.inputs[7])

    rgb = image_node("Pass B fire (clip on plate)", (-200, 900), os.path.join(layer, "rgb", "f0001.jpg"), "sRGB")
    matte = image_node("Pass B fire matte", (-200, 650), os.path.join(layer, "matte", "f0001.png"), "Non-Color")
    bw = node("CompositorNodeRGBToBW", "fire matte value", (60, 650))
    links.new(matte.outputs["Image"], bw.inputs["Image"])
    over = mix("CTRL fire over", (520, 900), "MIX")
    links.new(bw.outputs["Val"], over.inputs[0])
    links.new(relit.outputs[2], over.inputs[6])
    links.new(rgb.outputs["Image"], over.inputs[7])
    links.new(over.outputs[2], slot.inputs[0])

    out = os.path.abspath(args.blend)
    bpy.ops.wm.save_as_mainfile(filepath=out, copy=False)
    bpy.ops.file.make_paths_relative()
    bpy.ops.wm.save_mainfile()
    for img in bpy.data.images:
        print("image", img.name, img.filepath)
    print("saved", out)


if __name__ == "__main__":
    main()
