**Created:** 2026-08-02
**Modified:** 2026-10-17
**Version:** 2.24

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

The Jerry reference is tracked in the repository. The control video is restored
locally at `assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_control_832x448_81f_v001.mp4`
and still needs to be uploaded to a Pod. Large models stay on the network volume.

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
- **Network-volume support varies by data center and date.** The 2026-08-02
  setup could not use Montreal, but `CA-MTL-1` supported the replacement volume
  created on 2026-10-07. Confirm support with `runpodctl datacenter list`
  before provisioning; a volume is pinned to its data center.

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

As of 2026-10-08 the up-script defaults are A40 in `CA-MTL-1` with network
volume `avw5iclb48` and a two-hour termination guard. Check GPU availability
and the current volume before launch; never create a replacement Pod without
attaching the persistent volume that holds ComfyUI and the saved VACE latent.

`runpod-pod-up.sh` accepts overrides for when the default GPU is out of stock:

```bash
HOURS=4 scripts/runpod-pod-up.sh
GPU="NVIDIA RTX A6000" DC=US-TX-1 VOLUME= scripts/runpod-pod-up.sh
```

Explicit `VOLUME=` disables the default mount for an intentionally disposable
Pod; do not use that override when resuming shot004.

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

`scripts/runpod-comfy-api.sh submit` also sends `COMFY_API_KEY` from `.env` as
`extra_data.api_key_comfy_org`, which comfy.org partner nodes (Kling, Wan 2.7,
Runway) need on the Pod. Without it they fail with `Please login first`.

## Current Resume Point

No Pod is running. `ep5rr963ctx22t` was terminated 2026-10-17 and `RUNPOD_POD_ID` is cleared in `.env`. Compute spend is zero. Network volume `avw5iclb48` (`fw-ai-comfyui-vace`, 100 GB, `CA-MTL-1`) is untouched.

Still on the volume: VACE latents `shot004_vace_latent_00001_.latent` through `00003_.latent`, Pass A review clips `FW_fire_comp_proxy_00003_.mp4` through `00006_.mp4`, the rejected proxy `FW_fire_comp_proxy_00001_.mp4`, `seedance_test_00001_.mp4`, Kling Omni Edit tests `output/video/ComfyUI_00005_.mp4` (seed 436) and `ComfyUI_00006_.mp4` (seed 602), and Wan 2.7 Video Edit runs `output/video/shot004_wan27-videoedit_00001_.mp4` (seed 42) and `00002_.mp4` (seed 2126129005, the Pass A candidate). Local copies of the scored clips, plus extracted graphs, are indexed in `docs/vfx-element-benchmark.md`.

Stock VACE knobs are closed. Wan 2.7 Video Edit seed `2126129005` is the Pass A candidate; it is soft, so sharpness tests (`1080P` same seed, then a cropped-in source) come next. Runway Aleph is on hold. The SkyReels V3 R2V × VACE merge was on the deleted Illinois volume and is not on `avw5iclb48`. A Blender Jerry fire rig exists and is not the shot 004 motion driver; see `docs/pipeline-strategy.md`.

Start the next session at `docs/vfx-element-benchmark.md`. Bring a Pod up with `scripts/runpod-pod-up.sh` when needed. The volume stays attached by that script's default.

### VACE Model Files

- `models/unet/wan2.1_vace_14B_fp16.safetensors`: official Comfy-Org complete
  14B VACE diffusion model, 34,675,323,640 bytes. SHA-256:
  `f202a5c59b8a91ada1862c46a038214f1f7f216c61ec8350d25f69b919da4307`.
- `models/unet/Wan2_1-VACE_module_14B_bf16.safetensors`: Kijai's 6.1 GB
  VACE **module only**, preserved under its original name. It is not a
  substitute for the complete model in a `UNETLoader`.
- `models/vae/wan_2.1_vae.safetensors`: Kijai BF16 Wan 2.1 VAE, loaded by
  `VAELoader`.
- `models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors`: official
  Comfy-Org scaled FP8 UMT5 encoder, 6,735,906,897 bytes.

The first encoder load logged missing CLIP weights and selected `SD1ClipModel`
despite the submitted `CLIPLoader(type=wan)`. ComfyUI cached that bad loader
result; replacing the file alone did not clear the cache, and `CLIPTextEncode`
still failed with `Cannot copy out of meta tensor; no data!`.
A fresh Wan text-encode succeeded, then a Pod restart cleared the stale cache.
After restart, a minimal `CLIPLoader(type=wan, device=default)` →
`CLIPTextEncode` run and a separate
`UNETLoader(weight_dtype=fp8_e4m3fn)` run both completed successfully.
The full 1280×672, 49-frame VACE video graph has **not** been rendered or
verified end to end; do not equate these loader checks with a finished shot.

### 2026-10-08 VACE Decode OOM

The first 1280×672, 49-frame, 26-step VACE attempt finished sampling,
then the Pod's 50 GB RAM cgroup recorded an OOM kill at `VAEDecode`. The
ComfyUI process exited without a saved video; the Pod stayed running but its
HTTP proxy returned 502. Restarting the Pod restored ComfyUI.

`/Users/jamesfilios/Downloads/FW_Test_Workflow_Vace_Ready.json` now uses
`VAEDecodeTiled` with `tile_size=512`, `overlap=64`,
`temporal_size=16`, and `temporal_overlap=4`. A separate 49-frame
1280×672 synthetic-latent decode completed, produced 49 preview frames,
and used 2.39 GB peak container RAM without an OOM. This validates the
decode path only, not the entire graph with the sampler, cached models,
and control inputs in memory. Reload this updated JSON into the canvas
before retrying; an already-open browser workflow retains the old node.

### 2026-10-08 Two-Stage VACE Recovery

A second 26-step run also completed sampling and then OOM-killed ComfyUI
at the 50 GB container limit. Both sampler results were lost. The older
server-saved all-in-one workflows still contain untiled `VAEDecode`, although
the submitted retry graph is unavailable after the crash. Do not queue
either old all-in-one graph. Even a finishing-only synthetic-latent run
with the staged 4096x2160, 84-frame Scene 4 reference and 4K composite
OOM-killed this Pod. Tiled VAE decode alone does not make the old chain safe.

Use these separate, importable canvas workflows instead:

1. `workflows/comfyui/shot004_fire-vace14b_sample-latent_v001.json` ends at
   `SaveLatent` after `TrimVideoLatent`, with no VAE decode. Queue it once and
   confirm `ComfyUI/output/shot004_vace_latent_*.latent` exists before moving on.
2. `workflows/comfyui/shot004_fire-vace14b_decode-latent_v001.json` reads
   the saved output via `LoadLatent`'s `[output]` path annotation. Its default
   is `shot004_vace_latent_00001_.latent [output]`; select/edit the actual
   generated filename if the counter differs. It uses tiled Wan VAE decode
   (512/64 spatial, 16/4 temporal), 1280x672 scales and mask, and the
   49-frame proxy staged in `ComfyUI/input/`:
   `shot004_fw-test-scene_plate-proxy_1280x672_49f_v001.mp4`. The durable
   local source is under `assets/elements/by-shot/shot004_fire-jump/plates/`.
   Output prefix is `FW_fire_comp_proxy`; this is not a 4K delivery.

Both JSON files are also saved on the persistent volume at
`ComfyUI/user/default/workflows/FW/` for selection in the ComfyUI workflow
browser. Import one at a time; an already-open old graph is not replaced.

A synthetic latent was saved and loaded directly from `[output]`. Running the
complete finishing canvas against it created a 49-frame 1280x672, 24 fps MP4
with 7,819,919,360 bytes peak container RAM and zero OOM events. This verifies
the finishing workflow on test data; it did not prove a full VACE result.
Do final-resolution assembly/upscaling in a streaming compositor rather than
reloading the 4K plate and 84 frames into this 50 GB ComfyUI container.

The user then completed the real 26-step sampler and saved
`ComfyUI/output/shot004_vace_latent_00001_.latent`. Decoding and compositing
that latent through the proxy workflow produced
`ComfyUI/output/FW_fire_comp_proxy_00001_.mp4` (49 frames, 1280x672,
24 fps) without OOM. The preview shows orange fire/glow but visible
green/magenta artifacts; see the shot004 workflow test plan for the run log.
Keep the saved latent for non-destructive finishing experiments.

Use a GPU in `CA-MTL-1` to attach this network volume. Refresh Pod status and
GPU prices before launch; historical `US-IL-1` volume IDs below were retired.

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

The launch command below is historical: volume `ccv3wj09mn` was deleted.
Do not reuse it. For the current volume and Pod, see `Current Resume Point`.

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
| 1.3     | 2026-08-18 | Recorded the restored local shot004 control video; a Pod run still needs that file uploaded. |
| 1.4     | 2026-08-30 | Recorded the official Fun Control 14B models, LoRAs, wan_2.1 VAE, and sample inputs on the volume; the 2026-08-29 RTX 6000 Ada substitution when the Illinois 4090 was out of stock; ~48 GB used of 100 GB; and that the tutorial graph has not been queued. |
| 1.5     | 2026-09-07 | Fun Control learning closed; listed Jerry still and fire path-control inputs on the volume; next chapter VACE / Mickmumpitz. |
| 1.6     | 2026-09-07 | Pod `ijzpkfsy5sqmt6` up: Illinois RTX 4090, official template, volume `ccv3wj09mn`; Mickmumpitz merge download started. |
| 1.7     | 2026-09-08 | Terminated `ijzpkfsy5sqmt6`; relaunched `v3chqyqw2kowkx` on Illinois 4090 with the same volume (~78 GB used). |
| 1.8     | 2026-09-08 | Pod `1a2lj3lfp7wnju` up; Superhero and Office Flood example inputs uploaded to `input/mick/`. |
| 1.9     | 2026-09-08 | Terminated `1a2lj3lfp7wnju`; volume keeps merge, nodes, and `input/mick/` examples. |
| 2.0     | 2026-10-07 | Deleted old IL volume; created new CA-MTL-1 volume (avw5iclb48) for VACE 14B workflow. |
| 2.1     | 2026-10-08 | Corrected the current VACE Pod/model inventory, documented the stale encoder cache and verified loader-only recovery, and flagged the retired Illinois launch command. |
| 2.2     | 2026-10-08 | Diagnosed the 50 GB RAM OOM at post-sampling VAE decode, recorded the tiled workflow correction and the separate full-size decode smoke result. |
| 2.3     | 2026-10-08 | Recorded the second OOM and 4K composite OOM, introduced split latent/sample workflows and a 49-frame proxy finishing path verified below 8 GB container RAM. |
| 2.4     | 2026-10-08 | Recorded successful real VACE latent save and separate proxy composite; flagged visible color artifacts and preserved the latent for finishing iterations. |
| 2.5     | 2026-10-08 | Recorded safe A40 Pod termination, preserved CA-MTL-1 network volume and VACE artifacts, and the guided workflow-review resume point. |
| 2.6     | 2026-10-08 | Aligned Pod-up defaults and launch guidance with the surviving CA-MTL-1 VACE volume, preventing an unattached replacement Pod. |
| 2.7     | 2026-10-09 | Recorded resumed A40 Pod `03vbr9yofvf2z4` on the CA-MTL-1 VACE volume and the decode-only finding that the color artifacts are in the saved latent. |
| 2.8     | 2026-10-09 | Terminated A40 Pod `03vbr9yofvf2z4` and cleared the Pod ID. The CA-MTL-1 VACE volume remains. |
| 2.9     | 2026-10-09 | Replaced the stale running-Pod terminate instruction after `03vbr9yofvf2z4` was already shut down. |
| 2.10    | 2026-10-10 | Recorded resumed A40 Pod `l6ifya67dcq486` on the CA-MTL-1 VACE volume and the Seedance test file that survived the previous termination. |
| 2.11    | 2026-10-10 | Terminated A40 Pod `l6ifya67dcq486`. Recorded the second VACE latent and the agreed Pass A resume point. |
| 2.12    | 2026-10-11 | Recorded resumed A40 Pod `2q273z4gzxff6n` on the CA-MTL-1 VACE volume. |
| 2.13    | 2026-10-11 | Terminated A40 Pod `2q273z4gzxff6n`. Recorded Pass A latent `00003` and the strength-0.5 resume point. |
| 2.14    | 2026-10-13 | Recorded resumed A40 Pod `qgdedf20w84gnp` on the CA-MTL-1 VACE volume. |
| 2.15    | 2026-10-13 | Terminated A40 Pod `qgdedf20w84gnp` after verifying `KlingMotionControl` human-upper-body rejection. |
| 2.16    | 2026-10-13 | Terminated A40 Pod `7imyoqxk5n7w7o` after the Kling Omni Edit tests. |
| 2.17    | 2026-10-17 | Recorded resumed A40 Pod `c0u0flqd84rlen` after CA-MTL-1 A40 stock returned. |
| 2.18    | 2026-10-17 | Corrected the resume point: strength 0.5 and silhouette runs are scored, and the next test is not another local VACE knob. |
| 2.19    | 2026-10-17 | Terminated A40 Pod `c0u0flqd84rlen` and cleared the Pod ID. Next session starts at the benchmark; Wan 2.7 does not need the GPU. |
| 2.20    | 2026-10-17 | Pod `qblvqx3v4pjho8` up; Wan 2.7 Video Edit scored on it; `submit` now passes the comfy.org key; recorded that the SkyReels merge is not on the current volume. |
| 2.21    | 2026-10-17 | Terminated A40 Pod `qblvqx3v4pjho8` and cleared the Pod ID. |
| 2.22    | 2026-10-17 | Pod `ep5rr963ctx22t` up for a hands-on Wan 2.7 Video Edit session. |
| 2.23    | 2026-10-17 | Recorded Wan 2.7 run 2 on the volume and moved the resume point to sharpness tests on the candidate. |
| 2.24    | 2026-10-17 | Terminated A40 Pod `ep5rr963ctx22t` and cleared the Pod ID. |
