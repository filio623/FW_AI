**Created:** 2026-05-18
**Updated:** 2026-11-04

# Repository Guidelines

Working area for an AI-assisted short-film VFX pipeline. Markdown is the main format, and this repository is the only project memory: anything worth remembering is written into the files below.

## Where Things Live

- `shots/<shotNNN>_<slug>/`: one folder per shot. `README.md` (brief, `## State (as of …)`, dated shot decisions, where the files are), `plan.md` (current methods and next steps), one append-only log per pass (`pass-a_jerry_log.md`) and `comp_log.md`. New shots start from `shots/_template/`.
- `docs/`: project-wide records. `decisions.md` (register of project-wide decisions), `findings.md` (lessons that apply beyond one shot), `worklog.md` (one entry per session), `asset-inventory.md`, `pipeline-strategy.md`, `workspace-map.md`, character bibles. `docs/archive/` holds retired documents; nothing there is live.
- `assets/`: curated media, staged in `assets/inbox/` first. Shot media under `assets/elements/by-shot/<shot>/` (`plates/`, element folders, `benchmark/` for every kept run clip, `comps/`); characters under `assets/characters/`. Heavy media is gitignored; READMEs and metadata are tracked.
- `workflows/comfyui/`: graphs in use in `shot<NNN>-working/pass-<letter>_<layer>/` (mirrored on the Pod as `shot<NNN>/pass-<letter>_<layer>/`), one extract per kept run in `shot<NNN>-benchmark/` named like its clip, creator originals in their own folder. A knob change is a run; a structural change is a new `_vNNN`. Details: `workflows/comfyui/README.md`.
- `outputs/`: renders, previews, review sheets and scratch, laid out `outputs/<shot>/<pass or comp>/<task>/`. Gitignored except READMEs; unused folders move to `outputs/_archive/<date>/`.
- `mcp/`: one note per service (`runpod.md` with its `runpod_log.md`, `blender.md`, `higgsfield.md`, `comfy-cloud.md`). `scripts/`: automation (see its README). `references/`: research, the Mickmumpitz library, and manifests of off-repo media. `prompts/`: reusable prompts.
- **Placement rule (2026-11-04):** comp project files (`.blend`, `.setting`, `.drp`) and every layer or image a saved comp loads live in `assets/`, with `_vNNN` names. `outputs/` never holds anything a saved file depends on.
- Every working folder has a short `README.md`: what it holds, why, where it came from, and a dated history line for each addition. Vendor folders and `docs/archive/` are exempt.

## Resuming Work

Read, in order: this file, the last entry of `docs/worklog.md`, the shot's `README.md`, then the end of the relevant log. Read `plan.md` or older log entries only when the task needs them.

## Records

- **Run IDs.** Every generation run gets `s<shot>-<pass>-<NNN>`: shot number, pass letter (`a` Jerry element, `b` grass fire, `c` comp; new passes take the next letter and are listed in the shot README), a sequence per pass, never reused. The ID heads the log entry and goes into the names of the kept clip, its workflow extract, and anything built from it, so `grep` finds the record from any file.
- **Log entry fields:** Change (one change, or baseline), Tool (model, graph path, GPU, key settings), Inputs, Kept (paths or "not kept"), Result, Verdict (and who), Next. Template: `shots/_template/pass_log.md`.
- **What goes where:** a run → its pass log; a comp version or check → `comp_log.md`; a shot decision → the shot README; a project-wide decision → `docs/decisions.md`; a lesson that applies beyond the shot → `docs/findings.md`, citing run IDs; a Pod or infrastructure event → `mcp/runpod_log.md`; each session → `docs/worklog.md`.
- **Timestamps.** Decisions dated inline: `**Decision (2026-11-04, James):** …`. Status sections carry the date in the heading: `## State (as of 2026-11-04)`. Log headings are dated; runs and Pod events also get a UTC time when known. Facts that do not go stale (settings, paths, how something works) stay undated.

## Documents

- **Living doc:** current state, edited in place. It opens with `**Created:** YYYY-MM-DD` and `**Updated:** YYYY-MM-DD` and has no version number or changelog: when a decision or status changes, the text says so, dated, and Git keeps the old wording.
- **Log:** append-only dated entries, newest at the bottom; never edit an old entry. Same two-line header.
- **Frozen edition:** a `_vNNN` file that approved work is checked against. It never moves; a new edition is a new file, and the old one gets `**Superseded by:** <path>`.
- **Retiring:** a document with no successor moves to `docs/archive/`, mirroring its path, with `[ARCHIVED]` in the title, `**Archived:**` and `**Original path:**` lines and one line on why; update every link to it. This is the only use of `docs/archive/`.
- **Media:** always `_vNNN`, never overwritten; a new take is a new file. A superseded take moves to `_archive/` beside it and is noted in `docs/asset-inventory.md`. Never delete an approved look, a delivered element, a plate, or anything a comp has used.
- **Cold storage:** production media lives on the NAS (`/Volumes/FW_Backup/Robs-Mac-Studio.local/Volumes/Rob's 4tb FAST`); any move to or from it updates its manifest in `references/manifests/` in the same change.
- Signpost READMEs, templates, `assets/**` notes and `memories/seeds/` carry no header.

## Naming

Shot-first names for shot media and documents (`shot004_fire-jump_…`), subject-first for reusable character and reference media (`jerry_fire_approved-look_front_v001.png`). Kept run files carry the run ID after the method: `shot004_fire-jump_grassfire-flf_s004-b-023_seedance20-1080p_v001.mp4`. No spaces.

## Working Rules

- James builds and runs ComfyUI graphs himself. The agent prepares inputs and infrastructure, checks the queued or saved graph against the previous run before scoring, and scores and logs each run (kept clip, workflow extract, log entry).
- One change per test, and compare runs only on the same GPU type: on one GPU type a rerun is pixel-identical; another GPU gives a nearby sample.
- Show previews before saving new assets.
- Shut every Pod down by hand (`scripts/runpod-pod-down.sh`); auto-terminate does not work. RunPod details: `mcp/runpod.md`.
- Commit at the end of a chunk of work with a short imperative message. Never commit `.env`, `outputs/` media or large source media.
- Jerry and the other elemental characters have no embedded eyes, mouths, brows or drawn-on features; facial animation is a separate layer. Storyboards and temp face animation are performance references only.
- Plate stills and crops may go to third-party services as references; whole plate clips do not, unless James says so for a specific job.

## Tools On This Mac

- Python with numpy, OpenCV, SciPy and Pillow: `/usr/local/bin/python3`. The system `python3` lacks them and fails some TLS checks. Scripts stay small, standard-library-first where possible, 4-space indents.
- Blender 5.2.1: `/Applications/Blender.app/Contents/MacOS/Blender` (MCP bridge: `mcp/blender.md`). DaVinci Resolve Studio scripting: `/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Applications/ResolvePython`.
- `ffmpeg`/`ffprobe` from Homebrew; the build has no `drawtext` filter.
- RunPod: `scripts/runpod-pod-up.sh`, `runpod-pod-down.sh`, `runpod-with-auth.sh`. Higgsfield: MCP tools (the trial blocks CLI generation; `mcp/higgsfield.md`). Comfy Cloud: parked (`mcp/comfy-cloud.md`).
- Secrets only in `.env`; commit `.env.example` only.
