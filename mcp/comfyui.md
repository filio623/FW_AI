**Created:** 2026-05-18
**Updated:** 2026-10-08

# ComfyUI MCP

## Current Availability

There is no local ComfyUI installation or ComfyUI MCP connection on this machine. When a future session exposes a ComfyUI MCP server, its available tools may support:

- Listing models and workflows.
- Loading, analyzing, modifying, validating, and saving workflows.
- Enqueueing workflows.
- Checking queue, job status, history, logs, and output images.
- Managing VRAM and ComfyUI process state.

## Usage Rule

Use MCP when it is actually configured. For the current RunPod-hosted workflow, use the visual ComfyUI canvas or `scripts/runpod-comfy-api.sh` after a Pod is started and its ID is recorded; see `mcp/runpod.md`.

## Project Workflow Storage

Keep durable project copies in `workflows/comfyui/`, even when a workflow is also saved to the ComfyUI user library.
