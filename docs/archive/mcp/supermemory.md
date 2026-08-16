**Created:** 2026-05-18
**Modified:** 2026-08-16
**Version:** 1.2
**Archived:** 2026-08-16
**Original path:** `mcp/supermemory.md`

# [ARCHIVED] Supermemory MCP

> **Retired 2026-08-16.** Supermemory is no longer used by this project. The repository
> is the single source of truth for project memory; see the `Document Lifecycle & Versioning`
> section of `AGENTS.md`.
>
> Before retirement the account was exported and reviewed. It held 56 documents, of which
> only two concerned this project — both LLM summaries of the same 2026-08-02 session, and
> both stale on RunPod details that `mcp/runpod.md` records correctly. The two durable facts
> worth keeping (the $5 network-volume credit minimum and the data-center volume-support
> constraint) were merged into `mcp/runpod.md` v1.1.
>
> The launcher, upload script, and Codex MCP installer were deleted. This file is kept as a
> record of the setup that existed.


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
command = "/Users/jamesfilios/Software_Projects/FW_AI/scripts/supermemory-mcp.sh"
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

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Supermemory MCP. |
| 1.1     | 2026-08-16 | Replaced stale `/Users/robbiefilios/Documents/FW_AI_Workflow` paths with repo-relative paths and the current workspace root. |
| 1.2     | 2026-08-16 | Retired. Supermemory removed from the project after export; the repository is the source of truth for project memory. |
