# AGENTS.md Revision History

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
