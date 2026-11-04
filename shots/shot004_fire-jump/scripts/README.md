# Shot 004 scripts

Scripts used only by this shot. Run from the repo root with `/usr/local/bin/python3` (numpy, OpenCV) or Blender/ResolvePython as noted at the top of each file.

- `build_shot004_guide.py`: Pass A gray-in-mask guide and mask from the Houdini fire control.
- `build_shot004_grassfire_inputs.py`: Pass B inpaint inputs (window, spreading mask, control; combined masks; keyframes inside the control).
- `build_shot004_grassfire_layer.py`: turns a full-frame fire clip (first-last-frame video) into a Pass B layer: registration onto the plate, retime, fire light as a gain, fire matte.
- `shot004_comp_geometry.py`: plate placement and mask geometry shared by the comp builders.
- `blender/shot004_comp_build.py`: builds the Blender comp node tree (`comps/…_v001.blend`). `blender/shot004_comp_add_passb.py`: adds a Pass B layer to a comp and saves a new version.
- `resolve/shot004_comp_fusion.py`: the same comp as a Fusion node tree in Resolve Studio (reference only).

## Source and history

- 2026-11-04: moved here from `scripts/`, `scripts/blender/` and `scripts/resolve/`.
