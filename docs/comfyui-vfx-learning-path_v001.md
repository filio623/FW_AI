# ComfyUI VFX Learning Path v001

Date: 2026-08-02

## Project Goal

This is not simply a workflow for generating a video of fire. It is a controlled VFX pipeline:

- Use the existing CGI fire animation to control Jerry's timing, path, and silhouette.
- Use approved images to maintain Jerry's appearance.
- Generate Jerry as a separate element without damaging the live-action plate.
- Produce or extract a matte.
- Handle glow, grass ignition, smoke, scorch, occlusion, and other interactions as separate passes.
- Composite everything in Fusion/Resolve.

This matches the approach already documented in:

- `docs/comfyui-vfx-workflow-strategy_v001.md`
- `shots/shot004_fire-jump_workflow-test-plan_v001.md`

## Recommended Learning Path

### 1. Learn Only the Necessary ComfyUI Fundamentals

Spend a couple of hours on the official guides:

- [First Generation](https://docs.comfy.org/get_started/first_generation)
- [Workflow Concepts](https://docs.comfy.org/development/core-concepts/workflow)
- [Inpainting and Masking](https://docs.comfy.org/tutorials/basic/inpaint)

The important concepts for this project are images versus masks, conditioning, model loaders, sampling, frame batches, and partial execution. An enormous generic beginner course is not necessary before starting video work.

### 2. Start with the Official Wan2.2 Fun Control Tutorial

The [official Wan2.2 Fun Control tutorial](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-control) is the most immediately relevant exercise. It includes a downloadable workflow and practice material. It covers using a starting reference image plus a control video derived from Canny, depth, pose, line structure, or trajectory information.

It directly corresponds to the existing workflow:

- `workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.json`

That workflow has already run successfully. Its remaining problems are cropping, weak motion adherence, and lack of native alpha, rather than basic technical viability.

Run the official example unchanged first. Then substitute the Jerry reference and prepared fire proxy.

### 3. Work Through the Free Mickmumpitz VFX Workflow

The March 2026 guide [Generate EPIC VFX Shots with AI](https://mickmumpitz.ai/posts/free-guide-epic-154092216) is one of the closest complete free tutorials to the intended Jerry workflow.

It combines:

- A driving video
- A matching animated black-and-white mask
- Up to four reference images
- Text prompting
- VACE inpainting and control
- SkyReels reference-to-video conditioning

Start with its Simple graph at 576p. The full FP8 model is intended for approximately 24 GB or more of VRAM; it also provides a lower-memory GGUF route.

### 4. Watch the Recent ActionVFX Reference-Frame Tutorial

ActionVFX's June 12, 2026 tutorial, [Restyle Videos in ComfyUI with Wan 2.2](https://www.actionvfx.com/blog/restyle-videos-in-comfyui-with-wan-2-2), is valuable for understanding the VFX workflow: create one approved target frame, then propagate that treatment through the footage.

It also explains practical constraints such as keeping the source, reference frame, and generation dimensions synchronized. The video is free, but the downloadable graph and deeper object-insertion material are part of their paid course. Watch it for the technique rather than using it as the primary hands-on lesson.

### 5. Experiment with Wan-Alpha After Motion Control Works

The official [Wan-Alpha tutorial](https://docs.comfy.org/tutorials/video/wan/wan-alpha) generates RGB and alpha together and is specifically designed for transparent, glowing, smoky, and particulate elements.

That makes it highly relevant to fire, but it is text-to-video rather than proxy-controlled video. Treat it as an alpha/matte laboratory, not as the main Jerry-animation workflow.

## One Non-ComfyUI Case Study Worth Watching

Beeble's June 24, 2026 tutorial, [Add Realistic Fire VFX While Preserving Original Footage](https://beeble.ai/blog/canvas-tutorial-fire-vfx), addresses almost the exact creative problem: introducing fire into live footage, protecting the actor and environment with masks, generating a target fire look, and creating believable interactive illumination.

It uses Beeble Canvas rather than ComfyUI, and running the supplied project consumes paid credits. Nevertheless, the free walkthrough is useful for understanding how Jerry, the matte, environmental relighting, and the final grade should be separated conceptually.

## Best First Practice Assignment

1. Run the official Fun Control example unchanged.
2. Load the existing Jerry workflow.
3. Fix the proxy's cropping by padding and scaling the control element.
4. Test only 17-33 frames while adjusting control strength and reference conditioning.
5. Generate Jerry against a controlled dark or neutral background.
6. Build a rough matte and composite it over the untouched plate.
7. Only after Jerry works, add grass ignition, contact glow, smoke, and scorch as separate branches.

This provides a real ComfyUI learning exercise while advancing the actual shot. It also avoids spending cloud GPU time on generic text-to-video experiments that do not teach the controls this project needs.
