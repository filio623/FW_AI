---
name: comfy-cloud-vfx
description: "Use when running or preparing Comfy Cloud jobs for this AI short-film VFX workspace, including hosted partner-node generations through comfy-cli, direct Comfy Cloud API workflow execution, cloud queue/status/history checks, and deciding between local ComfyUI MCP, Comfy Cloud API, and Comfy Cloud MCP."
---

# Comfy Cloud VFX

## Core Rule

Use Comfy Cloud as the remote execution path when local Apple MPS is too slow, missing model support, or when hosted partner nodes are the right tool. Keep durable workflows, prompts, and findings in the repo; never store API keys in docs, skills, prompts, or committed files.

## Current Setup

- Project root: `/Users/robbiefilios/Documents/FW_AI_Workflow`
- Local secret: `.env` contains `COMFY_API_KEY`.
- MCP notes: `mcp/comfy-cloud.md`
- CLI wrapper: `scripts/comfy-cloud-cli.sh`
- Direct API helper: `scripts/comfy-cloud-api.py`
- Official CLI venv: `.venv-comfy-cli/`
- Comfy Cloud MCP launcher: `scripts/comfy-cloud-mcp.sh`

As of 2026-05-27, the regular Comfy Cloud API works for this account, but Comfy Cloud MCP returns 403 because MCP is not yet enabled for the account.

## Which Tool To Use

Use local ComfyUI MCP for local server inspection, local workflow execution, node/model management, and local output retrieval.

Use `scripts/comfy-cloud-cli.sh` for hosted partner-node one-shots and model-specific jobs such as Flux, Seedance, Kling, Luma, Nano Banana, Ideogram, Runway, Recraft, Stability, and similar `comfy generate` tasks.

Use `scripts/comfy-cloud-api.py` or direct HTTPS calls to `https://cloud.comfy.org/api/...` for full ComfyUI API-format workflow JSON execution, account checks, queue/status/history, and output download plumbing.

Use Comfy Cloud MCP only after Comfy enables MCP for the account. Until then, expect `/mcp` to fail with a 403 rollout message.

## Commands

Read-only account checks:

```bash
scripts/comfy-cloud-api.py user
scripts/comfy-cloud-api.py system-stats
```

Partner-node discovery:

```bash
scripts/comfy-cloud-cli.sh generate list
scripts/comfy-cloud-cli.sh generate schema flux-pro
```

Partner-node generation:

```bash
scripts/comfy-cloud-cli.sh generate flux-pro \
  --prompt "cinematic fire spirit, clean alpha-friendly silhouette" \
  --width 1024 \
  --height 1024 \
  --download outputs/test.png
```

Workflow submission:

```bash
scripts/comfy-cloud-api.py submit workflows/comfyui/example_api_workflow.json
```

## Workflow Discipline

- Save API-format workflow JSON under `workflows/comfyui/` with shot-first names.
- Save run notes, prompt changes, job IDs, and review notes in the relevant `shots/` file.
- Download generated assets into `outputs/` or a shot-specific output folder; do not commit generated media.
- For VFX shots, prefer outputs that are compositing-friendly: clean silhouette, separable RGB/alpha or matte, glow, shadow, contact light, smoke, steam, scorch, splash, and reference passes.
- If a Cloud API or CLI finding took time to discover, update `mcp/comfy-cloud.md`, `docs/findings.md`, or Supermemory.
