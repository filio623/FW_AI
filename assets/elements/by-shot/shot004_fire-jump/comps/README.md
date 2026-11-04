# Shot 004 comps

Comp project files for shot 004, `_vNNN` each, never overwritten. Every layer a comp loads also lives under `assets/` (placement rule, `AGENTS.md`). Versions and what each showed: `shots/shot004_fire-jump/comp_log.md`.

## Contents

- `shot004_fire-jump_comp-blender_run8-passb-s3_v002.blend`: v001 with the Pass B grass fire from Seedance S3 in its Pass B slot (`s004-c-003`). Loads `../scorch-contact/layers/shot004_fire-jump_grassfire-layer-s3_v001/`. Built from v001 by `scripts/blender/shot004_comp_add_passb.py`.
- `shot004_fire-jump_comp-blender_run8_v001.blend`: Blender Comp v001, run 8 over the plate with an empty Pass B slot (`s004-c-001`), built by `scripts/blender/shot004_comp_build.py`. The `.blend1` is Blender's automatic backup.
- `shot004_fire-jump_comp-fusion_run8_v001.setting`, `.drp`: the same comp built in Fusion by `scripts/resolve/shot004_comp_fusion.py`, kept for reference (`s004-c-002`; Resolve project `FW_AI_shot004_comp`).
- `shot004_fire-jump_comp-houdini-delivered-v031_1920x1080_v001.mp4`: the delivered Houdini comp (1920x1080, 84 frames), for comparison; ignition about frame 23, grass spreads through about frame 48. Production name `Shot4 V031-1.mp4` (renamed 2026-11-04); the NAS original is `Shot4 V031-1.mov`.

## Source and history

- 2026-11-02: Blender and Fusion comps built.
- 2026-11-04: v002 with Pass B from S3 added; the delivered comp copy renamed to the project naming.
- Renders and previews: `outputs/shot004/comp/`.
