**Created:** 2026-11-04
**Updated:** 2026-11-04

# Shot 004: Fire Jump

Jerry, a faceless fire character, jumps along the Houdini fire's path and lands in a grass clump, which catches fire. The plate is a locked-off 4096×2160, 24 fps, 84-frame shot (`assets/elements/by-shot/shot004_fire-jump/plates/FW_test_scene.mp4`). The delivered Houdini comp is the reference for timing: the fire lands around frame 23 and the grass catches and spreads through about frame 48.

Start here when resuming this shot: this README, then the end of the relevant log.

## State (as of 2026-11-04)

| Layer | Status | Current best | Log |
|---|---|---|---|
| Pass A: Jerry element | Candidate, not approved. Too large; the smaller guide awaits James's approval. Texture does not match the new fire. | run 9 (`s004-a-023`) | `pass-a_jerry_log.md` |
| Pass B: grass fire | Method found: first-last-frame video comped as a layer. Choosing between Seedance and Kling, then a full-resolution final. | Seedance S3 (`s004-b-020`), Kling K1 (`s004-b-021`) | `pass-b_grassfire_log.md` |
| Ground glow, ridge holdout | Done in the comp. | — | `comp_log.md` |
| Comp | Blender v002 with Pass B from S3. | `s004-c-003` | `comp_log.md` |

Next steps and methods: `plan.md`.

## Decisions

Shot-level decisions, oldest first. Project-wide decisions are in `docs/decisions.md`.

- **2026-10-17:** Pass A first: Jerry is generated as an element on black from the Houdini motion and the `JB-001` look; the plate is not an input. Grass and glow are separate layers.
- **2026-11-02 (James):** Blender is the comp tool; Fusion was built for comparison and kept for reference; Resolve stays the likely place for a final grade.
- **2026-11-02 (James):** Pass B is AI-first; the production grass-fire render is a timing reference, not the element.
- **2026-11-02 (James):** after landing, Jerry grows only slightly (about 1.2–1.3× linear by the last frame) as the grass catches; the grass carries the growth.
- **2026-11-03 (James):** plate stills and crops may go to Higgsfield and other services as references; whole plate clips stay off third-party services by default.
- **2026-11-03:** Pass B inpaint in the SkyReels graph stopped after `s004-b-017`; the fire always took the mask's shape.
- **2026-11-03 (James):** Pass B switches to first-last-frame video through the ComfyUI partner nodes (Seedance 2.0, Kling).
- **2026-11-04 (James):** comp files and every layer a saved comp loads live in `assets/`; `outputs/` holds renders and previews only.

## Where things are

- **Plan and methods:** `plan.md`. **Logs:** `pass-a_jerry_log.md`, `pass-b_grassfire_log.md`, `comp_log.md` (one entry per run or comp, each with a run ID).
- **First workflow test plan (frozen, 2026-10):** `../shot004_fire-jump_workflow-test-plan_v001.md`.
- **Assets:** `assets/elements/by-shot/shot004_fire-jump/` (`plates/`, `fire/`, `scorch-contact/` with Pass B inputs, keyframes and layers, `benchmark/` with every kept run clip, `comps/`). Each folder has a README.
- **Graphs:** `workflows/comfyui/shot004-working/` (graphs in use, by pass) and `workflows/comfyui/shot004-benchmark/` (one extract per kept run, named like its clip).
- **Renders and previews:** `outputs/shot004/` (not in Git; READMEs are).
- **Scripts:** `scripts/build_shot004_guide.py` (Pass A guide), `scripts/build_shot004_grassfire_inputs.py` (inpaint inputs), `scripts/build_shot004_grassfire_layer.py` (Pass B layer), `scripts/blender/shot004_comp_build.py` and `shot004_comp_add_passb.py` (comp).
