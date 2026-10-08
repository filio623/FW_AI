**Created:** 2026-05-27
**Modified:** 2026-10-08
**Version:** 1.2

# Comfy Cloud MCP

## Current Status

Comfy Cloud MCP is a remote MCP server hosted at:

`https://cloud.comfy.org/mcp`

As of 2026-05-27, this account's API key works against the regular Comfy Cloud API, but the MCP endpoint returns a 403 saying MCP is not yet available for the account.

The local launcher is:

`scripts/comfy-cloud-mcp.sh`

It reads `.env` and starts the remote MCP bridge through `mcp-remote` using:

- URL: `https://cloud.comfy.org/mcp`
- Auth header: `X-API-Key: <COMFY_API_KEY>`

## Requirements

Per the Comfy Cloud MCP repository:

- Active Comfy Cloud subscription, required to submit workflows.
- Comfy API key from `https://platform.comfy.org/profile/api-keys`.
- API key starts with `comfyui-`.
- Email/account enabled for the closed beta.

## API Fallback

The regular Comfy Cloud API can be used without MCP:

- Base URL: `https://cloud.comfy.org`
- Auth header: `X-API-Key: <COMFY_API_KEY>`
- Account check: `GET /api/user`
- Workflow submission: `POST /api/prompt`

The key currently returns `{"status":"active"}` from `/api/user`.

Official `comfy-cli` is another option for direct partner-node generation through `comfy generate`, using the same `COMFY_API_KEY`.

## Local Tools

The `.venv-comfy-cli/` environment and `comfy` executable are not installed in this checkout as of 2026-10-08. `scripts/comfy-cloud-cli.sh` requires an installed CLI and the API key in `.env`; the direct `scripts/comfy-cloud-api.py` fallback does not require the CLI. The old `.venv/` and `.uv-cache/` directories are also absent here. Create a Python virtual environment before using the wrapper.

Use the repo wrapper for the official CLI:

```bash
scripts/comfy-cloud-cli.sh generate list
scripts/comfy-cloud-cli.sh generate schema flux-pro
scripts/comfy-cloud-cli.sh generate flux-pro --prompt "a cinematic fire spirit" --download outputs/test.png
```

Use the direct API helper for full workflow JSON execution and account checks:

```bash
scripts/comfy-cloud-api.py user
scripts/comfy-cloud-api.py system-stats
scripts/comfy-cloud-api.py submit workflows/comfyui/your_api_workflow.json
```

Use `comfy-cli` for partner-node one-shots and simple model-specific jobs. Use direct Cloud API calls for saved ComfyUI API-format workflows, job polling, queue/history checks, and output retrieval.

## Recommended Codex MCP Setup

Add this to `~/.codex/config.toml`:

```toml
[mcp_servers.comfy_cloud]
command = "/Users/jamesfilios/Software_Projects/FW_AI/scripts/comfy-cloud-mcp.sh"
startup_timeout_sec = 30
tool_timeout_sec = 60
```

Restart Codex after changing MCP config.

## Local Secret

Add this to `.env`:

```bash
COMFY_API_KEY=comfyui_your_key_here
```

Do not commit `.env`.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-27 | Initial Comfy Cloud MCP. |
| 1.1     | 2026-08-16 | Replaced stale `/Users/robbiefilios/Documents/FW_AI_Workflow` paths with repo-relative paths and the current workspace root. |
| 1.2     | 2026-10-08 | Corrected the local `comfy-cli`/virtual-environment inventory; keep the direct API as the installed-free fallback. |
