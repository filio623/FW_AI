**Created:** 2026-05-18
**Modified:** 2026-05-18
**Version:** 1.0

# Jerry Character Development Plan

## Purpose

Develop Jerry, the small flame main character, into a consistent visual identity that can be used across Higgsfield, ComfyUI, LoRA/reference-conditioning tests, and final compositing workflows.

This is the first character-development track because Jerry is needed for the `shot004_fire-jump` workflow test.

## What To Collect First

Gather only material that helps define Jerry's identity, motion, or production constraints.

### High Priority

- Existing CGI renders of Jerry.
- Frames where Jerry's silhouette is clear.
- Frames where Jerry's face or expression reads clearly.
- Storyboard panels showing Jerry's important poses or emotional beats.
- Script excerpts that define Jerry's personality, actions, and relationship to Sally.
- Rough VFX shots showing Jerry's intended scale in a plate.

### Medium Priority

- External visual references for flame behavior, glow, embers, or appealing shape language.
- Motion references for jumping, flickering, landing, hiding, flaring, or reacting.
- Notes from director/editor about what Jerry should feel like.

### Low Priority For Now

- Final LoRA training sets.
- Full shot replacement generations.
- Highly polished composites.
- Long video generations.

## Where To Put Material

Use `assets/inbox/` for new unsorted uploads.

After review, copy or move curated material into:

- `assets/characters/jerry/source-cgi/`: existing CGI renders or extracted CGI stills of Jerry.
- `assets/characters/jerry/higgsfield-candidates/`: generated stills or clips from Higgsfield that may be useful.
- `assets/characters/jerry/approved/`: selected visual anchors for Jerry.
- `assets/characters/jerry/expressions/`: emotion and face references.
- `assets/characters/jerry/actions/`: jump, land, idle, flare, and other action references.
- `assets/characters/jerry/training-candidates/`: reviewed images that may later be useful for LoRA, Soul, or other character systems.
- `assets/storyboards/jerry/`: storyboard panels that primarily define Jerry.

Do not overwrite or rename original irreplaceable files. Keep original uploads intact, then make curated copies with clearer names.

## Naming Pattern

Use character-first names for reusable Jerry material:

`jerry_fire_idle_ref_v001.png`

Use shot-first names when the material only belongs to one shot:

`shot004_fire-jump_jerry_landing_ref_v001.png`

Use Higgsfield run names for generated candidates:

`jerry_higgsfield_casting_soul-v2_v001.png`

## Higgsfield Role

Use Higgsfield for character casting, look exploration, and motion reference.

Do not use Higgsfield as the only production workflow for Jerry unless a test proves the output is controllable and separable enough for compositing.

Best initial Higgsfield uses:

- Generate still-image casting options for Jerry.
- Create expression/action sheets after a look direction is chosen.
- Animate approved stills into short motion references.
- Compare several models on the same prompt.
- Explore how Jerry should feel emotionally before building controlled ComfyUI workflows.

Avoid at first:

- Full-shot baked video over the plate.
- Long video generations.
- Expensive 1080p tests before a look is approved.
- Training character systems before the desired Jerry look is clear.

## Recommended Higgsfield Sequence

### Step 1: Casting Stills

Goal: find the right Jerry design.

Generate batches of still images with:

- Isolated or neutral background.
- Full-body readable silhouette.
- Simple face.
- No plate background.
- No grass, dirt, or full scene.

Evaluate:

- Is Jerry appealing?
- Does he read as small and sentient?
- Is he fire, not a creature wearing fire?
- Is the silhouette clean enough for alpha/matte work?
- Does the face survive at small size?

### Step 2: Controlled Variations

Goal: test whether the chosen look survives different poses.

Generate:

- Idle.
- Happy.
- Worried.
- Brave.
- Jumping.
- Landing.
- Flaring up.
- Dimmed or vulnerable.

Evaluate:

- Does the same character come through?
- Do face and silhouette remain stable?
- Does the model invent unwanted limbs or monster traits?

### Step 3: Motion References

Goal: create short clips that guide timing and performance.

Generate:

- 3 to 5 second idle flicker.
- 3 to 5 second jump.
- 3 to 5 second landing and flare.

Use these as reference only unless they can be separated cleanly.

### Step 4: Production Handoff

Goal: convert the best results into ComfyUI and comp inputs.

Move approved stills to:

- `assets/characters/jerry/approved/`

Update:

- `docs/character-bible.md`
- `prompts/fire-water-character-language.md`
- `workflows/higgsfield/jerry/`
- `docs/findings.md`

## UI Or Agent/CLI?

Use the Higgsfield UI when you want fast visual browsing and manual comparison.

Use the CLI or agent workflow when:

- We need repeatable settings.
- We want exact prompts recorded.
- We want model/cost comparisons.
- We want outputs logged consistently.

Current practical recommendation:

- Start in the Higgsfield UI for Jerry casting if that feels faster.
- Save or download promising outputs.
- Put candidates in `assets/characters/jerry/higgsfield-candidates/`.
- Record the prompt/model/output URL in `workflows/higgsfield/jerry/jerry_higgsfield-casting-log_v001.md`.
- Once we know what looks promising, use the CLI for more controlled repeatable runs.

## MCP / Agent Support

This Codex session currently has Supermemory and ComfyUI MCP tools available, but not a Higgsfield MCP tool.

I can still help with Higgsfield by:

- Writing prompts.
- Creating run plans.
- Reading and organizing downloaded outputs.
- Logging UI results.
- Running the installed Higgsfield CLI if network/auth access is available in the shell.
- Comparing results and deciding what becomes approved reference.

If Higgsfield MCP is added to Codex later, we can move more of the generation loop directly into the agent.

## First Deliverable

The first Jerry milestone is:

- 6 to 12 Higgsfield still candidates.
- 2 or 3 approved Jerry design anchors.
- A short note explaining why the approved design works.
- Updated prompt language.
- One short motion-reference test after approval.

Do not start LoRA training until this milestone is complete.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Jerry Character Development Plan. |
