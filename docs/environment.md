**Created:** 2026-05-17
**Modified:** 2026-08-16
**Version:** 2.3

# Environment

Setup notes for the machine this repository is currently checked out on. Anything describing a remote or hosted service is summarized here and owned in detail by the matching file in `mcp/`.

Secrets live in the ignored `.env`; only `.env.example` is committed.

## Local Machine

- macOS, Apple Silicon with the MPS backend.
- Workspace: `/Users/jamesfilios/Software_Projects/FW_AI`.

## ComfyUI

Local ComfyUI is not installed in this checkout. The local install described in `docs/archive/environment-v1.0.md` belonged to a different machine, and none of its paths resolve here.

Current options for running workflows, in order of preference:

- **RunPod GPU Pod** — the intended path for Wan 2.2 and other heavy graphs. See `mcp/runpod.md`.
- **Comfy Cloud** — hosted partner nodes and one-shot jobs. See `mcp/comfy-cloud.md` and the `comfy-cloud-vfx` skill.
- **Local install** — if one is set up again, record its ComfyUI root, `models/`, `input/`, `output/`, and `user/` paths here and update `mcp/comfyui.md`.

Saved workflows live in `workflows/comfyui/`. The Shot 004 graph expects model files and video inputs that are not tracked in Git; its workflow note lists them.

## RunPod

Provisioned and authenticated. `mcp/runpod.md` is the authoritative record of Pod state, template IDs, network volumes, GPU selection, and the current resume point — do not duplicate those values here.

Summary: the official Codex plugin, RunPod documentation MCP, `runpodctl`, and `flash` are installed, and a persistent network volume backs `/workspace` so models and custom nodes survive Pod replacement.

## Higgsfield

The `higgsfield` CLI is **not installed on this machine** — it is not on `PATH`. It must be installed and authenticated before any Higgsfield workflow or run log can be reproduced.

Observations below are from the previous machine and are unverified here:

- CLI version previously observed: `higgsfield 0.1.40`.
- Account previously observed: `robfilios@gmail.com`, plan `ultra`.
- Credits previously observed: `385.45`.

Re-check cloud model availability, parameters, and credits before expensive generations. Setup detail lives in `mcp/higgsfield.md`.

## Comfy Cloud

`COMFY_API_KEY` in `.env` is required. Two access paths:

- `scripts/comfy-cloud-api.py` — standard library only, works as soon as the key is set.
- `scripts/comfy-cloud-cli.sh` — additionally needs the `comfy` CLI at `.venv-comfy-cli/bin/comfy`, which is **not installed here**. The install command is in the script's error message.

MCP is configured but the account still receives a 403 rollout message; see `mcp/comfy-cloud.md`.

## Project Memory

The repository is the source of truth. There is no external memory service.

Supermemory was retired on 2026-08-16 and its key, scripts, and MCP launcher were removed. The record of that setup is kept at `docs/archive/mcp/supermemory.md`.

## FFmpeg

- Installed with Homebrew on 2026-05-18.
- Version observed: `ffmpeg 8.1.1`; `ffprobe` available.
- Use for video metadata inspection, reference-frame extraction, proxy creation, alpha checks, transcoding, and thumbnail generation.

## Production Media

Bulk production media is not in this repository. It lives on the external production drive `/Volumes/Rob's 4tb FAST FW`, indexed by the manifests in `references/manifests/`. The drive is not mounted by default, so check before assuming a source path resolves.

The `FW_test/` working folder described in earlier notes is not present in this checkout. `outputs/` is ephemeral and is created on demand.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-17 | Initial Environment. |
| 2.0     | 2026-08-16 | Archived v1.0 and rewrote for the current machine: removed local ComfyUI paths that no longer resolve, delegated RunPod detail to `mcp/runpod.md`, and recorded external-drive and media availability. |
| 2.1     | 2026-08-16 | Corrected the Higgsfield CLI status to not-installed after verifying `PATH`, and recorded Comfy Cloud access paths and their prerequisites. |
| 2.2     | 2026-08-16 | Replaced the Supermemory section with a Project Memory note after Supermemory was retired. |
| 2.3     | 2026-08-16 | Repointed the Supermemory record at its new archive path. |
