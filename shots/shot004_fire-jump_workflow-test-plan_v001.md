# Shot004 Fire Jump Workflow Test Plan

Date: 2026-05-18

## Shot

- ID: `shot004_fire-jump`
- Plate: `FW_test/Scene 4/4 base plate.mov`
- Existing references:
  - `FW_test/Scene 4/FW_test_scene.mov`
  - `FW_test/Scene 4/Shot4 V031-1.mp4`
  - `FW_test/Scene 4/ren_small_fire6..mov`
  - `FW_test/Scene 4/ren_grassfire_cpu..mov`
  - `FW_test/Scene 4/ren_steam..mov`
- Status: planning

## Creative Intent

A small sentient fire character jumps across a dirt and grass plate, lands in or near the grass, and causes the grass to ignite. The shot should feel physically integrated with the plate while keeping the fire character and grass interaction separately revisable.

## Core Rule

Do not bake the whole shot into one AI video unless it is only for reference or editorial temp.

The production test should be built from layers.

## Required Layers

- Original plate.
- Fire character element.
- Fire character matte or alpha.
- Grass occlusion matte.
- Contact shadow or grounding pass.
- Fire glow/contact light on nearby grass and dirt.
- Grass ignition/flame spread pass.
- Smoke or heat distortion pass.
- Scorch/darkening pass.
- Final composite review export.

## Questions To Answer First

- What are the plate resolution, frame rate, duration, and codec?
- Do any existing CGI renders include alpha?
- Is `ren_small_fire6..mov` usable as motion/silhouette control?
- Is `ren_grassfire_cpu..mov` usable as an interaction reference or pass?
- Does the shot require the fire character to pass behind any grass or foreground detail?
- What frame should ignition begin?
- Does the final fire character need to match the CGI performance exactly, or only the broad action?

## Workflow Branches To Test

### Branch A: CGI/Proxy To AI Polish

Use the existing fire CGI as motion and silhouette guidance, then use AI to improve the look.

Inputs:

- `FW_test/Scene 4/ren_small_fire6..mov`
- Base plate stills for lighting context.
- Fire character prompt language.

Desired output:

- Improved fire character clip.
- Matte or alpha.
- Motion close to the original CGI.

Why this matters:

- This is likely the most controllable production path if the current CGI has useful timing.

### Branch B: Alpha-Native Fire Element

Use Wan-Alpha or another RGBA-capable workflow to generate a fire character element with transparency.

Inputs:

- Fire character prompt.
- Approved fire still or first frame if available.
- Neutral or transparent-compatible generation setup.

Desired output:

- Fire character with usable alpha.
- Clean silhouette.
- Minimal baked background contamination.

Why this matters:

- Native alpha could reduce roto/matting pain if the character quality is acceptable.

### Branch C: First/Last Frame Or I2V Motion

Create keyframes for the fire character jump, then let a video model interpolate or animate.

Inputs:

- Start pose.
- Landing pose.
- Prompt describing the jump and energy.
- Optional CGI frame references.

Desired output:

- Short controlled fire jump clip.
- Consistent character identity.
- Usable matte extraction path.

Why this matters:

- This tests whether we can direct action without relying on full proxy animation.

### Branch D: Cloud Reference

Use Higgsfield or another cloud model to generate a high-quality reference for motion, timing, or aesthetics.

Inputs:

- Base prompt.
- Optional plate/reference media if supported.
- Fire character description.

Desired output:

- Reference clip only, unless it separates cleanly.

Why this matters:

- Cloud output can show what good motion and style might look like, even when it is not directly compositable.

### Branch E: Interaction Passes

Generate or build the grass ignition, smoke, heat, glow, and scorch separately from the character.

Inputs:

- Base plate.
- Grass region mask.
- Timing from the character jump.
- Existing `FW_test/Scene 4/ren_grassfire_cpu..mov` and `FW_test/Scene 4/ren_steam..mov` references.

Desired output:

- Ignition pass.
- Smoke/steam or heat pass.
- Scorch/darkening pass.
- Glow/contact light pass.

Why this matters:

- The interaction may be easier to control as separate layers than as part of character generation.

## Acceptance Criteria

The test workflow is successful if:

- The plate remains intact.
- The fire character can be moved, retimed, or regenerated without replacing the grass ignition pass.
- The grass ignition can be adjusted without regenerating the character.
- The character reads consistently across the clip.
- The matte/alpha is good enough for a rough comp.
- At least one workflow branch is clearly worth developing into a reusable template.

## First Pass Task List

- Verify metadata and alpha status for all `FW_test/Scene 4/` videos.
- Extract representative still frames from:
  - base plate
  - fire character render
  - grass fire render
  - steam render
  - existing composite/reference
- Create a simple frame/action map for the fire jump.
- Define the first desired fire character look.
- Run Branch A and Branch B before investing in LoRA training.
- Create a rough comp proof with separated character and interaction timing.

## Notes Log

- 2026-05-18: Created as the first workflow test plan for developing the film's AI-assisted VFX pipeline.
