---
name: comfy-cloud-vfx
description: "Use when running or preparing Comfy Cloud jobs for this AI short-film VFX workspace, including hosted partner-node generations through comfy-cli, direct Comfy Cloud API workflow execution, cloud queue/status/history checks, and deciding between local ComfyUI MCP, Comfy Cloud API, and Comfy Cloud MCP."
---

**Created:** 2026-05-27
**Modified:** 2026-10-08
**Version:** 1.3

# Comfy Cloud VFX

## Core Rule

Use Comfy Cloud as the remote execution path when local Apple MPS is too slow, missing model support, or when hosted partner nodes are the right tool. Keep durable workflows, prompts, and findings in the repo; never store API keys in docs, skills, prompts, or committed files.

## Current Setup

- Project root: `/Users/jamesfilios/Software_Projects/FW_AI`
- Local secret: `.env` contains `COMFY_API_KEY`.
- MCP notes: `mcp/comfy-cloud.md`
- CLI wrapper: `scripts/comfy-cloud-cli.sh`
- Direct API helper: `scripts/comfy-cloud-api.py`
- Optional official CLI venv: `.venv-comfy-cli/` (not installed in this checkout as of 2026-10-08).
- Comfy Cloud MCP launcher: `scripts/comfy-cloud-mcp.sh`

As of 2026-05-27, the regular Comfy Cloud API works for this account, but Comfy Cloud MCP returns 403 because MCP is not yet enabled for the account.

## Which Tool To Use

Use local ComfyUI MCP only if a local server and MCP connection are actually configured. The current heavy-workflow path is RunPod; see `mcp/runpod.md`.

Use `scripts/comfy-cloud-cli.sh` for hosted partner-node one-shots only after installing the CLI. It is absent on this machine; the direct API helper below is available for API-format workflows.

Use `scripts/comfy-cloud-api.py` or direct HTTPS calls to `https://cloud.comfy.org/api/...` for full ComfyUI API-format workflow JSON execution, account checks, queue/status/history, and output download plumbing.

Use Comfy Cloud MCP only after Comfy enables MCP for the account. Until then, expect `/mcp` to fail with a 403 rollout message.

## Commands

Read-only account checks:

```bash
scripts/comfy-cloud-api.py user
scripts/comfy-cloud-api.py system-stats
```

Partner-node discovery (requires the optional CLI venv; see `mcp/comfy-cloud.md`):

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
scripts/comfy-cloud-api.py submit workflows/comfyui/your_api_workflow.json
```

## Workflow Discipline

- Save API-format workflow JSON under `workflows/comfyui/` with shot-first names.
- Save run notes, prompt changes, job IDs, and review notes in the relevant `shots/` file.
- Download generated assets into `outputs/` or a shot-specific output folder; do not commit generated media.
- For VFX shots, prefer outputs that are compositing-friendly: clean silhouette, separable RGB/alpha or matte, glow, shadow, contact light, smoke, steam, scorch, splash, and reference passes.
- If a Cloud API or CLI finding took time to discover, update `mcp/comfy-cloud.md` or `docs/findings.md`.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-27 | Initial Comfy Cloud VFX. |
| 1.1     | 2026-08-16 | Replaced stale `/Users/robbiefilios/Documents/FW_AI_Workflow` paths with repo-relative paths and the current workspace root. |
| 1.2     | 2026-08-16 | Removed Supermemory references after its retirement; project memory now lives in the repository. |
| 1.3     | 2026-10-08 | Marked the CLI virtual environment absent on this host, made MCP use conditional, and clarified placeholder workflow paths. |
