---
name: supermemory-vfx
description: "RETIRED 2026-08-16 — do not use. Supermemory is no longer part of this project and its scripts have been deleted. Durable project memory lives in the repository; see AGENTS.md."
---

**Created:** 2026-05-18
**Modified:** 2026-08-16
**Version:** 1.2
**Archived:** 2026-08-16
**Original path:** `skills/supermemory-vfx/SKILL.md`

# [ARCHIVED] Supermemory VFX

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


## Core Rule

Use Supermemory for durable project memory that should survive Codex session refreshes. Do not store secrets, raw API keys, private credentials, or large binary assets as memories.

## Project Defaults

- Container tag: `ai-video-workflows`
- Project header: `ai-video-workflows`
- Project root: `/Users/jamesfilios/Software_Projects/FW_AI`
- Local env file: `.env`
- MCP notes: `mcp/supermemory.md`
- Seed memories: `memories/seeds/`
- API responses: `memories/responses/`

## Workflow

1. Prefer the Supermemory MCP tools after Codex has been restarted with the configured MCP server.
2. Before MCP is available, use `scripts/supermemory_add_document.py`.
3. Save concise, factual, reusable context. Avoid noisy transcripts.
4. Use stable `customId` values so memories can be updated or deduplicated later.
5. Add metadata for filtering: `source`, `type`, `project`, `date`, and `tool`.
6. Keep a local copy of any important seeded memory under `memories/seeds/`.

## What To Remember

Save:

- Project goals and durable constraints.
- User preferences about workflow direction.
- Model/tool findings that took time to discover.
- Working prompts, command patterns, and workflow recipes.
- Shot-specific decisions and review notes.
- Setup details that future agents need.

Do not save:

- API keys or tokens.
- Unreviewed brainstorm noise.
- Large raw logs.
- Temporary failures unless the failure teaches a repeatable constraint.

## API Script

Use:

```bash
cd /Users/jamesfilios/Software_Projects/FW_AI
python3 scripts/supermemory_add_document.py memories/seeds/<file>.md
```

The script reads `.env`, sends the file to `https://api.supermemory.ai/v3/documents`, stores the response under `memories/responses/`, and does not print the API key.

## References

- `references/api-notes.md`: current API/MCP endpoint notes.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Supermemory VFX. |
| 1.1     | 2026-08-16 | Replaced stale `/Users/robbiefilios/Documents/FW_AI_Workflow` paths with repo-relative paths and the current workspace root. |
| 1.2     | 2026-08-16 | Retired alongside `mcp/supermemory.md`; frontmatter description marked RETIRED so the skill is not invoked. |
