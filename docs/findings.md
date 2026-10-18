**Created:** 2026-05-18
**Modified:** 2026-10-18
**Version:** 1.12

# Findings

## 2026-05-17

- Higgsfield `wan2_7` produced a strong robot/bunny benchmark from prompt alone.
- Local ComfyUI SD 1.5 text-to-image works.
- Local ComfyUI Wan2.2 5B video tests were not production-usable for prompt-adherent text-to-video from pure noise.
- Wan2.2 FP8 diffusion weights are not compatible with Apple MPS due to unsupported `Float8_e4m3fn`.
- For the short film, prioritize element generation, alpha/matte workflows, and compositing passes over full-shot AI video.

## 2026-05-19

- Scene 4 / shot004 should be developed as layered VFX, not a single baked AI video: Jerry element, matte/alpha, glow/contact light, grass ignition, smoke/heat, scorch, and preview comp should remain separately revisable.
- Current local ComfyUI install exposes useful video nodes, including `Wan22FunControlToVideo`, `LoadVideo`, `GetVideoComponents`, `CreateVideo`, and multiple cloud/API video nodes.
- Current local model inventory does not include ControlNet model files. ControlNet and IPAdapter workflows will need additional model installs before they can be serious production branches.
- First local ComfyUI element-control workflow created and validated: `workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.json`.
- Use a generation proxy resolution around 832x448 for first Wan2.2 tests, then composite/evaluate against the 4K plate in Fusion/Resolve. Keep the original `FW_test_scene.mov` as the final plate source.

## 2026-08-30

- Official Wan2.2 Fun Control tutorial weights, both `lightx2v` LoRAs, `wan_2.1_vae`, and the sample start image / pose video are on network volume `fw-ai-comfyui`. The tutorial graph was loaded but not queued.
- Illinois 4090 was out of stock; an RTX 6000 Ada (48 GB, $0.84/hr) in `US-IL-1` ran the same volume. Fun Control 14B fp8 fits that card.
- RunPod Direct can land 14B files in `models/unet/` while a parallel download lands the same filename in `models/diffusion_models/`. ComfyUI treats those folders as one UNET pool, so a second copy is wasted space. One duplicate low-noise 14B was deleted; volume usage after that was ~48 GB of 100 GB.

## 2026-09-07

- Fun Control learning closed. `Wan22FunControlToVideo` has no control-strength slider; concat control is structure. Canny or the full `ren_small_fire6` CGI made Jerry fill the old body. A ~56px centroid dot was too weak (idle bounce). A fat centroid streak was usable as path-only control.
- Jerry tests used the official 14B Fun Control template with `JB-001` + fire controls, not `shot004_jerry-wan22-funcontrol-element_v001.json` (5B TI2V). Next hands-on chapter is Mickmumpitz / VACE-1.3B.

## 2026-09-18

- Mick Superhero: matte from **plate** (`MASK_00005`), not the pose `DRIVINGVIDEO` and not `MASK-PLATE` (QC RGB). Suit restyle works. Pose-skeleton drive still 180° flips the body on the left-arm raise at `vace_ref_strength` 0.8. Next: plate as driving.
- Load Video only lists `input/`; Preprocess writes `output/AIVFX-PREPROCESS/`. Copy mattes into `input/` before Simple.
- CoTracker on 4K×395 Superhero frames killed ComfyUI (502). Bypass TRACK. Lenovo LoRA (`Lenovo.safetensors`) is on the volume.

## 2026-10-09

- Shot 004 VACE green/magenta is in the saved latent, not the proxy composite or tiled VAE decode. Raw `VAEDecodeTiled` of `shot004_vace_latent_00001_.latent` already shows the blobs inside the control ellipse; the plate, fire control, and Jerry stills are clean. `WanVaceToVideo` in ComfyUI 0.30.0 uses only the first reference image, so `JB-010` never conditioned the sample. The grass-ignition prompt, static 800×380 mask, 0.55 screen-blended control, strength 0.5, and CFG 6 are the conflict. Detail: `shots/shot004_fire-jump_workflow-test-plan_v001.md`.

## 2026-10-11

- Higgsfield catalog check for the shot004 Jerry element (CLI 1.1.26, schemas only). No video tool takes a mask or outputs alpha; never upload the plate. Edit tools keep the source clip's black background. Best fit: `kling_video_edit` (Kling 3.0 Omni Edit) with the Houdini clip plus Jerry refs, 6 credits `std` / 8 `pro` for the 4.0s clip. Backup: `seedance_2_5 --mode video_edit`, 14 credits at 480p, 30 at 720p, 48 at 1080p (4s minimum, so pad the 87-frame source to 96 frames). `kling3_0_motion_control` (8 credits) and the Genjutsu jobs (`hf_mult_*`, 12 at 480p) are likely body-driven motion transfer, so skip them for a faceless fireball.
- The trial account rejects `generate create` from the CLI with `only_mcp_usage_on_trial_is_available` and charges nothing. Generation needs the MCP server `https://mcp.higgsfield.ai/mcp`, now defined in `.omp/mcp.json`.
- MCP works on the trial. Upload IDs created with the CLI resolve in MCP. Both `get_cost` quotes matched the CLI. `kling_video_edit` std failed server-side with no reason given and was refunded automatically. `seedance_2_5 video_edit` 480p kept the Jerry look on black but drifted 16–19% of frame width off the Houdini landing, so it is not path-locked. Detail: `shots/shot004_fire-jump_workflow-test-plan_v001.md`.

## 2026-10-13

- ComfyUI `KlingMotionControl` (`kling-v3` / `kling-v2-6`) runs a mandatory human upper-body detector on `reference_image` before generation and rejects Jerry (`JB-001`) with `Image recognition failed... Error: No complete upper body detected in the image; ensure the upper body is clearly visible.` (0 credits deducted). Do not use `KlingMotionControl` for non-humanoid elemental characters; use general Video Edit / V2V nodes (`KlingOmniProEditVideoNode`, `KlingOmniProVideoToVideoNode`, `Wan2VideoEditApi`) instead.
- Kling 3.0 Omni Edit (`KlingOmniProEditVideoNode`) accepts Jerry, unlike `KlingMotionControl`, but on the Houdini fire clip it held the source look at the start and only adopted the still toward the end (`output/video/ComfyUI_00005_.mp4` seed 436, `ComfyUI_00006_.mp4` seed 602). The input also must be at least 720×720 and 3–10 seconds. A prompt that names `@image1` and `@video1` was suggested; if the ramp remains, stop spending credits on this node for a frame-1 swap.

## 2026-10-17

- The official Blender Lab MCP works end to end on Blender 5.2.1: stdio to `blender-mcp` to the TCP bridge on `localhost:9876`, with 26 tools. `execute_blender_code` rejects a non-dict `result` but still returns stdout. Headless `blender -b -c blender_mcp` fails with `--factory-startup` because user add-ons are skipped. Detail: `mcp/blender.md`.
- Blender Jerry fire rig (`assets/characters/jerry/source-cgi/jerry_fire-rig_v001.blend`): a rigged, invisible emitter body plus a bone-parented core-glow volume plus Mantaflow fire gives Jerry's teardrop silhouette with real flame edges, and the fire follows the animation. r09 is not approved: the flame texture is busier and flakier than JB-001/JB-010. Mantaflow pitfalls: any volume emission produces a tall white candle column; with flame smoke 0 the default domain `clipping` cuts the flame in hard horizontal lines (set it to 0); volume motion blur smears the fire. Bake 262 s per 120 frames at res 128 with ×2 upres on an M2 Pro. Detail: `workflows/blender/jerry/jerry_fire-rig_log_v001.md`.
- Stock `WanVaceToVideo` cannot take Jerry's look from `JB-001` while following the Houdini fire. Strength `0.5` (`FW_fire_comp_proxy_00005_.mp4`) smeared the path. A white-mask control video (`FW_fire_comp_proxy_00006_.mp4`) was drawn as gray smoke. Do not keep tuning that graph. Next test is Wan 2.7 Video Edit. Detail: `docs/vfx-element-benchmark.md`.
- Wan 2.7 Video Edit (`Wan2VideoEditApi`, 720P, seed 42, $0.68) is the first shot 004 run to hold the Houdini path (≤2.3% of frame width centroid drift, landing 1.1%) with a clean black background and a Jerry-like teardrop from frame 1, without Kling's late ramp. The look still fails: a glossy, generic candle-drop with a white core, not `JB-001`'s soft wispy fireball. It returns 30 fps 1280×720 with generated audio from a 24 fps 832×448 input. Next: Runway Aleph. Detail: `docs/vfx-element-benchmark.md`.
- The previous `COMFY_API_KEY` was revoked (`api.comfy.org` returned `Invalid Comfy API key`, Comfy Cloud 401); a new key went into `.env` on 2026-10-17. Pod partner nodes authenticate through `extra_data.api_key_comfy_org` on `/prompt`, which `scripts/runpod-comfy-api.sh submit` now sends, so the browser login is no longer needed. Without it the node fails with `Unauthorized: Please login first to use this node` before any upload or charge.
- The python.org Python 3.11 at `/usr/local/bin/python3` has no CA bundle, so `scripts/comfy-cloud-api.py` fails with `CERTIFICATE_VERIFY_FAILED`. Run it with `/opt/homebrew/bin/python3`, or run that framework's `Install Certificates.command` once.
- Wan 2.7 Video Edit varies a lot by seed. Same prompt, graph, and inputs: seed 42 gave a generic glossy teardrop, while seed `2126129005` read as `JB-001` (smoky edge, sparks, pale core) and passed path, look, and black. It is the first Pass A candidate for shot 004, at $0.676 per 3.4 s clip at 720P. Its weakness is softness: the flame is only 150–400 px tall in a 1280×720 frame, keeps ~70–75% of `JB-001`'s detail at equal size, and comes back at ~0.7 Mbps. Try `1080P` on the same seed first, then a cropped-in source. Detail: `docs/vfx-element-benchmark.md`.

## 2026-10-18

- Wan 2.7 Video Edit cannot be tuned one knob at a time. Adding `JB-010` as a second reference at the same seed (`2126129005`) produced an unrelated sample: a smooth white teardrop that failed path and look. It differed from the good run about as much as a run with a different seed did. A run with prompt v2, `JB-010`, and seed 508 was recognizable (user: ~75%) but drifted 25–27% of frame width mid-jump. Overall one good run in four, about $2.70. Wan 2.7 tuning stopped; seed-2126129005 run 2 is the paid fallback. Detail: `docs/vfx-element-benchmark.md`.
- Alibaba's Wan 2.7 video edit API rewrites the prompt with an LLM by default (`prompt_extend`, default true) and has a separate `negative_prompt` (≤500 chars). The ComfyUI `Wan2VideoEditApi` node sends neither, so every ComfyUI run is rewritten and negatives sit in the positive prompt. Source: Alibaba Model Studio `wan-video-editing-api-reference`.
- ComfyUI's Generated assets panel on a fresh Pod shows only that Pod's runs; older outputs are still in `output/` on the volume. Load them with a `[output]` entry in Load Video or from the repo's kept copies.
- Mickmumpitz AI-VFX 1.3 ADV (`260608_MICKMUMPITZ_AI-VFX_1-3_ADV.json`, on the Desktop in `VFX workflows/`) runs the VACE × SkyReels merge through `WanVacePhantomSimpleV2` (pack `wanvaceadvanced`) with the FusionX LoRA, 5 steps, CFG 1, `res_2s`/`beta57`, NAG, and per-frame `ComposeColorMatch`. Volume `avw5iclb48` has the merge, KJNodes, VHS, and the Mickmumpitz nodes but lacks `wanvaceadvanced`, the RES4LYF sampler and scheduler, ComfyUI-GGUF, and any LoRA.
