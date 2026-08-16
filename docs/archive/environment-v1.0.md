**Created:** 2026-05-17
**Modified:** 2026-05-17
**Version:** 1.0
**Archived:** 2026-08-16

# [ARCHIVED] Environment

Date started: 2026-05-17

## Local Machine

- macOS.
- Apple MPS backend.
- Workspace: `/Users/robbiefilios/Documents/FW_AI_Workflow`

## ComfyUI

- URL: `http://127.0.0.1:8000`
- Version previously observed: `0.21.1`
- Base models directory: `/Users/robbiefilios/Documents/ComfyUI/models`
- Input directory: `/Users/robbiefilios/Documents/ComfyUI/input`
- Output directory: `/Users/robbiefilios/Documents/ComfyUI/output`
- User library: `/Users/robbiefilios/Documents/ComfyUI/user`

These paths describe the previously observed local setup and do not match the
current cloned workspace at `/Users/jamesfilios/Software_Projects/FW_AI`.

## RunPod

- RunPod setup reconstructed on 2026-08-02 and provisioned on 2026-08-03.
- Official Codex plugin, RunPod documentation MCP, `runpodctl`, and `flash` are installed.
- Durable setup and remote ComfyUI instructions: `mcp/runpod.md`.
- Persistent storage: 100 GB `fw-ai-comfyui` network volume in `US-IL-1`,
  mounted at `/workspace` when a Pod is created.
- Recommended starter: official CUDA 12.8 ComfyUI template on a Secure Cloud
  RTX A5000 with only `8188/http` and `22/tcp` exposed.
- No Pod is currently running; the Illinois A5000 pool was supply-constrained
  during the latest launch attempts.

## Higgsfield

- CLI installed and authenticated.
- CLI version previously observed: `higgsfield 0.1.40`
- Account previously observed: `robfilios@gmail.com`
- Plan previously observed: `ultra`
- Credits previously observed: `385.45`

Re-check cloud model availability, parameters, and credits before expensive generations.

## Supermemory

- Local `.env` contains `SUPERMEMORY_API_KEY`.
- Default project/container scope: `ai-video-workflows`.
- MCP notes: `mcp/supermemory.md`.

## FFmpeg

- Installed with Homebrew on 2026-05-18.
- Version observed: `ffmpeg 8.1.1`.
- `ffprobe` is available.
- Use for video metadata inspection, reference frame extraction, proxy creation, alpha checks, transcoding, and thumbnail generation.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-17 | Initial Environment. |
