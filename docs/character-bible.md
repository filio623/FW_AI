# Character Bible

Date: 2026-05-18

## Purpose

Define stable identities for the film's main elemental characters so AI-generated assets remain consistent across shots, tools, prompts, and compositing workflows.

This document should guide:

- Prompt language.
- Reference image selection.
- LoRA or reference-conditioning decisions.
- Shot-specific action planning.
- Matte, alpha, and compositing requirements.

## Global Style Direction

The film should feel like a warm, expressive animated love story integrated into real environmental plates.

The characters should be appealing, readable, and emotionally clear, but they still need to behave like physical elements that can cast light, splash, burn, smoke, evaporate, or move grass and dust.

Avoid locking the look to a named studio style. Use concrete visual traits instead: feature-animation warmth, expressive body language, clean silhouettes, tactile elemental materials, and believable interaction with the plate.

Important facial-animation rule: base elemental body renders should not include embedded eyes, mouths, brows, noses, or drawn-on facial features unless explicitly testing facial animation. Faces and expressions are a separate animation/compositing layer. Storyboard panels and temp facial animation remain useful for personality, timing, and performance, but they should not force facial features into generated body assets.

## Production Rules For All Characters

- Each character needs a readable silhouette at small screen size.
- Base body renders should not include facial features; expression should be carried by shape language, motion, glow, and a separate face layer.
- Character identity should survive changes in lighting, angle, and scale.
- Generate characters as separable elements whenever possible.
- Keep interaction effects separate when revision control matters.
- Avoid baked backgrounds unless the output is only for reference.
- Record approved prompt language, reference frames, and failed prompt patterns.

## Jerry

### Role

Jerry is the small flame and one of the two main characters.

### Story Function

Jerry should feel vulnerable, energetic, brave, and emotionally open. He needs to be charming enough to carry a love story with Sally, while still physically reading as fire.

### Visual Direction

- Small sentient flame character.
- Bright inner core.
- Orange, yellow, and subtle ember-red edges.
- Clean flame silhouette.
- No embedded face in base flame-body renders.
- Warm glow that can affect nearby plate elements.
- Body shape can squash, stretch, flicker, and flare.

### Motion Direction

- Quick flickers and soft breathing motion even when still.
- Jumps should feel buoyant and flame-like, not heavy.
- Emotional changes can show through flame height, brightness, edge turbulence, and ember sparks.
- Contact with grass or dry material can motivate separate ignition passes.

### Avoid

- Monster-like fire demon.
- Full humanoid body unless specifically needed.
- Overly smoky silhouette that hides expression.
- Random facial features embedded into the flame body.
- Baked grass, dirt, or background when Jerry needs to be composited.

## Sally

### Role

Sally is the small water droplet and the other main character.

### Story Function

Sally should feel gentle, curious, emotionally intelligent, and visually distinct from Jerry. Her relationship with Jerry is central to the film.

### Visual Direction

- Small sentient water droplet character.
- Transparent or translucent blue body.
- Clean, glossy silhouette.
- Soft internal caustics and highlights.
- No embedded face in base droplet-body renders.
- Rounded, appealing shape language.
- Surface should feel liquid, not plastic or ice.

### Motion Direction

- Soft squash-and-stretch motion.
- Tiny ripples and surface wobble when reacting.
- Can splash, stretch, compress, and reform.
- Emotional changes can show through body shape, internal highlights, and droplet trembling.

### Avoid

- Ice creature.
- Opaque plastic blob.
- Generic slime character.
- Excessive internal detail that makes separate facial animation hard to read.
- Baked background when Sally needs to be composited.

## Tom

### Role

Tom is the much bigger fire and the main villain.

### Story Function

Tom should feel dangerous, dominant, and intimidating compared with Jerry. He is fire at a larger, more threatening scale.

### Visual Direction

- Large sentient fire character.
- More aggressive flame shape than Jerry.
- Deeper reds, hotter whites, darker smoke accents, and harsher edge turbulence.
- Stronger glow and environmental impact.
- No embedded face in base fire-body renders.
- Scale difference from Jerry must be obvious.

### Motion Direction

- Slower, heavier, more forceful flame movement.
- Larger flare-ups and bursts.
- Can drive smoke, heat distortion, scorch, and spreading fire passes.
- Should feel like a threat to the environment and to Jerry/Sally.

### Avoid

- Looking like just a scaled-up Jerry.
- Random horror-monster detail that breaks the film's emotional tone.
- Complex flames that would make separate facial animation hard to read.
- Over-baking villain effects into a plate when separate passes are needed.

## Wind Character

### Role

The wind character is a supporting character with limited appearance who helps Jerry.

### Story Function

This character should feel helpful, quick, light, and possibly playful. The character may be more abstract than Jerry, Sally, or Tom.

### Visual Direction

- Small gust of wind with readable personality through shape and motion.
- Semi-transparent wisps or ribbon-like motion.
- No embedded face in base wind-body renders unless explicitly testing facial animation.
- Shape should be distinct from smoke and steam.
- May interact with dust, grass, embers, water spray, or flame direction.

### Motion Direction

- Fast arcs, swirls, curls, and pushes.
- Can help move Jerry, redirect flame, clear smoke, or create a small burst of motion.
- Should be choreographed carefully so it reads as character action, not just environmental wind.

### Avoid

- Looking like smoke from fire.
- Looking like steam from Sally.
- Being too invisible to track emotionally.
- Overcomplicated wisps that cannot be matted cleanly.

## Character Relationship Notes

- Jerry and Sally are the emotional center.
- Jerry and Sally should contrast materially while sharing enough shape-language warmth to feel like they belong in the same film.
- Tom should be recognizably related to fire but visually and behaviorally distinct from Jerry.
- The wind character should support Jerry without competing for attention.

## Initial Workflow Implications

- Build approved stills for Jerry and Sally before training LoRAs.
- Use Tom as a separate identity, not a variant of Jerry.
- Treat the wind character as a later secondary design unless a test shot requires it.
- For the first fire/grass workflow test, focus on Jerry identity, Jerry motion, grass ignition, and separate interaction passes.
- Keep Sally in the bible now, but avoid blocking the first fire workflow on her final design.

## Open Questions

- What are the final names and personality notes for the wind character?
- What is the final separate facial-animation style for Jerry, Sally, Tom, and Wind?
- How stylized should the characters be relative to realistic plates?
- Are the current CGI renders meant to define final proportions, or only motion and placement?

## Approved References

Add approved stills, clips, and notes here as they are selected.

- Jerry: see `assets/characters/jerry/approved/` and `workflows/higgsfield/jerry/jerry_higgsfield-casting-log_v001.md`.
- Sally:
- Tom: draft only; see `docs/tom-character-bible_v001.md` and `references/manifests/tom_external-drive_reference_inventory_v001.md`. Do not promote references until Robbie review is complete.
- Wind:

## Prompt Seeds

These are draft seeds only. Promote working prompts to `prompts/` after testing.

### Jerry

Small sentient flame character named Jerry, expressive body language through flame shape only, no facial features, bright warm inner core, orange and yellow flame body with subtle ember edges, clean silhouette, charming and brave, soft animated-feature appeal, casts warm light, isolated element, no background.

### Sally

Small sentient water droplet character named Sally, transparent blue liquid body, no facial features, glossy surface, soft internal caustics, clean silhouette, emotionally expressive through shape and motion, squash and stretch motion, isolated element, no background.

### Tom

Large sentient fire villain named Tom, towering flame body, no facial features, aggressive flame silhouette, hot white core with orange red edges, darker smoke accents, powerful glow, threatening but still emotionally readable through shape and motion, isolated element, no background.

### Wind

Small helpful gust of wind character, semi-transparent curling wisps, light playful motion, friendly personality through shape and motion, no facial features, distinct from smoke or steam, clean silhouette, isolated element, no background.
