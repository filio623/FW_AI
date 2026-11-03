# Grass-fire inpaint, workflow v001

Inputs and raw results for the Pass B grass-fire inpaint (`workflows/comfyui/shot004-working/pass-b_grassfire/shot004_fire-jump_grassfire-inpaint_mick13_v001.json`). Each `testN.mp4` is the ComfyUI output; `testN.png` carries its embedded prompt and workflow, which is what each new run is diffed against.

## Contents

- `candidates/`, `candidates-gray/`: control, mask and start-frame candidates from `scripts/build_shot004_grassfire_inputs.py` (`--inside canny` and `--inside gray`). Chosen versions are copied to `assets/elements/by-shot/shot004_fire-jump/scorch-contact/`.
- `grassfire_inputs_preview_v001.mp4`, `preview_inputs_*.png`, `window_on_plate_f50.png`, `crop_grid.png`: input checks.
- `testN.mp4`, `testN.png`: test outputs. `testN_vs_testM.png` sheets compare a test with the one it changed from.
- `test1_changematte_f80.png`, `test1_edge_f80.png`, `test1_quickcomp.png`: the change-matte prototype that fixes the dark mask ring.
- `saved_test3*.json`: James's saved graphs checked before test 3.
- `stills/`: test 4 frames and contact sheet for the keyframe brief.

## Source and history

- 2026-11-02: inputs built; tests 1–2.
- 2026-11-03: tests 3–8 (A100, EU-RO-1). Tests 6–8 use the gray control; test 8 is test 6 with a second seed.
- Scores: `shots/shot004_fire-jump_pass-b_grassfire-log.md`. Plan and next steps: `shots/shot004_fire-jump_comp-and-pass-b-plan.md`, Pass B.
- Kept clips: `assets/elements/by-shot/shot004_fire-jump/benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test*`.
