**Created:** 2026-11-03
**Modified:** 2026-11-03
**Version:** 1.0

# Worklog

What was done when, one entry per working day, newest at the bottom. Each entry is a short summary with pointers to where the detail lives; it is not where decisions or scores are recorded. This is an append-only log: add an entry at the end of each session and never edit an old one. Entries up to 2026-11-02 were written on 2026-11-03 from the Git history.

## 2026-05-18

- Set up the VFX workflow workspace: folder layout, first docs, `AGENTS.md`.

## 2026-05-27

- Added the first character workflow assets (`assets/characters/`).

## 2026-08-03

- Set up RunPod for ComfyUI (`mcp/runpod.md`).

## 2026-08-16

- Added the RunPod Pod lifecycle scripts (`scripts/runpod-pod-up.sh`, `runpod-pod-down.sh`) and fixed the Cloudflare proxy access.
- Set the document lifecycle and versioning policy (`AGENTS.md`) and reorganized the docs.
- Expanded the ComfyUI learning path (since archived).
- Retired Supermemory; the repo became the only project memory (`docs/archive/mcp/supermemory.md`).

## 2026-10-08

- Recovered the shot 004 VACE test and archived obsolete guides (`shots/shot004_fire-jump_workflow-test-plan_v001.md`).

## 2026-10-17

- Set up the Blender MCP bridge and built the first Jerry fire rig (`workflows/blender/jerry/jerry_fire-rig_log_v001.md`).
- Started the shot 004 Pass A element benchmark (`docs/vfx-element-benchmark.md`); scored Wan 2.7 Video Edit runs.
- Updated environment, findings, asset inventory, the MCP index and the Higgsfield skills.

## 2026-10-18

- Restructured the benchmark into a staged test matrix and cut its cost.
- Scored Wan 2.7 runs 3–4 and stopped Wan 2.7 tuning for shot 004.
- Set up the Mickmumpitz 1.3 SkyReels stack on the RunPod volume (node installs, Lenovo LoRA, run settings).

## 2026-10-19

- Built the Mickmumpitz workflow library and its sorter (`references/mickmumpitz-library.md`).
- Scored Mick 1.3 SkyReels runs 1–8 for Pass A; run 8 became the baseline. Queued NAG, 720p and a comp check.

## 2026-11-01

- First comp preview of run 8 over the plate; recorded James's review notes (`shots/shot004_fire-jump_comp-and-pass-b-plan.md`).
- Recorded the CA-MTL-1 outage, which stranded the old volume.

## 2026-11-02

- Wrote the shot 004 comp and Pass B plan; chose Blender for the comp. Built Blender Comp v001 and a Fusion comp in Resolve for comparison; stayed in Blender.
- Built the smaller Jerry guide (`scripts/build_shot004_guide.py`); it awaits James's approval. Recorded Jerry's post-landing growth decision.
- Rebuilt the ComfyUI volume in EU-RO-1 with `scripts/runpod/setup_mick13_volume.sh`; replaced the crashing WanVideoNAG patch.
- Pass A: run 8r (run 8 reproduced on the new volume) and run 9 (NAG with face negatives). Deferred 720p behind the smaller guide.
- Pass B: set up the grass-fire inpaint (inputs, graph, workflow folders); scored tests 1–2. Found the dark mask ring and its comp fix. Recorded MiniMax H3 as a candidate.

## 2026-11-03

- A100 Pod on the EU-RO-1 volume. Pass B tests 3–7 (`shots/shot004_fire-jump_pass-b_grassfire-log.md`): prompt rewrite, `vace_strength` 0.6, an exact-rerun check, gray inside the mask (best interaction, too wild), and a calmer prompt (a floating flame ribbon, worse).
- Allowed plate stills and crops as Higgsfield references (`docs/findings.md`); built keyframe inputs for James's colleague.
- Documented the ComfyUI workflow layout and naming (`workflows/comfyui/README.md`).
- Made the GitHub repo private. Moved the Mickmumpitz library into `references/mickmumpitz/`. Reorganized `outputs/` by shot and pass.
- Added a README to every working folder, including `outputs/` (READMEs are now tracked there); moved the Pass B tests into their own log; started this worklog.
