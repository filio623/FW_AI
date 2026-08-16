**Created:** 2026-05-18
**Modified:** 2026-05-18
**Version:** 1.1
**Archived:** 2026-08-16
**Original path:** `skills/supermemory-vfx/references/api-notes.md`

# [ARCHIVED] Supermemory API Notes

> **Retired 2026-08-16** with `skills/supermemory-vfx/SKILL.md`. Kept as a record only.


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

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Supermemory API Notes. |
| 1.1     | 2026-08-16 | Retired with the Supermemory skill. |
