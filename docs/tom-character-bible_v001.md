# Tom Character Bible v001

Date: 2026-05-21

Status: draft working bible for source review and early generation tests. No Tom reference is approved yet.

## Purpose

Define Tom well enough to inventory and review existing source material, then generate controlled still-image candidates after human review.

This document is not a final character bible. It becomes production guidance only after Robbie reviews candidate references and selected items are promoted into `assets/characters/tom/approved/` and `assets/characters/tom/character-bible-v001/`.

## Core Identity

Tom is the much larger fire villain. He should feel like a dominant, dangerous fire force that tempts and overwhelms Jerry, threatens Sally, and consumes the forest.

Tom should feel:

- Dominant and powerful.
- Serious and intimidating.
- Larger, heavier, and more destructive than Jerry.
- Related to fire, but not a cute or vulnerable flame character.
- Emotionally readable through shape, movement, scale, and glow.

## Story Function

Tom appears after lightning strikes a tree. He grows from a large burning branch, beckons Jerry to join him, blocks Jerry from reaching Sally, consumes Jerry, shrugs off Sally's first attempts to put him out, spreads to more trees, and is finally extinguished by a larger water surge.

Tom is a villain, but the design should still fit the film's warm animated love-story tone. Avoid turning him into a generic horror creature.

## Visual Rules

- Body is a large living fire mass, not a monster wearing fire.
- Silhouette is aggressive, taller, heavier, and more turbulent than Jerry.
- Do not embed eyes, mouth, brows, nose, teeth, horns, or facial features in base fire-body renders.
- Personality should come from body scale, posture, flame shape, smoke accents, glow, and motion language.
- Facial animation, if used, will be created as a separate layer and composited or animated separately.
- Core can be hot white/yellow, surrounded by orange, red, ember, and darker smoke accents.
- Edges can tear, lash, and flare, but the body shape must remain readable.
- Strong glow, smoke, scorch, heat distortion, and spreading fire are separate production passes when revision control matters.
- Use black or neutral background for early casting unless plate context is being tested.

## Tom Versus Jerry

Tom must not look like Jerry scaled up.

Key contrast:

- Jerry: compact, rounded, vulnerable, lively, contained flicker.
- Tom: towering, forceful, jagged, dominant, broader flame mass, heavier motion.
- Jerry's palette is warm yellow/amber with soft ember edges.
- Tom's palette can push deeper reds, hotter whites, darker smoke, and harsher turbulence.
- Jerry's motion is quick and buoyant.
- Tom's motion is slower, larger, and more forceful.

## Avoid

- Just a scaled-up Jerry.
- Fire demon, skull, teeth, horns, armor, claws, humanoid limbs, or horror-monster anatomy.
- Random facial features embedded into the fire body.
- Overly dense smoke that hides the body.
- Generic campfire or wildfire plate without character body language.
- Over-baked backgrounds in core character-design images.
- A face design that cannot be separated for later facial animation.

## Current Source References

Use these as source leads, not approved references:

- `references/manifests/tom_external-drive_reference_inventory_v001.md`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Tom.png`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/shot_8H_comp_v07.mov`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/render_dn/Tom_DN/`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8G/render/Combined__tom_v001/`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8G/render_dn/Tom_DN/`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/ren_big_fire_shot 8L/`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/Shot_8L/shot_8L_anim_v05.mov`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/Shot_8L/render_dn/Tom_DN/`
- `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/Renders/8L_Comp_V1.mov`

Reference roles:

- The Tom 2D sheet should guide performance, pose, and face-layer intent only.
- Tom VFX EXR sequences should guide scale, material, glow, flame dynamics, and plate integration.
- Finished or rough comp movies should guide shot context, scale, timing, and interaction with Sally/Jerry.
- Big-fire passes may become material or action references, but should not define Tom's identity unless the character read is clear.

## Review Gate

Before finalizing Tom:

1. Extract or collect candidate stills/contact sheets from the source leads.
2. Organize them under `assets/characters/tom/approval-review/v001/`.
3. Assign stable review IDs, likely `TB-001`, `TB-002`, and later.
4. Robbie reviews and marks candidates as primary, secondary, source-only, performance-only, or rejected.
5. Only approved candidates are promoted into `assets/characters/tom/approved/`.
6. Only after that, assemble `assets/characters/tom/character-bible-v001/`.

## First Generation Target

After the first source review, generate one clean casting still:

- Single full-body Tom.
- Neutral or black background.
- No facial features.
- Large aggressive fire silhouette.
- Strong sense of scale and threat.
- No scene background.
- No other characters.
- No text.

## Draft Prompt

Large sentient fire villain named Tom, towering living fire body, no embedded facial features, no eyes, no mouth, no brows, no nose, no teeth, no horns, no face, dominant intimidating body language expressed only through flame shape and posture, hot white inner core, deep orange and red flame mass, darker smoke accents, jagged aggressive flame silhouette, powerful glow, heavier slower movement implied, physically made of real fire, clean isolated character design on black background, readable full body with negative space around the fire, high detail flame material.

Avoid scaled-up Jerry, cute small flame, mascot, humanoid limbs, armor, demon, skull, horror monster, horns, teeth, claws, campfire logs, grass, dirt, forest plate, baked background, face, smile, text, logo.

## Evaluation Criteria

- Does it feel like Tom, not just a generic large fire?
- Is Tom clearly distinct from Jerry?
- Does the body shape feel threatening without horror overdesign?
- Is the silhouette readable at small screen size?
- Can separate facial animation be added later without fighting the body design?
- Can smoke/glow/heat/scorch be separated into revisable passes?
- Does it support key actions: beckon, block, consume Jerry, react to Sally, grow, extinguish?

## Next Steps

1. Build the source-derived candidate review pack.
2. Review and mark selected references with Robbie.
3. Promote approved references only after review.
4. Run first controlled Tom generation tests using approved source roles.
5. Update this file with approved IDs and tested prompt language.
