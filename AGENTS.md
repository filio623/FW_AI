# Repository Guidelines

## Project Structure & Module Organization

This repository is a working area for an AI-assisted short-film VFX pipeline. Use `docs/` for durable decisions, setup notes, findings, and production strategy. Use `assets/` for source and curated media, with new uploads staged in `assets/inbox/` before classification. Shot-specific plans, run logs, and compositing notes belong in `shots/`; start from `shots/shot-template.md` for new shots. Reusable prompts live in `prompts/`, external research in `references/`, automation in `scripts/`, local agent skills in `skills/`, and saved ComfyUI/Higgsfield workflows in `workflows/`. Generated renders, composites, thumbnails, and review artifacts belong in `outputs/`, which is ignored by Git.

## Build, Test, and Development Commands

There is no application build step in this repository. Useful project commands are:

- `bash scripts/supermemory-mcp.sh`: starts the Supermemory MCP bridge using `.env`.
- `python3 scripts/supermemory_add_document.py docs/findings.md --custom-id findings`: uploads a markdown/text file to Supermemory and saves the API response under `memories/responses/`.
- `rg "shot004"`: searches notes, workflows, and documentation quickly.

Networked commands require valid `.env` values, especially `SUPERMEMORY_API_KEY`.

## Coding Style & Naming Conventions

Markdown is the primary format. Keep headings descriptive, notes scannable, and lists action-oriented. Use shot-first names for shot assets and documents, for example `shot004_fire-jump_plate-analysis_v001.md` or `shot004_fire-jump_plate_main_v001.mov`. Use subject-first names for reusable character/reference assets, such as `jerry_fire_approved-look_front_v001.png`. Use `v001`, `v002`, and later versions for revisions; do not overwrite source, approved, or delivered files.

Python scripts should be small, standard-library-first, and formatted with 4-space indentation.

## Testing Guidelines

No formal test suite is present. Validate changes by running the specific script or workflow you touched, checking links and paths in Markdown, and confirming generated Supermemory responses appear in `memories/responses/` when relevant. For shot work, update the associated file in `shots/` with the latest run, asset paths, and review notes.

## Commit & Pull Request Guidelines

This directory is a Git repository. Use concise imperative commit messages such as `Add Jerry character bible notes` or `Update Supermemory upload script`. Keep commits focused by workflow or shot when practical. Do not commit `.env`, generated `outputs/`, local test media, or large source media; commit durable metadata, docs, prompts, scripts, workflow notes, and small curated references when useful. Pull requests should summarize changed docs/workflows, list affected shots or assets, mention any required `.env` settings, and include thumbnails or review links for visual output when applicable.

## Character Generation Notes

For Jerry and the other elemental characters, base body renders should not include embedded eyes, mouths, brows, noses, smiles, or drawn-on facial features. Treat storyboard panels and temp facial animation as personality, timing, and performance references only. Facial animation is a separate layer; body-generation prompts should emphasize silhouette, posture, material, glow, motion language, and compositing needs.

## Security & Configuration Tips

Keep secrets in `.env` and commit only `.env.example`. Large media and generated outputs are intentionally ignored; track durable metadata in Markdown instead of committing heavy production files.
