# Pass B layer from Seedance S3 (s004-b-020)

S3 (`benchmark/shot004_fire-jump_grassfire-flf_seedance20_s3-full169-k2platebg-prompt-timing-480p-4s_seed42_v001.mp4`) on the 4096×2160 plate, built by `scripts/build_shot004_grassfire_layer.py` with `--map 20:25,72:54,96:80`. One file per comp frame, f0001 = plate frame 0.

## Contents

- `gain/`: fire light, a linear gain on the plate at quarter size (scaled ×4 in the comp).
- `rgb/`: S3 registered onto the plate.
- `matte/`: fire matte.
- `zone.png`: the area the fire may occupy. `layer_report.json`: registration, frame map, coverage.

## Source and history

- 2026-11-03: built for the first Blender comp check (`s004-c-003`).
- 2026-11-04: moved here from `outputs/shot004/pass-b_grassfire/layer_s3_v001/`; loaded by `comps/shot004_fire-jump_comp-blender_run8-passb-s3_v002.blend`. Media gitignored; this README and `layer_report.json` tracked.
