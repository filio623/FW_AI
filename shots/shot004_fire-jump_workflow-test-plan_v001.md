**Created:** 2026-05-18
**Modified:** 2026-10-08
**Version:** 1.6

# Shot004 Fire Jump Workflow Test Plan

## Shot

- ID: `shot004_fire-jump`
- Original base plate (not restored in this checkout): `FW_test/Scene 4/4 base plate.mov`
- Historical `FW_test/` reference paths (also absent here unless separately staged):
  - `FW_test/Scene 4/FW_test_scene.mov`
  - `FW_test/Scene 4/Shot4 V031-1.mp4`
  - `FW_test/Scene 4/ren_small_fire6..mov`
  - `FW_test/Scene 4/ren_grassfire_cpu..mov`
  - `FW_test/Scene 4/ren_steam..mov`
- Current VACE test reference: `assets/elements/by-shot/shot004_fire-jump/plates/FW_test_scene.mp4`; the 49-frame 1280x672 proxy is indexed in `docs/asset-inventory.md`.
- Restored fire motion source: `assets/elements/by-shot/shot004_fire-jump/fire/shot004_fire-jump_ren-small-fire6_source_v001.mov`.
- Status: technical VACE split-run proof complete; the proxy composite was rejected creatively. Next: guided graph review before further sampling.

## Creative Intent

A small sentient fire character jumps across a dirt and grass plate, lands in or near the grass, and causes the grass to ignite. The shot should feel physically integrated with the plate while keeping the fire character and grass interaction separately revisable.

## Core Rule

Do not bake the whole shot into one AI video unless it is only for reference or editorial temp.

The production test should be built from layers.

## Required Layers

- Original plate.
- Fire character element.
- Fire character matte or alpha.
- Grass occlusion matte.
- Contact shadow or grounding pass.
- Fire glow/contact light on nearby grass and dirt.
- Grass ignition/flame spread pass.
- Smoke or heat distortion pass.
- Scorch/darkening pass.
- Final composite review export.

## Questions To Answer First

- What are the plate resolution, frame rate, duration, and codec?
- Do any existing CGI renders include alpha?
- Is `ren_small_fire6..mov` usable as motion/silhouette control?
- Is `ren_grassfire_cpu..mov` usable as an interaction reference or pass?
- Does the shot require the fire character to pass behind any grass or foreground detail?
- What frame should ignition begin?
- Does the final fire character need to match the CGI performance exactly, or only the broad action?

## Workflow Branches To Test

### Branch A: CGI/Proxy To AI Polish

Use the existing fire CGI as motion and silhouette guidance, then use AI to improve the look.

Inputs:

- `FW_test/Scene 4/ren_small_fire6..mov`
- Base plate stills for lighting context.
- Fire character prompt language.

Desired output:

- Improved fire character clip.
- Matte or alpha.
- Motion close to the original CGI.

Why this matters:

- This is likely the most controllable production path if the current CGI has useful timing.

### Branch B: Alpha-Native Fire Element

Use Wan-Alpha or another RGBA-capable workflow to generate a fire character element with transparency.

Inputs:

- Fire character prompt.
- Approved fire still or first frame if available.
- Neutral or transparent-compatible generation setup.

Desired output:

- Fire character with usable alpha.
- Clean silhouette.
- Minimal baked background contamination.

Why this matters:

- Native alpha could reduce roto/matting pain if the character quality is acceptable.

### Branch C: First/Last Frame Or I2V Motion

Create keyframes for the fire character jump, then let a video model interpolate or animate.

Inputs:

- Start pose.
- Landing pose.
- Prompt describing the jump and energy.
- Optional CGI frame references.

Desired output:

- Short controlled fire jump clip.
- Consistent character identity.
- Usable matte extraction path.

Why this matters:

- This tests whether we can direct action without relying on full proxy animation.

### Branch D: Cloud Reference

Use Higgsfield or another cloud model to generate a high-quality reference for motion, timing, or aesthetics.

Inputs:

- Base prompt.
- Optional plate/reference media if supported.
- Fire character description.

Desired output:

- Reference clip only, unless it separates cleanly.

Why this matters:

- Cloud output can show what good motion and style might look like, even when it is not directly compositable.

### Branch E: Interaction Passes

Generate or build the grass ignition, smoke, heat, glow, and scorch separately from the character.

Inputs:

- Base plate.
- Grass region mask.
- Timing from the character jump.
- Existing `FW_test/Scene 4/ren_grassfire_cpu..mov` and `FW_test/Scene 4/ren_steam..mov` references.

Desired output:

- Ignition pass.
- Smoke/steam or heat pass.
- Scorch/darkening pass.
- Glow/contact light pass.

Why this matters:

- The interaction may be easier to control as separate layers than as part of character generation.

## Acceptance Criteria

The test workflow is successful if:

- The plate remains intact.
- The fire character can be moved, retimed, or regenerated without replacing the grass ignition pass.
- The grass ignition can be adjusted without regenerating the character.
- The character reads consistently across the clip.
- The matte/alpha is good enough for a rough comp.
- At least one workflow branch is clearly worth developing into a reusable template.

## First Pass Task List

- Verify metadata and alpha status for all `FW_test/Scene 4/` videos.
- Extract representative still frames from:
  - base plate
  - fire character render
  - grass fire render
  - steam render
  - existing composite/reference
- Create a simple frame/action map for the fire jump.
- Define the first desired fire character look.
- Run Branch A and Branch B before investing in LoRA training.
- Create a rough comp proof with separated character and interaction timing.

## Notes Log

- 2026-05-18: Created as the first workflow test plan for developing the film's AI-assisted VFX pipeline.
- 2026-05-19: Confirmed current source paths:
  - Plate: `FW_test/Scene 4/FW_test_scene.mov`
  - Rough VFX/motion reference: `FW_test/Scene 4/Shot4 V031-1.mp4`
  - Fire motion/control reference: `FW_test/Scene 4/ren_small_fire6..mov`
- 2026-05-19: Metadata check:
  - `FW_test_scene.mov`: 4096x2160, HEVC Main 10, BT.709, 24 fps, 84 frames, 3.5 seconds.
  - `Shot4 V031-1.mp4`: 1920x1080 H.264, BT.709, 24 fps, 84 frames, 3.5 seconds.
  - `ren_small_fire6..mov`: 1920x1080 H.264, 24 fps, about 3.63 seconds; use as a motion/silhouette reference, not final character quality.
- 2026-05-19: ComfyUI inspection:
  - Runtime: ComfyUI 0.21.1, Apple MPS, large shared memory pool.
  - Installed local model path has SD 1.5 and Wan2.2 assets, including `wan2.2_ti2v_5B_fp16.safetensors`.
  - No ControlNet model files are currently installed.
  - IPAdapter and ControlNet node surfaces exist, but the required adapter/control model files still need to be installed or verified.
- 2026-05-19: Created first local ComfyUI Branch A workflow:
  - Workflow: `workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.json`
  - Note: `workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.md`
  - Purpose: use `Wan22FunControlToVideo` with `JB-001` as Jerry look reference and `ren_small_fire6..mov` as control video.
  - Prepared proxy: `outputs/comfyui/scene4_firewater_test_v001/source_proxies/shot004_ren-small-fire6_control_832x448_81f_v001.mp4`
  - Validation: workflow validated successfully in ComfyUI.
- 2026-05-19: Ran Branch A Run 001 successfully.
  - Prompt ID: `22c9b551-6789-4d19-80ec-37a037f885c8`
  - Runtime: 358.73 seconds
  - Element output: `outputs/comfyui/scene4_firewater_test_v001/renders/jerry_wan22_funcontrol_element_v001_run001.mp4`
  - Preview comp: `outputs/comfyui/scene4_firewater_test_v001/renders/jerry_wan22_funcontrol_plate-key-preview_v001_run001.mp4`
  - Technical result: local Wan2.2 FunControl path runs and creates a clean face-free flame element.
  - Creative result: not final; motion is still too simple, several frames are cropped, and matte/alpha extraction needs a dedicated branch.
- 2026-08-18: Restored fire motion source from `/Volumes/FW_Backup` and rebuilt the control proxy:
  - Source: `assets/elements/by-shot/shot004_fire-jump/fire/shot004_fire-jump_ren-small-fire6_source_v001.mov`
  - Original filename copy: `assets/elements/by-shot/shot004_fire-jump/fire/ren_small_fire6..mov`
  - Control proxy: `assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_control_832x448_81f_v001.mp4`
  - Proxy rebuild is pad-to-fit at 832x448, first 81 frames, so the fire is not cropped.

- 2026-10-08: A RunPod A40 VACE 14B attempt at 1280×672 and 49 frames
  finished all 26 sampler steps in about 31 minutes, but the untiled
  `VAEDecode` exhausted the Pod's 50 GB RAM limit. ComfyUI exited before
  saving video; no generated shot artifact was retained.
  The local `FW_Test_Workflow_Vace_Ready.json` in `~/Downloads/` now uses
  `VAEDecodeTiled` (512-pixel tiles, 64-pixel spatial overlap,
  16-frame temporal chunks, 4-frame temporal overlap). A separate
  full-size 49-frame synthetic-latent decode succeeded, but the complete
  VACE workflow has not yet been rerun or reviewed.

- 2026-10-08: The second full 26-step A40 VACE attempt also finished
  sampling before ComfyUI was OOM-killed at the 50 GB container limit.
  Neither attempt saved a latent or a video; sampler output is unrecoverable.
  The previously saved all-in-one workflows had untiled `VAEDecode`;
  the submitted graph disappeared with the process, so the decoder used
  on retry is unknown. A separate finishing-only smoke using the staged
  4096x2160, 84-frame Scene 4 reference and 4K composite also OOM-killed
  the server, even with tiled decode.
- Recovery is split into `workflows/comfyui/shot004_fire-vace14b_sample-latent_v001.json`
  (VACE sampling through `TrimVideoLatent` and `SaveLatent`, no decode) and
  `workflows/comfyui/shot004_fire-vace14b_decode-latent_v001.json`
  (load the saved latent, tiled VAE decode, and 1280x672 proxy composite).
  The finishing workflow reads
  `assets/elements/by-shot/shot004_fire-jump/plates/shot004_fw-test-scene_plate-proxy_1280x672_49f_v001.mp4`
  staged on the Pod as `ComfyUI/input/shot004_fw-test-scene_plate-proxy_1280x672_49f_v001.mp4`.
  Select the actual `shot004_vace_latent_*.latent [output]` filename from the
  first workflow before queuing the second if its counter differs.
  A 49-frame synthetic-latent end-to-end finishing smoke produced a
  1280x672/24 fps MP4, with 7.82 GB peak container RAM and no OOM.
  At the time of this smoke, the real VACE sampler and two-stage sequence
  had not yet been run together; it proved finishing mechanics, not quality.

- 2026-10-08: The user ran the split sampling workflow successfully.
  ComfyUI logged completion in 31:28 and saved
  `ComfyUI/output/shot004_vace_latent_00001_.latent` (11,205,224 bytes).
  The separate proxy finishing workflow then completed as prompt
  `6f56566d-9c3e-4940-895e-0655e95509a8`, saving
  `ComfyUI/output/FW_fire_comp_proxy_00001_.mp4` (49 frames, 1280x672,
  24 fps, 2.042 s). No OOM event occurred on the successful split run.
  Local ignored review copy:
  `outputs/comfyui/shot004_fire-jump/shot004_fire-vace14b_proxy-comp_v001.mp4`.
  Early, middle, and late frame review shows an orange fire shape/glow on
  the ground, but conspicuous green/magenta image artifacts and no
  approved character look. This is a technical proof, not a deliverable.

## Next Session: Guided VACE Workflow Review

The user reviewed `shot004_fire-vace14b_proxy-comp_v001.mp4` and judged the
result unacceptable as a finished product. Do not promote this proxy as an
approved look or queue another expensive run without first walking through
the graph together. The successful latent and rejected export are baselines,
not creative approvals. No workflow parameters were changed after this review.

1. Agree on the intended shot using the plate, original fire motion,
   storyboard/character references, and specific frames of the rejected
   export. Establish desired silhouette, trajectory, scale, timing, and
   integration before diagnosing the model.
2. Trace the sampling inputs: `JB-001_upright-compact-idle.png`,
   `JB-010_round-idle-glow.png`, the 832x448 fire-motion control, and the
   staged `FW_test_scene.mp4` reference. Inspect how the scaling/cropping,
   batched reference frames, circular mask, blur, and screen blend condition
   `WanVaceToVideo`; verify each is the intended source and position.
3. Read the positive and negative text prompts together. Review the current
   VACE settings (1280x672, 49 frames, strength 0.5), then the fixed-seed
   sampler (seed 42, 26 steps, CFG 6, `uni_pc`/`simple`). Decide which
   controls to keep only after identifying the first visible failure.
4. Decode the **saved** latent separately and compare raw generated frames
   with the composite. Trace the finishing chain: tiled VAE, 49-frame
   Scene 4 proxy, red-channel-derived mask, circular blur/resize, and
   `ImageCompositeMasked`. Determine whether the green/magenta artifacts,
   fire shape, and motion problems precede or arise during compositing.
5. Make one controlled change at a time in a new version of the workflow,
   keep this latent and export intact, and compare the same early/middle/late
   frames before approving any further full sampling run. The current
   1280x672 proxy and its staged Scene 4 reference are not a 4K final plate.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Shot004 Fire Jump Workflow Test Plan. |
| 1.1     | 2026-08-18 | Recorded the restored fire source and rebuilt 832x448 control proxy under `assets/elements/by-shot/shot004_fire-jump/fire/`. |
| 1.2     | 2026-10-08 | Recorded the VACE sampler completion, post-sampling decode OOM, and validated tiled-decode mitigation without claiming a finished render. |
| 1.3     | 2026-10-08 | Recorded the second post-sampler OOM, the separate 4K composite OOM, split latent workflows, and successful 1280x672 finishing smoke. |
| 1.4     | 2026-10-08 | Logged the first successful split VACE latent and proxy composite, with technical output and visual-review limitations. |
| 1.5     | 2026-10-08 | Recorded the user's rejection of the proxy result and the specific next-session walkthrough before further generation. |
| 1.6     | 2026-10-08 | Clarified unrestored historical input paths, identified the staged test media, and updated shot status from planning to guided review. |
