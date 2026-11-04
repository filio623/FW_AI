**Created:** 2026-05-18
**Modified:** 2026-05-18
**Version:** 1.0

# ComfyUI MCP Notes

## Preferred MCP Flow

1. `get_system_stats` to confirm ComfyUI is reachable.
2. `list_local_models` to inspect installed model files.
3. `list_workflows` to find saved workflows.
4. `analyze_workflow` before modifying a saved workflow.
5. `validate_workflow` before enqueueing.
6. `enqueue_workflow` to run.
7. `get_job_status` and `get_history` to inspect output or failures.

## Saved Workflow Locations

Project copies should live in `workflows/comfyui/`.

ComfyUI user-library copies may also exist under the ComfyUI user folder. Keep project copies current when a workflow becomes important.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial ComfyUI MCP Notes. |
