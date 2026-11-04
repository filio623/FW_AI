# Shot 004 comps

Comp project files for shot 004, `_vNNN` each, never overwritten. Every layer a comp loads lives in this shot folder, never in `outputs/` (placement rule, `AGENTS.md`). Versions and what each showed: `../comp_log.md`.

## Contents

- `shot004_fire-jump_comp-blender_run8-passb-s3_v002.blend`: v001 with the Pass B grass fire from Seedance S3 in its Pass B slot (`s004-c-003`). Loads `../pass-b_grassfire/layers/shot004_fire-jump_grassfire-layer-s3_v001/`. Built from v001 by `shots/shot004_fire-jump/scripts/blender/shot004_comp_add_passb.py`.
- `shot004_fire-jump_comp-blender_run8_v001.blend`: Blender Comp v001, run 8 over the plate with an empty Pass B slot (`s004-c-001`), built by `shots/shot004_fire-jump/scripts/blender/shot004_comp_build.py`. The `.blend1` is Blender's automatic backup.
- `shot004_fire-jump_comp-fusion_run8_v001.setting`, `.drp`: the same comp built in Fusion by `shots/shot004_fire-jump/scripts/resolve/shot004_comp_fusion.py`, kept for reference (`s004-c-002`; Resolve project `FW_AI_shot004_comp`).

## Source and history

- 2026-11-02: Blender and Fusion comps built.
- 2026-11-04: v002 with Pass B from S3 added. The delivered comp copy moved to `../reference/`. All comps moved here from `assets/elements/by-shot/shot004_fire-jump/comps/`; their image paths were repointed and v002 renders identically.
- Renders and previews: `../outputs/comp/`.
