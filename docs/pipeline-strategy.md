**Created:** 2026-05-18
**Updated:** 2026-11-03

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

Plate use (James, 2026-11-03; replaces the 2026-10-11 rule "never upload the plate", whose reason was not recorded): stills or crops of the plate may go to Higgsfield as references, for example a plate frame to paint a burning-grass keyframe into. Parts of a Higgsfield-generated asset may be used in the comp or as reference stills. Keep whole plate clips and full-resolution plate media in the repo, on the NAS and on RunPod Secure Cloud, and share them only privately.

### Blender

Under evaluation, not adopted. A Jerry fire rig exists at `characters/jerry/source-cgi/jerry_fire-rig_v001.blend`. Setup is in `mcp/blender.md`. The run log is `characters/jerry/fire-rig/jerry_fire-rig_log_v001.md`. r09 is not an approved look.

Its job, if the pose and dash tests pass, would be rigged simulated elements rendered to multilayer EXR for compositing. It is not the shot 004 motion driver. That driver stays the Houdini fire proxy until a scored benchmark row replaces it.

Separately, Blender is the first compositing tool (decided 2026-11-02). The agent builds comps as Blender compositor node trees by script, renders and checks them, and hands over a `.blend` for James to adjust. Shot 004's plan is `shots/shot004_fire-jump/plan.md`.

### Compositing App

Use After Effects, Nuke, Fusion, or Resolve for final assembly. For agent-built comps, start in Blender (above). Move to Fusion when Resolve's color tools are needed: James has DaVinci Resolve Studio 21.1.1, so external scripting is available. Final assembly covers:

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
