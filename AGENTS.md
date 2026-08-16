**Created:** 2026-05-18
**Modified:** 2026-08-16
**Version:** 1.2

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

Markdown is the primary format. Keep headings descriptive, notes scannable, and lists action-oriented. Use shot-first names for shot assets and documents, for example `shot004_fire-jump_plate-analysis_v001.md` or `shot004_fire-jump_plate_main_v001.mov`. Use subject-first names for reusable character/reference assets, such as `jerry_fire_approved-look_front_v001.png`.

Media files always carry a `_vNNN` suffix and are never overwritten: a new take is a new file. Markdown documents follow the `Document Lifecycle & Versioning` rules below, where most documents keep a stable filename and carry their version inside the file.

Python scripts should be small, standard-library-first, and formatted with 4-space indentation.

## Document Lifecycle & Versioning

Every governed Markdown document opens with a metadata block and ends with a revision history. Both are added at creation time, not retrofitted later.

```text
**Created:** YYYY-MM-DD
**Modified:** YYYY-MM-DD
**Version:** X.Y
```

```markdown
## Changelog

| Version | Date       | Description              |
|---------|------------|--------------------------|
| 1.0     | YYYY-MM-DD | Initial <document name>. |
```

A new document starts at `1.0` with one row describing its creation. Order rows oldest first and never rewrite or delete an existing row. `Created` is set once for the document's lineage and never changes. Every edit updates `Modified`, increments `Version`, and appends a changelog row.

### Document Classes

Classify a document once, when you create it. The class decides how it is versioned.

- **Living document** — a stable filename with no version suffix, revised in place forever. This is the default for anything describing current state or intent: `docs/pipeline-strategy.md`, `docs/environment.md`, `mcp/runpod.md`.
- **Frozen edition** — a `_vNNN` filename naming a fixed edition that approved work is checked against, such as `docs/jerry-character-bible_v001.md` or `shots/shot004_fire-jump_workflow-test-plan_v001.md`. Shots comped against an edition must still resolve its exact path, so the file keeps its suffix and its path forever. Corrections inside an edition are ordinary minor revisions. Superseding an edition means publishing a new file at the next `_vNNN`, never renaming or rewriting the old one.
- **Append-only log** — dated entries are themselves the history, so these carry the metadata block but no changelog table: `docs/findings.md`, run logs, and casting logs. Add new entries; do not revise old ones.

### Minor And Major Revisions

Classify the change before editing.

- **Minor** — corrections, clarifications, progress updates, and small additions that do not reorganize the document or change a decision it records. Edit in place and increment the minor version, `2.0` to `2.1`.
- **Major** — substantial rewrites, structural expansion, or a reversal of a decision the document records. Archive a snapshot first (see `Archiving Strategy`), then publish the new version with the major bumped, `2.3` to `3.0`.

The minor version is a counter, not a decimal fraction, so `2.9` is followed by `2.10`. A major bump resets the minor version to `0`. A new canonical version carries forward the complete changelog from the archived snapshot and appends its own row.

### Scope And Exemptions

Governed: `docs/`, `mcp/`, `references/`, `prompts/`, `workflows/`, `shots/`, `skills/`, and the root `AGENTS.md` and `README.md`.

Exempt, because the ceremony would exceed the content:

- Directory-signpost READMEs that only orient a reader inside a folder.
- Templates, including `shots/shot-template.md` and `shots/_template/`.
- Changelog files themselves.
- `assets/**` notes and review galleries. These belong to a `vNNN` asset folder that is already frozen, and are indexed through `docs/asset-inventory.md`.
- `memories/seeds/`, which holds dated, immutable session snapshots.

`skills/**/SKILL.md` files begin with required YAML frontmatter. Their metadata block goes directly below the closing `---`, never above it, so skill parsing is unaffected.

A document loaded into every agent session keeps its metadata block but moves its changelog table to `docs/<NAME>-CHANGELOG.md`, leaving a one-line pointer, so history growth never costs session context. `AGENTS.md` is the only one today.

## Archiving Strategy

Nothing approved, delivered, or referenced by approved work is ever deleted. Archiving moves it somewhere predictable and marks it clearly; it does not discard it.

### Superseded Document Versions

On a major revision, copy the document's complete current contents to `docs/archive/<NAME>-v<OLD_VERSION>.md` before replacing it, regardless of where the canonical document lives. A major revision of the root `AGENTS.md` at `1.7` archives to `docs/archive/AGENTS-v1.7.md`. In the archived copy, prepend `[ARCHIVED]` to the title and add `**Archived:** YYYY-MM-DD` to the metadata block. Archived snapshots are immutable once written, except to correct an archival mistake.

### Superseded Frozen Editions

A frozen edition stays at its original path when a newer edition lands, because existing shots, comps, and approvals still reference it. Do not move it into `docs/archive/`. Add `**Superseded by:** <path>` to its metadata block, note the supersession in its changelog, and point the newer edition back at it. Both editions remain readable side by side, which is the entire reason the class exists.

### Retired Documents

A document retired with no successor keeps its path. Prepend `[ARCHIVED]` to its title, add `**Archived:** YYYY-MM-DD`, and record why in its changelog. Do not delete it and do not move it.

### Superseded Media And Assets

Media is versioned by filename, so a new take never overwrites an old one. When a take stops being current, keep it: move it to an `_archive/` subfolder beside the asset it replaced, for example `assets/characters/jerry/approved/_archive/`. Record the move in `docs/asset-inventory.md` with the reason and the replacement, so a superseded look can still be found by anything comped against it.

Never delete an approved look, a delivered element, or a plate. If a shot was ever comped against a file, that file is production history.

### Generated Outputs

`outputs/` is ignored by Git and treated as ephemeral. It may be cleared at any time and is not archived. Anything worth keeping is promoted first: copy it into the correct `assets/` subfolder under a proper `_vNNN` name, record it in `docs/asset-inventory.md`, and only then let the `outputs/` copy expire.

### Cold Storage

Bulk production media lives on the external production drive, not in this repository. When material moves to or from cold storage, update the matching manifest in `references/manifests/` in the same change. A manifest is the only durable record that an off-repo file exists, so an unrecorded move is indistinguishable from a deletion.

## Testing Guidelines

No formal test suite is present. Validate changes by running the specific script or workflow you touched, checking links and paths in Markdown, and confirming generated Supermemory responses appear in `memories/responses/` when relevant. For shot work, update the associated file in `shots/` with the latest run, asset paths, and review notes.

## Commit & Pull Request Guidelines

This directory is a Git repository. Use concise imperative commit messages such as `Add Jerry character bible notes` or `Update Supermemory upload script`. Keep commits focused by workflow or shot when practical. Do not commit `.env`, generated `outputs/`, local test media, or large source media; commit durable metadata, docs, prompts, scripts, workflow notes, and small curated references when useful. Pull requests should summarize changed docs/workflows, list affected shots or assets, mention any required `.env` settings, and include thumbnails or review links for visual output when applicable.

## Character Generation Notes

For Jerry and the other elemental characters, base body renders should not include embedded eyes, mouths, brows, noses, smiles, or drawn-on facial features. Treat storyboard panels and temp facial animation as personality, timing, and performance references only. Facial animation is a separate layer; body-generation prompts should emphasize silhouette, posture, material, glow, motion language, and compositing needs.

## Comfy Cloud Access

Comfy Cloud MCP is configured through `scripts/comfy-cloud-mcp.sh`, but the account currently receives a 403 rollout message from the MCP endpoint. Use the regular Comfy Cloud API and official CLI fallback until MCP is enabled for the account.

- Use `scripts/comfy-cloud-cli.sh generate list` and `scripts/comfy-cloud-cli.sh generate schema <model>` for hosted partner-node discovery.
- Use `scripts/comfy-cloud-cli.sh generate <model> ... --download outputs/<name>` for Flux, Seedance, Kling, Luma, Nano Banana, Ideogram, Runway, Recraft, Stability, and similar one-shot partner jobs.
- Use `scripts/comfy-cloud-api.py user`, `system-stats`, and `submit <workflow.json>` for account checks and API-format workflow execution against `https://cloud.comfy.org/api`.
- Keep `COMFY_API_KEY` only in `.env`; never copy it into commands, docs, memories, or committed files.
- Load the `comfy-cloud-vfx` skill for Comfy Cloud work and the `comfyui-vfx` skill for local ComfyUI workflow work.

## Security & Configuration Tips

Keep secrets in `.env` and commit only `.env.example`. Large media and generated outputs are intentionally ignored; track durable metadata in Markdown instead of committing heavy production files.

---

## Changelog

Revision history for this file lives in `docs/AGENTS-CHANGELOG.md`. Append a row there on every change.
