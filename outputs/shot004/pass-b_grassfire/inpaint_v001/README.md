# Grass-fire inpaint, workflow v001

Inputs and raw results for the Pass B grass-fire inpaint (`workflows/comfyui/shot004-working/pass-b_grassfire/shot004_fire-jump_grassfire-inpaint_mick13_v001.json`). Each `testN.mp4` is the ComfyUI output; `testN.png` carries its embedded prompt and workflow, which is what each new run is diffed against.

## Contents

- `candidates/`, `candidates-gray/`, `candidates-combo/`: control, mask and start-frame candidates from `scripts/build_shot004_grassfire_inputs.py` (`--inside canny`, `--inside gray`, and `--inside canny-gray --field 0.5`: full-strength mask on the blades, half on the space around them; `preview_combo.png`). Chosen versions are copied to `assets/elements/by-shot/shot004_fire-jump/scorch-contact/`.
- `grassfire_inputs_preview_v001.mp4`, `preview_inputs_*.png`, `window_on_plate_f50.png`, `crop_grid.png`: input checks.
- `testN.mp4`, `testN.png`: test outputs. `testN_vs_testM.png` sheets compare a test with the one it changed from.
- `test1_changematte_f80.png`, `test1_edge_f80.png`, `test1_quickcomp.png`: the change-matte prototype that fixes the dark mask ring.
- `saved_test3*.json`: James's saved graphs checked before test 3.
- `stills/`: test 4 frames and contact sheet for the keyframe brief.

## Source and history

- 2026-11-02: inputs built; tests 1–2.
- 2026-11-03: test 12 (`k2` as a reference at 0.4; about test 10). `candidates-key/`: `k2` inside the control at frames 49–52 (`preview_key.png`), uploaded for test 14.
- 2026-11-03: test 11b (plate in the half-strength area; pale tubes on the blade strips, small fire). Combined-mask branch stopped.
- 2026-11-03: test 11 (combined mask; gray veil). `candidates-combo-plate/`: the fix, plate under the half-strength area (`preview_combo-plate.png`), uploaded for test 11b.
- 2026-11-03: combined-mask candidates built and uploaded to the Pod. Test 10: `vace_strength` 0.8 with extra negatives.
- 2026-11-03: tests 3–9 (A100, EU-RO-1). Tests 6–9 use the gray control; tests 8 and 9 are test 6 with a second and third seed. `mask_vs_fire_f60.png`: the mask's extent against tests 6 and 9.
- Scores: `shots/shot004_fire-jump_pass-b_grassfire-log.md`. Plan and next steps: `shots/shot004_fire-jump_comp-and-pass-b-plan.md`, Pass B.
- Kept clips: `assets/elements/by-shot/shot004_fire-jump/benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test*`.
