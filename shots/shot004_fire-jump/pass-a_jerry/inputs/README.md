# Shot 004 Pass A inputs

Control videos built from the Houdini fire (`../../reference/ren_small_fire6..mov`), 832x448, 24 fps, 81 frames (the first 81 of 87).

## Contents

- `shot004_ren-small-fire6_control_832x448_81f_v001.mp4`: the fire scaled pad-to-fit so it is not cropped. The frozen motion input.
- `shot004_ren-small-fire6_trajectory-dot_832x448_81f_v001.mp4`: path only, the luma centroid as a soft ~56 px warm dot on black.
- `shot004_ren-small-fire6_trajectory-streak_832x448_81f_v001.mp4`: stronger path control, ~72 px head and a 10-frame trail.
- `shot004_ren-small-fire6_control-shrunk40_832x448_81f_v001.mp4`: the fire silhouette scaled 40% about its centroid.
- `shot004_ren-small-fire6_control-graymask-grow16_832x448_81f_v001.mp4`, `shot004_ren-small-fire6_mask-grow16-soft_832x448_81f_v001.mp4`: gray-in-mask control and soft mask for the Mick 1.3 runs.

The smaller guide (candidate `grow6-round14-30-post125`, built by `../../scripts/build_shot004_guide.py`) is in `../../outputs/pass-a_jerry/guide_v002/` until James approves it; on approval it comes here as `_v001`.

## Source and history

- 2026-09-03: control, trajectory and shrunk controls built.
- 2026-10-19: gray-mask control and mask for the Mick 1.3 runs.
- 2026-11-04: moved here from `assets/elements/by-shot/shot004_fire-jump/fire/`.
