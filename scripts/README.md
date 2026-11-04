# Scripts

Project automation. Python is standard-library-first; the media builders need `/usr/local/bin/python3` (numpy, OpenCV). Each builder writes a JSON report of its settings next to its outputs.

Shot-only scripts live in their shot folder (shot 004: `shots/shot004_fire-jump/scripts/`, README there). This folder holds shared tools.

## Characters and library

- `build_jerry_training_candidates.py`: source-derived Jerry candidate stills.
- `mickmumpitz-library.py`: sorts Mickmumpitz Patreon downloads into `library/mickmumpitz/` and writes its index.

## Services

- RunPod: `runpod-pod-up.sh` (create a Pod on the EU-RO-1 volume and record its ID), `runpod-pod-down.sh` (terminate it; always run by hand), `runpod-with-auth.sh` (run a RunPod CLI command with `.env` auth), `runpod-comfy-api.sh` (upload and submit to the Pod's ComfyUI). Details: `mcp/runpod.md`.
- `runpod/setup_mick13_volume.sh`: rebuilds the Mick 1.3 + VACE × SkyReels stack on a fresh network volume (`all|nodes|patch|models`).
- Comfy Cloud (parked): `comfy-cloud-api.py` (`user`, `system-stats`, `submit`). Details: `mcp/comfy-cloud.md`.
- `runpod-mcp.sh`: launches the RunPod MCP for Codex (`~/.codex/config.toml`).

Removed 2026-11-04 (unused): `comfy-cloud-cli.sh`, `comfy-cloud-mcp.sh`, `update-codex-comfy-cloud-mcp.py`, `update-codex-runpod-mcp.py`; they are in Git history.

## Blender

Run with `/Applications/Blender.app/Contents/MacOS/Blender -b …` (usage at the top of each file).

- `blender/comp_tap.py`: renders one compositor node's output, for checking a node tree.
- `blender/jerry_fire_rig_build.py`, `blender/fluid_bake.py`, `blender/render_frames.py`: Jerry fire rig build, Mantaflow rebake, and Metal render.
- `blender/mcp_call.py`: calls the Blender MCP server from a shell.
