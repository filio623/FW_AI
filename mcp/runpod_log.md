**Created:** 2026-11-04
**Updated:** 2026-11-04

# RunPod + ComfyUI Log

Append-only. Full history behind `mcp/runpod.md`'s current state: Pod sessions, outages, custom-node installs, VACE model checksums, and the 2026-10-08 OOM recovery. Newest entries at the bottom; never edit an old entry.

## 2026-08-02 — Repository reconstructed; first account constraints

Date reconstructed: 2026-08-02. The repository had no previous RunPod-specific notes, scripts, Pod IDs, templates, or credentials. The existing reusable starting point was the API-format workflow `workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.json`, expecting `wan2.2_ti2v_5B_fp16.safetensors`, `wan2.2_vae.safetensors`, `umt5_xxl_fp8_e4m3fn_scaled.safetensors`, `jerry_JB-001_upright-compact-idle.png`, and `shot004_ren-small-fire6_control_832x448_81f_v001.mp4`. The Jerry reference was tracked in the repository; the control video needed restoring locally and uploading to a Pod. Large models were to stay on the network volume.

Two account constraints surfaced this session: a first attempt at network-volume creation was blocked by a $2.14 balance (volumes need at least $5 credit), and the setup could not use the Montreal data center at that time (Montreal later supported the replacement volume created 2026-10-07).

## 2026-08-03 — Historical Pod/volume state (superseded)

No Pod was running; compute spend was zero. Persistent network volume `fw-ai-comfyui` (`ccv3wj09mn`) existed in `US-IL-1`: 100 GB mounted at `/workspace`, about $7/month. A dedicated local RunPod Ed25519 key was registered with the account. The official Codex plugin and both RunPod MCP entries were installed. Official template `ComfyUI - CUDA 12.8`: `cw3nka7d08`, image `runpod/comfyui:cuda12.8`, persistent ComfyUI path `/workspace/runpod-slim/ComfyUI`. Recommended starter GPU: Secure Cloud `NVIDIA RTX A5000`, 24 GB VRAM, at $0.27/hour when checked — the Shot 004 Wan 2.2 5B workflow fit this class. The Illinois A5000 pool was marked low stock; two launch attempts were rejected with `SUPPLY_CONSTRAINT`, no Pod created, no charge. An earlier two-minute allocation used to inspect host RAM was stopped and deleted; its network volume was not deleted.

Launch command used at the time (volume `ccv3wj09mn` was later deleted; do not reuse):

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

## 2026-08-16 — First working Pod; Cloudflare proxy filtering discovered

First working Pod and the installed Shot 004 model set, the up/down helper scripts, and the Cloudflare proxy user-agent requirement were all established this session, along with an RTX 4090 substitution for the unavailable A5000 and a VRAM upgrade path. Cold start observed: about four minutes from `pod create` to ComfyUI answering — RunPod's "up to 30 minutes" tutorial figure applies to a first-ever deploy that installs ComfyUI; the volume already had it.

## 2026-08-18 — Control video restored locally

The Shot 004 control video was restored locally; a Pod run still needed that file uploaded.

## 2026-08-29–30 — Fun Control 14B models installed

Official Fun Control 14B models, LoRAs, the `wan_2.1` VAE, and sample inputs were installed on the volume; about 48 GB used of 100 GB. On 2026-08-29 an RTX 6000 Ada was substituted when the Illinois 4090 was out of stock. The tutorial graph had not yet been queued.

## 2026-09-07 — Fun Control closed; Pod `ijzpkfsy5sqmt6` up

Fun Control learning closed; Jerry and fire path-control inputs remained on the volume. Next chapter: VACE / Mickmumpitz. Pod `ijzpkfsy5sqmt6` came up on an Illinois RTX 4090, official template, volume `ccv3wj09mn`; the Mickmumpitz merge download started.

## 2026-09-08 — Pod churn: `ijzpkfsy5sqmt6` → `v3chqyqw2kowkx` → `1a2lj3lfp7wnju`

Terminated `ijzpkfsy5sqmt6`; relaunched `v3chqyqw2kowkx` on the same Illinois 4090 and volume (~78 GB used). Pod `1a2lj3lfp7wnju` then came up; Superhero and Office Flood example inputs were uploaded to `input/mick/`. `1a2lj3lfp7wnju` was terminated the same day; the volume kept the merge, nodes, and the `input/mick/` examples.

## 2026-10-07 — New CA-MTL-1 volume `avw5iclb48`

Deleted the old Illinois volume; created new `CA-MTL-1` volume `avw5iclb48` (`fw-ai-comfyui-vace`, 100 GB) for the VACE 14B workflow.

## 2026-10-08 — VACE Pod/model inventory corrected; stale encoder cache recovery

Corrected the current VACE Pod/model inventory on `avw5iclb48`:

- `models/unet/wan2.1_vace_14B_fp16.safetensors`: official Comfy-Org complete 14B VACE diffusion model, 34,675,323,640 bytes. SHA-256 `f202a5c59b8a91ada1862c46a038214f1f7f216c61ec8350d25f69b919da4307`.
- `models/unet/Wan2_1-VACE_module_14B_bf16.safetensors`: Kijai's 6.1 GB VACE module only, preserved under its original name — not a substitute for the complete model in a `UNETLoader`.
- `models/vae/wan_2.1_vae.safetensors`: Kijai BF16 Wan 2.1 VAE, loaded by `VAELoader`.
- `models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors`: official Comfy-Org scaled FP8 UMT5 encoder, 6,735,906,897 bytes.

The first encoder load logged missing CLIP weights and selected `SD1ClipModel` despite the submitted `CLIPLoader(type=wan)`. ComfyUI cached that bad loader result; replacing the file alone did not clear the cache, and `CLIPTextEncode` still failed with `Cannot copy out of meta tensor; no data!`. A fresh Wan text-encode succeeded, then a Pod restart cleared the stale cache. After restart, a minimal `CLIPLoader(type=wan, device=default)` → `CLIPTextEncode` run and a separate `UNETLoader(weight_dtype=fp8_e4m3fn)` run both completed successfully. The full 1280×672, 49-frame VACE video graph had **not** been rendered or verified end to end; these loader checks were not equivalent to a finished shot. The retired Illinois launch command (see 2026-08-03 entry) was flagged as historical only.

## 2026-10-08 — VACE Decode OOM

The first 1280×672, 49-frame, 26-step VACE attempt finished sampling, then the Pod's 50 GB RAM cgroup recorded an OOM kill at `VAEDecode`. The ComfyUI process exited without a saved video; the Pod stayed running but its HTTP proxy returned 502. Restarting the Pod restored ComfyUI.

`/Users/jamesfilios/Downloads/FW_Test_Workflow_Vace_Ready.json` was updated to use `VAEDecodeTiled` with `tile_size=512`, `overlap=64`, `temporal_size=16`, and `temporal_overlap=4`. A separate 49-frame 1280×672 synthetic-latent decode completed, produced 49 preview frames, and used 2.39 GB peak container RAM without an OOM — this validated the decode path only, not the entire graph with the sampler, cached models, and control inputs in memory. An already-open browser workflow retains the old node; the updated JSON must be reloaded into the canvas before retrying.

## 2026-10-08 — Two-stage VACE recovery; first real latent and color artifacts

A second 26-step run also completed sampling and then OOM-killed ComfyUI at the 50 GB container limit; both sampler results were lost. The older server-saved all-in-one workflows still contained untiled `VAEDecode`, and the submitted retry graph was unavailable after the crash — neither old all-in-one graph was safe to queue. Even a finishing-only synthetic-latent run with the staged 4096×2160, 84-frame Scene 4 reference and 4K composite OOM-killed the Pod; tiled VAE decode alone did not make the old chain safe.

Split into two separate, importable canvas workflows instead:

1. `workflows/comfyui/shot004_fire-vace14b_sample-latent_v001.json` ends at `SaveLatent` after `TrimVideoLatent`, no VAE decode. Queue once and confirm `ComfyUI/output/shot004_vace_latent_*.latent` exists before moving on.
2. `workflows/comfyui/shot004_fire-vace14b_decode-latent_v001.json` reads the saved output via `LoadLatent`'s `[output]` path annotation (default `shot004_vace_latent_00001_.latent [output]`; select/edit the actual filename if the counter differs). Uses tiled Wan VAE decode (512/64 spatial, 16/4 temporal), 1280×672 scale and mask, and the 49-frame proxy staged in `ComfyUI/input/`: `shot004_fw-test-scene_plate-proxy_1280x672_49f_v001.mp4` (durable local source under `assets/elements/by-shot/shot004_fire-jump/plates/`). Output prefix `FW_fire_comp_proxy`; not a 4K delivery.

Both JSON files were also saved on the persistent volume at `ComfyUI/user/default/workflows/FW/` for selection in the ComfyUI workflow browser; import one at a time, as an already-open old graph is not replaced.

A synthetic latent was saved and loaded directly from `[output]`; running the complete finishing canvas against it created a 49-frame 1280×672, 24 fps MP4 with 7,819,919,360 bytes peak container RAM and zero OOM events — this verified the finishing workflow on test data, not a full VACE result. Final-resolution assembly/upscaling should go through a streaming compositor rather than reloading the 4K plate and 84 frames into the 50 GB ComfyUI container.

The user then completed the real 26-step sampler and saved `ComfyUI/output/shot004_vace_latent_00001_.latent`. Decoding and compositing that latent through the proxy workflow produced `ComfyUI/output/FW_fire_comp_proxy_00001_.mp4` (49 frames, 1280×672, 24 fps) without OOM. The preview showed orange fire/glow but visible green/magenta artifacts. The saved latent was kept for non-destructive finishing experiments.

## 2026-10-08 — A40 Pod terminated; pod-up defaults aligned to CA-MTL-1

The A40 Pod running this session was terminated safely; the `CA-MTL-1` network volume and the VACE artifacts above were preserved, and the resume point was set to a guided workflow review. `scripts/runpod-pod-up.sh` defaults were aligned with the surviving `CA-MTL-1` VACE volume to prevent an unattached replacement Pod (superseded 2026-11-02 when defaults moved to `EU-RO-1`).

## 2026-10-09 — Pod `03vbr9yofvf2z4` resumed and terminated

Resumed A40 Pod `03vbr9yofvf2z4` on the `CA-MTL-1` VACE volume; decode-only testing found the color artifacts were in the saved latent itself, not the decode step. Terminated `03vbr9yofvf2z4` and cleared the Pod ID; the `CA-MTL-1` VACE volume remained.

## 2026-10-10 — Pod `l6ifya67dcq486` resumed and terminated

Resumed A40 Pod `l6ifya67dcq486` on the `CA-MTL-1` VACE volume; the Seedance test file survived the previous termination. Terminated `l6ifya67dcq486`; recorded the second VACE latent and the agreed Pass A resume point.

## 2026-10-11 — Pod `2q273z4gzxff6n` resumed and terminated

Resumed A40 Pod `2q273z4gzxff6n` on the `CA-MTL-1` VACE volume. Terminated `2q273z4gzxff6n`; recorded Pass A latent `00003` and the strength-0.5 resume point.

## 2026-10-13 — Pods `qgdedf20w84gnp` and `7imyoqxk5n7w7o`

Resumed A40 Pod `qgdedf20w84gnp` on the `CA-MTL-1` VACE volume; terminated it after verifying `KlingMotionControl` rejects human-upper-body input. Separately, A40 Pod `7imyoqxk5n7w7o` was terminated after Kling Omni Edit tests.

## 2026-10-17 — Pods `c0u0flqd84rlen`, `qblvqx3v4pjho8`, `ep5rr963ctx22t`

Resumed A40 Pod `c0u0flqd84rlen` after `CA-MTL-1` A40 stock returned. Strength-0.5 and silhouette runs were confirmed scored; the next test was not another local VACE knob. Terminated `c0u0flqd84rlen` and cleared the Pod ID; next session was set to start at the benchmark, since Wan 2.7 does not need the GPU.

Pod `qblvqx3v4pjho8` came up; Wan 2.7 Video Edit was scored on it; `scripts/runpod-comfy-api.sh submit` started passing the comfy.org key; the SkyReels merge was confirmed not on the current volume. Terminated `qblvqx3v4pjho8` and cleared the Pod ID.

Pod `ep5rr963ctx22t` came up for a hands-on Wan 2.7 Video Edit session; Wan 2.7 run 2 was recorded on the volume and the resume point moved to sharpness tests on the candidate. Terminated `ep5rr963ctx22t` and cleared the Pod ID.

## 2026-10-18 — Mickmumpitz 1.3 setup: Pods, custom nodes, VACE × SkyReels merge, LoRAs

Resume point was pointed at Stage 1 of the benchmark's staged queue. Pod `iqe2i06yi7w9uy` came up; downloaded and verified the VACE × SkyReels V3 R2V FP8 merge, recorded the working SSH key, and recorded the Pass A canvas state with its live Kling node. Pod `iqe2i06yi7w9uy` was then replaced with `aafjaefo4nupf4` for a fresh 2-hour guard. Terminated A40 Pod `aafjaefo4nupf4`; recorded Wan 2.7 runs 3–4 on the volume, the end of Wan 2.7 tuning, and the missing Mickmumpitz 1.3 prerequisites.

Pod `p5u3i5lk87mrlk` came up. Installed into `custom_nodes/` on the volume, by `git clone` from the default branch, for Mickmumpitz 1.3 ADV:

- `ComfyUI-WanVaceAdvanced` (`drozbay`, commit `049213c`, 2026-10-01; registry latest 1.5.1, Mick's graph saved with 1.1.0). Provides `WanVacePhantomSimpleV2`.
- `RES4LYF` (`ClownsharkBatwing`, commit `56e4475`, 2026-10-01). Provides the `res_2s` sampler and `beta57` scheduler for the stock `KSampler`.
- `rgthree-comfy` (`rgthree`, commit `d7297b4`, 2026-10-06). Provides Mick's `Label (rgthree)` nodes; without it the frontend reports a missing node pack. No Python requirements.
- `ComfyUI-GGUF` (`city96`, commit `6ea2651`, 2026-01-12). Provides `UnetLoaderGGUF` for the low-VRAM model path; installed `gguf` and `protobuf` into the venv.

Not installed: `comfyui-easy-use`. Its requirements (diffusers, accelerate, onnxruntime, peft, and others) are heavy, and Mick 1.3 uses it only for two `easy cleanGpuUsed` VRAM-cleanup pass-throughs, which were bypassed instead.

For WanVaceAdvanced and RES4LYF, every requirement was already in the venv except `PyWavelets`, installed with `.venv-cu128/bin/python -m pip install PyWavelets`. `opencv-python` was skipped on purpose because the venv already imports `cv2` 5.0.0, and a second OpenCV build can conflict. All four packs imported without errors. A RunPod-fixed copy of Mick 1.3 and the 1.3 workflow were saved on the volume.

Restarting ComfyUI after a node install: `start.sh` does not relaunch ComfyUI after it exits, and ComfyUI-Manager's `/manager/reboot` returns 404. Use `/workspace/restart_comfyui.sh` (on the volume), which sources `/etc/rp_environment`, activates `.venv-cu128`, and runs `main.py` with the template's arguments; launch it with `setsid nohup … > /workspace/comfyui_restart.log`. Stop the old process by PID, not with `pkill -f "main.py …"` over SSH: that pattern also matches the SSH shell's own command line and kills it.

Model downloads this session:

- `models/diffusion_models/wan-14B_vace_skyreels_v3_R2V_e4m3fn_v1.safetensors`: VACE × SkyReels V3 R2V merge, FP8, from `Inner-Reflections/VACE_Skyreels_V3_R2V_Merge`, 17,344,681,528 bytes. SHA-256 `59511532de0baa48d719ea49f857ada5672d384e5d92e70ea59848ece025d23d` (matches the Hugging Face LFS id). Downloaded with `hf download` in about 20 minutes, unauthenticated, at about 30 MB/s.
- `models/loras/Wan2.1_T2V_14B_FusionX_LoRA.safetensors`: FusionX LoRA from `vrgamedevgirl84/Wan14BT2VFusioniX` (`FusionX_LoRa/`), 316,822,496 bytes. SHA-256 `c653087fa7c9163abdd1a4c627bfc483966c6d78a4426667d1185f860951c30e` (matches the Hugging Face LFS id).
- `models/loras/wan/Lenovo.safetensors`: Lenovo UltraReal v1.0 Wan, a realism LoRA for Wan 14B text-to-video from Civitai (model version 2066914), 306,846,851 bytes. SHA-256 `64002d78edc3cea47d440c4d7bd7bb9de9c8a67177fe10607632cd6281144631` (matches Civitai). Trigger word `l3n0v0`. Downloaded without a Civitai token. Mick 1.3 shipped with this node bypassed.

Terminated A40 Pod `p5u3i5lk87mrlk` before any run; recorded the Mick 1.3 run settings for the next session.

## 2026-10-19 — Pod `amsu1bpsrdzgfr`; NAG/crossfade/seed-wire fixes; termination guard failure

Pod `amsu1bpsrdzgfr` came up after waiting out A40 stock-outs in `CA-MTL-1`; confirmed the custom nodes and models persist across Pods. It ran 15:42–20:01Z (about $2.55). It was created with `--terminate-after 2026-10-19T17:42:03Z` and was still `RUNNING` at 18:14Z, with `runpodctl pod get` showing no stored termination time — the first direct evidence the termination guard does not fire; every earlier Pod had been terminated by hand before its guard.

The shot 004 Mick 1.3 graph, `user/default/workflows/shot004_fire-jump_mick13-skyreels_v001.json`, needed three fixes on this Pod:

- `WanVideoNAG` (KJNodes `78cd992`, unchanged upstream as of this date) failed with `mat1 and mat2 must have the same dtype, but got Half and Float8_e4m3fn` on the FP8 merge — its `patch()` ran `diffusion_model.text_embedding` on 16-bit conditioning before ComfyUI wrapped the FP8 weights for casting. Patched on the volume (marked `FW_AI patch 2026-10-19` in `nodes/model_optimization_nodes.py`): when the text-embedding weights are FP8, `patch()` runs a temporary 16-bit deep copy instead. Only correct for plain FP8; the merge has 1,327 `F8_E4M3` tensors and no scale keys. `git -C custom_nodes/ComfyUI-KJNodes checkout nodes/model_optimization_nodes.py` reverts it. Unverified until a NAG-un-bypassed run succeeded — later superseded on the `EU-RO-1` volume by the 2026-11-02 patch, after this deep copy crashed there.
- `ControlCrossfadeIterationFix` (Mickmumpitz nodes) crashed with `'NoneType' object has no attribute 'shape'` whenever the image mode was `Reference Only`, or `Auto-Detect` with more than one reference, because the router passed `start_frames=None` and iteration 0 read `start_frames.shape`. Patched on the volume (marked `FW_AI patch 2026-10-19` at the top of `apply_crossfade` in `nodes/control_crossfade.py`): `None` becomes an empty batch, so iteration 0 injects nothing. `git -C custom_nodes/ComfyUI-Mickmumpitz-Nodes checkout nodes/control_crossfade.py` reverts it; a pull of that pack will conflict or drop it.
- Mick's 1.3 file was missing the wire from `MultiChannelSlicer`'s `seed` output to the Sampler subgraph's `KSampler` `seed`; versions 1.0 and 1.1 have it. Without it every chunk used the KSampler's fixed `1218564478` and `IterSeedBatch` did nothing. Reconnected in the shot 004 graph, so `seed_1` on the main canvas now sets the seed for chunk 1; `-1` in a later `seed_N` reuses the last valid seed.

Mick's driving video must be a guide signal (pose, depth, canny, tracking), not the RGB of the element. Fed the Houdini fire RGB, run `6bac1820` traced it within ~1% of frame size. Gray-in-mask inputs were placed in `input/`: `shot004_ren-small-fire6_control-graymask-grow16_832x448_81f_v001.mp4` and `shot004_ren-small-fire6_mask-grow16-soft_832x448_81f_v001.mp4`.

Terminated A40 Pod `amsu1bpsrdzgfr` after Mick 1.3 SkyReels runs 1–6; recorded the missing seed wire, the outputs on the volume, and the next one-knob tests.

## 2026-10-19/20 — Pod `jnfjz83llx199h`; NAG patch applied; run 8 current best

Pod `jnfjz83llx199h` (A40, `CA-MTL-1`) came up at 00:08Z on 2026-10-20, patching KJNodes `WanVideoNAG` for plain-FP8 text-embedding weights (unverified until a NAG run). It ran to 00:51Z, about 43 min / $0.43, and was terminated by hand after Mick 1.3 runs 7–8. `RUNPOD_POD_ID` was cleared in `.env`.

Still on the volume at this point: VACE latents `shot004_vace_latent_00001_.latent` through `00003_.latent`, Pass A review clips `FW_fire_comp_proxy_00003_.mp4` through `00006_.mp4`, the rejected proxy `FW_fire_comp_proxy_00001_.mp4`, `seedance_test_00001_.mp4`, Kling Omni Edit tests `output/video/ComfyUI_00005_.mp4` (seed 436) and `ComfyUI_00006_.mp4` (seed 602), Wan 2.7 Video Edit runs `output/video/shot004_wan27-videoedit_00001_.mp4` through `00004_.mp4` (`00002_` is the paid fallback), and Mick 1.3 SkyReels runs `output/shot004_mick13-skyreels_00001.mp4` through `00008.mp4` (`00008` is the current best). Local copies of the scored clips, plus extracted graphs, were indexed in `shots/shot004_fire-jump/pass-a_jerry_log.md`.

Stock VACE knobs and Wan 2.7 tuning were closed. Current best: Mick 1.3 SkyReels run 8 (`shot004_mick13-skyreels_00008.mp4`) — gray-in-mask inputs, `JB-001` + `JB-010`, prompt v3 with `l3n0v0`, Lenovo on, `vace_strength` 1.25, `seed_1` 1218565630, NAG bypassed, 512p. The saved graph `shot004_fire-jump_mick13-skyreels_v001` was in that state. Resume point set to benchmark step 8c: NAG with a negative prompt (the first real test of the KJNodes patch), then 720p, then a comp check over the plate. The older `mickmumpitz/260608_MICKMUMPITZ_AI-VFX_1-3_ADV_runpod.json` and the Pass A canvas `shot004_fire-vace14b_sample-latent_v001_pass_A.json` (silhouette state, live `KlingOmniProEditVideoNode`; bypass before any run) were superseded for this work. A Blender Jerry fire rig existed and was not the shot 004 motion driver; see `docs/pipeline-strategy.md`.

Account balance check: A40 stock in `CA-MTL-1` can drop to `none`; `scripts/runpod-with-auth.sh runpodctl gpu list --include-unavailable` shows per-data-center stock. SSH works with `-i ~/.ssh/id_ed25519_runpod -o IdentitiesOnly=yes`; the `~/.runpod/ssh/runpodctl-ssh-key` path that `runpodctl pod get` prints does not exist on this Mac. A new Pod has a new host key; pass `-o StrictHostKeyChecking=accept-new`.

## 2026-11-01 — `CA-MTL-1` is down

RunPod's status page has had "CA-MTL-1 DC is Unavailable" open since 2026-10-31 20:30 UTC. `gpu list` shows no GPU type in `CA-MTL-1`, and `scripts/runpod-pod-up.sh` fails with "no longer any instances available" (nothing is charged). Volume `avw5iclb48` still lists in the account, but no Pod anywhere can attach it until the data center returns. If the outage lasts days, the fallback is a new volume in another data center, rebuilt from this project's model, node, and patch notes plus the repo's workflows and inputs, at roughly 25 GB of downloads.

## 2026-11-02 16:40–17:58 UTC — `CA-MTL-1` still down; decision to wait

The status-page incident "CA-MTL-1 and EU-SE-1 DC is Unavailable" had no update since it opened on 2026-10-31 20:30 UTC. `gpu list --include-unavailable` listed no GPU type in `CA-MTL-1`; volume `avw5iclb48` still listed there. No Pod was started. At 17:58 UTC it was still down; the incident's first update (17:34 UTC) said only that work continues. James chose to wait rather than rebuild the volume in another data center (A100 SXM 80 GB had Low stock in `US-KS-2` and `US-MD-1` at $1.79/hr).

## 2026-11-02 — New volume `dqlwnz6nq8` built in `EU-RO-1`

With `CA-MTL-1` down, James approved rebuilding elsewhere. `EU-RO-1` was chosen because it hosts the most GPU types of any data center (16, including RTX A6000 48 GB at $0.59/hr, L4, RTX 4090/5090, A100, RTX PRO 6000) and supports Runpod's S3-compatible volume API, so files can be moved without a Pod; it is in Romania. Volume `fw-ai-comfyui-eu-ro` (`dqlwnz6nq8`), 100 GB. Data on `avw5iclb48` could not be copied out while `CA-MTL-1` is down (moving data needs a running Pod on each side, and `CA-MTL-1` has no S3 API), but nothing on it was irreplaceable, so the new volume was rebuilt from scratch.

Setup Pod `ji7jkj0lcps26b` (L4 24 GB, $0.59/hr; the RTX 2000 Ada and A6000 were unavailable) ran 19:05Z on 2026-11-02 to 00:14Z on 2026-11-03 (about 5 h 9 min, roughly $3.04 at $0.59/hr) and was terminated by hand with `scripts/runpod-pod-down.sh`. Balance after the top-up: $21.89. The template installed ComfyUI 0.30.0 into `/workspace/runpod-slim/ComfyUI` (venv `.venv-cu128`, Python 3.12, torch 2.10.0+cu128) with ComfyUI-Manager, ComfyUI-KJNodes `78cd992`, Civicomfy, and ComfyUI-RunpodDirect. `scripts/runpod/setup_mick13_volume.sh`, run on the Pod, then installed everything else in about 15 minutes:

- Nodes at pinned commits: VideoHelperSuite (latest), Mickmumpitz-Nodes `270afbd`, WanVaceAdvanced `049213c`, RES4LYF `56e4475`, rgthree `d7297b4`, GGUF `6ea2651`, plus PyWavelets, gguf, protobuf. All import; `/object_info` has every node type in the run 8 graph and the `res_2s` sampler and `beta57` scheduler.
- Both patches reapplied by the script; the Mickmumpitz `start_frames=None` bug is still upstream at `270afbd`. The first NAG run (2026-11-02, L4) showed the 2026-10-19 NAG patch does not work on ComfyUI 0.30.0: its deep copy of the text embedding raised `CUDA error: invalid argument` under dynamic VRAM (comfy-aimdo), then ComfyUI died with `free(): double free detected` in `comfy_aimdo/host_buffer.py`. The script now applies a replacement, marked `FW_AI patch 2026-11-02`: `patch()` runs each text-embedding layer through `forward_comfy_cast_weights`, ComfyUI's own casting path, in the model's `manual_cast_dtype` (FP16 here). A standalone test on the Pod loaded the merge (FP8 weights) and patched all 40 blocks without error, and the full NAG run (benchmark run 9, 684 s on the L4) completed, so the patch is verified. `bash setup_mick13_volume.sh patch` reapplies only the patches.
- Models: the merge (checksum verified), UMT5 FP8 encoder (size verified), Kijai's BF16 Wan VAE as `wan_2.1_vae.safetensors`, FusionX and Lenovo LoRAs (checksums verified). The merge downloaded at about 30 MB/s.
- `/workspace/restart_comfyui.sh` recreated by the script.
- Inputs uploaded to `input/`: the grow16 guide and mask, `JB-001`, `JB-010`. The run 8 graph extract is saved as `user/default/workflows/shot004_fire-jump_mick13-skyreels_v001.json`.

No Pod is running after this session; the two volumes cost about $0.019/hr together. Resume point set to Pass B test 3.

## 2026-11-02 — Run 8 reproduced on new volume (run 8r)

James ran the saved graph unchanged on the L4; it finished in 667 s (run 8 took 353 s on the A40) and gave a nearby sample, not a bit-identical one (see `shots/shot004_fire-jump/pass-a_jerry_log.md`). The stack is verified; one-knob tests on it compare against run 8r on the same GPU type. Account balance was $4.90 at 19:24Z against $0.61/hr.

## 2026-11-02 — ComfyUI version and template-overwrite behavior

Checked 2026-11-02: the official template image `runpod/comfyui:1.3.3-comfyuiv0.30.0-cuda12.8` bakes ComfyUI 0.30.0; upstream is at 0.43.0 (2026-10-27). On every boot `start.sh` compares the volume's bundle manifest with the image's; when they differ (a new template image) it rsyncs the image's ComfyUI core over the volume's, keeping `models`, `input`, `output`, `user`, `custom_nodes` and the venv. So a ComfyUI updated by hand on the volume survives restarts until RunPod ships a new template image, which then overwrites it, possibly with an older version. Updating in place also risks the pinned custom nodes and the NAG patch and changes the seed baseline, so it should be done at a break between tests, with a rollback (record the commit and `pip freeze` first), or as a second install on the same volume.

## 2026-11-03 19:20Z — Pod `g0jkc58x01xpa2` started (A100)

Running on the `EU-RO-1` volume, an A100 80 GB PCIe at $1.79/hr, started about 19:20Z. The L4, RTX A6000, RTX 4090, RTX 5090 and RTX PRO 6000 all returned "no longer any instances available"; only the A100 started. Created with `runpodctl pod create` directly (same template, volume and ports as the up-script, no `--terminate-after`). Patches, nodes and workflow folders were intact; A100 samples are not comparable seed-for-seed with the L4 runs. After Pass B test 7, the resume point was updated to point at the new Pass B test log (now `shots/shot004_fire-jump/pass-b_grassfire_log.md`). Terminated after Pass B test 14; resume point set to test 15.

## 2026-11-03 ~23:15 UTC — Pod `bd2rmuu6fy08ks` started (RTX 4090)

RTX 4090 24 GB, $0.89/hr, on the `EU-RO-1` volume (no A100 80 GB in stock; James chose the 4090). SSH `ssh -i ~/.ssh/id_ed25519_runpod -o IdentitiesOnly=yes -p 16172 root@213.173.110.143`; ComfyUI `https://bd2rmuu6fy08ks-8188.proxy.runpod.net`. Because results only match on the same GPU type, test 14 was rerun here first as the 4090 baseline (test 14r), then test 15.

## 2026-11-04 00:50 UTC — Pod `bd2rmuu6fy08ks` terminated; Pass B moved to FLF video

Terminated at about 00:50 UTC; balance $15.06, volume only ($0.019/hr). Pass B moved to first-last-frame video through ComfyUI API nodes (Seedance 2.0, Kling), which bill the Comfy account and do not need the GPU; the graph is `shot004/pass-b_grassfire/shot004_fire-jump_grassfire-flf_seedance20_v001.json` (Seedance and Kling branches), and the repo copy matches. The inpaint graph still holds James's first Seedance nodes (3614, 3615); remove them before the next inpaint run or each run also queues a paid Seedance call. Next: comp Kling K1 like S3 (`scripts/build_shot004_grassfire_layer.py`, `scripts/blender/shot004_comp_add_passb.py`), choose the generator, make the final at full resolution; steps in `shots/shot004_fire-jump/plan.md`. A GPU Pod is only needed again for Jerry (Pass A) or SkyReels inpaint tests. The smaller Jerry guide still awaits James's approval.
