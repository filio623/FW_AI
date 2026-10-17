# MCP Notes

## Current Status

- No local ComfyUI installation or ComfyUI MCP is assumed on this machine; use a running Pod's API as documented in `runpod.md`.
- Comfy Cloud MCP returns a 403 rollout response for this account; the direct API remains the fallback in `comfy-cloud.md`.
- RunPod Pod management and remote ComfyUI setup are documented in `runpod.md`.
- Higgsfield CLI 1.1.26 is installed and authenticated, but the trial account generates only through the official MCP server (`.omp/mcp.json`); see `higgsfield.md`.
- Official Blender Lab MCP server and add-on 1.0.3 are installed for Blender 5.2.1 and defined as the `blender` stdio server in `.omp/mcp.json`; see `blender.md`.
- Supermemory was retired on 2026-08-16 and moved to `docs/archive/mcp/supermemory.md`.

## Goal

Use MCP where it gives agents reliable tool access without re-discovering commands each session.

## ComfyUI MCP

Track practical usage in `comfyui.md`.

## Comfy Cloud MCP

Track remote Comfy Cloud setup in `comfy-cloud.md`.

## RunPod MCP

Track RunPod Pod management, authentication, and remote ComfyUI API usage in `runpod.md`.

## Higgsfield MCP

The official hosted server is `https://mcp.higgsfield.ai/mcp`, defined for OMP in `.omp/mcp.json`. Track auth steps, CLI behavior, and trial limits in `higgsfield.md`.

## Blender MCP

The official Blender Lab server (`blender-mcp`) bridges to an add-on inside a running Blender on `localhost:9876`. It runs model-written Python without guards. Track install, upgrade, and tool behavior in `blender.md`.

## Supermemory MCP (retired)

Retired on 2026-08-16 and moved to `docs/archive/mcp/supermemory.md`. The
repository is the source of truth for project memory.
