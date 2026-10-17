**Created:** 2026-05-18
**Modified:** 2026-10-11
**Version:** 1.3

# Higgsfield MCP

## Current Status

Verified 2026-10-11:

- CLI: `@higgsfield/cli` 1.1.26, installed with `npm i -g @higgsfield/cli` and authenticated with `higgsfield auth login`. Workspace `94c8514f-0185-440f-a5ad-6f6fec32541d` ("Private") selected with `higgsfield workspace set`. Account `jamesfilios@gmail.com`, plan `plus` (trial), 110 credits.
- Companion skills: `npx skills add higgsfield-ai/skills` installs eight `higgsfield-*` skills under `.agents/skills/`.
- **The trial account cannot generate through the CLI/API.** `higgsfield generate create` returns `{"error_type":"only_mcp_usage_on_trial_is_available"}` and charges nothing. Read-only calls still work: `model list/get`, `workflow list/get`, `generate cost`, `upload create/list`, `account status`.
- The web app also asks for an upgrade before Seedance 2.5 Edit runs.
- `generate cost` reads a prompt from stdin when `--prompt` is omitted, so run it with `</dev/null` in scripts. It auto-uploads local media paths; pass upload IDs to price without re-uploading.

## MCP Server

Official hosted endpoint: `https://mcp.higgsfield.ai/mcp` (Streamable HTTP, OAuth; scope `openid email offline_access`). Source: [Higgsfield help center](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent). This is the only generation path a trial account accepts.

- OMP: `.omp/mcp.json` defines the `higgsfield` server. Authorize with `/mcp reload`, then `/mcp reauth higgsfield`; the credential stays in the OMP profile, not the repository.
- Claude Desktop / claude.ai: Settings → Connectors → Add custom connector, URL above.
- Every MCP generation deducts credits.

## MCP Candidate Requirements

A useful Higgsfield MCP should support:

- Account/status check.
- Model listing.
- Model parameter inspection.
- Cost estimation.
- Generation submission.
- Wait/poll.
- Output URL retrieval.
- Run log creation.

## Verified MCP Behavior (2026-10-11)

- `/mcp reauth higgsfield` connected; tools appear as `mcp__higgsfield_*`.
- Upload IDs created with `higgsfield upload create` resolve in MCP generation calls.
- `generate_video` with `get_cost: true` quotes without submitting; quotes matched the CLI.
- A literal prompt can return a `preset_recommendation`; pass `declined_preset_id` to generate as written.
- `jobs_wait` long-polls up to 15s per call. `job_status` takes `jobId`; `raw_data: true` gave no failure reason for a failed `kling_video_edit` job.
- Failed jobs are refunded automatically (see `transactions`).

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Higgsfield MCP. |
| 1.1     | 2026-10-08 | Corrected the host-specific Higgsfield CLI availability claim; the skill does not install or authenticate the CLI. |
| 1.2     | 2026-10-11 | Recorded the installed CLI 1.1.26, trial account, the trial CLI/API generation block, and the official MCP endpoint and OMP config. |
| 1.3     | 2026-10-11 | Replaced the next step with verified MCP behavior: upload reuse, cost preflight, preset prompts, polling, and automatic refunds. |
