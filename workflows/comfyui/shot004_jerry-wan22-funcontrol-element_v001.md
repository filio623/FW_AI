# Shot004 Jerry Wan2.2 FunControl Element v001

Date: 2026-05-19

## Purpose

First local ComfyUI test for Scene 4 / `firewater_test`.

This workflow tests whether the existing fire animation render can drive Jerry's motion while the approved Jerry bible still controls the character look. Treat the output as a fire-character element candidate, not a final comp.

## Source Inputs

- Background plate, for comp context only: `FW_test/Scene 4/FW_test_scene.mov`
- Rough VFX reference: `FW_test/Scene 4/Shot4 V031-1.mp4`
- Motion/control source: `FW_test/Scene 4/ren_small_fire6..mov`
- Jerry look reference: `assets/characters/jerry/character-bible-v001/references/primary-body/JB-001_upright-compact-idle.png`

## Prepared ComfyUI Inputs

- Uploaded image: `jerry_JB-001_upright-compact-idle.png`
- Uploaded control video: `shot004_ren-small-fire6_control_832x448_81f_v001.mp4`
- Local project proxy copy: `outputs/comfyui/scene4_firewater_test_v001/source_proxies/shot004_ren-small-fire6_control_832x448_81f_v001.mp4`

The control video is 832x448, 24 fps, 81 frames. The shot source is 84 frames, but Wan-style video lengths commonly use `4n+1`; 81 frames keeps the run close to 3.5 seconds while matching the node's expected stepping.

## Workflow

File: `workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.json`

Node path:

1. Load Wan2.2 TI2V 5B FP16 model, Wan VAE, and Wan text encoder.
2. Load Jerry reference still.
3. Load the fire render control proxy and split it into frame images.
4. Feed prompt, negative prompt, Jerry reference, and control frames into `Wan22FunControlToVideo`.
5. Sample with Euler/simple, 22 steps, CFG 4.5.
6. Decode and save H.264 MP4 under ComfyUI output prefix `shot004/jerry_wan22_funcontrol_element_v001`.

## Evaluation

Judge this run on:

- Does motion broadly follow the existing fire render?
- Does Jerry keep the approved compact, face-free flame body?
- Is the silhouette clean enough to matte later?
- Does the output avoid baking water, facial features, or extra characters?
- Is the result useful as an element source, or only as motion/look reference?

## Run 001 Result

- Prompt ID: `22c9b551-6789-4d19-80ec-37a037f885c8`
- Status: success
- Runtime: 358.73 seconds
- Output copied to: `outputs/comfyui/scene4_firewater_test_v001/renders/jerry_wan22_funcontrol_element_v001_run001.mp4`
- Element contact sheet: `outputs/comfyui/scene4_firewater_test_v001/review/jerry_wan22_funcontrol_element_v001_run001_contact_8up.jpg`
- Plate preview comp: `outputs/comfyui/scene4_firewater_test_v001/renders/jerry_wan22_funcontrol_plate-key-preview_v001_run001.mp4`
- Plate preview contact sheet: `outputs/comfyui/scene4_firewater_test_v001/review/jerry_wan22_funcontrol_plate-key-preview_v001_run001_contact_8up.jpg`

Output facts:

- 832x448
- 24 fps
- 81 frames
- 3.375 seconds
- H.264 MP4

Review notes:

- Successful technical baseline: the workflow runs locally on Apple MPS and produces a face-free Jerry-like flame element.
- The output preserves the no-face rule.
- The output is too simple and rounded compared with the desired lively fire motion.
- The element is partially cropped in several frames, so the next run needs more frame padding or a smaller/lower-positioned control source.
- Motion control is present but not yet strong enough for final shot timing.
- The dark-background output can be keyed well enough for a quick preview comp, but this is not a final matte/alpha solution.

## Current Limitations

- No ControlNet model files are installed yet.
- IPAdapter nodes exist, but required adapter model files still need to be confirmed or installed.
- This workflow does not preserve the plate because it is element-first.
- Alpha is not native; matte extraction or a later RGBA/alpha workflow is still required.

## Next Branches

- Add matte extraction from the generated element.
- Build a preview comp over `FW_test_scene.mov`.
- Install/test ControlNet models for canny/depth/scribble control.
- Install/test IPAdapter or equivalent reference conditioning for stronger Jerry identity.
- Test ComfyUI API video nodes such as Wan 2.7 Video Edit or Kling 3.0 Omni Video-to-Video as cloud comparison branches, while treating them as preview/reference unless they can produce clean separable elements.
