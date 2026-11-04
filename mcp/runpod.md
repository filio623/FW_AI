**Created:** 2026-08-02
**Updated:** 2026-11-04

# RunPod + ComfyUI

RunPod hosts the GPU Pod that runs ComfyUI for Shot 004 Pass A/B generation work (Mickmumpitz 1.3 VACE, Wan 2.1/2.2, SkyReels, NAG). Full session-by-session history, custom-node install notes, VACE model checksums, and the 2026-10-08 OOM recovery are in `mcp/runpod_log.md`.

## Account And Region

- Network volumes require at least $5 account credit before creation.
- Network-volume support varies by data center; confirm with `runpodctl datacenter list` before provisioning — a volume is pinned to its data center.
- `EU-RO-1` (Romania) is the current region: it has the most GPU types of any data center (16, including RTX A6000 48 GB at $0.59/hr, L4, RTX 4090/5090, A100, RTX PRO 6000) and supports RunPod's S3-compatible volume API, so files move without a Pod.
- Old volume `avw5iclb48` (`fw-ai-comfyui-vace`, `CA-MTL-1`): unused; `CA-MTL-1` went down 2026-10-31 and has stayed down since.

## Authentication

```bash
flash login
scripts/runpod-with-auth.sh runpodctl user
```

`flash login` stores the key in `~/.runpod/config.toml`; project wrappers (`scripts/runpod-with-auth.sh`, `scripts/runpod-comfy-api.sh`, `scripts/runpod-mcp.sh`) read it at runtime, so it never needs to go into Git, Codex config, or shell history. Alternatively set `RUNPOD_API_KEY` in the ignored `.env` file. Never commit `.env`, `~/.runpod/config.toml`, or an API key.

## Current Setup

Volume `dqlwnz6nq8` (`fw-ai-comfyui-eu-ro`, 100 GB) in `EU-RO-1`, mounted at `/workspace`, built 2026-11-02 by `scripts/runpod/setup_mick13_volume.sh` after the `CA-MTL-1` outage. Official RunPod ComfyUI template image `runpod/comfyui:1.3.3-comfyuiv0.30.0-cuda12.8` bakes ComfyUI 0.30.0 (upstream is 0.43.0 as of 2026-10-27). On every boot `start.sh` compares the volume's bundle manifest with the image's and, when they differ, rsyncs the image's ComfyUI core over the volume's, keeping `models`, `input`, `output`, `user`, `custom_nodes`, and the venv — so a hand-updated ComfyUI survives restarts until the next new template image overwrites it. ComfyUI lives at `/workspace/runpod-slim/ComfyUI` (venv `.venv-cu128`, Python 3.12, torch 2.10.0+cu128).

Installed by the template: ComfyUI-Manager, ComfyUI-KJNodes `78cd992`, Civicomfy, ComfyUI-RunpodDirect. Installed by `setup_mick13_volume.sh` (`bash setup_mick13_volume.sh patch` reapplies only the two patches below):

- Nodes at pinned commits: VideoHelperSuite (latest), Mickmumpitz-Nodes `270afbd`, WanVaceAdvanced `049213c`, RES4LYF `56e4475`, rgthree `d7297b4`, GGUF `6ea2651`, plus PyWavelets, gguf, protobuf.
- Two patches: the Mickmumpitz `ControlCrossfadeIterationFix` `start_frames=None` fix (`nodes/control_crossfade.py`, still needed — the upstream bug is unfixed at `270afbd`), and a `WanVideoNAG` fix in `nodes/model_optimization_nodes.py`, marked `FW_AI patch 2026-11-02`: `patch()` now runs each text-embedding layer through `forward_comfy_cast_weights`, ComfyUI's own casting path, in the model's `manual_cast_dtype` (FP16 here). This replaced the 2026-10-19 NAG patch, which crashed on ComfyUI 0.30.0; the new one is verified (benchmark run 9, 684 s on an L4).
- Models: VACE × SkyReels V3 R2V FP8 merge (checksum verified), UMT5 FP8 encoder (size verified), Kijai's BF16 Wan VAE as `wan_2.1_vae.safetensors`, FusionX and Lenovo LoRAs (checksums verified). Checksums and sources are in the log.
- Inputs in `input/`: the grow16 guide and mask, `JB-001`, `JB-010`. Current Pass A graph: `user/default/workflows/shot004_fire-jump_mick13-skyreels_v001.json` (saved in the run 8 state — see the log for what run 8 is).
- `/workspace/restart_comfyui.sh`: the only way to relaunch ComfyUI after a node install — `start.sh` does not relaunch it and ComfyUI-Manager's `/manager/reboot` returns 404. It sources `/etc/rp_environment`, activates `.venv-cu128`, and runs `main.py` with the template's arguments; launch with `setsid nohup … > /workspace/comfyui_restart.log`. Stop the old process by PID, not `pkill -f "main.py …"` over SSH — that pattern also matches the SSH shell's own command line and kills it.

Expose only `8188/http` (ComfyUI) and `22/tcp` (SSH) by default; do not share the proxy URL (see Cloudflare note below).

## Starting And Stopping

```bash
scripts/runpod-pod-up.sh      # create, wait for ComfyUI, record RUNPOD_POD_ID in .env
scripts/runpod-pod-down.sh    # terminate and clear the id; the volume is untouched
```

Defaults (as of 2026-11-02): RTX A6000 in `EU-RO-1`, volume `dqlwnz6nq8`, two-hour termination guard. Override with `GPU="NVIDIA RTX A6000" DC=US-TX-1 VOLUME= scripts/runpod-pod-up.sh` or `HOURS=4 scripts/runpod-pod-up.sh` when the default GPU is out of stock; explicit `VOLUME=` disables the default mount for an intentionally disposable Pod — do not use it when resuming shot004. Everything valuable lives on the volume, so terminating loses nothing and is the normal way to stop working.

**The `--terminate-after` guard is not reliable.** Pod `amsu1bpsrdzgfr` was created with `--terminate-after 2026-10-19T17:42:03Z` and was still `RUNNING` at 18:14Z, with `runpodctl pod get` showing no stored termination time; the guard has never been seen to fire. Always run `scripts/runpod-pod-down.sh` by hand at the end of a session. Do not use `runpodctl pod stop` either — the container disk holds about 16 MB, so a stopped Pod preserves nothing worth paying for.

Sample results only match within the same GPU type (seed-for-seed): compare a new GPU's output against a baseline rerun on that same GPU, never across GPU types.

## The Proxy Is Behind Cloudflare

`https://<POD_ID>-8188.proxy.runpod.net` rejects default `curl`/Python user agents with `error code: 1010` — browser-signature filtering, not authentication, so an API key does not help; browsers work normally. `scripts/runpod-comfy-api.sh` sends a browser user agent for this reason; any new tooling that talks to the proxy must do the same. Treat this as bot filtering, not access control — a browser with the URL still reaches ComfyUI, so the URL stays sensitive and should not be shared. `scripts/runpod-comfy-api.sh submit` also sends `COMFY_API_KEY` from `.env` as `extra_data.api_key_comfy_org`, which comfy.org partner nodes (Kling, Wan 2.7, Runway) need on the Pod; without it they fail with `Please login first`.

## Codex MCP Connection

Codex runs the RunPod MCP through `scripts/runpod-mcp.sh` (entry `mcp_servers.runpod` in `~/.codex/config.toml`). Restart Codex after any MCP or plugin config change, then verify by listing Pods. For direct ComfyUI workflow access — a separate control surface from Pod/infrastructure control — set `RUNPOD_POD_ID` and `RUNPOD_COMFYUI_PORT=8188` in `.env` and use `scripts/runpod-comfy-api.sh status|upload|submit`.

## State (as of 2026-11-04)

No Pod is running; balance $15.06, volume-only cost about $0.019/hr. Pod `bd2rmuu6fy08ks` (RTX 4090) was terminated by hand about 00:50 UTC after the Seedance S4 and Kling K1 Pass B tests. Pass B moved to first-last-frame video through ComfyUI API nodes (Seedance 2.0, Kling), which bill the Comfy account and do not need the GPU — the graph is `shot004/pass-b_grassfire/shot004_fire-jump_grassfire-flf_seedance20_v001.json` (Seedance and Kling branches), and the repo copy matches. The inpaint graph still holds James's first Seedance nodes (3614, 3615); remove them before the next inpaint run or each run also queues a paid Seedance call. Next: comp Kling K1 like S3 (`shots/shot004_fire-jump/scripts/build_shot004_grassfire_layer.py`, `shots/shot004_fire-jump/scripts/blender/shot004_comp_add_passb.py`), choose the generator, make the final at full resolution — steps in `shots/shot004_fire-jump/plan.md`. A GPU Pod is only needed again for Jerry (Pass A) or SkyReels inpaint tests; the smaller Jerry guide still awaits James's approval.
