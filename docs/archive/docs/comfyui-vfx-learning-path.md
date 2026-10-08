**Created:** 2026-08-02
**Modified:** 2026-10-08
**Version:** 2.6
**Archived:** 2026-10-08
**Original path:** docs/comfyui-vfx-learning-path.md

# [ARCHIVED] ComfyUI VFX Learning Path

This 2026 learning syllabus and its Pod/volume instructions are historical. The active guided VACE graph review is in `shots/shot004_fire-jump_workflow-test-plan_v001.md`; current infrastructure is in `mcp/runpod.md`. Do not resume from the "Current next step" below.

## Project Goal

This is not simply a workflow for generating a video of fire. It is a controlled VFX pipeline:

- Use the existing CGI fire animation to control Jerry's timing, path, and silhouette.
- Use approved images to maintain Jerry's appearance.
- Generate Jerry as a separate element without damaging the live-action plate.
- Produce or extract a matte.
- Handle glow, grass ignition, smoke, scorch, occlusion, and other interactions as separate passes.
- Composite everything in Fusion/Resolve.

This matches the approach already documented in:

- `docs/comfyui-vfx-workflow-strategy.md`
- `shots/shot004_fire-jump_workflow-test-plan_v001.md`

## Where You Run This

Work happens on a RunPod GPU Pod, not locally. Setup, Pod IDs, and the current resume point live in `mcp/runpod.md`.

The up-script default is an **RTX 4090, 24 GB VRAM, at $0.74/hour**. If that SKU is out of stock in `US-IL-1`, attach the same volume to whatever GPU is actually available there (2026-08-29: RTX 6000 Ada, 48 GB, $0.84/hour). ComfyUI and all downloaded models live on the volume at `/workspace/runpod-slim/ComfyUI`, so they survive Pod termination and GPU changes. Current volume inventory is in `mcp/runpod.md`.

Two habits that matter because the Pod bills by the hour:

- **Read and watch with the Pod off.** Every tutorial below can be studied without a GPU. Only start a Pod when you are about to run something.
- **Always set `--terminate-after`.** A forgotten Pod is the only way this gets expensive.

Changing GPU later costs nothing but a few minutes: terminate the Pod, create a new one with a different `--gpu-id`, and attach the same network volume. Everything under `/workspace` persists.

## Which Model Family, And Why

The requirement that drives this choice is control, not raw video quality. This project needs a generated character to follow an existing CGI render's motion, keep an approved look, and come out separable enough to matte.

**Wan (Alibaba) is the right family for now.** It is Apache 2.0, it has the deepest control ecosystem in ComfyUI, and the Shot 004 workflow already produced a working baseline with it. Three relevant variants:

- **Wan 2.2 Fun Control** — control video plus a reference image. This is what `shot004_jerry-wan22-funcontrol-element_v001.json` uses.
- **Wan VACE** — a unified editing model that takes control video *and* reference images together, plus masks, inpainting, outpainting, and first/last-frame. This is closer in shape to the actual problem than Fun Control and is the most promising next branch. Note the size split: VACE-1.3B is ~7 GB and fits the 4090 easily; **VACE-14B is ~32 GB and will not fit in 24 GB VRAM**.
- **Wan-Alpha** — generates RGB and alpha together. Genuinely useful for transparent, glowing, smoky elements, but it is **text-to-video only**, so it cannot take the fire render as a motion control. Treat it as an alpha laboratory, not the Jerry animation path.

**Worth watching, not switching to yet:**

- **LTX-2.3 (Lightricks)** — 22B, considerably faster than Wan, with depth/canny/pose control delivered as an In-Context LoRA and video-to-video support. Its synchronized-audio feature is irrelevant here. If iteration speed becomes the bottleneck, this is the alternative to test, because generation speed is money on an hourly Pod.
- **HunyuanVideo 1.5 (Tencent)** — runs in less VRAM, but a thinner control ecosystem than Wan.

**On API models (Kling, Runway, Veo, Sora, Seedance, Luma).** They are more powerful and more coherent than anything open-weight, and they are the wrong tool for element generation. They return a finished baked frame: no alpha, no layer separation, no way to iterate a matte, and limited fidelity when following a specific CGI motion path. Their correct role in this project is motion and look reference, and temp previews for review — which is exactly what `docs/pipeline-strategy.md` already specifies and what the Higgsfield/Seedance tests under `workflows/higgsfield/` are for. Use them to answer "does this read as Jerry," not to produce a deliverable element.

Revisit this section if an API provider ships true alpha output or per-layer export.

## Before You Start: Restored Shot004 Media

The practice assignment uses these restored files:

- `assets/elements/by-shot/shot004_fire-jump/fire/shot004_fire-jump_ren-small-fire6_source_v001.mov` — 1920x1080, 24 fps, 87-frame fire render. Production filename copy: `ren_small_fire6..mov` in the same folder.
- `assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_control_832x448_81f_v001.mp4` — rebuilt 832x448, 24 fps, 81-frame control proxy.

Restored 2026-08-18 from `/Volumes/FW_Backup/Robs-Mac-Studio.local/Volumes/Rob's 4tb FAST/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6/Proxy/ren_small_fire6..mov`. The old `outputs/` proxy was never on the production drive; this copy is pad-to-fit so the fire is not cropped.

The plate and other Scene 4 passes are still only on the backup. Run official tutorials on their own sample footage until a Pod is needed.

## Recommended Learning Path

### 1. Learn Only the Necessary ComfyUI Fundamentals

Spend a couple of hours on the official guides:

- [First Generation](https://docs.comfy.org/get_started/first_generation)
- [Workflow Concepts](https://docs.comfy.org/development/core-concepts/workflow)
- [Inpainting and Masking](https://docs.comfy.org/tutorials/basic/inpaint)

The important concepts for this project are images versus masks, conditioning, model loaders, sampling, frame batches, and partial execution. An enormous generic beginner course is not necessary before starting video work.

### 2. Start with the Official Wan2.2 Fun Control Tutorial

The [official Wan2.2 Fun Control tutorial](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-control) is the most immediately relevant exercise. It covers using a starting reference image plus a control video derived from Canny, depth, pose, line structure, or trajectory information.

**Important: the tutorial does not use the same models as the Shot 004 workflow.** Expect the filenames to differ, and do not assume something is broken when they do.

| | Official tutorial | `shot004_jerry-wan22-funcontrol-element_v001.json` |
|---|---|---|
| Diffusion | `wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors` + `..._low_noise_...` | `wan2.2_ti2v_5B_fp16.safetensors` |
| VAE | `wan_2.1_vae.safetensors` | `wan2.2_vae.safetensors` |
| LoRAs | 2x `wan2.2_i2v_lightx2v_4steps_lora_v1_{high,low}_noise` | none |
| Text encoder | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | same |

Same node family, different weights: the tutorial uses the 14B Fun Control pair, the project workflow uses the 5B TI2V model. Running the tutorial unchanged means about four additional model downloads.

Run the official example first on its own sample material, then move to the project workflow.

**Done for learning, 2026-09-07.** Official sample, Lightning LoRA, and Jerry still + fire-jump control were all run on the 14B Fun Control graph. Findings: control video is structure, not a motion slider (Canny/full CGI fills the old body; a tiny centroid dot is too weak and idles; a fat streak is usable). There is no control-strength widget. Fine-tuning can wait; the next hands-on chapter is VACE, not more Fun Control seeds.

### 3. Learn the Speed Trick Early

The official tutorial benchmarks an RTX 4090 with 24 GB at 640x640 and 81 frames:

- Without acceleration: **~524 seconds** per run, ~89% VRAM.
- With the 4-step `lightx2v` LoRA: **~138 seconds** per run.

That is roughly 3.8x faster. On a $0.74/hour Pod it is the difference between about $0.11 and $0.03 per run, and more importantly it is the difference between iterating and waiting. Learn the LoRA setup before doing any exploratory work.

For reference, Shot 004 Run 001 took 358 seconds at 832x448 and 81 frames on Apple MPS. Use 81 frames as the default length: Wan expects `4n+1` stepping.

### 4. Work Through the Free Mickmumpitz VFX Workflow

Session handoff for a fresh chat: `docs/mickmumpitz-vfx-setup.md`.

**Current next step.** Companion YouTube (watch with the Pod off): [I Built a FREE VFX Pipeline with Local AI (2026 Masterclass)](https://www.youtube.com/watch?v=_n0ir5V5tX4) (~19 min). Written guide and free Simple graph: [Generate EPIC VFX Shots with AI](https://mickmumpitz.ai/posts/free-guide-epic-154092216).

It combines:

- A driving video
- A matching animated black-and-white mask
- Up to four reference images
- Text prompting
- VACE inpainting and control
- SkyReels reference-to-video conditioning

Start with its Simple graph at 576p. The full FP8 model targets roughly 24 GB of VRAM, which the current 4090 Pod has, so the lower-memory GGUF route it also documents should not be necessary.

The mask-plus-driving-video-plus-references combination here is the single closest public example to the Jerry problem. Study how the mask is authored.

### 5. Watch the Recent ActionVFX Reference-Frame Tutorial

ActionVFX's June 2026 tutorial, [Restyle Videos in ComfyUI with Wan 2.2](https://www.actionvfx.com/blog/restyle-videos-in-comfyui-with-wan-2-2) — YouTube: [Restyle Any Video in ComfyUI — Sky, Weather & Full Set Changes (Wan 2.2)](https://www.youtube.com/watch?v=pzbLO4dybIc) (~29 min). Watch for the VFX workflow: create one approved target frame, then propagate that treatment through the footage.

It also explains practical constraints such as keeping the source, reference frame, and generation dimensions synchronized. The video is free, but the downloadable graph and deeper object-insertion material are part of their paid course. Watch it for the technique rather than using it as the primary hands-on lesson.

### 6. Evaluate VACE as the Next Branch

The [ComfyUI VACE tutorial](https://docs.comfy.org/tutorials/video/wan/vace) covers Wan 2.1 VACE; community Wan 2.2 VACE workflows also exist.

VACE matters here because it accepts a control video and reference images **at the same time**, and adds masks and inpainting. That maps more directly onto "drive Jerry's motion from the fire render, hold his look from the bible references, and keep the plate intact" than Fun Control does.

Start with VACE-1.3B (~7 GB). Do not attempt VACE-14B (~32 GB) on a 24 GB card. Use `comfyui_controlnet_aux` for depth preprocessing.

### 7. Experiment with Wan-Alpha After Motion Control Works

The official [Wan-Alpha tutorial](https://docs.comfy.org/tutorials/video/wan/wan-alpha) generates RGB and alpha together and is designed for transparent, glowing, smoky, and particulate elements — highly relevant to fire.

Two constraints to plan around:

- It is **text-to-video only**, so it cannot follow the fire render's motion.
- It needs its own model set: a Wan 2.1 14B t2v checkpoint, two separate VAEs (`wan_alpha_2.1_vae_rgb_channel` and `wan_alpha_2.1_vae_alpha_channel`), and an RGBA LoRA. That is a substantial download.

Use it to learn what a clean generated alpha looks like, and as a source of unlinked fire elements. It is not the Jerry animation path.

### 8. Learn Matte Extraction, Because Alpha Is Not Free

This is the step most easily skipped and the one the pipeline actually depends on. `workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.md` records it directly: alpha is not native to the Fun Control path, and matte extraction is still required.

Since Wan-Alpha cannot take a control video, controlled Jerry motion will come out as RGB on a background. Learn to get a matte from it:

- Generate against pure black or a neutral background to make keying tractable.
- Luma keying for glow and fire, which is well suited to emissive elements.
- Background removal and segmentation nodes for the body.
- Where a matte is imperfect, decide whether to fix it in ComfyUI or hand a cleanup pass to Fusion/Resolve.

Judge every result by whether it mattes cleanly, not only by whether it looks good.

### 9. Add ControlNet and IPAdapter Conditioning

Both are named as next branches in the Shot 004 workflow notes and neither is installed yet.

- **ControlNet** (canny, depth, scribble) for tighter structural control than a raw control video gives.
- **IPAdapter** or equivalent reference conditioning for stronger Jerry identity than a single reference image provides.

Install the model files first and confirm the node types resolve through `/object_info` before building a graph around them.

### 10. Getting Elements Out to Comp

Generation is not the deliverable. The element has to land in Fusion/Resolve intact.

- Prefer image sequences (PNG or EXR) over MP4 for anything carrying alpha. H.264 has no alpha channel, which is why the Run 001 output needed keying.
- Keep generation dimensions and frame rate aligned with the plate, and record any mismatch.
- Note the colour space assumption rather than discovering it during the comp.
- Promote anything worth keeping out of `outputs/` into `assets/` under a `_vNNN` name. `outputs/` is ephemeral and the Shot 004 review artifacts have already been lost to this once.

## One Non-ComfyUI Case Study Worth Watching

Beeble's June 24, 2026 tutorial, [Add Realistic Fire VFX While Preserving Original Footage](https://beeble.ai/blog/canvas-tutorial-fire-vfx), addresses almost the exact creative problem: introducing fire into live footage, protecting the actor and environment with masks, generating a target fire look, and creating believable interactive illumination.

It uses Beeble Canvas rather than ComfyUI, and running the supplied project consumes paid credits. Nevertheless, the free walkthrough is useful for understanding how Jerry, the matte, environmental relighting, and the final grade should be separated conceptually.

## Best First Practice Assignment

1. Run the official Fun Control example unchanged, on its own sample footage. **Done 2026-09-07.**
2. Add the 4-step LoRA and confirm the speed difference for yourself. **Done.**
3. Restore the Scene 4 fire render and rebuild the 832x448 control proxy. **Done 2026-08-18** — source, pad-to-fit proxy, trajectory-dot, streak, and 40%-shrunk controls live in `assets/elements/by-shot/shot004_fire-jump/fire/`.
4. Load the existing Jerry workflow. **Deferred.** Jerry tests used the official 14B Fun Control template with `JB-001` + fire control, not the Shot 004 5B JSON. Revisit that JSON after VACE if Fun Control is still in the kit.
5. Fix the proxy's cropping by padding and scaling the control element. **Done** (pad-to-fit proxy).
6. Test only 17-33 frames while adjusting control strength and reference conditioning. **Done for learning.** Fun Control has no strength slider; path vs body is authored in the control movie (streak usable, full CGI too much shape, tiny dot too weak).
7. Generate Jerry against a controlled dark or neutral background. **Started** — dark-bg 14B runs exist on the volume. Not a hero take.
8. Extract a matte and composite it over the untouched plate. **Not started** — after VACE / a path-following body.
9. Only after Jerry works, add grass ignition, contact glow, smoke, and scorch as separate branches.

**Next:** Superhero Simple — plate as driving (`060_Superhero_PLATE.mp4`) to kill the 180° flip. Details in `docs/mickmumpitz-vfx-setup.md`.

This provides a real ComfyUI learning exercise while advancing the actual shot. It also avoids spending cloud GPU time on generic text-to-video experiments that do not teach the controls this project needs.

Record durable findings in `docs/findings.md` and run detail in the relevant workflow or shot note.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-08-02 | Initial ComfyUI VFX Learning Path. |
| 2.0     | 2026-08-16 | Archived v1.0 and expanded for the RunPod execution environment: added Pod/cost guidance, a model-family comparison covering VACE, LTX-2.3, and API models, the Fun Control model mismatch, the 4-step LoRA speed benchmark, matte extraction, ControlNet/IPAdapter, comp hand-off, and the media that must be restored first. |
| 2.1     | 2026-08-18 | Recorded the restored shot004 fire source and rebuilt 832x448 control proxy. |
| 2.2     | 2026-08-30 | Noted Fun Control tutorial models on the volume (run not queued) and the Illinois GPU fallback. |
| 2.3     | 2026-09-07 | Marked Fun Control complete for learning; recorded path-vs-body control findings; pointed next work at Mickmumpitz YouTube + VACE; added ActionVFX YouTube URL. |
| 2.4     | 2026-09-07 | Pointed at `docs/mickmumpitz-vfx-setup.md` for a clean session handoff. |
| 2.5     | 2026-09-18 | Superhero VACE: suit works, pose-drive 180° flip; next is plate as driving. |
| 2.6     | 2026-10-08 | Retired the completed learning syllabus after its Illinois/Mickmumpitz next steps became obsolete; active shot review lives in the shot004 plan. |
