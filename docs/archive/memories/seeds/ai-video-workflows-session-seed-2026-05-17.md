# AI Video Workflows Memory Seed

Date: 2026-05-17
Project: AI short-film VFX workspace
Container tag: ai-video-workflows

## Project Goal

The user is building an AI-assisted VFX pipeline for a short film. The film needs consistent small fire and water droplet characters that can animate and react on screen over existing environmental footage.

The target is not generic AI video. The target is controllable character/effect generation that can be composited over real plates.

## Core VFX Requirement

Keep original plates untouched whenever possible. Generate separable elements and passes for compositing:

- character RGB
- alpha/matte
- glow or contact light
- shadow/contact pass
- smoke, steam, splash, scorch, wetness, heat distortion, or grass fire interaction passes

Final assembly should happen in a compositing app such as After Effects, Nuke, Fusion, or Resolve.

## Fire And Water Characters

The project has CGI-rendered fire and water character files in `FW_test/`. These are not the desired final look, but they are valuable references for:

- character identity
- motion/timing
- LoRA training material
- IPAdapter/reference conditioning
- ControlNet guides
- proxy animation for video-to-video refinement

## Current Test Assets

`FW_test/` contains:

- `4 base plate.mov`
- `FW_test_scene.mov`
- `Shot4 V031-1.mp4`
- `ren_grassfire_cpu..mov`
- `ren_small_fire6..mov`
- `ren_small_waterCHAR8..mov`
- `ren_small_waterSplash..mov`
- `ren_steam..mov`

`ffmpeg` and `ffprobe` were not installed in the shell during setup, so codec, resolution, duration, frame rate, and alpha-channel status still need verification.

## ComfyUI Findings

Local ComfyUI is available at `http://127.0.0.1:8000`. The observed version was `0.21.1`.

ComfyUI local paths:

- models: `/Users/robbiefilios/Documents/ComfyUI/models`
- input: `/Users/robbiefilios/Documents/ComfyUI/input`
- output: `/Users/robbiefilios/Documents/ComfyUI/output`
- user library: `/Users/robbiefilios/Documents/ComfyUI/user`

SD 1.5 text-to-image worked locally with `v1-5-pruned-emaonly-fp16.safetensors`.

Wan2.2 5B files were downloaded and made readable:

- `wan2.2_ti2v_5B_fp16.safetensors`
- `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
- `wan2.2_vae.safetensors`

Local Wan2.2 5B text-to-video produced blurry, weak, non-production-usable output for the robot/bunny test. The current working theory is that local Wan2.2 5B pure T2V is not strong enough for prompt-adherent final shots.

Wan2.2 14B FP8 high/low-noise models failed on Apple MPS because `Float8_e4m3fn` is unsupported. Use FP16/BF16-compatible models on Apple MPS.

## Higgsfield Findings

Higgsfield CLI is installed and authenticated. It produced a strong robot/bunny benchmark with `wan2_7`, 5 seconds, 720p, 16:9.

The successful benchmark URL was:

`https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260517_200503_27504c7a-cf03-483c-b2ac-9d57c69a2cf5.mp4`

Higgsfield is useful for:

- quality benchmarking
- motion exploration
- reference renders
- temp baked shots
- cloud model comparisons

Higgsfield should not automatically be treated as the final production path when a shot requires clean alpha, layer separation, and exact revision control.

## Recommended Pipeline Direction

Use ComfyUI as a controllable VFX element lab and Higgsfield as a high-quality cloud renderer/reference source.

Best current direction:

1. Build plate-aware shot plans.
2. Use CGI/proxy animation, stills, masks, and control passes to guide AI generation.
3. Generate or refine separable fire/water character elements.
4. Generate interaction passes separately.
5. Composite over original plates.
6. Use Higgsfield outputs as reference or temp comps when useful.

Avoid pure text-to-video as the default final-shot workflow.

## Workspace Structure

The repo `/Users/robbiefilios/Documents/FW_AI_Workflow` was turned into a working project brain with:

- `docs/`
- `mcp/`
- `skills/`
- `workflows/`
- `shots/`
- `prompts/`
- `references/`
- `scripts/`
- `outputs/`
- `assets/`
- `memories/`

Project-local skills currently include:

- `comfyui-vfx`
- `higgsfield-vfx`
- `supermemory-vfx`

## Supermemory Setup

Supermemory API key is stored in local `.env` as `SUPERMEMORY_API_KEY`.

Default project/container scope:

- `SUPERMEMORY_CONTAINER_TAG=ai-video-workflows`
- `SUPERMEMORY_PROJECT=ai-video-workflows`

Supermemory MCP was added to `~/.codex/config.toml` through `scripts/supermemory-mcp.sh`. Codex must be restarted for the MCP server/tools to appear.

Before MCP is available, use `scripts/supermemory_add_document.py` to seed Supermemory documents through the API.

## User Preference

The user is willing to learn the best long-term path, even if it requires ComfyUI, LoRAs, ControlNets, MCP, APIs, CLI tooling, and custom workflows. The user wants this directory to become a durable working space for skills, workflows, templates, docs, and knowledge that can help future agents.

## Next Useful Work

- Verify `FW_test` video metadata and alpha channels after installing `ffmpeg`.
- Build shot-level notes for the fire-in-grass example.
- Research alpha/RGBA video workflows, especially Wan Alpha-style workflows.
- Research LoRA/reference conditioning strategy for consistent fire and water characters.
- Use Supermemory MCP after Codex restart to recall/save project facts during future sessions.
