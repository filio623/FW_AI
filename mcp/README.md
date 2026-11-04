# MCP And Service Notes

One note per external service; each says what works today.

- `runpod.md`: GPU Pods for ComfyUI: current setup, start/stop, state. History in the append-only `runpod_log.md`. Codex reaches the RunPod MCP through `scripts/runpod-mcp.sh`.
- `blender.md`: the Blender Lab MCP server and add-on 1.0.3 for Blender 5.2.1 (`blender` in `.omp/mcp.json`). It runs model-written Python without guards.
- `higgsfield.md`: Higgsfield through its hosted MCP (`https://mcp.higgsfield.ai/mcp`, `.omp/mcp.json`); the trial blocks CLI generation.
- `comfy-cloud.md`: parked (MCP 403); partner API nodes run inside the Pod's ComfyUI instead.
- `comfyui.md`: no local ComfyUI; use a Pod's API.

Supermemory was retired on 2026-08-16 (`docs/archive/mcp/supermemory.md`).
