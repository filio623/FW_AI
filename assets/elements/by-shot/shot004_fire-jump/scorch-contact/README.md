# Shot 004 grass-fire inputs (Pass B)

Inputs for the grass-fire inpaint workflow `workflows/comfyui/shot004-working/pass-b_grassfire/shot004_fire-jump_grassfire-inpaint_mick13_v001.json`. Built by `scripts/build_shot004_grassfire_inputs.py`; each JSON report records the exact build settings.

## Contents

- `shot004_grassfire_control-plate-canny-start25-full50_912x512_81f_v001.mp4`: plate window with Canny edges inside the mask. Tests 1–5.
- `shot004_grassfire_control-plate-gray-start25-full50_912x512_81f_v001.mp4`: plate window with flat gray inside the mask. Tests 6 onward.
- `shot004_grassfire_mask-start25-full50-soft_912x512_81f_v001.mp4`: the inpaint mask. Starts at frame 25, covers the burn zone by frame 50.
- `shot004_grassfire_control-plate-canny-gray-start25-full50_912x512_81f_v001.mp4`: plate window with Canny edges on gray inside the mask. For the combined mask.
- `shot004_grassfire_mask-start25-full50-blades4-field050-soft_912x512_81f_v001.mp4`: combined mask, full strength on the blades (strong plate edges grown 4 px), 0.5 on the rest of the spread. Same timing as the solid mask.
- `shot004_grassfire_start-frame_912x512_v001.png`: start frame (gitignored).
- `keyframes/`: Higgsfield stills of the fire at its height, registered to the window (README there).
- `shot004_grassfire_inputs-*.json`: build reports. Their `outputs/` paths are the pre-2026-11-03 locations.

Window: 1824x1024 at plate (1838, 488), scaled to 912x512.

## Source and history

- 2026-11-02: Canny inputs built.
- 2026-11-03: gray inputs built; combined-mask inputs built (`--inside canny-gray --field 0.5`); Higgsfield keyframes added.
- Tests and scores: `shots/shot004_fire-jump_pass-b_grassfire-log.md`.
