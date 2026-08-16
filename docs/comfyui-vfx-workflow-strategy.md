**Created:** 2026-05-19
**Modified:** 2026-05-19
**Version:** 1.0

# ComfyUI VFX Workflow Strategy

## Goal

Develop a repeatable ComfyUI workflow for the short-film VFX pipeline that can generate Jerry/fire and Sally/water as controllable compositing elements over live-action plates.

The workflow should prioritize controllability, separation, and iteration speed over single-pass spectacle.

## Scene 4 Test Target

- Plate: `FW_test/Scene 4/FW_test_scene.mov`
- Rough comp / motion reference: `FW_test/Scene 4/Shot4 V031-1.mp4`
- Jerry motion source: `FW_test/Scene 4/ren_small_fire6..mov`
- Jerry approved references: `assets/characters/jerry/character-bible-v001/`

The first test should recreate Jerry jumping into the grass and triggering ignition, while preserving the base plate for comp.

## Layer Strategy

Use separate passes:

- Jerry fire element
- Jerry matte/alpha
- grass occlusion matte
- contact shadow / grounding
- contact glow and local color-light spill
- grass ignition/fire spread
- smoke, steam, heat distortion
- scorch/darkening
- preview composite over the plate

For Resolve/Fusion handoff, prefer PNG sequences or ProRes/DNxHR intermediates plus separate matte passes. For later After Effects handoff, the same elements still work; avoid workflows that depend on one compositor-only feature.

## Branch Order

### Branch A: Proxy-Controlled Jerry Element

Use the existing CGI/fire render as motion control and Jerry bible stills as look references.

Current implementation:

- `workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.json`
- `Wan22FunControlToVideo`
- control video: `ren_small_fire6..mov` proxy
- reference image: `JB-001_upright-compact-idle.png`

This branch answers whether local Wan2.2 can follow the existing motion strongly enough to become an element source.

### Branch B: Plate-Aware Preview Composite

Use the real plate as context, but still output this branch as a preview only unless matte separation is good.

Candidate approaches:

- ComfyUI API video-edit nodes: Wan 2.7 Video Edit, Kling 3.0 Omni Video-to-Video, Grok Video Edit, Vidu/Runway/Luma nodes if credentials are available.
- Higgsfield CLI/UI Motion Control if it offers better separate slots for plate, motion reference, and Jerry image reference.

Cloud/API models are likely better for overall video quality, but weaker for production control unless they expose separate plate, motion, identity, and matte controls.

### Branch C: Matte/Alpha Extraction

Generate or extract alpha after Branch A:

- black-background fire element matte extraction
- luminance/keyed fire matte
- separate manual cleanup pass in Fusion
- later: alpha-native/RGBA-capable workflows if a reliable model/node path is found

### Branch D: ControlNet/IPAdapter Version

Install model files for control and reference conditioning, then test:

- canny/scribble control for the fire silhouette path
- depth/lineart only if useful for plate interaction
- IPAdapter or equivalent for Jerry look consistency
- LoRA only after the reference set is stable and simple conditioning is not enough

Current blocker: ControlNet model files are not installed locally.

### Branch E: Interaction Passes

Build grass ignition separately from Jerry:

- use `ren_grassfire_cpu..mov` as timing/look reference
- generate ignition/smoke/scorch passes independently
- comp contact light and heat distortion in Fusion

## Model Strategy

### Local

- Use installed Wan2.2 TI2V 5B FP16 first because it is already available and supports local iteration.
- Avoid FP8 diffusion weights on Apple MPS unless a compatible route is proven.
- Consider LTX-2/LTX-2.3 next for faster iteration and image-to-video work. Official LTX docs describe ComfyUI image-to-video as useful for maintaining identity and composition from a source frame, with lower-resolution quick iterations and higher-quality final passes.
- Consider HunyuanVideo 1.5 only after setup review; its technical report describes an 8.3B open-source model for text-to-video and image-to-video with consumer-GPU-oriented efficiency, but local Comfy setup/model compatibility still needs to be verified.

### API / Cloud

Use API/cloud branches as reference or preview unless they can return separable elements or reliable mattes.

Promising local ComfyUI API nodes already present:

- `KlingOmniProVideoToVideoNode`: video plus up to four reference images.
- `Wan2VideoEditApi`: video edit with reference images.
- `Wan2ReferenceVideoApi`: reference-to-video for object/character consistency.
- `Vidu2ReferenceVideoNode` / `Vidu2StartEndToVideoNode`: reference and start/end frame control.
- `RunwayImageToVideoNodeGen4`: first-frame video generation.

Do not spend cloud credits on mixed-reference tests until each input role is isolated.

## Research Sources

- Wan-AI/Wan2.2-TI2V-5B Hugging Face model card: supports T2V/I2V at 720P/24fps and lists ComfyUI integration.
- Wan-AI/Wan2.2-Animate-14B Hugging Face model card: describes character animation/replacement as video plus character image input.
- LTX Image-to-Video docs: recommends image-to-video for maintaining identity and composition from a source frame, with source image, frame count, resolution, FPS, and sampling controls.
- HunyuanVideo 1.5 technical report: describes an open-source 8.3B video model for text-to-video and image-to-video.

## Near-Term Acceptance Criteria

The first useful workflow does not need to look final. It needs to prove:

- Jerry can follow the rough motion path.
- Jerry remains face-free and close to the approved character bible.
- A matte can be extracted or generated.
- The plate remains available as a clean comp base.
- The workflow exposes enough knobs to test one variable at a time.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-19 | Initial ComfyUI VFX Workflow Strategy. |
