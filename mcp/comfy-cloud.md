**Created:** 2026-05-27
**Updated:** 2026-11-04

# Comfy Cloud

## Current Status (as of 2026-11-04): parked

- **Comfy Cloud MCP** (`https://cloud.comfy.org/mcp`): returns a 403, MCP not available for this account (since 2026-05-27). Its launcher script was removed on 2026-11-04.
- **Comfy Cloud API:** the account key returns `{"status":"active"}` from `/api/user`. `scripts/comfy-cloud-api.py user | system-stats | submit <api-workflow.json>` uses it.
- **What we use instead:** the partner API nodes (Seedance, Kling, …) inside the Pod's ComfyUI, billed to the same Comfy account (`shots/shot004_fire-jump/pass-b_grassfire_log.md`).
- The official `comfy-cli` is not installed; its wrapper script was removed on 2026-11-04.

## API

- Base URL `https://cloud.comfy.org`, header `X-API-Key: <COMFY_API_KEY>`.
- Account check `GET /api/user`; workflow submission `POST /api/prompt`.
- The key lives only in `.env` (`COMFY_API_KEY=…`); never copy it into commands, docs or commits.
- On this Mac, the system `python3` fails the Cloud API's TLS check (`CERTIFICATE_VERIFY_FAILED`, 2026-11-03); fix the Python certificates before relying on the helper.

## Requirements (from the Comfy Cloud MCP repository)

Active Comfy Cloud subscription; API key from `https://platform.comfy.org/profile/api-keys`; MCP needs the account enabled for the closed beta.
