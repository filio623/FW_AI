# Document Archive

Nothing in here is live. Anything under `docs/archive/` is a historical record: it describes
how things once were, and its paths, commands, and claims may no longer resolve. That is
expected and is not a defect to fix.

This folder holds two kinds of document, distinguished by where they sit.

## Superseded Versions — flat, with a version suffix

`<NAME>-v<OLD_VERSION>.md` at the top level of this folder.

A snapshot taken when a canonical document underwent a major revision, copied before the
canonical document was replaced. The document itself lives on at its normal path; only this
frozen copy of an earlier version lives here.

- `environment-v1.0.md`
- `character-bible-v1.0.md`
- `vfx-element-benchmark-v1.8.md`
- `vfx-element-benchmark-v2.0.md`
- `mickmumpitz-library-v1.2.md`
- `shot004_fire-jump_comp-and-pass-b-plan-v1.16.md`

Since 2026-11-04 no new snapshots are made: living documents no longer carry versions, and Git keeps their history (`AGENTS.md`, Documents).

## Retired Documents — mirroring their original path

A document with no successor, moved here under a subfolder matching where it used to live,
so `mcp/supermemory.md` becomes `docs/archive/mcp/supermemory.md`. Each carries an
`**Original path:**` line in its metadata block.

- `mcp/supermemory.md`
- `skills/supermemory-vfx/`
- `docs/comfyui-vfx-learning-path.md` and `docs/mickmumpitz-vfx-setup.md`: retired learning syllabus and Illinois-volume setup handoff.
- `docs/production-roadmap.md` and `docs/comfyui-vfx-workflow-strategy.md`: retired 2026-11-04; their plans (Wan 2.7 next, Fusion comps) were out of date.
- `docs/vfx-element-benchmark.md`: retired 2026-11-04; split into `shots/shot004_fire-jump/pass-a_jerry_log.md` and the shot plan.
- `docs/environment.md`: retired 2026-11-04; its current facts moved to `AGENTS.md` and `mcp/`.
- `docs/AGENTS-CHANGELOG.md`: retired 2026-11-04; Git history records `AGENTS.md` changes from here on.
- `skills/comfyui-vfx/`, `skills/comfy-cloud-vfx/`, `skills/higgsfield-vfx/`: retired 2026-11-04; never loaded by the agent and out of date.
- `prompts/handoffs/scene4_jerry-fire-video-test_handoff_v001.md`: completed first-test prompt whose original inputs are unavailable.

Moving is deliberate. A retired document left at its original path keeps turning up in
search, keeps reading as current, and — for a retired skill — keeps being loaded and
invoked. Collecting them here means one location where nothing is live.

## What does not belong here

**Superseded frozen editions** such as `docs/jerry-character-bible_v001.md` stay at their
original paths when a newer edition lands, because approved shots reference those paths
directly. They are marked with `**Superseded by:**` instead of being moved.

## Rules

Archived documents are immutable once written, except to correct an archival mistake. Every
one carries `[ARCHIVED]` in its title and an `**Archived:**` date.

See the `Archiving Strategy` section of `AGENTS.md` for the full rules.
