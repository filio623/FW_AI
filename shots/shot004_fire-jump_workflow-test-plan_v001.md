**Created:** 2026-05-18
**Modified:** 2026-10-19
**Version:** 1.16

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
- Status: stock VACE Pass A is scored and closed. Path can lock; the still's look does not transfer. Next test is Wan 2.7 Video Edit. Score sheet: `docs/vfx-element-benchmark.md`.

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

- 2026-10-09: Pod `03vbr9yofvf2z4` (A40, `CA-MTL-1`, volume `avw5iclb48`)
  resumed the same latent. A decode-only prompt
  `7886d760-9025-4124-92e9-ebcb5e04db04` (15.2 s) wrote
  `ComfyUI/output/shot004_raw_tiled_f000_00001_.png`,
  `shot004_raw_tiled_f024_00001_.png`, and
  `shot004_raw_tiled_f048_00001_.png` from
  `VAEDecodeTiled` with the same 512/64, 16/4 settings. No new sample.
  The raw frames already contain the green/magenta blobs. Inside the
  composite mask, raw vs rejected proxy differs by about 5 levels, which
  is h264 error. Plate, fire-control, and both Jerry stills are clean.
  Latent `shot004_vace_latent_00001_.latent` is `(1, 16, 13, 84, 160)`
  float32, no NaN/Inf, range about -9.6 to 8.9. The inactive region
  decodes as the plate, so tiled VAE decode is not the color failure.
  Causes in the sampling graph, confirmed against ComfyUI 0.30.0
  `WanVaceToVideo`: the positive prompt describes grass ignition, not a
  jumping character; the control mask is a static 800×380 ellipse while
  the CGI fire covers 1–3% of the frame; `reference_image[:1]` drops
  `JB-010`; the control video is a 0.55 screen blend of plate and fire;
  strength 0.5 and CFG 6 let the model invent chroma garbage inside that
  large mask. By frame 48, 27% of the CGI fire has left the ellipse, and
  the raw frame shows a green ghost where a character should be.
- 2026-10-11: Branch D Higgsfield run 001, through the official MCP
  (the trial account blocks CLI/API generation). Motion:
  `outputs/shot004_houdini-motion_1280x720_96f.mp4`, made from
  `shot004_fire-jump_ren-small-fire6_source_v001.mov` (87 frames)
  scaled to 1280×720 with 9 black frames added (96 frames, 4.0s). Look:
  `JB-001`, `JB-010`, `JB-004`. Prompt: replace the fire shape with a
  faceless flame creature, keep path/timing/size, pure black, no scene.
  `kling_video_edit` std (job `acf90fd4-82df-4b6d-a8dd-ffce0d4386be`)
  failed with no reason given; its 6 credits were refunded.
  `seedance_2_5` `video_edit` 480p, no audio (job
  `989f837b-f97a-461d-a0d2-ab83caa6dd69`, 14 credits) completed:
  `outputs/higgsfield/shot004_jerry_seedance25-edit_480p_run001.mp4`,
  854×480, 24 fps, 89 frames. Look holds (JB-style core and comet tail,
  no face, background black at ≤2/255). Not path-locked: brightness
  centroid within ~4–8% of frame width through frame 24, then 16–19%
  of frame width left of the Houdini landing from frame 30 on. About
  3–4× the Houdini fire's area. Jerry hard-cuts to black at frame 82;
  the source fire runs to 86. Usable as a look/reference clip, not as
  a locked element.
- 2026-10-11: Pass A VACE 14B Run 001 (`shot004_fire-vace14b_sample-latent_v001_pass_A.json`, prompt `ce04c4d6-b605-46c0-a3d4-1ac1a8e83107`) ran 17 frames on black at 1280×672 (`strength=1.0`, `cfg=3.0`, `JB-001` reference, Houdini fire-on-black control video, red-channel mask expanded by 20px and blurred by 8px) and saved `ComfyUI/output/shot004_vace_latent_00003_.latent`. Decoded video (`FW_fire_comp_proxy_00003_.mp4` / `00004_.mp4`) followed the Houdini jump trajectory on black cleanly, but `strength=1.0` copied the rough Houdini flame texture rather than transferring `JB-001`'s look.
- 2026-10-13: Tested ComfyUI `KlingMotionControl` (Node ID `4463629993286452`) on Pod `qgdedf20w84gnp`. First attempt failed with `Unauthorized: Please login first to use this node`; second attempt after login failed at Kling's server pre-check (`task_id: 939111787268550684`, 0 credits charged): `Image recognition failed. Please make sure your image meets the requirements. Error: No complete upper body detected in the image; ensure the upper body is clearly visible.` `KlingMotionControl` requires a human upper-body skeleton and cannot be used for non-humanoid fire elements.
- 2026-10-17: Wan 2.7 Video Edit (`Wan2VideoEditApi`) on Pod `qblvqx3v4pjho8`, prompt `1a2d2bf9-982f-444c-b53d-3f2068eeed7c`, graph `workflows/comfyui/shot004_fire-jump_wan27-videoedit_api_v001.json`: Houdini control clip (81f, 24 fps, 832×448) + `JB-001` as `image1`, 720P, 16:9, duration auto, seed 42, $0.68. Output 101 frames at 30 fps 1280×720 with generated audio, kept as `assets/elements/by-shot/shot004_fire-jump/benchmark/shot004_fire-jump_wan27-videoedit_seed42_v001.mp4`. Trajectory pass (≤2.3% of frame width centroid drift), black pass, no face. Look fail: a clean, glossy teardrop with a white core from frame 1, not `JB-001`'s wispy fireball. An unauthenticated dry submit (`3e7b7f4b-…`) failed with `Please login first` at no cost.
- 2026-10-17: Wan 2.7 Video Edit run 2 on Pod `ep5rr963ctx22t`, queued by hand from the canvas (prompt `464e0967-23df-4c19-b817-f50990c4595e`). Same graph, prompt, inputs, and 720P settings as run 1; seed `2126129005` (randomized), $0.676. Kept as `assets/elements/by-shot/shot004_fire-jump/benchmark/shot004_fire-jump_wan27-videoedit_seed2126129005_v001.mp4`. Passes trajectory (≤5.5% centroid drift, landing 0.3%), look (reads as `JB-001`, slightly peachier), and black (only its own smoke, ≤17/255). Soft compared with the still, so this is the Pass A candidate pending sharpness work. An earlier attempt (`7418a0d9-…`) failed with `Please login first` before sign-in, at no cost.
- 2026-10-18: Wan 2.7 run 3 on Pod `iqe2i06yi7w9uy` (prompt `7f8c7ace-7e67-4062-9584-49dc5a72d228`, 196 s): prompt v2, `JB-001` + `JB-010`, seed 508. Kept as `…/benchmark/shot004_fire-jump_wan27-videoedit_seed508-promptv2-jb010_v001.mp4`. Recognizable (user: ~75%) but 25–27% off mid-jump with no flame on frame 0. Three changes at once, so confounded.
- 2026-10-18: Wan 2.7 run 4 on Pod `aafjaefo4nupf4` (prompt `0acfe4cd-c788-49a3-beac-c3edf849f320`, 215 s), intended as a reproducibility check of run 2 but run with `JB-010` still wired as `image2`. Kept as `…/benchmark/shot004_fire-jump_wan27-videoedit_seed2126129005-jb010_v001.mp4`. White glossy teardrop, path fail. Same seed plus one image gave an unrelated sample, so Wan 2.7 tuning stopped with run 2 as the paid fallback. Both runs had an earlier `Please login first` attempt at no cost.
- 2026-10-19: Mickmumpitz 1.3 ADV with the VACE × SkyReels merge on Pod `amsu1bpsrdzgfr`, graph `shot004_fire-jump_mick13-skyreels_v001` (FusionX, 5 steps, CFG 1, `res_2s`/`beta57`, 512p, `JB-001` Reference Only, NAG and Lenovo bypassed). Run 1 (`6bac1820`) used the Houdini fire RGB as driving video and mask and traced it. Run 2 (`c52a9114`) switched to gray-in-mask inputs and got its own body, but with a face. Run 3 (`2d60bae7`) used a "round ball" prompt and got an opaque sphere. Run 4 (`663517dd`) used prompt v3 and got a close, faceless flame body. Run 5 (`3924211c`, `seed_1` 1218565630 after restoring the seed wire) replicated it with the tightest path yet (≤0.9% / ≤1.9%). Run 6 (`05ac8918`) added `JB-010` and looked very similar. Clips are kept in `…/benchmark/shot004_fire-jump_mick13-skyreels_*_v001.mp4`; the inputs are in `…/fire/`. Four earlier attempts did not render: two skipped generation with `resume_from_iteration` 1, one failed in NAG, and one was cancelled. NAG was then bypassed and the crossfade node patched.
- 2026-10-19 (00:08–00:51Z on 10-20, Pod `jnfjz83llx199h`, ~$0.43): KJNodes `WanVideoNAG` patched for FP8 on the volume, not yet exercised. Run 7 (`ca30dacf`): run 6 with `vace_strength` 1.0. More flame texture, but a gray cone from the guide shows at the top. Run 8 (`56fa49b0`): `vace_strength` 1.25 plus the Lenovo LoRA with `l3n0v0`. No cone, more ragged flame tongues; current best. Run 8's two changes are not separated. One cancelled attempt (`7ab6a0e6`) ran before `l3n0v0` was added. Next session: benchmark step 8c (NAG with negatives, 720p, comp check).

## Current Test Status

Working queue and scores: `docs/vfx-element-benchmark.md`. Do not keep a second queue here.

As of 2026-10-17, local `WanVaceToVideo` knobs are closed. Strength `1` copied the Houdini fire. Strength `0.5` smeared it. A white-mask control video was drawn as gray smoke and did not become `JB-001`. Kling Motion Control cannot take a non-human still. Kling Omni Edit ramps the look in late. Next test is Wan 2.7 Video Edit, then Runway Aleph only if that fails. Pass B waits for a Pass A winner.


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
| 1.7     | 2026-10-09 | Diagnosed green/magenta as sample conditioning, not composite or tiled VAE decode; recorded the raw latent frames and the next conditioning change. |
| 1.8     | 2026-10-11 | Logged Branch D Higgsfield run 001: Kling Omni Edit failed (refunded), Seedance 2.5 video_edit result with measured path drift. |
| 1.9     | 2026-10-13 | Logged Pass A VACE Run 001 (`00003_.latent`), `KlingMotionControl` human-upper-body rejection, and the structured Phase 1–3 VFX testing roadmap. |
| 1.10    | 2026-10-13 | Pointed the Pass A roadmap at `docs/vfx-element-benchmark.md` as the working score sheet. |
| 1.11    | 2026-10-17 | Replaced the open strength/silhouette queue with the closed VACE result and pointed current work at the benchmark. |
| 1.12    | 2026-10-17 | Logged the Wan 2.7 Video Edit run: path and black pass, look fails. |
| 1.13    | 2026-10-17 | Logged Wan 2.7 run 2 (seed 2126129005) as the first Pass A candidate. |
| 1.14    | 2026-10-18 | Logged Wan 2.7 runs 3 and 4 and the stop on Wan 2.7 tuning. |
| 1.15    | 2026-10-19 | Logged Mick 1.3 SkyReels runs 1–6 and the first local setup to pass path, black, and face on two seeds. |
| 1.16    | 2026-10-19 | Logged Mick 1.3 runs 7 and 8 and the next-session order. |
