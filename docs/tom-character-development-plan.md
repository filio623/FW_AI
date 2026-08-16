**Created:** 2026-05-21
**Modified:** 2026-08-16
**Version:** 1.1

# Tom Character Development Plan

Status: draft plan. Do not treat any Tom reference as final until Robbie reviews and approves it.

## Purpose

Develop Tom, the larger villain fire character, into a consistent visual identity that can be used across Higgsfield, ComfyUI, reference-conditioning tests, and final compositing workflows.

Tom should be built as his own character identity, not as a scaled-up Jerry variant.

## Review-First Rule

Tom needs a human review gate before anything is promoted into an approved character bible.

Working rule:

- `docs/tom-character-bible_v001.md` is a draft design and prompt document.
- `assets/characters/tom/source-cgi/`, `actions/`, `expressions/`, `look-references/`, and `training-candidates/` can hold candidates.
- `assets/characters/tom/approval-review/v001/` is where selected candidates should be organized for Robbie review.
- `assets/characters/tom/approved/` stays empty until Robbie explicitly approves specific images or clips.
- `assets/characters/tom/character-bible-v001/` should only be assembled after the approval review is complete.

## What To Collect First

Gather only material that helps define Tom's identity, motion, or production constraints.

### High Priority

- Existing CGI renders of Tom or large fire passes.
- Frames where Tom's scale relative to Jerry, Sally, trees, or the plate is clear.
- Frames where Tom's silhouette reads as threatening without becoming a generic monster.
- The Tom 2D character/action sheet.
- Storyboard panels or script beats where Tom beckons, consumes Jerry, reacts to Sally, grows, or is extinguished.
- Rough or finished comp clips showing Tom's intended plate scale and environmental impact.

### Medium Priority

- External visual references for large fire behavior, ember sheets, smoke accents, heat distortion, scorch, and glow.
- Motion references for flare-ups, slow looming movement, spreading fire, recoiling from water, and being extinguished.
- Notes from director/editor about how scary, stylized, or emotionally readable Tom should feel.

### Low Priority For Now

- Final LoRA training sets.
- Full shot replacement generations.
- Long video generations.
- Polished composites before the approved body language is clear.

## Known Source Leads

Initial local/drive scan found these likely high-value sources:

- `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Tom.png`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/shot_8H_comp_v07.mov`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/render_dn/Tom_DN/`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8G/render/Combined__tom_v001/`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8G/render_dn/Tom_DN/`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/ren_big_fire_shot 8L/`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/Shot_8L/shot_8L_anim_v05.mov`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/Shot_8L/render_dn/Tom_DN/`
- `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/Renders/8L_Comp_V1.mov`

Keep full EXR sequences on the external drive. Pull only proxies, contact sheets, and selected stills into this repo.

## Where To Put Material

Use `assets/inbox/` for new unsorted uploads.

After review, copy or move curated material into:

- `assets/characters/tom/source-cgi/`: existing CGI renders, extracted stills, and proxy references of Tom or large fire.
- `assets/characters/tom/look-references/`: curated references that define Tom's body look, silhouette, material, scale, and movement language.
- `assets/characters/tom/higgsfield-candidates/`: generated stills or clips that may be useful.
- `assets/characters/tom/approval-review/`: review packs with stable candidate IDs, galleries, manifests, and notes.
- `assets/characters/tom/approved/`: selected visual anchors only after Robbie approval.
- `assets/characters/tom/expressions/`: emotion and face-layer references.
- `assets/characters/tom/actions/`: looming, beckoning, consuming, recoiling, growing, extinguishing, and other action references.
- `assets/characters/tom/training-candidates/`: reviewed images that may later be useful for LoRA, Soul, or other character systems.
- `assets/storyboards/tom/`: storyboard panels that primarily define Tom.

Do not overwrite or rename original irreplaceable files. Keep original uploads intact, then make curated copies with clearer names.

## Naming Pattern

Use character-first names for reusable Tom material:

`tom_fire_villain_looming_ref_v001.png`

Use shot-first names when the material only belongs to one shot:

`shot008h_tom_sally-impact_ref_v001.png`

Use generated-candidate names for model outputs:

`tom_higgsfield_casting_nano-banana-pro_v001.png`

## Recommended Sequence

### Step 1: Source Inventory

Goal: identify the best existing Tom references before generating anything new.

Create:

- A narrow Tom source manifest.
- Contact sheets for Tom VFX clips and EXR-derived stills.
- A small selected-stills folder for review.

Evaluate:

- Does Tom read as a character or just a wall of fire?
- Is the scale relationship to Jerry/Sally clear?
- Does the silhouette feel threatening without breaking the film's emotional tone?
- Are there clear poses for beckoning, consuming Jerry, reacting to Sally, and being extinguished?

### Step 2: Approval Review Pack

Goal: let Robbie choose what defines Tom before anything becomes canonical.

Create:

- `assets/characters/tom/approval-review/v001/review_gallery.md`
- `assets/characters/tom/approval-review/v001/approval_manifest.tsv`
- Stable IDs such as `TB-001`, `TB-002`, and later.

Review categories should mirror Jerry where practical:

- `primary-body`: main body/look candidates.
- `motion-poses`: action and body-language candidates.
- `material`: fire, smoke, glow, heat, and edge-behavior support.
- `secondary-training`: useful but not primary identity anchors.
- `source-ref-only`: CGI or plate references that guide scale/material but are not ideal training images.
- `performance-2d-ref-only`: 2D sheet/storyboard/expression references only.

### Step 3: Draft Generation Tests

Goal: test whether selected references can produce a clean, face-free Tom body.

Generate:

- Full-body neutral-background Tom.
- Front/3/4 looming pose.
- Beckoning pose.
- Water-impact/recoiling pose.
- Transparent-friendly dark or neutral background element.

Evaluate:

- Does Tom stay distinct from Jerry?
- Does Tom avoid horror-demon overdesign?
- Can the design support separate facial animation?
- Can it be matted and composited without baked background problems?

### Step 4: Bible Assembly After Review

Only after Robbie approval:

- Promote selected images into `assets/characters/tom/approved/`.
- Assemble `assets/characters/tom/character-bible-v001/`.
- Update `docs/tom-character-bible_v001.md` with approved IDs.
- Update `docs/character-bible.md` under Approved References.
- Record the review decision in this plan and in `docs/findings.md`.

## First Deliverable

The first Tom milestone is:

- A Tom source inventory.
- A review pack plan with categories and stable IDs.
- 6 to 12 source-derived or generated candidate stills for Robbie review.
- No final approved Tom bible until review decisions are recorded.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-21 | Initial Tom Character Development Plan. |
| 1.1     | 2026-08-16 | Removed Supermemory references after its retirement; project memory now lives in the repository. |
