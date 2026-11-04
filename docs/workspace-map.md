**Created:** 2026-05-18
**Updated:** 2026-11-04

# Workspace Map

The folder tree in more detail than `AGENTS.md`. Every working folder also has its own `README.md`.

## Shot-first rule (2026-11-04)

Anything used by one shot lives in that shot's folder; anything that defines the film or is used by more than one shot lives project-wide. When a shot's file starts being used elsewhere, move it project-wide and leave a pointer.

## Shot folder

```
shots/shot004_fire-jump/
  README.md  plan.md  comp_log.md  workflow-test-plan_v001.md (frozen)
  plates/  reference/  comps/  scripts/  outputs/
  pass-a_jerry/      log.md  inputs/  workflows/ (early/)  runs/
  pass-b_grassfire/  log.md  inputs/  keyframes/  layers/  workflows/  runs/
```

`runs/` holds each kept run's clip and extracted workflow side by side. `outputs/` (renders, previews, review sheets, scratch, `_archive/<date>/`) is gitignored except READMEs. Heavy media everywhere is gitignored; READMEs, logs and small metadata are tracked.

## Project-wide

- `characters/<name>/`: bible (`bible_vNNN.md`), `development-plan.md`, reference sets, approval reviews, candidates, CGI, training material, `outputs/`. `characters/character-bible.md`: shared rules.
- `docs/`: `decisions.md`, `findings.md`, `worklog.md`, `todo.md`, `asset-inventory.md`, `asset-intake.md`, `pipeline-strategy.md`, this map. `docs/archive/`: retired documents and the 2026-11-04 move list.
- `source/`: screenplay; storyboards, audio and editorial when they arrive. `inbox/`: uploads waiting for intake.
- `library/`: Mickmumpitz library (`mickmumpitz/`, described in `mickmumpitz-library.md`), research, `manifests/` for media kept off the repo.
- `workflows/`: ComfyUI conventions and creator originals; Higgsfield notes.
- `scripts/`: shared tools (RunPod, Blender helpers, library sorter). `mcp/`: one note per service. `prompts/`: reusable prompt blocks.
- `outputs/`: project-wide scratch only (reference studies, tool schemas).

## Naming

- Shot files: `shot004_fire-jump_plate-analysis_v001.md`, `shot004_fire-jump_plate_main_v001.mov`.
- Reusable templates: tool-first, `comfyui_wan-alpha-fire-element_v001.json`.
- Character and reference media: subject-first, `jerry_fire_approved-look_front_v001.png`.
- Kept generation runs: the run ID after the method, `shot004_fire-jump_grassfire-flf_s004-b-023_seedance20-1080p_v001.mp4` (from 2026-11-04; earlier runs map to IDs in each pass log).

## Intake Flow

1. Put new uploads in `inbox/`.
2. Classify and name curated copies using `docs/asset-intake.md`.
3. File them in the shot folder or project-wide area that uses them, with a README line.
4. Record source media in `docs/asset-inventory.md`.
