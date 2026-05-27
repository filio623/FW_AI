# Jerry Character Bible v001

Date: 2026-05-18

Status: working bible for first generation tests.

## Purpose

Define Jerry well enough to generate consistent still-image candidates for the short film, then expand the approved direction into body shape, pose, motion, and compositing references.

## Core Identity

Jerry is a small sentient flame. He should read as fire first, but with a simple, appealing personality that can carry emotional scenes with Sally.

Jerry should feel:

- Brave but vulnerable.
- Energetic and curious.
- Warm, charming, and emotionally open.
- Small compared with the environment and with larger fire characters.

## Visual Rules

- Body is a living flame, not a creature wearing fire.
- Silhouette is compact, soft, and readable at small size.
- Do not embed eyes, mouth, brows, or facial features in the flame-body render.
- Personality should come from silhouette, posture, flame shape, glow, squash/stretch, and motion language.
- Facial animation will be created as a separate layer and composited or animated separately.
- Core color is warm yellow-white, surrounded by orange and amber flame.
- Edges can flicker and stretch while the core silhouette stays readable.
- Jerry can squash, stretch, flare, dim, and lean with emotion.
- Use black or neutral background for early casting unless plate context is being tested.

## Avoid

- Fire demon, monster, skull, horror, or villain traits.
- Human arms, legs, clothes, armor, horns, or mascot costume anatomy.
- A generic campfire.
- Any eyes, mouth, brows, nose, smile, or drawn-on face.
- Heavy smoke obscuring the flame body.
- Baked grass, dirt, plate, or scene background in core character-design images.

## Current Source References

Use these review sources before promoting anything into final assets:

- `assets/characters/jerry/look-references/external-v001/`
- `outputs/review/jerry_asset-triage_v001/single-images/storyboard-priority/`
- `outputs/review/jerry_asset-triage_v001/single-images/exr-black-stills/`
- `outputs/review/jerry_asset-triage_v001/single-images/composite-footage-stills/`
- `outputs/review/jerry_asset-triage_v001/contact-sheets/storyboards/storyboards_jerry-priority-crops_contact.jpg`

Reference roles:

- External look references define the current best no-face Jerry body direction: compact, warm, alive, and poseable.
- Storyboards define charm, expression, and character appeal, but temp faces in those references are personality and performance guides only.
- EXR black stills define flame body, color, material, and silhouette.
- Composite stills define plate scale, glow, and integration constraints.

## Current Look Direction

The strongest current direction comes from `assets/characters/jerry/look-references/external-v001/`.

Jerry's base body should be:

- A compact living flame with a rounded lower body and teardrop silhouette.
- Face-free, with no embedded eyes, mouth, brows, nose, smile, or facial marks.
- Warm yellow-white core with amber/orange outer flame and subtle ember-red rim.
- Soft enough to feel appealing and vulnerable, but still physically made of fire.
- Poseable through body shape: upright idle, leaning/curious, curled turn, comet dash, drooping/falling, and flaring.
- Isolated on black or transparent-friendly background for generation and compositing tests.

Best current still-reference categories:

- Idle body: `jerry_external-look_v001_01_upright-compact-idle.png`, `06_upright-soft-idle.png`, `09_small-upright-idle.png`, `10_round-idle-glow.png`.
- Material/detail: `03_upright-bright-core.png`, `12_upright-wild-flicker.png`, plus Run 004 as close-up material support.
- Motion/body language: `04_fast-right-comet.png`, `05_low-left-comet.png`, `07_curling-ring-turn.png`, `08_drooping-downward-pose.png`, `11_fast-left-streak.png`, `13_low-roll-comet.png`, `14_large-fast-right-comet.png`.

These references are not final approved anchors yet, but they are closer than Runs 001-004 to the desired no-face Jerry body.

## Approval Review Collection

Current approval review pack:

- `assets/characters/jerry/approval-review/v001/review_gallery.md`
- `assets/characters/jerry/approval-review/v001/approval_manifest.tsv`

Assembled bible reference set:

- `assets/characters/jerry/character-bible-v001/`
- `assets/characters/jerry/character-bible-v001/selection_manifest.tsv`

Use the `JB-###` IDs in that folder for final approval notes.

Current recommended approval read:

- Primary body look should come from `JB-001`, `JB-002`, `JB-003`, `JB-006`, `JB-009`, and `JB-010`.
- Motion and body-language references should come from `JB-004`, `JB-005`, `JB-011`, and `JB-013`.
- `JB-007` and `JB-008` are secondary/training references only; `JB-007` may be useful for Scene 12 when Jerry comes back to life.
- `JB-012` is the approved material reference.
- `JB-014`, `JB-015`, `JB-016`, and `JB-017` are excluded from the character-bible set.
- Storyboards and expression sheets are performance/face-layer references only. Their temporary eyes and mouths should not be baked into base-body renders.

## First Generation Target

Generate one clean casting still:

- Single full-body Jerry.
- Neutral or black background.
- No facial features.
- Compact flame silhouette.
- No scene background.
- No other characters.
- No text.

## First Prompt

Small sentient flame character named Jerry, full body visible, compact teardrop flame silhouette, brave but vulnerable personality expressed only through flame shape and posture, warm yellow-white inner core, orange and amber flame body, soft flickering edges, charming animated-film appeal, physically made of real fire, clean isolated character design on black background, high detail flame material, no facial features, no eyes, no mouth, no brows, no other characters.

Avoid monster, demon, skull, horror, humanoid limbs, costume, campfire logs, grass, dirt, forest, plate background, eyes, mouth, smile, face, text, logo.

## Evaluation Criteria

- Does it feel like Jerry, not a random flame?
- Does the body shape feel emotionally readable without facial features?
- Does the silhouette work as a small character?
- Does the flame material feel useful for the short film?
- Can this direction support expression sheets and motion tests?

## Next Steps After Run 001

If promising:

1. Generate 4 to 8 variations around the same design.
2. Create front, side, and 3/4 views.
3. Create body-language set: happy, worried, scared, brave, sad, surprised, using only flame posture and shape.
4. Create action set: idle, jump, land, flare, dim/vulnerable.
5. Promote selected images into `assets/characters/jerry/higgsfield-candidates/`.

If not promising:

1. Adjust prompt weight toward storyboard appeal or EXR material.
2. Try a second model: GPT Image 2 for polished design or Nano Banana Pro with fewer references.

## Run 001 Result

Local result:

- `assets/characters/jerry/higgsfield-candidates/run001/jerry_higgsfield_nano-banana-pro_casting_run001.png`

Assessment:

- Strong: cute, friendly vulnerable appeal; avoids monster/demon direction.
- Weak: missed black background; too soft/mascot-like; flame body is more painted icon than production fire material.
- Decision: keep as an appeal reference, not as an approved final Jerry design.

Run 002 should push harder toward real fire material and black-background isolation, with no embedded eyes, mouth, or facial features. Preserve the cute/vulnerable body language through silhouette only.

## Run 002 Result

Local result:

- `assets/characters/jerry/higgsfield-candidates/run002/jerry_higgsfield_nano-banana-pro_no-face-body_run002.png`

Assessment:

- Strong: obeys the no-face rule; no embedded eyes or mouth; black background; better real-fire body material than Run 001.
- Weak: less cute and less Jerry-specific; reads more like a clean flame element than a character body.
- Decision: keep as a base-body/material candidate, not approved.

Run 003 should combine the strengths of Run 001 and Run 002: no facial features, black background, real fire material, but a more compact/cute/vulnerable silhouette with stronger character posture.

## Run 003 Result

Local result:

- `assets/characters/jerry/higgsfield-candidates/run003/jerry_higgsfield_nano-banana-pro_no-face-body_run003.png`

Assessment:

- Strong: obeys the no-face rule; black background; consistent with Run 002.
- Weak: did not gain enough cute/Jerry-specific body language from the storyboard reference.
- Decision: keep as a no-face continuity candidate, not approved.

## Run 004 Result

Local result:

- `assets/characters/jerry/higgsfield-candidates/run004/jerry_higgsfield_nano-banana-pro_no-face-body_4k_run004.png`

Assessment:

- Strong: sharper 4k material; no embedded face; useful internal flame detail and glow.
- Weak: too close-up/tall; loses the small full-body Jerry silhouette.
- Decision: use as material/detail reference, not as the body anchor.

Current read:

- Run 001 is best for cute appeal, but invalid for base body because it has a face.
- Run 002/003 are best for no-face full-body silhouette, but still generic.
- Run 004 is best for sharper fire detail, but not full-body enough.
- External look references v001 are currently the best body-language and pose reference set.

Next look pass should use the external look references as the primary body/pose target, Run 004 only as material/detail reference, and the storyboard crops only as personality/performance reference. Keep strong instructions for a small full-body silhouette, negative space around the flame, and no embedded facial features.

## Run 005 Result

Local result:

- `assets/characters/jerry/higgsfield-candidates/run005/jerry_higgsfield_nano-banana-pro_final-look-candidate_run005.png`

Assessment:

- Strong: no embedded face; useful higher-resolution flame material and glow continuity.
- Weak: Run 004 dominated the output, making the flame too tall and close-up. It lost the compact external-v001 body target.
- Decision: use as material/detail support only, not as an approved body anchor.

Generation note:

- For the next body-look pass, avoid using Run 004 or Run 005 as image inputs unless the task is strictly material/upscaling. Use external-v001 body references first.

## Final-Look Prompt Seed

Create a production-ready no-face Jerry base-body reference for an animated short film. Jerry is a small living flame character with no embedded facial features: no eyes, no mouth, no brows, no nose, no smile, no face, no facial marks. Express personality only through body shape, posture, glow, and flame motion. Compact rounded lower body, soft teardrop silhouette, warm yellow-white inner core, amber/orange flame body, subtle ember-red rim, transparent wispy flame edges, contained but lively flicker, cute vulnerable brave body language. Full body visible with negative space around the flame, isolated on pure black background, high-resolution real fire material, no logs, no grass, no dirt, no scene, no text, no logo.
