"""Render one compositor node's output instead of the comp result, for checking a node tree.

    /Applications/Blender.app/Contents/MacOS/Blender -b FILE.blend \
        --python scripts/blender/comp_tap.py -- FRAME OUT_PREFIX "node name[:output index]" ...

Writes OUT_PREFIX_<n>.exr (scene-linear float) per tapped node. Does not save the .blend.
"""

import sys

import bpy

args = sys.argv[sys.argv.index("--") + 1:]
frame, prefix, taps = int(args[0]), args[1], args[2:]
scene = bpy.context.scene
ng = scene.compositing_node_group
out = next(n for n in ng.nodes if n.bl_idname == "NodeGroupOutput")
scene.frame_set(frame)
scene.render.image_settings.file_format = "OPEN_EXR"
scene.render.image_settings.color_depth = "32"
for i, tap in enumerate(taps):
    name, _, index = tap.partition(":")
    node = ng.nodes[name]
    socket = node.outputs[int(index)] if index else next(s for s in node.outputs if s.enabled)
    for link in list(out.inputs[0].links):
        ng.links.remove(link)
    ng.links.new(socket, out.inputs[0])
    scene.render.filepath = f"{prefix}_{i}.exr"
    bpy.ops.render.render(write_still=True)
    print("tap", name, "->", scene.render.filepath)
