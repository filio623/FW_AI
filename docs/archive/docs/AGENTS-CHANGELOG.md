**Archived:** 2026-11-04
**Original path:** `docs/AGENTS-CHANGELOG.md`

# [ARCHIVED] AGENTS.md Revision History

Full revision history for the root-level `AGENTS.md`.

This history lives outside `AGENTS.md` because that file is loaded into every agent session through `CLAUDE.md`. Keeping the table here means the history can grow without consuming session context. See the `Document Lifecycle & Versioning` section of `AGENTS.md` for the rule.

This file is a revision history, so it is exempt from the metadata-and-changelog requirement that applies to governed documents.

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial contributor guide creation. |
| 1.1     | 2026-08-16 | Added document lifecycle, versioning, and archiving strategy; separated media filename versioning from in-file document versioning. |
| 1.2     | 2026-08-16 | Corrected the media-archive example to use the real `approved/` folder name. |
| 1.3     | 2026-08-16 | Retired Supermemory: removed its commands and testing/commit references, and added a Project Memory section naming the repository as the single source of truth. |
| 1.4     | 2026-08-16 | Retired documents now move into `docs/archive/` mirroring their original path, instead of staying in place; clarified how that differs from a superseded frozen edition. |
| 1.5     | 2026-10-08 | Clarified that the optional Comfy Cloud CLI is absent on this machine and that the ComfyUI skill applies to RunPod-hosted workflows too. |
| 1.6     | 2026-11-03 | Added the ComfyUI workflow layout (working folders per shot and pass, mirrored on the Pod; frozen benchmark extracts; vendor originals) with a pointer to `workflows/comfyui/README.md`. |
| 1.7     | 2026-11-03 | Added the `outputs/` layout: per shot and pass, comps, reference, and non-shot folders for characters, reference and tools. |
| 1.8     | 2026-11-03 | Added the folder README rule (outputs READMEs tracked), per-pass append-only test logs, and the session worklog `docs/worklog.md`. |
| 1.9     | 2026-11-04 | Cut the Comfy Cloud section to one line (parked; MCP launcher and CLI wrapper removed). |

Retired 2026-11-04: living docs no longer carry changelogs; Git history records changes to `AGENTS.md` from here on.
