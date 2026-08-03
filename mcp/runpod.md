# RunPod + ComfyUI

Date reconstructed: 2026-08-02

## What Was Found

The repository had no previous RunPod-specific notes, scripts, Pod IDs, templates,
or credentials. The existing reusable starting point is the API-format workflow:

`workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.json`

It expects:

- `wan2.2_ti2v_5B_fp16.safetensors`
- `wan2.2_vae.safetensors`
- `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
- `jerry_JB-001_upright-compact-idle.png`
- `shot004_ren-small-fire6_control_832x448_81f_v001.mp4`

The Jerry reference is tracked in the repository. The control video and large
models are not tracked and must be restored or downloaded separately.

## Installed Local Integration

- Official RunPod Codex plugin: `runpod@runpod`
- Official RunPod documentation MCP: `https://docs.runpod.io/mcp`
- RunPod CLI: `runpodctl`
- Flash CLI: `flash` (primarily for browser login and future Serverless work)
- Authenticated RunPod MCP launcher: `scripts/runpod-mcp.sh`
- Auth wrapper for terminal commands: `scripts/runpod-with-auth.sh`
- Remote ComfyUI API helper: `scripts/runpod-comfy-api.sh`

Restart Codex after MCP or plugin configuration changes so the new tools load.

## Authentication

Recommended human setup:

```bash
flash login
scripts/runpod-with-auth.sh runpodctl user
```

`flash login` stores the key in `~/.runpod/config.toml`. The project wrappers
read it at runtime, so the key does not need to be copied into Git, Codex config,
or shell history. Alternatively, set `RUNPOD_API_KEY` in the ignored `.env` file.

Never commit `.env`, `~/.runpod/config.toml`, or an API key.

## Recommended ComfyUI Shape

Use an interactive GPU Pod while developing workflows. Use RunPod's official
prebuilt ComfyUI template, a 24 GB NVIDIA RTX A5000 for the initial Wan 2.2 5B
workflow, and a network volume mounted at `/workspace` so models, custom nodes,
workflows, and outputs survive Pod replacement. If the A5000 proves too slow or
tight for a specific graph, terminate it and attach the same network volume to a
faster GPU in the same data center rather than rebuilding the environment.

Expose only these ports by default:

- `8188/http`: ComfyUI
- `22/tcp`: SSH

The official template also supports FileBrowser on `8080` and JupyterLab on
`8888`. Do not expose FileBrowser with the template's documented default
credentials. Enable JupyterLab only when needed and set a strong
`JUPYTER_PASSWORD` outside Git.

Add a short `--terminate-after` cost guard to every development Pod. The ComfyUI
proxy URL is public to anyone who has it, so do not share it. Use Secure Cloud
for unreleased plates and project assets.

Discover the current official template and GPU availability at deployment time:

```bash
scripts/runpod-with-auth.sh runpodctl template search comfyui
scripts/runpod-with-auth.sh runpodctl gpu list
scripts/runpod-with-auth.sh runpodctl datacenter list
```

Official setup reference:
https://docs.runpod.io/tutorials/pods/comfyui

## Connect Codex To RunPod

The RunPod MCP manages infrastructure such as Pods, GPUs, storage, templates,
billing, and lifecycle. The ComfyUI HTTP API manages workflows running inside a
Pod; these are two separate control surfaces.

Install the authenticated local MCP entry:

```bash
python3 scripts/update-codex-runpod-mcp.py
```

Restart Codex, then verify the RunPod MCP by listing Pods. For direct ComfyUI
workflow access, add the Pod ID to the ignored `.env` file:

```bash
RUNPOD_POD_ID=your_pod_id
RUNPOD_COMFYUI_PORT=8188
```

Then:

```bash
scripts/runpod-comfy-api.sh status
scripts/runpod-comfy-api.sh upload assets/characters/jerry/character-bible-v001/references/primary-body/JB-001_upright-compact-idle.png
scripts/runpod-comfy-api.sh submit workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.json
```

Do not submit the Shot 004 workflow until its three model files, Jerry input, and
control-video input are present and `/object_info` confirms every node type.

## Session Checklist

1. Authenticate and verify `runpodctl user`.
2. Confirm an SSH key is registered before Pod creation.
3. Create or select a persistent network volume and compatible data center.
4. Create the official ComfyUI Pod with ports and a termination guard.
5. Poll `/system_stats` through the external proxy until it answers.
6. Verify workflow node types through `/object_info`.
7. Install/download the required models into the appropriate ComfyUI model folders.
8. Upload the Jerry reference and restored control video.
9. Submit the workflow and poll its history.
10. Download outputs, record the run, and terminate the Pod when finished.

## Current Resume Point

On 2026-08-03, authentication and storage were verified again. Current state:

- No Pod is currently running, so current compute spend is zero.
- Persistent network volume `fw-ai-comfyui` (`ccv3wj09mn`) now exists in
  `US-IL-1`: 100 GB mounted at `/workspace`, approximately $7/month.
- A dedicated local RunPod Ed25519 key is registered with the account.
- The official Codex plugin and both RunPod MCP entries are installed; restart
  Codex after provisioning so the tools appear in a new session.
- Official `ComfyUI - CUDA 12.8` template: `cw3nka7d08`.
- Template image: `runpod/comfyui:cuda12.8`.
- Persistent ComfyUI path: `/workspace/runpod-slim/ComfyUI`.
- Recommended starter GPU: Secure Cloud `NVIDIA RTX A5000`, 24 GB VRAM, at
  $0.27/hour when checked. The current Shot 004 Wan 2.2 5B workflow fits this
  class of GPU.
- The Illinois A5000 pool was marked low stock, but two launch attempts were
  rejected with `SUPPLY_CONSTRAINT`. No Pod was created and no compute charge
  resulted from those attempts.
- An earlier two-minute allocation used to inspect host RAM was stopped and
  deleted. Its persistent network volume was not deleted.

Resume by refreshing inventory and launching only when the Illinois A5000 is
actually schedulable:

```bash
scripts/runpod-with-auth.sh runpodctl gpu list
date -u -v+2H +%Y-%m-%dT%H:%M:%SZ
scripts/runpod-with-auth.sh runpodctl pod create \
  --name fw-ai-comfyui-dev \
  --template-id cw3nka7d08 \
  --gpu-id "NVIDIA RTX A5000" \
  --cloud-type SECURE \
  --data-center-ids US-IL-1 \
  --network-volume-id ccv3wj09mn \
  --volume-mount-path /workspace \
  --container-disk-in-gb 50 \
  --ports "8188/http,22/tcp" \
  --terminate-after REPLACE_WITH_TIMESTAMP
```

After creation, save the returned Pod ID in the ignored `.env`, poll
`scripts/runpod-comfy-api.sh status`, verify SSH and `nvidia-smi`, and confirm
that `/workspace/runpod-slim/ComfyUI` lives on the network volume.
