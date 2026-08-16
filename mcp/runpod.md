**Created:** 2026-08-02
**Modified:** 2026-08-16
**Version:** 1.2

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

## Account And Region Constraints

Two constraints learned during the 2026-08-02 setup session. Both cost time to
discover, so check them before planning a Pod.

- **Network volumes require at least $5 in account credit.** A first attempt at
  volume creation was blocked by a $2.14 balance. Top up before provisioning
  storage, not after.
- **Not every data center supports network volumes.** Montreal was ruled out for
  this reason before `US-IL-1` was selected. Confirm volume support for a region
  with `runpodctl datacenter list` before committing to it, because a volume is
  pinned to its data center and moving regions means rebuilding storage.

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

Add a short `--terminate-after` cost guard to every development Pod. Do not share
the ComfyUI proxy URL; see `The Proxy Is Behind Cloudflare` below for what that
filtering does and does not protect. Use Secure Cloud for unreleased plates and
project assets.

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

## Starting And Stopping

Two helper scripts wrap the whole cycle. Everything valuable lives on the network
volume, so terminating a Pod loses nothing and is the normal way to stop working.

```bash
scripts/runpod-pod-up.sh      # create, wait for ComfyUI, record RUNPOD_POD_ID in .env
scripts/runpod-pod-down.sh    # terminate and clear the id; the volume is untouched
```

`runpod-pod-up.sh` accepts overrides for when the default GPU is out of stock:

```bash
HOURS=4 scripts/runpod-pod-up.sh
GPU="NVIDIA RTX A6000" DC=US-TX-1 VOLUME= scripts/runpod-pod-up.sh
```

Do not use `runpodctl pod stop`. The container disk holds about 16 MB — ComfyUI and
every model live on the network volume — so a stopped Pod preserves nothing worth
paying for.

Observed cold start on 2026-08-16: about four minutes from `pod create` to ComfyUI
answering. The "up to 30 minutes" figure in RunPod's tutorial applies to a first-ever
deploy that has to install ComfyUI; the volume already has it.

## The Proxy Is Behind Cloudflare

`https://<POD_ID>-8188.proxy.runpod.net` rejects default `curl` and Python
user-agents with `error code: 1010`. This is browser-signature filtering, not
authentication, so an API key does not help. Browsers work normally.

`scripts/runpod-comfy-api.sh` sends a browser `User-Agent` for this reason. Any new
tooling that talks to the proxy must do the same.

Treat this as bot filtering, not access control. A browser with the URL still
reaches ComfyUI, so the URL is still sensitive and should not be shared.

## Current Resume Point

On 2026-08-16 a working Pod was created and the Shot 004 model set was installed.
Current state:

- **Network volume `fw-ai-comfyui` (`ccv3wj09mn`)**, 100 GB in `US-IL-1`, ~$7.10/month.
  Verified: it persisted across a two-week gap and a GPU change.
- **ComfyUI 0.30.0** installed at `/workspace/runpod-slim/ComfyUI` on the volume.
  Note this is the real path; RunPod's tutorial says `/workspace/madapps/...`, which
  is wrong for this template.
- **Shot 004 models installed on the volume (18 GB total):**
  - `models/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors` (9.4 GB)
  - `models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors` (6.3 GB)
  - `models/vae/wan2.2_vae.safetensors` (1.4 GB)
- **All 13 node types** required by `shot004_jerry-wan22-funcontrol-element_v001.json`
  resolve through `/object_info`, including `Wan22FunControlToVideo`.
- **GPU substitution:** the RTX A5000 has been out of stock in `US-IL-1` since at
  least 2026-08-03. The RTX 4090 (24 GB, $0.74/hr) was used instead and works.
- **Still blocking a real Shot 004 run:** the control video
  `shot004_ren-small-fire6_control_832x448_81f_v001.mp4` and its source
  `FW_test/Scene 4/ren_small_fire6..mov` are not in this checkout. Restore from the
  external drive via `references/manifests/external-drive_inventory_v001.md`.

### Upgrade Path

24 GB fits Wan 2.2 TI2V 5B and Fun Control 14B fp8, but not VACE-14B (~32 GB).
Bigger VRAM is not more expensive per hour — A40 48 GB is $0.44 and RTX A6000 48 GB
is $0.53, both below the 4090's $0.74. The cost is that neither is offered in
`US-IL-1`, so a 48 GB card means a new volume in another region and re-downloading
the models. A40 stock is best in `EU-SE-1`; A6000 in `US-KS-2` and `US-TX-1`.

### Historical Note

The state below was recorded on 2026-08-03 and is kept for context.

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

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-08-02 | Initial RunPod + ComfyUI. |
| 1.1     | 2026-08-16 | Recorded the $5 credit minimum for network volumes and the data-center volume-support constraint, merged from Supermemory before its retirement. |
| 1.2     | 2026-08-16 | Recorded the first working Pod and installed Shot 004 model set, the up/down helper scripts, the Cloudflare proxy user-agent requirement, the RTX 4090 substitution for the unavailable A5000, and the VRAM upgrade path. |
