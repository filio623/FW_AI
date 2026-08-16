**Created:** 2026-05-18
**Modified:** 2026-05-18
**Version:** 1.0

# ComfyUI MCP

## Available Capabilities

The current session exposes ComfyUI MCP tools for:

- Listing models and workflows.
- Loading, analyzing, modifying, validating, and saving workflows.
- Enqueueing workflows.
- Checking queue, job status, history, logs, and output images.
- Managing VRAM and ComfyUI process state.

## Usage Rule

Prefer MCP for ComfyUI operations instead of manual API calls when the tool exists. It returns structured workflow and execution information that is easier for agents to reason about.

## Project Workflow Storage

Keep durable project copies in `workflows/comfyui/`, even when a workflow is also saved to the ComfyUI user library.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial ComfyUI MCP. |
