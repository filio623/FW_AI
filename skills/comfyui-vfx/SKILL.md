---
name: comfyui-vfx
description: "Use when working on project-specific ComfyUI workflows for the AI short film: image/video generation, VFX element generation, alpha/matte workflows, ControlNet/IPAdapter/LoRA experiments, Wan/LTX/Hunyuan video tests, model setup on Apple MPS, ComfyUI MCP operations, workflow debugging, and reusable templates for fire/water character shots."
---

**Created:** 2026-05-18
**Modified:** 2026-08-16
**Version:** 1.1

# ComfyUI VFX

## Core Rule

Treat ComfyUI as a controllable VFX element lab, not as the default final-shot generator. Prefer workflows that produce or refine separable elements: RGB, alpha/matte, glow, shadow, contact light, smoke, steam, scorch, splash, and clean reference frames.

## Project Context

- Local ComfyUI is expected at `http://127.0.0.1:8000`.
- Apple MPS is the target local backend. Avoid FP8 diffusion weights on MPS unless a compatible path is proven.
- Project root: `/Users/jamesfilios/Software_Projects/FW_AI`.
- Base ComfyUI paths are documented in `docs/environment.md`.
- Project workflows live in `workflows/comfyui/`.
- Shot notes live in `shots/`.

## Workflow Selection

Use this order when designing a shot workflow:

1. **Plate analysis**: identify camera motion, occlusion areas, contact points, lighting direction, and interaction regions.
2. **Character element plan**: define whether fire/water is generated from stills, rough CGI, masks, ControlNet guides, or video-to-video.
3. **Interaction plan**: separate character performance from environmental effects such as grass ignition, steam, splash, glow, shadows, and scorch.
4. **Alpha strategy**: prefer native RGBA/alpha workflows, clean neutral-background generation with matting, or explicit mask generation.
5. **Compositing handoff**: keep outputs layered and documented for After Effects, Nuke, Fusion, or Resolve.

Avoid pure text-to-video for final assets when the shot requires exact timing, plate interaction, or clean compositing.

## Common Tasks

### Inspect ComfyUI

Use the ComfyUI MCP tools first when available:

- `get_system_stats` for GPU/VRAM and runtime.
- `list_local_models` to confirm checkpoints, diffusion models, VAEs, LoRAs, ControlNets, and text encoders.
- `list_workflows`, `analyze_workflow`, `get_workflow`, and `validate_workflow` for existing workflows.
- `get_queue`, `get_job_status`, `get_history`, and `get_logs` for failed or running jobs.

### Build Workflows

Prefer saving both:

- API/execution workflow: compact and runnable.
- Visible workflow: opened cleanly in the ComfyUI canvas with node layout.

Name workflows with shot, task, model, and version, for example:

`shot004_fire-i2v-wan22-alpha_v001.json`

### Debug Failures

Check in this order:

1. Missing node types or custom node packs.
2. Missing model files or wrong model directories.
3. Unsupported dtype on MPS, especially FP8.
4. Shape/resolution/frame-count mismatches.
5. Broken VAE/text encoder/model pairing.
6. Sampler or scheduler settings that are inappropriate for the model family.

Record durable findings in `docs/findings.md` or the relevant shot note.

## References

Read these only when needed:

- `references/model-notes.md`: local model compatibility and known project findings.
- `references/comfyui-mcp.md`: MCP usage notes and common tool patterns.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial ComfyUI VFX. |
| 1.1     | 2026-08-16 | Replaced stale `/Users/robbiefilios/Documents/FW_AI_Workflow` paths with repo-relative paths and the current workspace root. |
