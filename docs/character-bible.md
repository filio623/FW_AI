**Created:** 2026-05-18
**Modified:** 2026-08-16
**Version:** 2.0

# Character Bible

## Purpose

Define stable identities for the film's main elemental characters so AI-generated assets remain consistent across shots, tools, prompts, and compositing workflows.

This document owns what is **shared** across characters: global style direction, production rules, relationships, and the index of per-character bibles. It also holds the full specs for Sally and the wind character, which do not have their own bibles yet.

Characters with their own frozen edition are specified there, not here. Do not restate a character's visual rules, avoid-list, or prompt seed in this file — one spec per character.

## Character Index

| Character | Role | Specification |
|---|---|---|
| Jerry | Small flame, lead | `docs/jerry-character-bible_v001.md` |
| Sally | Small water droplet, lead | This document, below |
| Tom | Large fire, villain | `docs/tom-character-bible_v001.md` |
| Wind | Supporting helper | This document, below |

Development plans, which cover process rather than identity, live in `docs/jerry-character-development-plan.md` and `docs/tom-character-development-plan.md`.

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

## Sally

### Role

Sally is the small water droplet and one of the two main characters.

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

### Prompt Seed

Draft only. Promote working prompts to `prompts/` after testing.

Small sentient water droplet character named Sally, transparent blue liquid body, no facial features, glossy surface, soft internal caustics, clean silhouette, emotionally expressive through shape and motion, squash and stretch motion, isolated element, no background.

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

### Prompt Seed

Draft only. Promote working prompts to `prompts/` after testing.

Small helpful gust of wind character, semi-transparent curling wisps, light playful motion, friendly personality through shape and motion, no facial features, distinct from smoke or steam, clean silhouette, isolated element, no background.

## Character Relationship Notes

- Jerry and Sally are the emotional center.
- Jerry and Sally should contrast materially while sharing enough shape-language warmth to feel like they belong in the same film.
- Tom should be recognizably related to fire but visually and behaviorally distinct from Jerry. The scale difference from Jerry must be obvious.
- The wind character should support Jerry without competing for attention.

## Initial Workflow Implications

- Build approved stills for Jerry and Sally before training LoRAs.
- Use Tom as a separate identity, not a variant of Jerry.
- Treat the wind character as a later secondary design unless a test shot requires it.
- For the first fire/grass workflow test, focus on Jerry identity, Jerry motion, grass ignition, and separate interaction passes.
- Keep Sally in this bible now, but avoid blocking the first fire workflow on her final design.

## Approved References

Nothing is approved into an `approved/` folder for any character yet.

- Jerry: current reference set is `assets/characters/jerry/character-bible-v001/`, with casting history in `workflows/higgsfield/jerry/jerry_higgsfield-casting-log_v001.md`. Approved anchors would land in `assets/characters/jerry/approved/`.
- Sally: no references collected yet.
- Tom: draft only. See `docs/tom-character-bible_v001.md` and `references/manifests/tom_external-drive_reference_inventory_v001.md`. Do not promote references until Robbie review is complete.
- Wind: no references collected yet.

## Open Questions

- What are the final names and personality notes for the wind character?
- What is the final separate facial-animation style for Jerry, Sally, Tom, and Wind?
- How stylized should the characters be relative to realistic plates?
- Are the current CGI renders meant to define final proportions, or only motion and placement?

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Character Bible. |
| 2.0     | 2026-08-16 | Archived v1.0 and restructured as the shared-rules document and character index: Jerry and Tom now point at their frozen editions, Sally and Wind keep full specs here, and the approved-reference list was corrected against what exists. |
