# Pass B layer from Seedance S3

S3 (`../seedance-flf_v001/sd03_full169-platebg-timing-480p.mp4`) on the 4096×2160 plate, built by `scripts/build_shot004_grassfire_layer.py` with `--map 20:25,72:54,96:80`. One file per comp frame, f0001 = plate frame 0.

## Contents

- `gain/`: fire light, a linear gain on the plate at quarter size (scaled ×4 in the comp).
- `rgb/`: S3 registered onto the plate.
- `matte/`: fire matte.
- `zone.png`: the area the fire may occupy. `layer_report.json`: registration, frame map, coverage.

## Source and history

- 2026-11-03: built for the first Blender comp check (`../../comp/blender/passb_s3/`). Log: `shots/shot004_fire-jump_pass-b_grassfire-log.md`.
