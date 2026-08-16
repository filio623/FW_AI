**Created:** 2026-05-18
**Modified:** 2026-08-16
**Version:** 1.1

# AI Video Workflows

Workspace for building an AI-assisted VFX pipeline for the short film.

Start here:

- `AGENTS.md`: repository conventions, document lifecycle, and archiving strategy.
- `docs/workspace-map.md`: where things go.
- `docs/production-roadmap.md`: working plan for the AI-assisted VFX pipeline.
- `docs/pipeline-strategy.md`: current production strategy and tool roles.
- `docs/environment.md`: what is installed on this machine and where workflows can run.

Characters:

- `docs/character-bible.md`: shared style rules, character relationships, and the index of per-character bibles.
- `docs/jerry-character-bible_v001.md` and `docs/tom-character-bible_v001.md`: the current frozen editions.
- `docs/jerry-character-development-plan.md`: first character-development track and Higgsfield plan.
- `assets/characters/jerry/character-bible-v001/`: current assembled Jerry reference set.

Doing the work:

- `docs/asset-intake.md`: how to upload, classify, name, and track incoming film assets.
- `docs/asset-inventory.md`: index of tracked assets and restorable source media.
- `docs/comfyui-vfx-workflow-strategy.md`: layer strategy and the Scene 4 branch plan.
- `docs/comfyui-vfx-learning-path.md`: what to learn, in order, to run those workflows.
- `docs/findings.md`: running log of what worked and what did not.
- `mcp/runpod.md`: RunPod GPU setup and the current resume point.
- `prompts/handoffs/`: copy/paste prompts for focused new sessions.

Directories:

- `assets/`: scripts, storyboards, plates, VFX elements, character references, audio, and editorial source files.
- `mcp/`: MCP status and setup notes.
- `references/`: external research and the external-drive manifests.
- `skills/`: project-local Codex skills.
- `shots/`: shot plans and run logs.
- `workflows/`: ComfyUI workflows and Higgsfield run docs.
- `outputs/`: generated renders and review artifacts. Ignored by Git and treated as ephemeral; promote anything worth keeping into `assets/`.

Core principle: keep plates untouched and generate separable character/effect elements for compositing whenever possible.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial AI Video Workflows. |
| 1.1     | 2026-08-16 | Grouped the Start here list and added AGENTS.md, the per-character bibles, both ComfyUI VFX docs, findings, RunPod, references, and outputs. |
