# Comfy Cloud CLI/API Setup - 2026-05-27

Comfy Cloud MCP is configured in Codex through `scripts/comfy-cloud-mcp.sh`, but the account currently receives a 403 rollout message from `https://cloud.comfy.org/mcp`: MCP is not yet available for the account.

The regular Comfy Cloud API works with the project `.env` `COMFY_API_KEY`; `/api/user` returns account status `active`.

Use:

- `scripts/comfy-cloud-cli.sh` for hosted partner-node jobs through the official `comfy generate` command.
- `scripts/comfy-cloud-api.py` for direct Cloud API account checks, system stats, queue/history/status work, and API-format workflow submission.
- `mcp/comfy-cloud.md` and `skills/comfy-cloud-vfx/SKILL.md` for current workflow notes.

The current `comfy-cli` on PyPI did not expose the documented `generate` command, so the workspace uses the official GitHub `Comfy-Org/comfy-cli` main branch in `.venv-comfy-cli/` with Python 3.12. `.venv/` is retained because it contains `uv`, and `.uv-cache/` stores local uv-managed dependencies.

Do not store or print the actual `COMFY_API_KEY`.
