# ComfyUI Workflows

Conventions for ComfyUI graphs, and creator originals. Graphs in use live in the shot folders.

## Where graphs live

| Place | Holds | Changes? |
|---|---|---|
| `shots/<shot>/pass-<letter>_<layer>/workflows/` | The graph in use for one pass, e.g. `shots/shot004_fire-jump/pass-b_grassfire/workflows/` | Yes; it tracks the latest saved state on the Pod |
| `shots/<shot>/pass-<letter>_<layer>/runs/` | One extract per kept run, beside its clip, same name | No; frozen with its clip |
| `workflows/comfyui/<vendor>/`, e.g. `mickmumpitz/` | Untouched originals from a creator or template | No |

The Pod's ComfyUI workflow browser (`/workspace/runpod-slim/ComfyUI/user/default/workflows/`) mirrors the working folders with the same file names: `shot<NNN>/pass-<letter>_<layer>/` and `<vendor>/`. The full Mickmumpitz library, every workflow and guide per video, is in `library/mickmumpitz/` (`library/mickmumpitz-library.md`).

## Naming

- Working graph: `<shot>_<shot-slug>_<layer>-<method>_<model-or-graph>_vNNN.json`, e.g. `shot004_fire-jump_grassfire-inpaint_mick13_v001.json`.
- Kept run: the clip's exact name with `.workflow.json` (or `.prompt.json` for API-format prompts). From 2026-11-04 the name carries the run ID after the method: `shot004_fire-jump_grassfire-flf_s004-b-023_seedance20-1080p_v001.workflow.json`.
- Output prefix in the graph's video-save node: one per pass (`shot004_mick13-skyreels`, `shot004_grassfire`), so outputs on the Pod sort by pass.

## Versions and records

- A knob change (seed, strength, prompt, a reference on or off) is a run, not a new version; it is logged in the pass's `log.md` under its run ID, and its exact graph is the run's extract.
- A structural change (new inputs or input format, new nodes or subgraphs, a different method) is a new version: save `_v002` beside `_v001`, on the Pod and in the repo, and keep `_v001`.
- At the end of a session, copy the graphs saved on the Pod back into the matching working folder.
- Inputs a graph loads live in the pass's `inputs/` under `_vNNN` names, built by a script that also writes a JSON report of its settings, and are uploaded to the Pod's `input/` under the same names.
