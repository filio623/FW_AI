**Created:** 2026-11-04
**Updated:** 2026-11-04

# Decisions

Append-only register of project-wide decisions: tools, rules, infrastructure and methods that apply beyond one shot. One line each, oldest first: date, who, the decision, why, and where the detail is. Shot-level decisions are in each shot's README. Entries before 2026-11-04 were collected that day from the docs and Git history.

- **2026-08-16 (James):** retire Supermemory; the repository is the only project memory. `docs/archive/mcp/supermemory.md`.
- **2026-10-17:** test generation methods on one fixed benchmark shot (shot 004) with frozen inputs, one change per run and the same checks, before scaling to other shots. `shots/shot004_fire-jump/plan.md`.
- **2026-11-02 (James):** Blender is the comp tool, built by script so every layer stays editable; Fusion kept for reference; Resolve is the likely place for a final grade. `shots/shot004_fire-jump/comp_log.md` (`s004-c-001`, `s004-c-002`).
- **2026-11-02:** rebuild the ComfyUI network volume in RunPod `EU-RO-1` (`dqlwnz6nq8`, by `scripts/runpod/setup_mick13_volume.sh`) after `CA-MTL-1` went down; it has the most GPU types. `mcp/runpod.md`.
- **2026-11-03 (James):** plate stills and crops may go to third-party services as references and parts of their output may be comped; whole plate clips stay off third-party services unless James says so for a job. `docs/findings.md`, 2026-11-03.
- **2026-11-03 (James):** ComfyUI graphs live in per-shot, per-pass working folders, with one extract per kept run named like its clip. `workflows/comfyui/README.md`.
- **2026-11-03 (James):** the GitHub repository is private (it holds paid Mickmumpitz workflows); the Mickmumpitz library moves into `library/mickmumpitz/`, workflows tracked, media local. `library/mickmumpitz-library.md`.
- **2026-11-03 (James):** `outputs/` is laid out by shot and pass, and every working folder gets a README, including `outputs/` folders (only READMEs tracked there). `AGENTS.md`.
- **2026-11-03 (James):** generated video through ComfyUI partner API nodes (Seedance, Kling) is an accepted method, billed to the Comfy account; first used for shot 004 Pass B. `shots/shot004_fire-jump/pass-b_grassfire/log.md` (`s004-b-018` on).
- **2026-11-04 (James):** shorter document rules: living docs have Created/Updated dates and no versions or changelogs (Git keeps history); logs are append-only; frozen `_vNNN` editions never move; only retired docs go to `docs/archive/`. Replaces the 2026-08-16 lifecycle policy. `AGENTS.md`, Documents.
- **2026-11-04 (James):** one folder per shot under `shots/`, with README, plan, a log per pass and a comp log; every generation run gets a run ID (`s004-b-021`) used in its log entry and file names; this register for project-wide decisions. `AGENTS.md`, Records.
- **2026-11-04 (James):** comp project files and everything a saved comp loads live in `assets/` with `_vNNN` names; `outputs/` holds renders and previews only. Unused `outputs/` folders are archived to `shots/shot004_fire-jump/outputs/_archive/<date>/`, not deleted. `AGENTS.md`.
- **2026-11-04 (James):** Comfy Cloud parked (MCP 403, CLI not installed; its scripts removed); the eight companion Higgsfield skills and the project's own three skills retired (unused; reinstall when needed). `mcp/comfy-cloud.md`, `mcp/higgsfield.md`.
- **2026-11-04 (James):** shot-first layout: everything used by one shot (docs, plates, reference, per-pass inputs, graphs, kept runs, comps, shot scripts, outputs) lives in `shots/<shot>/`; project-wide material lives in `characters/`, `source/`, `library/`, `docs/`, `workflows/`, `scripts/`. `assets/` and `references/` are gone (`library/` replaces `references/`). Frozen editions moved once, as an exception (the Jerry and Tom bibles to `characters/<name>/bible_v001.md`, the first shot 004 test plan into the shot folder), because nothing approved pointed at their paths yet. Every move: `docs/archive/restructure_2026-11-04_moves.tsv`. Supersedes the `assets/` placement in the entry above. `AGENTS.md`, Where Things Live.
