# ComfyUI Workflows

Store project copies of ComfyUI workflows here.

Recommended naming:

`shot004_fire-i2v-wan22-alpha_v001.json`

For important workflows, include a sidecar note:

`shot004_fire-i2v-wan22-alpha_v001.md`

Current shot004 VACE technical baselines:

- `shot004_fire-vace14b_sample-latent_v001.json`: sample and save the latent before decoding.
- `shot004_fire-vace14b_decode-latent_v001.json`: tiled decode and 1280x672 proxy composite from that saved latent.

The proxy result is not an approved look. See `shots/shot004_fire-jump_workflow-test-plan_v001.md` for the rejected output and the next guided graph review; do not queue the old all-in-one graph.

## Layout

- `shot004-working/`: the current working graphs, one folder per pass. `pass-a_jerry/` holds the Mick 1.3 Jerry graph as last saved on the Pod (run 9 state: NAG on). `pass-b_grassfire/` holds the grass-fire inpaint graph. The Pod's ComfyUI workflow browser mirrors this as `shot004/pass-a_jerry/` and `shot004/pass-b_grassfire/`, plus `mickmumpitz/` for Mick's untouched 1.3 ADV original.
- `shot004-benchmark/`: one extracted graph per scored run, frozen with its clip.
- `mickmumpitz/`: Mickmumpitz originals and early adaptations, for reference.
- The loose `shot004_*` files in this folder are earlier VACE, Wan 2.2 and Wan 2.7 graphs. They stay where they are because frozen and archived documents link to these exact paths.
