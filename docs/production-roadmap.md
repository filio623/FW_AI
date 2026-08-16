**Created:** 2026-05-18
**Modified:** 2026-08-16
**Version:** 1.1

# AI VFX Production Roadmap

## Purpose

Build a repeatable workflow for generating consistent fire and water characters as controllable VFX elements over existing plates.

The goal is not to generate full replacement shots. The goal is to generate character and interaction elements that can be revised, layered, and composited.

## Guiding Principle

Treat the work as VFX first and AI video second.

Every production workflow should preserve:

- The original plate.
- Character control.
- Alpha or matte control.
- Separate interaction passes.
- A path for director notes and revisions.

## Target Deliverables Per Shot

Each shot should aim to produce:

- Untouched plate.
- Fire character RGB.
- Water character RGB when needed.
- Character alpha or matte.
- Occlusion matte from the plate.
- Contact shadow.
- Glow or contact light.
- Interaction pass such as grass fire, scorch, smoke, steam, splash, wetness, or heat distortion.
- Composite notes and review export.

## Working Phases

### Phase 1: Inspect And Organize Source Assets

Goal: know exactly what is in the current plates and CGI reference renders.

Tasks:

- Verify codec, duration, resolution, frame rate, and alpha status for every `FW_test/Scene 4/` video.
- Extract representative stills from the base plate and CGI renders.
- Identify which CGI renders are character reference, motion reference, or interaction reference.
- Store shot-specific notes in `shots/`.
- Store reusable stills or curated references in `assets/` or `references/`.

Decision point:

- If the CGI renders contain usable alpha, use them as direct comp/proxy inputs.
- If they do not, treat them as visual and motion references only.

### Phase 2: Build The Character Bible

Goal: define stable character identities before doing expensive generation.

Tasks:

- Maintain `docs/character-bible.md` as the shared style/rules source and character index.
- Maintain each character's own bible as the durable identity source: `docs/jerry-character-bible_v001.md`, `docs/tom-character-bible_v001.md`, and Sally/Wind inside the shared bible until they earn their own.
- Create approved fire character stills.
- Create approved water character stills.
- Define scale, silhouette, face readability, material behavior, and personality.
- Build action states: idle, jump, land, flare, extinguish, splash, react.
- Update `prompts/fire-water-character-language.md` with accepted prompt wording and failure modes.

Decision point:

- Do not train LoRAs until the desired character look is clear and there are enough usable stills.

### Phase 3: Establish The First Test Shot Workflow

Goal: use one real shot to prove the pipeline.

Test shot:

- Jerry jumps across dirt/grass.
- Fire enters grass.
- Grass ignites.
- Firelight, smoke, heat, and scorch integrate with the plate.

Primary plan file:

- `shots/shot004_fire-jump_workflow-test-plan_v001.md`

Success criteria:

- The plate remains untouched.
- The fire character can be revised independently from the grass ignition.
- The fire has a usable matte or alpha.
- Interaction passes can be timed independently.
- The final composite can survive basic notes without regenerating everything.

### Phase 4: Compare Workflow Branches

Goal: identify which generation path is most production-useful.

Branches:

- Proxy/CGI to AI polish: use existing CGI or rough animation as structure, then stylize with AI.
- Alpha-native generation: test Wan-Alpha or similar RGBA workflows for clean compositable fire/water elements.
- Controlled I2V or first-last-frame generation: use first/last/keyframes to direct motion.
- Cloud reference generation: use Higgsfield, Runway, Kling, Seedance, or similar tools for motion and look references.
- Interaction-only generation: create grass fire, smoke, scorch, glow, and heat distortion separately.

Evaluation criteria:

- Character consistency.
- Motion control.
- Matte quality.
- Plate integration.
- Revision cost.
- Render time.
- Setup complexity.

### Phase 5: Convert The Winning Branch Into Templates

Goal: turn experiments into reusable production assets.

Tasks:

- Save working ComfyUI workflows under `workflows/comfyui/`.
- Save cloud commands and settings under `workflows/higgsfield/` or another provider folder.
- Save prompts under `prompts/`.
- Save shot logs under `shots/`.
- Save findings under `docs/findings.md`.
- Add reusable agent instructions under `skills/` when a workflow becomes repeatable.

### Phase 6: Scale To Additional Shots

Goal: apply the proven approach to the rest of the film.

For each new shot:

- Create a shot plan from `shots/shot-template.md`.
- Identify required characters and interaction passes.
- Choose the simplest proven workflow branch.
- Log generation settings, failures, and final comp notes.
- Promote reusable discoveries back into docs, prompts, workflows, and skills.

## Near-Term Checklist

- Verify `FW_test/Scene 4/` video metadata and alpha status.
- Create the shot004 fire-jump plan.
- Extract still references from plate and CGI renders.
- Run one proxy/CGI-to-AI-polish test.
- Run one alpha-native fire element test.
- Run one cloud reference generation test.
- Composite a rough layered proof of concept.
- Decide which branch becomes the first reusable workflow template.

## Current Bias

The most likely production path is:

1. Use CGI or simple proxy animation for timing and silhouette.
2. Use AI to improve the character look while preserving motion control.
3. Generate or extract alpha/matte.
4. Generate interaction passes separately.
5. Composite in a real compositing app.

Pure text-to-video should remain an exploration tool, not the final production backbone.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial AI VFX Production Roadmap. |
| 1.1     | 2026-08-16 | Updated Phase 2 for the split between the shared character bible and the per-character frozen editions. |
