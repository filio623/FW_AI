# Shot 004 grass-fire keyframes

Still frames of the grass fire at its height, used to show the Pass B model the look we want: soft, translucent flame tongues among the plate's own blades, like Jerry's fire. Made by James's colleague in Higgsfield as edits of a full plate frame (plate stills may go to Higgsfield as references; `docs/findings.md`, 2026-11-03). The PNGs are gitignored like the plate; this README and the registration JSON are tracked.

## Contents

- `source/shot004_grassfire_keyframe-k<N>_higgsfield-<job>_2752x1536_v001.png`: the four Higgsfield images as delivered, renamed. Original names were `hf_20261103_<time>_<job-id>.png`; the full job IDs are in the JSON.
- `shot004_grassfire_keyframe-k<N>_window_1824x1024_v001.png`: each image registered back onto the 4096×2160 plate and cut to the Pass B window (plate x 1838, y 488), so it lines up with the Pass B inputs pixel for pixel.
- `shot004_grassfire_keyframe-k<N>_window_912x512_v001.png`: the same at the inpaint size. These are what the graph loads (also in the Pod's `input/`).
- `shot004_grassfire_plate-window_f025_1824x1024_v001.png`: the clean plate window at frame 25 (Jerry's landing, before ignition), cut from `plates/FW_test_scene.mp4`. First frame for first-last-frame video models.
- `shot004_grassfire_plate-full169_f025_{3840x2160,1920x1080}_v001.png`: the clean plate at frame 25, cropped to 16:9 (plate x 128–3968, full height), so the Pass B window sits well inside it. First frame for full-frame first-last-frame runs.
- `shot004_grassfire_keyframe-k{2,4}_full169_{3840x2160,1920x1080}_v001.png`: the keyframes registered to the full plate and given the same crop.
- `shot004_grassfire_keyframe-k2_full169-platebg_{3840x2160,1920x1080}_v001.png`: `k2` inside a soft area around its flames (feather about 60 px at 4K) and the plate outside it, so a video model heading for it has no reason to regrade the whole frame.
- `shot004_grassfire_keyframes_registration_v001.json`: original file, Higgsfield job ID, and the similarity transform from each image to plate pixels.

| Key | Higgsfield job | Read |
|---|---|---|
| k1 | 00f25511 | Redrew the blades; one large flame wave across the base. Least faithful to the plate. |
| k2 | 7bf0d60d | Soft tongues among the plate's blades, blades blackening in front, many embers. First choice. |
| k3 | 0b66d612 | Calmer, fewer flames, more embers. |
| k4 | 28f4b4d7 | Like k2, a little sparser on the right. |

All four regrade the whole frame warmer than the plate (outside the fire about +13 luma and +30 red), as fire light would.

## Source and history

- 2026-11-03: received from James (Desktop `higgs/`), moved here, registered to the plate with SIFT and a similarity transform (median error about 2 px at 4K).
- How they are used: `shots/shot004_fire-jump/plan.md`, Pass B tests; runs in `shots/shot004_fire-jump/pass-b_grassfire/log.md`.
