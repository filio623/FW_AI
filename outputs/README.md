# Outputs

Generated renders, comps, review sheets and scratch files. Git ignores everything here except these README files, so the media can be cleared at any time while each folder keeps its context. Anything worth keeping is promoted into `assets/` under a `_vNNN` name and recorded in `docs/asset-inventory.md` first (`AGENTS.md`, Generated Outputs).

## Layout

- `shot004/`: shot 004 (Jerry fire jump), split by pass, comp and reference.
- `characters/`: character work that is not tied to one shot, such as the Jerry fire rig.
- `reference/`: extracted third-party examples studied for a technique.
- `tools/`: service schemas and upload logs.

New work goes in `outputs/<shot>/<pass>/<task>[_vNNN]/`, `outputs/<shot>/comp/<tool>/`, `outputs/<shot>/reference/`, `outputs/characters/<name>/<task>/`, `outputs/reference/<topic>/` or `outputs/tools/<service>/`. Give every new folder a README.

## Source and history

- 2026-11-03: reorganized from loose top-level folders into this layout.
- What was done when: `docs/worklog.md`.
