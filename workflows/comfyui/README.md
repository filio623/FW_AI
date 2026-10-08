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
