**Created:** 2026-05-18
**Modified:** 2026-10-17
**Version:** 1.1

# Pipeline Strategy

## Goal

Create consistent fire and water characters that can be animated, art-directed, and composited over existing environmental plates.

## Recommended Direction

Use AI as part of a VFX pipeline, not as a replacement for the whole shot.

Primary outputs should be:

- Character RGB.
- Character alpha or matte.
- Glow/light pass.
- Shadow/contact pass.
- Interaction pass: grass fire, scorch, steam, splash, wetness, smoke, or heat distortion.
- Notes for comp integration.

## Tool Roles

### ComfyUI

Use for controlled local experiments:

- Character stills and keyframes.
- Video-to-video polish from CGI/proxy animation.
- ControlNet/IPAdapter/LoRA testing.
- Alpha/matte workflows.
- Plate-aware interaction passes.

### Higgsfield

Use for high-quality cloud generation:

- Motion exploration.
- Reference renders.
- Model comparisons.
- Temp baked shots.
- Candidate element-generation tests when separability is not required or can be extracted.

### Blender

Under evaluation, not adopted. A Jerry fire rig exists at `assets/characters/jerry/source-cgi/jerry_fire-rig_v001.blend`. Setup is in `mcp/blender.md`. The run log is `workflows/blender/jerry/jerry_fire-rig_log_v001.md`. r09 is not an approved look.

Its job, if the pose and dash tests pass, would be rigged simulated elements rendered to multilayer EXR for compositing. It is not the shot 004 motion driver. That driver stays the Houdini fire proxy until a scored benchmark row replaces it.

### Compositing App

Use After Effects, Nuke, Fusion, or Resolve for final assembly:

- Layer timing.
- Masks and roto.
- Color integration.
- Grain.
- Motion blur.
- Light wrapping.
- Final review exports.

## Avoid

- Pure text-to-video as the default final-shot method.
- Baked outputs when a shot needs revisions by layer.
- Training LoRAs before the visual target and dataset requirements are clear.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Pipeline Strategy. |
| 1.1     | 2026-10-17 | Added Blender as an unevaluated CG track and kept it off the shot 004 motion driver. |
