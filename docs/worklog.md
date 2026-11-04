**Created:** 2026-11-03
**Updated:** 2026-11-04

# Worklog

What was done when, one entry per working day, newest at the bottom. Each entry is a short summary with pointers to where the detail lives; it is not where decisions or scores are recorded. This is an append-only log: add an entry at the end of each session and never edit an old one. Entries up to 2026-11-02 were written on 2026-11-03 from the Git history.

## 2026-05-18

- Set up the VFX workflow workspace: folder layout, first docs, `AGENTS.md`.

## 2026-05-27

- Added the first character workflow assets (`characters/`).

## 2026-08-03

- Set up RunPod for ComfyUI (`mcp/runpod.md`).

## 2026-08-16

- Added the RunPod Pod lifecycle scripts (`scripts/runpod-pod-up.sh`, `runpod-pod-down.sh`) and fixed the Cloudflare proxy access.
- Set the document lifecycle and versioning policy (`AGENTS.md`) and reorganized the docs.
- Expanded the ComfyUI learning path (since archived).
- Retired Supermemory; the repo became the only project memory (`docs/archive/mcp/supermemory.md`).

## 2026-10-08

- Recovered the shot 004 VACE test and archived obsolete guides (`shots/shot004_fire-jump/workflow-test-plan_v001.md`).

## 2026-10-17

- Set up the Blender MCP bridge and built the first Jerry fire rig (`characters/jerry/fire-rig/jerry_fire-rig_log_v001.md`).
- Started the shot 004 Pass A element benchmark (`docs/archive/docs/vfx-element-benchmark.md`); scored Wan 2.7 Video Edit runs.
- Updated environment, findings, asset inventory, the MCP index and the Higgsfield skills.

## 2026-10-18

- Restructured the benchmark into a staged test matrix and cut its cost.
- Scored Wan 2.7 runs 3–4 and stopped Wan 2.7 tuning for shot 004.
- Set up the Mickmumpitz 1.3 SkyReels stack on the RunPod volume (node installs, Lenovo LoRA, run settings).

## 2026-10-19

- Built the Mickmumpitz workflow library and its sorter (`library/mickmumpitz-library.md`).
- Scored Mick 1.3 SkyReels runs 1–8 for Pass A; run 8 became the baseline. Queued NAG, 720p and a comp check.

## 2026-11-01

- First comp preview of run 8 over the plate; recorded James's review notes (`shots/shot004_fire-jump/plan.md`).
- Recorded the CA-MTL-1 outage, which stranded the old volume.

## 2026-11-02

- Wrote the shot 004 comp and Pass B plan; chose Blender for the comp. Built Blender Comp v001 and a Fusion comp in Resolve for comparison; stayed in Blender.
- Built the smaller Jerry guide (`shots/shot004_fire-jump/scripts/build_shot004_guide.py`); it awaits James's approval. Recorded Jerry's post-landing growth decision.
- Rebuilt the ComfyUI volume in EU-RO-1 with `scripts/runpod/setup_mick13_volume.sh`; replaced the crashing WanVideoNAG patch.
- Pass A: run 8r (run 8 reproduced on the new volume) and run 9 (NAG with face negatives). Deferred 720p behind the smaller guide.
- Pass B: set up the grass-fire inpaint (inputs, graph, workflow folders); scored tests 1–2. Found the dark mask ring and its comp fix. Recorded MiniMax H3 as a candidate.

## 2026-11-03

- A100 Pod on the EU-RO-1 volume. Pass B tests 3–7 (`shots/shot004_fire-jump/pass-b_grassfire/log.md`): prompt rewrite, `vace_strength` 0.6, an exact-rerun check, gray inside the mask (best interaction, too wild), and a calmer prompt (a floating flame ribbon, worse).
- Allowed plate stills and crops as Higgsfield references (`docs/findings.md`); built keyframe inputs for James's colleague.
- Documented the ComfyUI workflow layout and naming (`workflows/comfyui/README.md`).
- Made the GitHub repo private. Moved the Mickmumpitz library into `library/mickmumpitz/`. Reorganized `outputs/` by shot and pass.
- Added a README to every working folder, including `outputs/` (READMEs are now tracked there); moved the Pass B tests into their own log; started this worklog.

## 2026-11-03, afternoon

- Pass B tests 8–14 on the A100 (`shots/shot004_fire-jump/pass-b_grassfire/log.md`):
  - Tests 8–9: two more seeds of test 6. The size is the same; smoke and interaction change with the seed.
  - Test 10: `vace_strength` 0.8 with extra negatives. About the same.
  - Tests 11 and 11b: James's combined mask (blades at full strength, the rest at half). A gray veil, then pale tubes on the thin blade strips; branch stopped.
  - Tests 12–13: Higgsfield keyframe `k2` as a reference at 0.4 and 1.0. No real change.
  - Test 14: `k2` inside the clip on frames 49–52. The first real change of look: soft peach tongues among the blades after frame 53, but a glowing dome before it.
- Received four Higgsfield keyframes from James's colleague; registered them to the plate and the Pass B window (`shots/shot004_fire-jump/pass-b_grassfire/keyframes/`).
- Grass input builder gained the combined mask, edges on gray, and keyframe groups (`shots/shot004_fire-jump/scripts/build_shot004_grassfire_inputs.py`).
- Pod terminated; next is test 15, the keyframe on three groups (`mcp/runpod.md`, resume point).

## 2026-11-03, evening (to about 00:50 UTC on 2026-11-04)

- RTX 4090 Pod (no A100 in stock). Pass B tests 14r and 15 (`shots/shot004_fire-jump/pass-b_grassfire/log.md`): keyframes inside the inpaint fixed the look but the growth stayed mask-shaped; James: not a success.
- Switched Pass B to first-last-frame video through ComfyUI API nodes: the clean plate at frame 25 to keyframe `k2`. Seedance S1 (window), S2 (full frame, `k2` on the plate background: framing and regrade fixed), S3–S4 (timing; S4 ≈ S3, prompt timing words barely change a sample), Kling K1 (1080p, the most natural ignition, slow).
- First comp check: S3 as a Pass B layer in the Blender comp (`shots/shot004_fire-jump/outputs/comp/blender/passb_s3/`), built by the new `shots/shot004_fire-jump/scripts/build_shot004_grassfire_layer.py` and `shots/shot004_fire-jump/scripts/blender/shot004_comp_add_passb.py`. Works as a layer; soft at 480p; Jerry's texture does not match the fire (James).
- Pod terminated; resume point in `mcp/runpod.md`.

## 2026-11-04

- Housekeeping and a new record-keeping system, approved by James (`docs/decisions.md`, 2026-11-04 entries):
  - `AGENTS.md` rewritten from about 2,000 to about 1,000 words: shorter document rules (living docs carry Created/Updated only; Git keeps history), records (run IDs, what goes where, timestamps), placement rule, working rules, tool paths.
  - One folder per shot: `shots/shot004_fire-jump/` with `README.md`, `plan.md` (cut from 5,600 to about 3,000 words), `pass-a_jerry/log.md` (new, from the benchmark doc, runs `s004-a-001`–`023`), `pass-b_grassfire/log.md` (moved; run ID map `s004-b-001`–`022` appended), `comp_log.md` (`s004-c-001`–`003`). Templates in `shots/_template/`.
  - `mcp/runpod.md` cut to current setup and state; its history moved to the append-only `mcp/runpod_log.md`.
  - New `docs/decisions.md` register.
  - Version lines and changelog tables removed from 29 living docs (about 2,500 words).
  - Retired to `docs/archive/`: `docs/vfx-element-benchmark.md`, `docs/environment.md`, `docs/AGENTS-CHANGELOG.md`, `docs/production-roadmap.md`, `docs/comfyui-vfx-workflow-strategy.md`, the three project skills. Removed: the eight Higgsfield companion skills and four unused Comfy Cloud/Codex MCP scripts. Comfy Cloud parked.
  - Comp v002 (`assets/…/comps/shot004_fire-jump_comp-blender_run8-passb-s3_v002.blend`) and its layer (`assets/…/scorch-contact/layers/shot004_fire-jump_grassfire-layer-s3_v001/`) moved into `assets/`; renders identically. The delivered comp copy renamed `shot004_fire-jump_comp-houdini-delivered-v031_1920x1080_v001.mp4`.
  - Unused `outputs/` folders (Fusion renders, first previews, early Pass A tests) archived to `shots/shot004_fire-jump/outputs/_archive/2026-11-04/`.
  - Paths of moved docs were updated inside the append-only logs too (path-only edits, no content changes), so their links still resolve.
- Shot-first restructure (James, later the same day; rewind point: Git tag `pre-restructure-2026-11-04`):
  - Everything for shot 004 moved into `shots/shot004_fire-jump/`: `plates/`, `reference/`, `comps/`, `scripts/`, `outputs/`, and per pass `log.md`, `inputs/`, `workflows/`, `runs/` (each kept clip beside its extracted workflow), plus Pass B `keyframes/` and `layers/`.
  - Project-wide: `characters/<name>/` (bibles and development plans moved in from `docs/`), `source/` (screenplay), `inbox/`, `library/` (was `references/`). `assets/` is gone; empty scaffold folders removed.
  - Paths updated in all docs, READMEs and scripts (logs: path-only). Script roots fixed and checked; both Blender comps repointed, v002 renders identically.
  - Every move, including untracked media: `docs/archive/restructure_2026-11-04_moves.tsv`.

