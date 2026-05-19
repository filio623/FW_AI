# Supermemory API Notes

## Current Endpoints

Use `POST https://api.supermemory.ai/v3/documents` to add text, URLs, or other content as a document.

Required header:

- `Authorization: Bearer <SUPERMEMORY_API_KEY>`

Useful JSON fields:

- `content`
- `containerTag`
- `customId`
- `metadata`
- `taskType`
- `entityContext`

Use `containerTag=ai-video-workflows` for this project.

## MCP

Supermemory MCP is configured through `scripts/supermemory-mcp.sh` and documented in `mcp/supermemory.md`.

Expected MCP tools:

- `memory`
- `recall`
- `whoAmI`
