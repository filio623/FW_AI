**Created:** 2026-05-18
**Updated:** 2026-11-04

# Workspace Map

The folder tree in more detail than `AGENTS.md`. Every working folder also has its own `README.md`.

## Directories

- `assets/`: source and curated production media (heavy media gitignored).
  - `inbox/`: unsorted uploads waiting for intake (`docs/asset-intake.md`).
  - `scripts/`: screenplay PDF and script breakdown notes.
  - `storyboards/`: storyboard images, panels and animatics.
  - `plates/`: source plates by shot (the shot 004 working plate sits under `elements/by-shot/shot004_fire-jump/plates/`).
  - `elements/by-shot/<shot>/`: everything a shot's comp uses: `plates/`, element folders (`fire/`, `scorch-contact/` with inputs, `keyframes/` and `layers/`), `benchmark/` (every kept run clip), `comps/` (comp project files).
  - `characters/`: character references, approved stills, action sheets, training candidates; `characters/jerry/character-bible-v001/` is Jerry's assembled reference set.
  - `references/`, `audio/`, `editorial/`: visual references, sound, and edit-facing material.
- `docs/`: project-wide records: `decisions.md`, `findings.md`, `worklog.md`, `asset-inventory.md`, `asset-intake.md`, `pipeline-strategy.md`, character bibles and development plans. `docs/archive/`: retired documents and older snapshots, mirroring their original paths; nothing there is live.
- `shots/`: one folder per shot (README, plan, pass logs, comp log); `_template/` for new shots; the frozen first shot 004 test plan.
- `workflows/`: `comfyui/` (working graphs by shot and pass, one extract per kept run, creator originals), `higgsfield/` and `blender/` run docs.
- `mcp/`: one note per service; RunPod has a living `runpod.md` and an append-only `runpod_log.md`.
- `references/`: research, the Mickmumpitz library (`references/mickmumpitz/`, described in `mickmumpitz-library.md`), and `manifests/` for media kept off the repo.
- `prompts/`: reusable prompt blocks and character language.
- `scripts/`: automation; `scripts/README.md` lists each script.
- `outputs/`: renders, previews, review sheets and scratch, `outputs/<shot>/<pass or comp>/<task>/`, plus `characters/`, `reference/`, `tools/` and `_archive/<date>/`. Gitignored except READMEs.
- `memories/seeds/`: dated session snapshots from before 2026-08-16; read-only history.

## Naming

- Shot files: `shot004_fire-jump_plate-analysis_v001.md`, `shot004_fire-jump_plate_main_v001.mov`.
- Reusable templates: tool-first, `comfyui_wan-alpha-fire-element_v001.json`.
- Character and reference media: subject-first, `jerry_fire_approved-look_front_v001.png`.
- Kept generation runs: the run ID after the method, `shot004_fire-jump_grassfire-flf_s004-b-023_seedance20-1080p_v001.mp4` (from 2026-11-04; earlier runs map to IDs in each pass log).

## Intake Flow

1. Put new uploads in `assets/inbox/`.
2. Classify and name curated copies using `docs/asset-intake.md`.
3. Move or copy curated assets into the correct `assets/` subfolder, with a README line.
4. Link shot assets from the shot's README.
5. Record them in `docs/asset-inventory.md`.
