# Tom External Drive Reference Inventory v001

Date: 2026-05-21

Status: first-pass source inventory. This is not an approval list.

## Purpose

Identify likely source material for Tom's character-bible review without copying whole EXR sequences into the repository.

## Review Policy

Do not promote any listed item directly into the final Tom character bible. First create selected stills/contact sheets, then review them with Robbie in `assets/characters/tom/approval-review/v001/`.

## Highest-Value Tom Sources

| Priority | Source | Details | Use |
| --- | --- | --- | --- |
| High | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Tom.png` | PNG, 3300x2550, RGBA | Tom character/action sheet. High-value performance and pose reference. Treat any drawn face as face-layer/performance reference only. |
| High | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/shot_8H_comp_v07.mov` | ProRes, 1920x1012, 24fps, 111 frames, 4.625s | Shot-level comp reference. Useful for Tom/Sally/Jerry scale, interaction, glow, and timing. |
| High | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/render_dn/Tom_DN/` | 115 EXR frames | Named Tom render sequence. Likely strongest source for Tom material, scale, and plate integration. |
| High | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8G/render/Combined__tom_v001/` | 44 EXR frames | Named combined Tom pass. Likely useful for body/action reference and interaction context. |
| High | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8G/render_dn/Tom_DN/` | 44 EXR frames | Named Tom DN pass. Useful as source-derived candidate stills. |
| High | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/Shot_8L/render_dn/Tom_DN/` | 115 EXR frames | Named Tom sequence in Shot 8L package. Useful for later-story Tom behavior and scale. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/ren_big_fire_shot 8L/` | 70 EXR frames | Big-fire render sequence. Useful for material/action support if it reads as Tom. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/Shot_8L/shot_8L_anim_v05.mov` | ProRes, 1920x1012, 24fps, 67 frames, 2.792s | Shot animation reference near Tom/Jerry interaction sources. Needs visual scrub. |
| Medium | `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/Renders/8L_Comp_V1.mov` | Found in exports. Specs not checked yet. | Candidate finished/semi-finished shot context for Tom scale and action. |

## Related Interaction Sources

These are not Tom-only, but can help define blocking, relationships, and scale:

| Priority | Source | Notes |
| --- | --- | --- |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/render_dn/ren_jerry/` | Jerry sequence in the same Shot 8H context. Useful for scale comparison with Tom. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/render_dn/Drop_DN/` | Sally/water sequence in same context. Useful for Sally attacking Tom and water impact scale. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/render_dn/steam_DN1/` | Steam sequence. Useful for Tom/Sally interaction effects, not Tom identity. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8G/render/ren_small_water/` | Sally/water sequence in same Shot 8G context. Useful for Tom/water interaction scale. |

## Script Anchors

Tom story beats from `assets/scripts/fire-and-water_script_extracted.md`:

- Lightning strikes a tree; a branch falls and catches fire, much bigger than Jerry.
- Tom is described as a fire demon, serious and all powerful.
- Rain does not affect Tom as he grows to a nearby tree.
- Tom beckons Jerry to join him.
- Tom blocks Jerry from reaching Sally.
- Jerry jumps into Tom and struggles inside him.
- Tom comes out victorious after consuming Jerry.
- Sally attacks Tom with a small stream; Tom is only briefly shocked and then laughs it off.
- Sally briefly sees Jerry trapped inside Tom through the area she affected.
- Tom grows by leaps and bounds and spreads to more trees.
- Tom is finally extinguished by Sally's larger water surge.

For generation language, translate "fire demon" into behavior and threat. Do not bake demon anatomy into the base body unless explicitly approved.

## Recommended First Review Pack

Create a review pack with:

- 6 to 10 stills from `X_Sheet_Tom.png` cropped or shown as sheet-level performance reference.
- 8 to 12 stills/contact frames from `Shot_8H/render_dn/Tom_DN/`.
- 6 to 8 stills/contact frames from `Shot_8G/render/Combined__tom_v001/`.
- 6 to 8 stills/contact frames from `shot_8L/Shot_8L/render_dn/Tom_DN/`.
- 4 to 6 material/action support frames from `shot_8L/ren_big_fire_shot 8L/`.
- Contact sheets for `shot_8H_comp_v07.mov`, `shot_8L_anim_v05.mov`, and `8L_Comp_V1.mov` if visually useful.

Initial review categories:

- `primary-body`: candidates that define Tom's main silhouette/look.
- `motion-poses`: candidates that define looming, beckoning, growing, recoiling, or extinguishing.
- `material`: fire/smoke/glow/heat support.
- `source-ref-only`: shot or comp context, scale, and plate integration.
- `performance-2d-ref-only`: Tom 2D sheet and story/performance intent.
- `rejected`: anything too generic, too busy, too horror, or too close to Jerry.

## Next Steps

1. Extract selected stills and contact sheets into `outputs/review/tom_asset-triage_v001/`.
2. Copy only chosen review candidates into `assets/characters/tom/approval-review/v001/`.
3. Assign stable `TB-###` IDs and create `approval_manifest.tsv`.
4. Review with Robbie before creating `assets/characters/tom/character-bible-v001/`.
