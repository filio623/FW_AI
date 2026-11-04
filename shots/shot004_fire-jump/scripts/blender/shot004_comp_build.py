"""Build the shot004 fire-jump comp as an editable Blender compositor node tree.

    /Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup \
        --python shots/shot004_fire-jump/scripts/blender/shot004_comp_build.py -- OUT.blend [--jerry CLIP.mp4]

Layer stack (bottom to top), one Frame node per layer:

  Plate -> Ground glow -> (Pass B slot) -> Jerry (core over + Screen glow + bloom)
        -> Ridge holdout -> Final grade -> Group Output / Viewer

Media paths are stored relative to the .blend. Tunable values sit on nodes labelled
"CTRL ..." so the comp can be adjusted node by node.

Placement and mask geometry come from shots/shot004_fire-jump/scripts/shot004_comp_geometry.py, shared with the
Fusion builder. The compositor centres images on the render canvas, so the Transform
node scales Jerry by JERRY_SCALE with no offset. Render at 100%: the 5.2 compositor does
not scale image inputs with the resolution percentage.

Mask coordinates: x = px / width, y = (height/2 - row) / width + 0.5, where row is the
pixel row from the top (verified 2026-11-02 on Blender 5.2.1).
"""

import argparse
import os
import sys

import bpy

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from shot004_comp_geometry import (GROUND_POLYGON, H, JERRY, JERRY_FRAMES, JERRY_SCALE,  # noqa: E402
                                   PLATE, PLATE_FRAMES, RIDGE_POLYGON, W)

# Starting values for the CTRL nodes; tune in the .blend afterwards.
LOOK = {
    "jerry_saturation": 1.2,
    "jerry_gain": (1.25, 1.0, 0.78),
    "core_fill_px": 30.0,          # blur before the core matte, so darker interior patches stay opaque
    "core_range": (0.03, 0.22),    # luminance (scene linear) mapped to matte 0..1
    "core_opacity": 0.85,
    "bloom_threshold": 0.25,
    "bloom_strength": 0.6,
    "bloom_size": 0.9,
    "light_blur_px": 900.0,
    "light_full": 0.08,            # blurred luminance at which the light map saturates to 1
    "glow_tint": (1.0, 0.42, 0.10),
    "ground_glow_strength": 2.5,   # plate gain at full light: lit = plate x (1 + strength x tint x light)
    "dark_fill_px": 140.0,         # Lighten Jerry with a blurred copy of himself: fills dark interior
    "dark_fill_amount": 1.0,       # patches that read as eyes and a mouth once Jerry is opaque
}


def mask_co(x, row):
    return (x / W, (H / 2 - row) / W + 0.5)


def polygon_mask(name, points):
    mask = bpy.data.masks.new(name)
    mask.frame_start, mask.frame_end = 1, PLATE_FRAMES
    spline = mask.layers.new(name=name).splines.new()
    spline.points.add(len(points) - 1)
    for p, (x, row) in zip(spline.points, points):
        p.handle_type = "VECTOR"
        p.co = mask_co(x, row)
    spline.use_cyclic = True
    return mask


def movie(path, frames):
    img = bpy.data.images.load(path, check_existing=True)
    img.colorspace_settings.name = "sRGB"
    return img, frames


class Tree:
    def __init__(self, ng):
        self.ng = ng

    def node(self, kind, label, loc, parent=None, **inputs):
        n = self.ng.nodes.new(kind)
        n.label = label
        n.name = label
        n.location = loc
        if parent is not None:
            n.parent = parent
        for key, value in inputs.items():
            n.inputs[key.replace("_", " ")].default_value = value
        return n

    def frame(self, label, color):
        f = self.ng.nodes.new("NodeFrame")
        f.label = label
        f.name = label
        f.use_custom_color = True
        f.color = color
        f.label_size = 28
        return f

    def link(self, out, inp):
        self.ng.links.new(out, inp)

    def mix(self, label, loc, blend, parent=None, factor=1.0):
        n = self.node("ShaderNodeMix", label, loc, parent)
        n.data_type = "RGBA"
        n.blend_type = blend
        n.clamp_factor = False
        n.clamp_result = False
        n.inputs[0].default_value = factor
        return n

    def value(self, label, loc, v, parent=None):
        n = self.node("ShaderNodeValue", label, loc, parent)
        n.outputs[0].default_value = v
        return n

    def math(self, label, loc, op, parent=None):
        n = self.node("ShaderNodeMath", label, loc, parent)
        n.operation = op
        return n


def mix_in(n, which):
    """ShaderNodeMix RGBA sockets: A = inputs[6], B = inputs[7], Result = outputs[2]."""
    return n.inputs[6 if which == "A" else 7]


def build(jerry_path):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s = bpy.context.scene
    s.name = "shot004_comp"
    s.render.resolution_x, s.render.resolution_y, s.render.resolution_percentage = W, H, 100
    s.render.fps = 24
    s.frame_start, s.frame_end = 1, JERRY_FRAMES
    s.view_settings.view_transform = "Standard"
    s.view_settings.look = "None"
    s.render.compositor_device = "GPU"
    s.render.image_settings.file_format = "JPEG"
    s.render.image_settings.quality = 92

    ng = bpy.data.node_groups.new("shot004_comp", "CompositorNodeTree")
    ng.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
    s.compositing_node_group = ng
    t = Tree(ng)

    plate_img, _ = movie(PLATE, PLATE_FRAMES)
    jerry_img, _ = movie(jerry_path, JERRY_FRAMES)
    ridge = polygon_mask("ridge_holdout", RIDGE_POLYGON)
    ground = polygon_mask("ground_glow_limit", GROUND_POLYGON)

    # --- Plate ---
    f_plate = t.frame("PLATE  FW_test_scene (staged test plate)", (0.25, 0.25, 0.3))
    plate = t.node("CompositorNodeImage", "Plate", (-1400, 600), f_plate)
    plate.image, plate.frame_duration, plate.frame_start = plate_img, PLATE_FRAMES, 1

    # --- Jerry source and placement ---
    f_jerry = t.frame("JERRY  Pass A element on black (Mick 1.3 run 8)", (0.45, 0.25, 0.12))
    jerry = t.node("CompositorNodeImage", "Jerry clip", (-1400, -200), f_jerry)
    jerry.image, jerry.frame_duration, jerry.frame_start = jerry_img, JERRY_FRAMES, 1
    place = t.node("CompositorNodeTransform", "Jerry placement (x4.3077, centred)", (-1150, -200), f_jerry,
                   Scale=JERRY_SCALE, Interpolation="Bicubic")
    t.link(jerry.outputs["Image"], place.inputs["Image"])

    sat = t.node("CompositorNodeHueSat", "CTRL Jerry saturation", (-900, -200), f_jerry,
                 Saturation=LOOK["jerry_saturation"])
    t.link(place.outputs["Image"], sat.inputs["Image"])
    hot = t.node("CompositorNodeColorBalance", "CTRL Jerry hotter grade (gain)", (-680, -200), f_jerry)
    hot.inputs["Type"].default_value = "Lift/Gamma/Gain"
    hot.inputs[8].default_value = (*LOOK["jerry_gain"], 1.0)  # Gain colour
    t.link(sat.outputs["Image"], hot.inputs["Image"])
    dark_blur = t.node("CompositorNodeBlur", "CTRL dark-patch fill blur (px)", (-680, -20), f_jerry,
                       Size=(LOOK["dark_fill_px"],) * 2, Type="Gaussian")
    t.link(hot.outputs["Image"], dark_blur.inputs["Image"])
    jerry_rgb = t.mix("CTRL dark-patch fill (Lighten)", (-440, -20), "LIGHTEN", f_jerry,
                      factor=LOOK["dark_fill_amount"])
    t.link(hot.outputs["Image"], mix_in(jerry_rgb, "A"))
    t.link(dark_blur.outputs["Image"], mix_in(jerry_rgb, "B"))

    luma = t.node("CompositorNodeRGBToBW", "Jerry luminance", (-1150, -520), f_jerry)
    t.link(place.outputs["Image"], luma.inputs["Image"])
    fill = t.node("CompositorNodeBlur", "CTRL core matte fill (px)", (-900, -520), f_jerry,
                  Size=(LOOK["core_fill_px"],) * 2, Type="Gaussian")
    t.link(luma.outputs["Val"], fill.inputs["Image"])
    core = t.node("ShaderNodeMapRange", "CTRL core matte range", (-680, -520), f_jerry)
    core.inputs["From Min"].default_value, core.inputs["From Max"].default_value = LOOK["core_range"]
    core.clamp = True
    t.link(fill.outputs["Image"], core.inputs["Value"])
    core_op = t.value("CTRL core opacity", (-680, -760), LOOK["core_opacity"], f_jerry)
    core_mul = t.math("core matte x opacity", (-440, -560), "MULTIPLY", f_jerry)
    t.link(core.outputs["Result"], core_mul.inputs[0])
    t.link(core_op.outputs[0], core_mul.inputs[1])

    bloom = t.node("CompositorNodeGlare", "CTRL Jerry bloom", (-200, -200), f_jerry,
                   Type="Fog Glow", Quality="High", Threshold=LOOK["bloom_threshold"],
                   Strength=LOOK["bloom_strength"], Size=LOOK["bloom_size"])
    t.link(jerry_rgb.outputs[2], bloom.inputs["Image"])

    # --- Ground glow ---
    f_glow = t.frame("GROUND GLOW  Jerry's light map warms the plate", (0.4, 0.3, 0.1))
    lm_blur = t.node("CompositorNodeBlur", "CTRL light map blur (px)", (-900, 300), f_glow,
                     Size=(LOOK["light_blur_px"],) * 2, Type="Fast Gaussian")
    t.link(luma.outputs["Val"], lm_blur.inputs["Image"])
    lm_norm = t.node("ShaderNodeMapRange", "CTRL light map range", (-660, 460), f_glow)
    lm_norm.inputs["From Min"].default_value, lm_norm.inputs["From Max"].default_value = 0.0, LOOK["light_full"]
    lm_norm.clamp = True
    t.link(lm_blur.outputs["Image"], lm_norm.inputs["Value"])
    tint = t.node("CompositorNodeRGB", "CTRL glow tint", (-900, 120), f_glow)
    tint.outputs[0].default_value = (*LOOK["glow_tint"], 1.0)
    tinted = t.mix("light map x tint", (-660, 300), "MULTIPLY", f_glow)
    t.link(lm_norm.outputs["Result"], mix_in(tinted, "A"))
    t.link(tint.outputs[0], mix_in(tinted, "B"))
    lit = t.mix("plate x light", (-440, 520), "MULTIPLY", f_glow)
    t.link(plate.outputs["Image"], mix_in(lit, "A"))
    t.link(tinted.outputs[2], mix_in(lit, "B"))

    gmask = t.node("CompositorNodeMask", "ground glow limit (mask: ground_glow_limit)", (-900, -20), f_glow)
    gmask.mask = ground
    gsoft = t.node("CompositorNodeBlur", "ground limit softness", (-660, -20), f_glow,
                   Size=(220.0, 220.0), Type="Fast Gaussian")
    t.link(gmask.outputs["Mask"], gsoft.inputs["Image"])
    g_str = t.value("CTRL ground glow strength", (-660, 120), LOOK["ground_glow_strength"], f_glow)
    g_fac = t.math("strength x ground limit", (-440, 120), "MULTIPLY", f_glow)
    t.link(gsoft.outputs["Image"], g_fac.inputs[0])
    t.link(g_str.outputs[0], g_fac.inputs[1])
    plate_lit = t.mix("plate + glow", (-200, 600), "ADD", f_glow)
    t.link(g_fac.outputs[0], plate_lit.inputs[0])
    t.link(plate.outputs["Image"], mix_in(plate_lit, "A"))
    t.link(lit.outputs[2], mix_in(plate_lit, "B"))

    # --- Pass B slot: grass ignition goes between plate_lit and Jerry when it exists ---
    f_passb = t.frame("PASS B SLOT  grass ignition (not generated yet): insert between 'plate + glow' and 'Jerry core over'",
                      (0.2, 0.3, 0.2))
    passb = t.node("NodeReroute", "Pass B in", (40, 600), f_passb)
    t.link(plate_lit.outputs[2], passb.inputs[0])

    # --- Jerry over the plate ---
    f_over = t.frame("JERRY COMP  core 'over' + Screen glow + bloom", (0.45, 0.25, 0.12))
    over = t.mix("Jerry core over", (240, 400), "MIX", f_over)
    t.link(core_mul.outputs[0], over.inputs[0])
    t.link(passb.outputs[0], mix_in(over, "A"))
    t.link(jerry_rgb.outputs[2], mix_in(over, "B"))
    scr = t.mix("CTRL Jerry Screen glow", (460, 400), "SCREEN", f_over, factor=1.0)
    t.link(over.outputs[2], mix_in(scr, "A"))
    t.link(jerry_rgb.outputs[2], mix_in(scr, "B"))
    blo = t.mix("bloom add", (680, 400), "ADD", f_over, factor=1.0)
    t.link(scr.outputs[2], mix_in(blo, "A"))
    t.link(bloom.outputs["Glare"], mix_in(blo, "B"))

    # --- Ridge holdout ---
    f_ridge = t.frame("RIDGE HOLDOUT  plate ridge back over Jerry (edit mask: ridge_holdout)", (0.25, 0.3, 0.35))
    rmask = t.node("CompositorNodeMask", "ridge mask", (680, 100), f_ridge)
    rmask.mask = ridge
    rsoft = t.node("CompositorNodeBlur", "CTRL ridge edge softness (px)", (900, 100), f_ridge,
                   Size=(28.0, 28.0), Type="Gaussian")
    t.link(rmask.outputs["Mask"], rsoft.inputs["Image"])
    hold = t.mix("ridge holdout", (1120, 400), "MIX", f_ridge)
    t.link(rsoft.outputs["Image"], hold.inputs[0])
    t.link(blo.outputs[2], mix_in(hold, "A"))
    t.link(passb.outputs[0], mix_in(hold, "B"))

    # --- Final grade and outputs ---
    f_out = t.frame("FINAL GRADE + OUTPUT", (0.3, 0.3, 0.3))
    grade = t.node("CompositorNodeColorBalance", "CTRL final grade (neutral)", (1360, 400), f_out)
    t.link(hold.outputs[2], grade.inputs["Image"])
    out = t.node("NodeGroupOutput", "Group Output", (1600, 400), f_out)
    t.link(grade.outputs["Image"], out.inputs[0])
    view = t.node("CompositorNodeViewer", "Viewer", (1600, 200), f_out)
    t.link(grade.outputs["Image"], view.inputs["Image"])
    return s


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    ap = argparse.ArgumentParser()
    ap.add_argument("blend")
    ap.add_argument("--jerry", default=JERRY)
    args = ap.parse_args(argv)
    blend = os.path.abspath(args.blend)
    os.makedirs(os.path.dirname(blend), exist_ok=True)
    build(os.path.abspath(args.jerry))
    bpy.ops.wm.save_as_mainfile(filepath=blend)
    bpy.ops.file.make_paths_relative()
    bpy.ops.wm.save_mainfile()
    for img in bpy.data.images:
        print("image", img.name, img.filepath)
    print("saved", blend)


if __name__ == "__main__":
    main()
