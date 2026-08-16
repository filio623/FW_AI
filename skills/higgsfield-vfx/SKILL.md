---
name: higgsfield-vfx
description: "Use when generating, benchmarking, or documenting Higgsfield AI video outputs for the AI short film: CLI model discovery, cost estimation, prompt testing, image-to-video/reference video generation, comparing cloud models against ComfyUI, and recording output URLs, settings, and credits."
---

**Created:** 2026-05-18
**Modified:** 2026-08-16
**Version:** 1.1

# Higgsfield VFX

## Core Rule

Use Higgsfield as a high-quality cloud renderer and benchmark source. Do not assume its outputs are compositing-ready unless alpha, clean background, or extraction has been explicitly tested.

## Project Context

- Higgsfield CLI is installed and authenticated.
- Project root: `/Users/jamesfilios/Software_Projects/FW_AI`.
- Account, model, and credit findings are documented in `docs/environment.md`.
- Higgsfield outputs and test logs should be recorded in `workflows/higgsfield/` or the relevant shot note under `shots/`.

## Workflow

1. Define the purpose: reference, temp composite, motion exploration, final baked shot, or element-generation attempt.
2. Check model parameters and cost before running expensive generations.
3. Use stable prompts that preserve project character language.
4. Save command, model, settings, cost estimate, output URL, and qualitative notes.
5. Compare against the plate/compositing requirement before treating the result as production-usable.

## CLI Patterns

Use the local CLI help and model parameter inspection before assuming options.

Known useful command shape:

```bash
higgsfield generate create wan2_7 \
  --prompt "<prompt>" \
  --duration 5 \
  --aspect_ratio 16:9 \
  --resolution 720p \
  --wait \
  --wait-timeout 20m \
  --wait-interval 10s
```

## Output Logging

For every meaningful generation, record:

- Date.
- Model.
- Prompt.
- Input media, if any.
- Duration, aspect ratio, resolution, and mode.
- Credit estimate or actual cost when available.
- Output URL or local file path.
- What worked.
- What failed.
- Whether the output is reference-only, temp, or production candidate.

Use `references/run-log-template.md` when creating a new log.

## References

Read these only when needed:

- `references/model-notes.md`: current Higgsfield project findings.
- `references/run-log-template.md`: compact logging format for generations.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Higgsfield VFX. |
| 1.1     | 2026-08-16 | Replaced stale `/Users/robbiefilios/Documents/FW_AI_Workflow` paths with repo-relative paths and the current workspace root. |
