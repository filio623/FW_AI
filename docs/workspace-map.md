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

## Intake Flow

1. Put new uploads in `assets/inbox/`.
2. Classify and name curated copies using `docs/asset-intake.md`.
3. Move or copy curated assets into the correct `assets/` subfolder.
4. Link shot-specific assets from `shots/`.
5. Record useful metadata in `docs/asset-inventory.md`.

## Core Production Principle

Keep the original plate untouched. Generate separable elements and interaction passes whenever possible, then composite them over the plate.
