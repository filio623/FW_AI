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

- `outputs/review/jerry_asset-triage_v001/single-images/storyboard-priority/`
- `outputs/review/jerry_asset-triage_v001/single-images/exr-black-stills/`
- `outputs/review/jerry_asset-triage_v001/single-images/composite-footage-stills/`
- `outputs/review/jerry_asset-triage_v001/contact-sheets/storyboards/storyboards_jerry-priority-crops_contact.jpg`

Reference roles:

- Storyboards define charm, expression, and character appeal, but temp faces in those references are personality and performance guides only.
- EXR black stills define flame body, color, material, and silhouette.
- Composite stills define plate scale, glow, and integration constraints.

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
