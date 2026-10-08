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

## Retired Documents — mirroring their original path

A document with no successor, moved here under a subfolder matching where it used to live,
so `mcp/supermemory.md` becomes `docs/archive/mcp/supermemory.md`. Each carries an
`**Original path:**` line in its metadata block.

- `mcp/supermemory.md`
- `skills/supermemory-vfx/`
- `docs/comfyui-vfx-learning-path.md` and `docs/mickmumpitz-vfx-setup.md`: retired learning syllabus and Illinois-volume setup handoff.
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
