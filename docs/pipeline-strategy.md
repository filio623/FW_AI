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
