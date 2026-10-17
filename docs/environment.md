**Created:** 2026-05-17
**Modified:** 2026-10-17
**Version:** 2.7

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

Saved graphs live in `workflows/comfyui/`; the current split shot004 VACE workflow and its non-Git media dependencies are indexed in `shots/shot004_fire-jump_workflow-test-plan_v001.md` and `mcp/runpod.md`.

## RunPod

Provisioned and authenticated. `mcp/runpod.md` is the authoritative record of Pod state, template IDs, network volumes, GPU selection, and the current resume point — do not duplicate those values here.

Summary: the official Codex plugin, RunPod documentation MCP, `runpodctl`, and `flash` are installed, and a persistent network volume backs `/workspace` so models and custom nodes survive Pod replacement.

## Higgsfield

Verified 2026-10-11: `higgsfield` CLI 1.1.26 is installed globally through npm (`~/.nvm/versions/node/v24.21.0/bin/higgsfield`) and authenticated as `jamesfilios@gmail.com`, plan `plus` (trial), 110 credits.

The trial blocks generation through the CLI/API (`only_mcp_usage_on_trial_is_available`); catalog, cost, and upload commands still work. Generation goes through the official MCP server configured in `.omp/mcp.json`. Setup and auth steps live in `mcp/higgsfield.md`.

Re-check cloud model availability, parameters, and credits before expensive generations.

## Comfy Cloud

`COMFY_API_KEY` in `.env` is required. Two access paths:

- `scripts/comfy-cloud-api.py` — standard library only, works as soon as the key is set.
- `scripts/comfy-cloud-cli.sh` — additionally needs the `comfy` CLI at `.venv-comfy-cli/bin/comfy`, which is **not installed here**. The install command is in the script's error message.

MCP is configured but the account still receives a 403 rollout message; see `mcp/comfy-cloud.md`.

## Blender

Blender 5.2.1 LTS is at `/Applications/Blender.app`. The official Blender Lab MCP add-on and server, both 1.0.3, are installed, and OMP connects through the `blender` entry in `.omp/mcp.json`. The server runs model-written Python without guards. Setup, upgrade, and tool notes are in `mcp/blender.md`.

## Project Memory

The repository is the source of truth. There is no external memory service.

Supermemory was retired on 2026-08-16 and its key, scripts, and MCP launcher were removed. The record of that setup is kept at `docs/archive/mcp/supermemory.md`.

## FFmpeg

- Installed with Homebrew. Reinstalled 2026-08-18 after the previous binary was missing from `PATH`.
- Version observed: `ffmpeg 9.0.1`; `ffprobe` available at `/opt/homebrew/bin/ffmpeg`.
- Use for video metadata inspection, reference-frame extraction, proxy creation, alpha checks, transcoding, and thumbnail generation.

## Production Media

Bulk production media is not in this repository. The original inventory path is `/Volumes/Rob's 4tb FAST FW`. The copy currently mounted is the NAS backup `/Volumes/FW_Backup/Robs-Mac-Studio.local/Volumes/Rob's 4tb FAST`. Indexed by the manifests in `references/manifests/`.

The original `FW_test/` working folder is not present in this checkout. `outputs/` is ephemeral. The shot004 fire source and control proxy were restored under `assets/elements/by-shot/shot004_fire-jump/fire/`; a separate Scene 4 test reference MP4 and 49-frame proxy are indexed under `assets/elements/by-shot/shot004_fire-jump/plates/`. The original `4 base plate.mov` has not been restored here.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-17 | Initial Environment. |
| 2.0     | 2026-08-16 | Archived v1.0 and rewrote for the current machine: removed local ComfyUI paths that no longer resolve, delegated RunPod detail to `mcp/runpod.md`, and recorded external-drive and media availability. |
| 2.1     | 2026-08-16 | Corrected the Higgsfield CLI status to not-installed after verifying `PATH`, and recorded Comfy Cloud access paths and their prerequisites. |
| 2.2     | 2026-08-16 | Replaced the Supermemory section with a Project Memory note after Supermemory was retired. |
| 2.3     | 2026-08-16 | Repointed the Supermemory record at its new archive path. |
| 2.4     | 2026-08-18 | Recorded the reinstalled `ffmpeg 9.0.1`, the `/Volumes/FW_Backup` restore copy, and the restored shot004 fire media. |
| 2.5     | 2026-10-08 | Linked the current split VACE shot record and clarified staged Scene 4 reference media versus the unrestored original base plate. |
| 2.6     | 2026-10-11 | Replaced the stale previous-machine Higgsfield notes with the verified CLI install, trial account, and MCP-only generation path. |
| 2.7     | 2026-10-17 | Recorded Blender 5.2.1 and the official Blender Lab MCP add-on and server setup. |
