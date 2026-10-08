# MCP Notes

## Current Status

- No local ComfyUI installation or ComfyUI MCP is assumed on this machine; use a running Pod's API as documented in `runpod.md`.
- Comfy Cloud MCP returns a 403 rollout response for this account; the direct API remains the fallback in `comfy-cloud.md`.
- RunPod Pod management and remote ComfyUI setup are documented in `runpod.md`.
- The Higgsfield CLI is not installed on this machine; see `higgsfield.md` and `docs/environment.md` before planning an authenticated run.
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

Track CLI behavior and possible MCP server design in `higgsfield.md`. If an official or community Higgsfield MCP server is identified, document install steps and config here before enabling it.

## Supermemory MCP (retired)

Retired on 2026-08-16 and moved to `docs/archive/mcp/supermemory.md`. The
repository is the source of truth for project memory.
