# Supermemory MCP

## Current Status

The workspace has a local `.env` containing:

- `SUPERMEMORY_API_KEY`
- `SUPERMEMORY_CONTAINER_TAG`
- `SUPERMEMORY_PROJECT`

The key is intentionally not copied into docs or committed files. `.gitignore` excludes `.env`.

## Recommended Codex MCP Setup

Use the local launcher:

`scripts/supermemory-mcp.sh`

It reads `.env` and starts Supermemory MCP through `mcp-remote`:

- URL: `https://mcp.supermemory.ai/mcp`
- Auth header: `Authorization: Bearer <SUPERMEMORY_API_KEY>`
- Project scope header: `x-sm-project: ai-video-workflows`

Add this to `~/.codex/config.toml`:

```toml
[mcp_servers.supermemory]
command = "/Users/robbiefilios/Documents/FW_AI_Workflow/scripts/supermemory-mcp.sh"
startup_timeout_sec = 30
tool_timeout_sec = 60
```

Restart Codex after changing MCP config.

The connection was tested successfully with `mcp-remote-client`, but that diagnostic client echoed resolved headers. Do not keep a reusable test script that prints auth headers; verify normal operation through Codex after restart instead.

## Tools Expected From Supermemory

Per current Supermemory docs:

- `memory`: save or forget memory content.
- `recall`: search memories and optionally include profile context.
- `whoAmI`: return current account/session information.

## Project Usage

Use `ai-video-workflows` as the project/container scope for this film workspace unless a shot-specific or user-specific scope is needed.
