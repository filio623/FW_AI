**Created:** 2026-05-18
**Modified:** 2026-08-16
**Version:** 1.2

# Workspace Map

This repo is the shared working area for the AI short-film VFX pipeline.

## Directories

- `assets/`: source and curated production assets.
  - `assets/inbox/`: unsorted uploads waiting for intake.
  - `assets/scripts/`: screenplay PDF and script breakdown notes.
  - `assets/storyboards/`: storyboard images, panels, and animatics.
  - `assets/plates/`: source plates, shot-organized plates, proxies, stills, and mattes.
  - `assets/elements/`: generated or rendered fire, water, smoke, steam, splash, scorch, contact, and matte elements.
  - `assets/characters/`: character reference, approved stills, action sheets, and training candidates.
    - `assets/characters/jerry/character-bible-v001/`: current assembled Jerry reference set for generation and review.
  - `assets/references/`: visual, motion, and style references.
  - `assets/audio/`: music, dialogue, sound effects, and temp audio.
  - `assets/editorial/`: EDL/XML files, reference exports, and edit-facing material.
- `docs/`: durable decisions, setup notes, findings, and pipeline strategy.
  - `docs/archive/`: immutable records. Major-revision snapshots sit flat with a `-vNNN` suffix; retired documents sit under a subfolder mirroring their original path. Nothing here is live.
- `FW_test/`: current test plates and CGI fire/water renders supplied for exploration.
- `mcp/`: MCP setup notes and server plans.
- `outputs/`: generated renders, composites, thumbnails, and review artifacts.
- `prompts/`: reusable prompt blocks, character language, and handoff prompts.
- `references/`: external docs, copied snippets, model notes, and research summaries.
- `scripts/`: project automation that is not specific to a single skill.
- `shots/`: shot-by-shot plans, run logs, and compositing notes.
- `skills/`: project-local Codex skills for repeatable workflows.
- `workflows/`: ComfyUI and Higgsfield workflow templates, commands, and saved experiments.

## Naming

Use shot-first names when a file belongs to a shot:

`shot004_fire-jump_plate-analysis_v001.md`

For media assets:

`shot004_fire-jump_plate_main_v001.mov`

Use tool-first names for reusable templates:

`comfyui_wan-alpha-fire-element_v001.json`

Use subject-first names for reusable character or reference assets:

`jerry_fire_approved-look_front_v001.png`

## Versioning And Archiving

Media always carries a `_vNNN` suffix and is never overwritten. Most Markdown documents keep a stable filename and carry their version in a metadata block inside the file; only frozen editions such as character bibles and shot test plans keep `_vNNN` in the name.

Superseded media moves to an `_archive/` subfolder beside the asset it replaced and is recorded in `docs/asset-inventory.md`. Superseded document versions and retired documents both go to `docs/archive/`. Superseded frozen editions are the exception and stay at their original paths, because approved work resolves them directly. Nothing approved, delivered, or referenced by a comp is ever deleted.

See the `Document Lifecycle & Versioning` and `Archiving Strategy` sections of `AGENTS.md` for the full rules.

## Intake Flow

1. Put new uploads in `assets/inbox/`.
2. Classify and name curated copies using `docs/asset-intake.md`.
3. Move or copy curated assets into the correct `assets/` subfolder.
4. Link shot-specific assets from `shots/`.
5. Record useful metadata in `docs/asset-inventory.md`.

## Core Production Principle

Keep the original plate untouched. Generate separable elements and interaction passes whenever possible, then composite them over the plate.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Workspace Map. |
| 1.1     | 2026-08-16 | Documented the document archive, media `_archive/` convention, and versioning split between media and Markdown. |
| 1.2     | 2026-08-16 | Recorded that `docs/archive/` also holds retired documents under mirrored paths, and that superseded frozen editions stay put. |
