# ComfyUI Workflows

Project copies of ComfyUI workflows. The layout and naming below are the convention for every shot; shot 004 is the worked example.

## Layout

| Folder | Holds | Changes? |
|---|---|---|
| `shot<NNN>-working/pass-<letter>_<layer>/` | The graph in use for one pass of one shot, e.g. `shot004-working/pass-a_jerry/`, `shot004-working/pass-b_grassfire/` | Yes; it tracks the latest saved state on the Pod |
| `shot<NNN>-benchmark/` | One graph extract per scored run, pulled from that run's output metadata | No; frozen with its clip |
| `<vendor>/`, e.g. `mickmumpitz/` | Untouched originals from a creator or template, plus early adaptations | No |

The full Mickmumpitz library, every workflow and guide per video, is in `references/mickmumpitz/` (`references/mickmumpitz-library.md`); `workflows/comfyui/mickmumpitz/` holds only the originals copied for use.

The Pod's ComfyUI workflow browser (`/workspace/runpod-slim/ComfyUI/user/default/workflows/`) mirrors the working folders with the same file names: `shot<NNN>/pass-<letter>_<layer>/` and `<vendor>/`. A pass is one layer of the comp built by one generation method (Pass A Jerry, Pass B grass ignition); its letter and layer name match the shot's comp plan in `shots/`.

## Naming

- Working graph: `<shot>_<shot-slug>_<layer>-<method>_<model-or-graph>_vNNN.json`, e.g. `shot004_fire-jump_grassfire-inpaint_mick13_v001.json`. The Jerry graph predates this pattern and keeps its original name, `shot004_fire-jump_mick13-skyreels_v001.json`.
- Benchmark extract: the kept clip's exact name with `.workflow.json` (or `.prompt.json` for API-format prompts), e.g. `shot004_fire-jump_grassfire-inpaint_mick13_test1_seed1218565630_v001.workflow.json` beside `assets/elements/by-shot/shot004_fire-jump/benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test1_seed1218565630_v001.mp4`. The clip name carries what the run changed (`test2-jb010`, `str125-lenovo-nag`), the seed, and where needed the setup (`eu-ro-l4`).
- Output prefix in the graph's video-save node: one per pass (`shot004_mick13-skyreels`, `shot004_grassfire`), so outputs on the Pod sort by pass.

## Versions

- A knob change (seed, strength, prompt, a reference on or off) is a run, not a new version. It is recorded in the pass's score rows, and its exact graph lives in the benchmark extract.
- A structural change (new inputs or input format, new nodes or subgraphs, a different method) is a new version: save it as `_v002` beside `_v001` in the working folder, on the Pod and in the repo, and keep `_v001`.
- At the end of a session, copy the graphs saved on the Pod back into the matching working folder here.

## Inputs And Notes

- Inputs a graph loads (guides, masks, control videos, start frames) live in `assets/elements/by-shot/<shot>/<category>/` under `_vNNN` names, built by a script in `scripts/` that also writes a JSON report of its settings. They are uploaded to the Pod's `input/` under the same names.
- Method and plan go in the shot's plan in `shots/`. Each run's settings and scores go in the pass's test log: `docs/vfx-element-benchmark.md` for Pass A, `shots/<shot>_<slug>_pass-<letter>_<layer>-log.md` for later passes (e.g. `shots/shot004_fire-jump_pass-b_grassfire-log.md`). Not in sidecar files. Older graphs may still have a sidecar `.md`.

## Earlier Graphs

The loose `shot004_*` files in this folder are earlier VACE, Wan 2.2 and Wan 2.7 graphs (`shot004_fire-vace14b_sample-latent_v001.json`, `shot004_fire-vace14b_decode-latent_v001.json`, and others). They stay where they are because frozen and archived documents link to these exact paths. The VACE proxy result they produced is not an approved look; see `shots/shot004_fire-jump_workflow-test-plan_v001.md`.
