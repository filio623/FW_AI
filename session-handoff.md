# AI Video Workflows Session Handoff

Date: 2026-05-17

## Environment

- User machine: macOS, Apple MPS backend.
- ComfyUI is reachable at `http://127.0.0.1:8000`.
- ComfyUI version: `0.21.1`.
- ComfyUI base/user paths:
  - Base models directory: `/Users/robbiefilios/Documents/ComfyUI/models`
  - Input directory: `/Users/robbiefilios/Documents/ComfyUI/input`
  - Output directory: `/Users/robbiefilios/Documents/ComfyUI/output`
  - User library: `/Users/robbiefilios/Documents/ComfyUI/user`

## Initial ComfyUI Test

Created and successfully ran a basic SD 1.5 text-to-image test.

- Checkpoint: `v1-5-pruned-emaonly-fp16.safetensors`
- Output file: `/Users/robbiefilios/Documents/ComfyUI/output/ComfyUI_txt2img_test_00001_.png`
- Prompt: small ceramic robot on a desk
- Result: generated successfully in about 11 seconds.

## Local Models Installed / Discussed

Already present before video work:

- `/Users/robbiefilios/Documents/ComfyUI/models/checkpoints/v1-5-pruned-emaonly-fp16.safetensors`

Downloaded for Wan2.2 5B tests:

- `/Users/robbiefilios/Documents/ComfyUI/models/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors`
- `/Users/robbiefilios/Documents/ComfyUI/models/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors`
- `/Users/robbiefilios/Documents/ComfyUI/models/vae/wan2.2_vae.safetensors`

Important: the VAE and text encoder initially had incomplete downloads and produced safetensors errors. They were resumed and verified with `safetensors.safe_open`. All three Wan2.2 5B files became readable.

## Workflows Created

Saved in the ComfyUI user workflow library.

### 1. `wan22_t2v_robot_petting_bunny_test.json`

API/execution-format workflow. It may execute but can appear blank in the visual editor because it lacks UI node layout.

Purpose:

- Native Wan2.2 5B text-to-video.
- Prompt: robot petting a bunny.
- Resolution: `832x480`
- Length: `121` frames
- FPS: `24`
- Steps: `20`
- CFG: `5`
- Sampler: `uni_pc`
- Scheduler: `simple`
- ModelSamplingSD3 shift: `8`

### 2. `wan22_t2v_robot_petting_bunny_test_visible.json`

Visible canvas version of the first workflow.

Issue observed:

- It generated a video, but the result was very blurry and did not follow the prompt well.
- It looked like an early diffusion / underdeveloped output.
- Diagnosis: not obviously a broken workflow, but Wan2.2 5B text-to-video from pure noise is weak for exact composition; prompt included soft/depth-of-field language; low resolution and limited step budget likely contributed.

### 3. `wan22_t2v_robot_petting_bunny_quality_test.json`

Tuned text-to-video attempt.

Changes:

- Length: `81` frames
- FPS: `16`, still about 5 seconds
- Steps: `30`
- Sampler: `euler`
- Scheduler: `simple`
- Sharper prompt and stronger blur-negative prompt

Purpose:

- Try to improve quality while keeping the same local Wan2.2 5B model.

### 4. `robot_bunny_sd15_firstframe_wan22_i2v.json`

API/execution version of an image-to-video pipeline.

### 5. `robot_bunny_sd15_firstframe_wan22_i2v_visible.json`

Visible canvas version of the image-to-video pipeline.

Purpose:

- Generate a clear first frame using local SD 1.5.
- Feed that image into `Wan22ImageToVideoLatent` as `start_image`.
- Use Wan2.2 5B to animate the first frame.

Why:

- Local Wan2.2 5B text-to-video had poor prompt adherence from pure noise.
- Image-to-video should anchor the robot/bunny composition better.

Settings:

- First-frame model: `v1-5-pruned-emaonly-fp16.safetensors`
- First-frame resolution: `768x448`
- First-frame steps: `28`
- First-frame sampler/scheduler: `dpmpp_2m` / `karras`
- Wan I2V resolution: `768x448`
- Wan I2V length: `81` frames
- Wan I2V FPS: `16`
- Wan I2V steps: `30`
- Wan I2V sampler/scheduler: `euler` / `simple`
- Wan shift: `8`

## ComfyUI Built-In Wan2.2 Template Issue

The user tried the built-in `wan2.2 text to video` template with high-noise and low-noise 14B FP8 models:

- `wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors`
- `wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors`

Error:

```text
TypeError: Trying to convert Float8_e4m3fn to the MPS backend but it does not have support for that dtype.
```

Diagnosis:

- This is caused by FP8 quantized Wan diffusion weights being used on Apple MPS.
- Apple MPS does not support `Float8_e4m3fn`.
- The sampler is where the model first executes, but the sampler is not the root cause.
- The built-in template is likely CUDA/NVIDIA-oriented when using FP8 models.

Recommended fix:

- Use FP16 diffusion models on MPS.
- Specifically download:
  - `wan2.2_t2v_high_noise_14B_fp16.safetensors`
  - `wan2.2_t2v_low_noise_14B_fp16.safetensors`
- Put both in:
  - `/Users/robbiefilios/Documents/ComfyUI/models/diffusion_models/`
- Then select the FP16 files in the two `Load Diffusion Model` nodes.

Notes:

- These FP16 files are large, about 28.6 GB each, about 57 GB total.
- User said these were downloading.

Useful links:

- High noise FP16:
  `https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_high_noise_14B_fp16.safetensors`
- Low noise FP16:
  `https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_low_noise_14B_fp16.safetensors`

## Higgsfield CLI

The Higgsfield CLI is installed and authenticated.

- CLI version: `higgsfield 0.1.40`
- Account shown by CLI: `robfilios@gmail.com`
- Plan: `ultra`
- Credits at check time: `385.45`

Available video models returned by CLI included:

- `cinematic_studio_3_0`
- `cinematic_studio_video`
- `cinematic_studio_video_v2`
- `veo3`
- `veo3_1`
- `veo3_1_lite`
- `grok_video`
- `kling2_6`
- `kling3_0`
- `marketing_studio_video`
- `minimax_hailuo`
- `seedance1_5`
- `seedance_2_0`
- `soul_cast`
- `wan2_6`
- `wan2_7`

Model parameter checks:

- `wan2_7`
  - Required: `prompt`
  - Params: `aspect_ratio`, `duration`, `medias`, `resolution`
  - Default duration: `5`
  - Resolutions: `720p`, `1080p`
- `seedance_2_0`
  - Required: `prompt`
  - Params: `aspect_ratio`, `duration`, `genre`, `medias`, `mode`, `resolution`
  - Mode: `std`, `fast`
  - Resolutions: `480p`, `720p`, `1080p`
- `kling3_0`
  - Required: `prompt`
  - Params: `aspect_ratio`, `duration`, `mode`, `prompt`, `sound`

Cost estimates for the robot/bunny test:

- `wan2_7`, 5s, 720p, 16:9: `7.5 credits`
- `seedance_2_0`, 5s, 720p, 16:9, fast: `17.5 credits`

Ran one Higgsfield benchmark:

```bash
higgsfield generate create wan2_7 \
  --prompt "A small white ceramic service robot gently pets a calm gray bunny on a clean sunlit studio floor. The bunny blinks and leans into the robot's rounded hand. Stable camera, warm natural daylight, detailed fur, clear subject edges, peaceful tender mood." \
  --duration 5 \
  --aspect_ratio 16:9 \
  --resolution 720p \
  --wait \
  --wait-timeout 20m \
  --wait-interval 10s
```

Result URL:

`https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260517_200503_27504c7a-cf03-483c-b2ac-9d57c69a2cf5.mp4`

## Research / Strategy Notes

The user wants to step back and spend time researching current best AI video workflows and models, especially for ComfyUI and local/cloud comparison.

Working theory so far:

- Local Wan2.2 5B T2V is not enough for high-quality prompt-adherent text-to-video from pure noise.
- I2V with a strong first frame is likely a better workflow structure.
- The current first-frame generator is SD 1.5, which is weak by modern standards; upgrading first-frame generation will probably improve downstream I2V substantially.
- On Apple MPS, avoid FP8 diffusion models. Use FP16/BF16-compatible models, or keep incompatible quantized components off MPS.
- Higgsfield CLI is useful as a cloud benchmark and reference-output generator while local ComfyUI workflows are tuned.

## Workspace Setup Added

Created a project workspace structure for the short-film VFX effort:

- `README.md`
- `docs/`
  - `workspace-map.md`
  - `pipeline-strategy.md`
  - `environment.md`
  - `findings.md`
  - `asset-inventory.md`
- `mcp/`
  - `README.md`
  - `comfyui.md`
  - `higgsfield.md`
- `skills/`
  - `comfyui-vfx/`
  - `higgsfield-vfx/`
- `workflows/`
  - `comfyui/`
  - `higgsfield/`
  - `templates/`
- `shots/`
- `prompts/`
- `references/`
- `scripts/`
- `outputs/`
- `assets/`

The project-local skills are intended as reusable agent instructions:

- `skills/comfyui-vfx/SKILL.md`
  - Use for ComfyUI VFX workflows, model/debug notes, alpha/matte workflows, and MCP-based ComfyUI operations.
- `skills/higgsfield-vfx/SKILL.md`
  - Use for Higgsfield CLI generation, model/cost checks, run logging, and cloud benchmark comparisons.

Validation note:

- The skill validator script exists, but `python3` currently lacks `PyYAML`, so `quick_validate.py` failed with `ModuleNotFoundError: No module named 'yaml'`.
- A lightweight structural check confirmed each skill has `SKILL.md`, `agents/openai.yaml`, and reference files.

## Supermemory Setup Added

Added local Supermemory setup:

- `.env`
  - Contains `SUPERMEMORY_API_KEY`
  - Contains `SUPERMEMORY_CONTAINER_TAG=ai-video-workflows`
  - Contains `SUPERMEMORY_PROJECT=ai-video-workflows`
- `.env.example`
  - Non-secret template.
- `.gitignore`
  - Ignores `.env`, `.DS_Store`, and `outputs/`.
- `scripts/supermemory-mcp.sh`
  - Reads `.env`.
  - Starts Supermemory MCP through `mcp-remote`.
  - Passes auth and project headers via environment placeholders instead of embedding the key in Codex config.
- `scripts/update-codex-supermemory-mcp.py`
  - Idempotently adds/updates the Supermemory MCP block in `~/.codex/config.toml`.
  - Created a backup at update time.
- `mcp/supermemory.md`
  - Documents the setup.

Updated global Codex config:

```toml
[mcp_servers.supermemory]
command = "/Users/robbiefilios/Documents/FW_AI_Workflow/scripts/supermemory-mcp.sh"
startup_timeout_sec = 30
tool_timeout_sec = 60
```

Connection test:

- A one-off `mcp-remote-client` test successfully connected to `https://mcp.supermemory.ai/mcp`.
- The diagnostic client echoed resolved headers, so no persistent test script was kept.
- Restart Codex to load the new `supermemory` MCP server in future sessions.

Seeded Supermemory documents before refresh:

- `ai-video-workflows-session-seed-2026-05-17`
  - File: `memories/seeds/ai-video-workflows-session-seed-2026-05-17.md`
  - Document id: `L6QJhytqFP4CxJuNJCmtUn`
- `ai-video-workflows-pipeline-strategy-2026-05-17`
  - File: `docs/pipeline-strategy.md`
  - Document id: `1ZoFBBQHWSqJeNuyQ6zBBM`
- `ai-video-workflows-workspace-map-2026-05-17`
  - File: `docs/workspace-map.md`
  - Document id: `1HYTkkUj49tpr5E6PCijJM`
- `ai-video-workflows-findings-2026-05-17`
  - File: `docs/findings.md`
  - Document id: `VutxtjmGboSKvtDhfeYcu4`
- `ai-video-workflows-session-handoff-2026-05-17`
  - File: `session-handoff.md`
  - Document id: `ix6LaVCSYwN6t1d1xVvhUM`

Added local Supermemory skill and helper:

- `skills/supermemory-vfx/SKILL.md`
- `scripts/supermemory_add_document.py`

Suggested next-session priorities:

1. Verify whether the Wan2.2 14B FP16 high/low-noise models finished downloading and are readable with `safetensors.safe_open`.
2. Test the built-in Wan2.2 template again with FP16 high/low-noise models.
3. Compare output quality against the Higgsfield Wan 2.7 reference.
4. Research current ComfyUI video stacks:
   - Wan2.2 / Wan2.7 workflows
   - LTX Video / LTX 2.x
   - HunyuanVideo
   - Kling/Seedance/Veo via cloud APIs
   - Best first-frame generation models for I2V
5. Decide whether the local target is:
   - best quality regardless of render time,
   - fastest usable local iteration,
   - best hybrid local/cloud workflow,
   - or a repeatable production pipeline.
