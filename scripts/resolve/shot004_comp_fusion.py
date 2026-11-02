"""Build the shot004 fire-jump comp as a Fusion node tree inside DaVinci Resolve Studio.

Needs Resolve Studio running with Preferences > System > General > External scripting
using = Local. Run with Resolve's bundled Python (no environment variables needed):

    "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Applications/ResolvePython" \
        scripts/resolve/shot004_comp_fusion.py [--setting OUT.setting] [--render-preview DIR]

Works on the current project. If the project has no timeline named TIMELINE, it imports
the plate and Jerry, puts the plate on V1 and Jerry on V2 at frame 0, and turns both into
one Fusion clip, so MediaIn1 is the plate and MediaIn2 is Jerry. The project must use
4096x2160, 24 fps and the default "Scale entire image to fit" for mismatched sizes:
Resolve then hands Jerry to Fusion already scaled x4.21875 (fit to height) and centred,
and Jerry_Place adds the rest of JERRY_SCALE.

The comp's tools are written as a Fusion settings block (the text Fusion copies and
pastes), which is also saved to --setting. Paste drops links to tools outside the block,
so after pasting the block by hand, wire the EXTERNAL_LINKS below (MediaIn1 = plate,
MediaIn2 = Jerry). Rebuilding deletes every tool except MediaIn1, MediaIn2, MediaOut1
and the audio displays, then pastes the block. Fusion tool names are case-insensitive, so
the underlays are prefixed "Layer_" to stay distinct from the tools.

Fusion in Resolve works on the Rec.709 (gamma 2.4) values it receives, not scene linear
as Blender's compositor does, so gains and thresholds differ from the Blender comp.
Polyline points: X = px / width - 0.5, Y = 0.5 - row / height (verified 2026-11-02).
Blur and glow sizes are not pixels: at 4096 wide a Blur of size 1 has a sigma of about
2.45 px (measured 2026-11-02).
"""

import argparse
import os
import re
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from shot004_comp_geometry import (GROUND_POLYGON, H, JERRY, JERRY_FRAMES, JERRY_SCALE,  # noqa: E402
                                   PLATE, PLATE_FRAMES, RIDGE_POLYGON, W)

import DaVinciResolveScript as dvr  # noqa: E402

TIMELINE = "shot004_comp_v001"
RESOLVE_FIT = H / 512  # Resolve fits the 912x512 clip to the 2160 height
KEEP = {"MediaIn1", "MediaIn2", "MediaOut1"}
# Paste drops links to tools outside the pasted block, so these are wired after the paste:
# (tool, input, source tool). MediaIn1 is the plate, MediaIn2 is Jerry.
EXTERNAL_LINKS = [("Jerry_Place", "Input", "MediaIn2"), ("Glow_PlateXLight", "Background", "MediaIn1"),
                  ("Glow_Add", "Background", "MediaIn1"), ("MediaOut1", "Input", "Final_Grade")]

# Starting values; tune in the Fusion page afterwards. Gamma-encoded (Rec.709) values.
LOOK = {
    "jerry_saturation": 1.5,           # gamma-space Screen whitens more than Blender's linear one
    "jerry_gain": (1.15, 1.0, 0.82),
    "dark_fill_size": 20.0,            # Lighten Jerry with a blurred copy: fills dark interior patches
    "dark_fill_amount": 1.0,
    "core_fill_size": 4.0,             # blur before the core matte
    "core_low_high": (0.23, 0.53),     # luminance range mapped to the core matte 0..1
    "core_opacity": 0.85,
    "glow_threshold": 0.45,
    "glow_gain": 0.6,
    "glow_size": 15.0,
    "light_blur_size": 180.0,
    "light_gain": 3.0,                 # normalises the blurred light map; clipped at 1
    "light_tint": (1.0, 0.55, 0.20),
    "ground_glow_strength": 1.5,       # lit = plate + strength x plate x tint x light
    "ground_soft_edge": 0.05,          # fraction of the frame width
    "ridge_soft_edge": 0.007,
}


def lua_num(v):
    return repr(float(v))


def polyline(points):
    pts = ", ".join(f"{{ Linear = true, X = {lua_num(x / W - 0.5)}, Y = {lua_num(0.5 - row / H)} }}"
                    for x, row in points)
    return f"Polyline {{ Closed = true, Points = {{ {pts} }} }}"


def inp(value):
    return f"Input {{ Value = {value} }}"


def src(tool, output="Output"):
    return f'Input {{ SourceOp = "{tool}", Source = "{output}" }}'


def tool(name, kind, pos, inputs, comment=None):
    ins = dict(inputs)
    if comment:
        ins["Comments"] = inp(f'"{comment}"')
    body = ",\n".join(f"        {k} = {v}" for k, v in ins.items())
    return (f"    {name} = {kind} {{\n      Inputs = {{\n{body}\n      }},\n"
            f"      ViewInfo = OperatorInfo {{ Pos = {{ {pos[0]}, {pos[1]} }} }},\n    }}")


def underlay(name, pos, size, comment):
    return (f'    {name} = Underlay {{\n      NameSet = true,\n'
            f'      Inputs = {{ Comments = Input {{ Value = "{comment}" }} }},\n'
            f"      ViewInfo = UnderlayInfo {{ Pos = {{ {pos[0]}, {pos[1]} }}, Size = {{ {size[0]}, {size[1]} }} }},\n    }}")


def settings_block():
    L = LOOK
    r, g, b = L["jerry_gain"]
    tr, tg, tb = L["light_tint"]
    lo, hi = L["core_low_high"]
    tools = [
        underlay("Layer_Jerry_Element", (-110, -280), (1100, 200),
                 "Mick 1.3 run 8 placed, graded, dark patches filled, core matte and glow"),
        tool("Jerry_Place", "Transform", (0, -240), {
            "Size": inp(lua_num(JERRY_SCALE / RESOLVE_FIT))},
            f"Resolve fits Jerry x{RESOLVE_FIT:.5f}; this adds the rest of x{JERRY_SCALE:.4f}"),
        tool("Jerry_Sat", "BrightnessContrast", (110, -240), {
            "Saturation": inp(lua_num(L["jerry_saturation"])), "Input": src("Jerry_Place")}),
        tool("Jerry_Gain", "ColorCorrector", (220, -240), {
            "MasterRedGain": inp(lua_num(r)), "MasterGreenGain": inp(lua_num(g)),
            "MasterBlueGain": inp(lua_num(b)), "Input": src("Jerry_Sat")}, "Hotter grade"),
        tool("Jerry_DarkBlur", "Blur", (330, -200), {
            "XBlurSize": inp(lua_num(L["dark_fill_size"])), "Input": src("Jerry_Gain")}),
        tool("Jerry_DarkFill", "Merge", (440, -240), {
            "ApplyMode": inp('"Lighten"'), "Blend": inp(lua_num(L["dark_fill_amount"])),
            "Background": src("Jerry_Gain"), "Foreground": src("Jerry_DarkBlur")},
            "Lighten with a blurred copy: fills dark interior patches that read as a face"),
        tool("Jerry_MatteBlur", "Blur", (110, -160), {
            "XBlurSize": inp(lua_num(L["core_fill_size"])), "Input": src("Jerry_Place")}),
        tool("Jerry_CoreKey", "LumaKeyer", (220, -160), {
            "Low": inp(lua_num(lo)), "High": inp(lua_num(hi)), "Input": src("Jerry_MatteBlur")},
            "Core matte from Jerry's brightness"),
        tool("Jerry_Core", "ChannelBoolean", (550, -160), {
            "ToRed": inp("5"), "ToGreen": inp("6"), "ToBlue": inp("7"), "ToAlpha": inp("3"),
            "Background": src("Jerry_DarkFill"), "Foreground": src("Jerry_CoreKey")},
            "Graded Jerry RGB with the core matte as alpha"),
        tool("Jerry_Glow", "SoftGlow", (550, -240), {
            "Threshold": inp(lua_num(L["glow_threshold"])), "Gain": inp(lua_num(L["glow_gain"])),
            "XGlowSize": inp(lua_num(L["glow_size"])), "Input": src("Jerry_DarkFill")}),

        underlay("Layer_Ground_Glow", (-110, -40), (1100, 160),
                 "Jerry's blurred brightness lights the plate, limited to the ground and grass"),
        tool("Glow_LightBlur", "Blur", (0, 0), {
            "XBlurSize": inp(lua_num(L["light_blur_size"])), "Input": src("Jerry_Place")}),
        tool("Glow_LightNorm", "BrightnessContrast", (110, 0), {
            "Gain": inp(lua_num(L["light_gain"])), "ClipWhite": inp("1"), "Input": src("Glow_LightBlur")}),
        tool("Glow_Tint", "ColorCorrector", (220, 0), {
            "MasterRGBGain": inp(lua_num(L["ground_glow_strength"])),
            "MasterRedGain": inp(lua_num(tr)), "MasterGreenGain": inp(lua_num(tg)),
            "MasterBlueGain": inp(lua_num(tb)), "Input": src("Glow_LightNorm")},
            "Tint x strength (MasterRGBGain)"),
        tool("Glow_PlateXLight", "ChannelBoolean", (330, 40), {
            "Operation": inp("6"), "ToRed": inp("0"), "ToGreen": inp("1"), "ToBlue": inp("2"),
            "ToAlpha": inp("4"), "Foreground": src("Glow_Tint")},
            "Plate x light, per channel"),
        tool("Glow_GroundMask", "PolylineMask", (440, -40), {
            "SoftEdge": inp(lua_num(L["ground_soft_edge"])), "Polyline": inp(polyline(GROUND_POLYGON))},
            "Edit the points in the viewer"),
        tool("Glow_Add", "Merge", (550, 40), {
            "ApplyMode": inp('"LinearDodge"'),
            "Foreground": src("Glow_PlateXLight"), "EffectMask": src("Glow_GroundMask", "Mask")}),

        tool("PassB_Slot", "PipeRouter", (660, 40), {"Input": src("Glow_Add")},
             "Pass B grass ignition goes in here (not generated yet)"),

        underlay("Layer_Jerry_Comp", (640, -80), (500, 160), "Core over, then Screen with glow"),
        tool("Jerry_Over", "Merge", (770, 0), {
            "Blend": inp(lua_num(L["core_opacity"])), "SubtractiveAdditive": inp("0"),
            "Background": src("PassB_Slot"), "Foreground": src("Jerry_Core")}, "Core opacity = Blend"),
        tool("Jerry_Screen", "Merge", (880, 0), {
            "ApplyMode": inp('"Screen"'), "Background": src("Jerry_Over"), "Foreground": src("Jerry_Glow")}),

        underlay("Layer_Ridge_Holdout", (860, 60), (400, 140), "Plate ridge back over Jerry"),
        tool("Ridge_Mask", "PolylineMask", (880, 120), {
            "SoftEdge": inp(lua_num(L["ridge_soft_edge"])), "Polyline": inp(polyline(RIDGE_POLYGON))},
            "Edit the points in the viewer"),
        tool("Ridge_Holdout", "Merge", (990, 0), {
            "Background": src("Jerry_Screen"), "Foreground": src("PassB_Slot"),
            "EffectMask": src("Ridge_Mask", "Mask")}),
        tool("Final_Grade", "ColorCorrector", (1100, 0), {"Input": src("Ridge_Holdout")}, "Neutral final grade"),
    ]
    return "{\n  Tools = ordered() {\n" + ",\n".join(tools) + "\n  }\n}\n"


def tool_names(comp):
    return {t.Name for t in comp.GetToolList(False).values()}


def ensure_timeline(resolve, proj):
    for i in range(1, proj.GetTimelineCount() + 1):
        tl = proj.GetTimelineByIndex(i)
        if tl.GetName() == TIMELINE:
            proj.SetCurrentTimeline(tl)
            return tl
    for key, value in [("timelineResolutionWidth", str(W)), ("timelineResolutionHeight", str(H)),
                       ("timelineFrameRate", "24")]:
        proj.SetSetting(key, value)
    mp = proj.GetMediaPool()
    plate, jerry = mp.ImportMedia([PLATE, JERRY])  # the dict form returned None on 21.1.1
    tl = mp.CreateEmptyTimeline(TIMELINE)
    proj.SetCurrentTimeline(tl)
    tl.AddTrack("video")
    start = tl.GetStartFrame()
    mp.AppendToTimeline([{"mediaPoolItem": plate, "startFrame": 0, "endFrame": PLATE_FRAMES,
                          "trackIndex": 1, "recordFrame": start, "mediaType": 1}])
    mp.AppendToTimeline([{"mediaPoolItem": jerry, "startFrame": 0, "endFrame": JERRY_FRAMES,
                          "trackIndex": 2, "recordFrame": start, "mediaType": 1}])
    items = tl.GetItemListInTrack("video", 1) + tl.GetItemListInTrack("video", 2)
    tl.CreateFusionClip(items)
    return tl


def open_comp(resolve, tl):
    tl.SetCurrentTimecode(tl.GetStartTimecode())
    resolve.OpenPage("fusion")
    for _ in range(50):
        comp = resolve.Fusion().GetCurrentComp()
        if comp and {"MediaIn1", "MediaIn2", "MediaOut1"} <= tool_names(comp):
            return comp
        time.sleep(0.2)
    raise SystemExit("Fusion page did not open the comp with MediaIn1, MediaIn2 and MediaOut1")


def build(comp, block):
    comp.Lock()
    for t in list(comp.GetToolList(False).values()):
        if t.Name not in KEEP and t.GetAttrs()["TOOLS_RegID"] != "AudioDisplay":
            t.Delete()
    comp.Unlock()
    comp.Execute("comp:Paste(bmd.readstring([==[" + block + "]==]))")  # runs asynchronously
    wanted = set(re.findall(r"^    (\w+) = \w+ \{", block, re.M))
    for _ in range(50):
        if wanted <= tool_names(comp):
            break
        time.sleep(0.2)
    else:
        raise SystemExit("pasted tools did not appear")
    tools = {t.Name: t for t in comp.GetToolList(False).values()}
    for name, key, source in EXTERNAL_LINKS:
        setattr(tools[name], key, tools[source].Output)
    return tools


def verify(tools):
    checks = [("Jerry_Place", "Size", JERRY_SCALE / RESOLVE_FIT), ("Jerry_DarkFill", "ApplyMode", "Lighten"),
              ("Jerry_Over", "Blend", LOOK["core_opacity"]), ("Jerry_Screen", "ApplyMode", "Screen"),
              ("Glow_Add", "ApplyMode", "LinearDodge"), ("Glow_PlateXLight", "Operation", 6.0),
              ("Jerry_Core", "ToAlpha", 3.0), ("Jerry_CoreKey", "High", LOOK["core_low_high"][1])]
    bad = []
    for name, key, want in checks:
        got = tools[name].GetInput(key)
        if (abs(got - want) > 1e-4) if isinstance(want, float) else got != want:
            bad.append(f"{name}.{key} = {got!r}, want {want!r}")
    for name in ["Ridge_Holdout", "Glow_Add"]:
        if tools[name].EffectMask.GetConnectedOutput() is None:
            bad.append(f"{name} has no effect mask")
    for name, key, source in EXTERNAL_LINKS + [("Jerry_Sat", "Input", "Jerry_Place"), ("Ridge_Holdout", "Foreground", "PassB_Slot")]:
        out = getattr(tools[name], key).GetConnectedOutput()
        if out is None or out.GetTool().Name != source:
            bad.append(f"{name}.{key} is not fed by {source}")
    if bad:
        raise SystemExit("verification failed:\n  " + "\n  ".join(bad))


def render_preview(comp, tools, out_dir, frames):
    os.makedirs(out_dir, exist_ok=True)
    comp.Lock()
    saver = comp.AddTool("Saver", 12, 1)
    comp.Unlock()
    saver.Clip = os.path.join(out_dir, "f.png")
    saver.Input = tools["Final_Grade"].Output
    try:
        for f in frames:
            if not comp.Render({"Start": f, "End": f, "Wait": True, "Tool": saver}):
                raise SystemExit(f"render failed at frame {f}")
    finally:
        saver.Delete()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--setting", help="also write the settings block to this .setting file")
    ap.add_argument("--render-preview", metavar="DIR", help="render PNG frames of the result to DIR")
    ap.add_argument("--frames", default=f"0-{JERRY_FRAMES - 1}", help="preview frames, A-B or comma list (comp frames)")
    args = ap.parse_args()

    resolve = dvr.scriptapp("Resolve")
    if resolve is None:
        raise SystemExit("cannot reach Resolve: is it running with External scripting = Local?")
    proj = resolve.GetProjectManager().GetCurrentProject()
    tl = ensure_timeline(resolve, proj)
    comp = open_comp(resolve, tl)
    block = settings_block()
    tools = build(comp, block)
    verify(tools)
    if args.setting:
        with open(args.setting, "w") as fh:
            fh.write(block)
    print(f"project {proj.GetName()}, timeline {tl.GetName()}: comp built and verified")
    if args.render_preview:
        frames = []
        for part in args.frames.split(","):
            a, _, b = part.partition("-")
            frames.extend(range(int(a), int(b or a) + 1))
        render_preview(comp, tools, args.render_preview, frames)
        print(f"rendered {len(frames)} frames to {args.render_preview}")


if __name__ == "__main__":
    main()
