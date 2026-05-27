# Handoff Prompt: Scene 4 Jerry Fire Video Test v001

Copy/paste this prompt into a fresh Codex session.

```text
Please read `AGENTS.md`, `docs/jerry-character-bible_v001.md`, `assets/characters/jerry/character-bible-v001/README.md`, `assets/characters/jerry/character-bible-v001/selection_manifest.tsv`, `workflows/higgsfield/jerry/jerry_higgsfield-casting-log_v001.md`, and use the `higgsfield-generate`, `higgsfield-vfx`, and `supermemory-vfx` skills.

Goal: run the first Higgsfield video-generation test for Scene 4 using the newly assembled Jerry character-bible references.

Task:

- Generate a short baked preview of Jerry's fire element/motion on top of the base Scene 4 footage.
- Use this as a Higgsfield exploration/benchmark first, not a final compositing-ready deliverable.
- Do not generate Sally/water droplet.
- Do not add eyes, mouth, brows, nose, smile, or baked-in facial features to Jerry. Facial animation is a separate layer.
- Do not overwrite or modify source footage.

Source media:

- Base footage / plate to generate on top of:
  `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/FW_test_scene.mov`
- Existing rough comp / motion reference:
  `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/Shot4 V031-1.mp4`

Relevant Jerry references:

- Main assembled reference folder:
  `/Users/robbiefilios/Documents/FW_AI_Workflow/assets/characters/jerry/character-bible-v001/`
- Primary body references:
  `/Users/robbiefilios/Documents/FW_AI_Workflow/assets/characters/jerry/character-bible-v001/references/primary-body/`
- Motion references:
  `/Users/robbiefilios/Documents/FW_AI_Workflow/assets/characters/jerry/character-bible-v001/references/motion-poses/`
- Material reference:
  `/Users/robbiefilios/Documents/FW_AI_Workflow/assets/characters/jerry/character-bible-v001/references/material/JB-012_upright-wild-flicker_material-ref.png`
- Source grounding only:
  `/Users/robbiefilios/Documents/FW_AI_Workflow/assets/characters/jerry/character-bible-v001/references/source-ref-only/`

Suggested first reference images:

- `references/primary-body/JB-001_upright-compact-idle.png`
- `references/primary-body/JB-009_small-upright-idle.png`
- `references/primary-body/JB-010_round-idle-glow.png`
- `references/motion-poses/JB-004_fast-right-comet.png`
- `references/material/JB-012_upright-wild-flicker_material-ref.png`

Clip facts already checked:

- `FW_test_scene.mov`: 4096x2160, 24 fps, 3.5 seconds.
- `Shot4 V031-1.mp4`: 1920x1080, 24 fps, 3.5 seconds.

Recommended model path:

1. Start with Higgsfield `seedance_2_0`.
2. Inspect `higgsfield model get seedance_2_0 --json` before running.
3. Use 16:9, 1080p if accepted, 5 seconds if the model cannot accept 3.5 seconds. If a 3.5 second duration is rejected, use 5 seconds and note the mismatch.
4. Use the base footage as the primary video/plate input.
5. Use the rough comp as motion/reference video if the CLI/model accepts multiple video media inputs. If it does not, use the base video plus Jerry image references first, then run a second test using the rough comp as the video reference.
6. Use `--wait --wait-timeout 30m --wait-interval 10s`.

Prompt seed:

Generate a baked preview of Jerry, a small face-free living flame character, composited into the provided Scene 4 plate. Jerry should appear as a compact teardrop-shaped fire body moving along the same timing and path suggested by the rough reference clip. Only generate Jerry's fire element and its natural glow; do not generate the water droplet or any other character. Jerry has no embedded facial features: no eyes, no mouth, no brows, no nose, no smile, no face, no facial marks. Express life only through flame body shape, posture, squash and stretch, glow, and flickering motion. Use the Jerry character-bible references for compact rounded lower body, warm yellow-white core, amber/orange flame body, ember-red rim, and lively but contained flicker. Preserve the original plate camera and environment. Keep the result grounded in the footage, with believable scale, light, color, and motion. No text, no logo, no extra characters, no water droplet, no cartoon face, no monster fire, no campfire logs.

Suggested first command shape, after validating media flags:

`higgsfield generate create seedance_2_0 --prompt "<prompt seed above>" --video "/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/FW_test_scene.mov" --image "/Users/robbiefilios/Documents/FW_AI_Workflow/assets/characters/jerry/character-bible-v001/references/primary-body/JB-001_upright-compact-idle.png" --image "/Users/robbiefilios/Documents/FW_AI_Workflow/assets/characters/jerry/character-bible-v001/references/primary-body/JB-010_round-idle-glow.png" --image "/Users/robbiefilios/Documents/FW_AI_Workflow/assets/characters/jerry/character-bible-v001/references/motion-poses/JB-004_fast-right-comet.png" --image "/Users/robbiefilios/Documents/FW_AI_Workflow/assets/characters/jerry/character-bible-v001/references/material/JB-012_upright-wild-flicker_material-ref.png" --aspect_ratio 16:9 --resolution 1080p --duration 5 --mode std --wait --wait-timeout 30m --wait-interval 10s`

If the CLI allows the rough reference as a second video media input, include:

`--video "/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/Shot4 V031-1.mp4"`

If multiple `--video` inputs are not accepted, do not fight the CLI. Run one base-plate test and then one reference-video test, and compare.

Save outputs and notes:

- Download or copy the output URL into:
  `outputs/higgsfield/scene4_jerry-fire-test_v001/`
- Create/update:
  `workflows/higgsfield/scene4/scene4_jerry-fire-video-test_log_v001.md`
- Record model, command, input media, reference images, duration, resolution, output URL, local output path if downloaded, and whether the result is usable as:
  `reference-only`, `baked-preview`, `temp-comp candidate`, or `production candidate`.
- Save a concise Supermemory note under project/container `ai-video-workflows`.

Evaluation criteria:

- Jerry only, no water droplet.
- No embedded facial features.
- Jerry's body follows the Scene 4 fire motion path well enough to judge timing.
- Jerry keeps the approved compact teardrop body language.
- Flame material is close to the approved material reference.
- Plate/background is not damaged too badly.
- Note whether Higgsfield is suitable for temp preview only or could inform a later ComfyUI/custom element workflow.
```
