#!/usr/bin/env bash
# Install the shot004 Mick 1.3 + VACE x SkyReels stack on a fresh network volume.
#
# Run ON the Pod (official ComfyUI - CUDA 12.8 template, volume at /workspace), after
# the template has installed ComfyUI into /workspace/runpod-slim/ComfyUI:
#
#   bash setup_mick13_volume.sh              # nodes, patches, restart script, then models
#   bash setup_mick13_volume.sh nodes        # only custom nodes + patches + restart script
#   bash setup_mick13_volume.sh models       # only model downloads + checksum checks
#   bash setup_mick13_volume.sh patch        # only reapply the node patches
#
# Idempotent: existing clones, patched files and complete downloads are left alone.
# Model list, checksums and patch rationale: mcp/runpod.md.
set -euo pipefail

COMFY=/workspace/runpod-slim/ComfyUI
VENV="$COMFY/.venv-cu128"
PIP="$VENV/bin/pip"
PY="$VENV/bin/python"
NODES="$COMFY/custom_nodes"
MODELS="$COMFY/models"
WHAT="${1:-all}"

[[ -d "$COMFY" && -x "$PY" ]] || { echo "ComfyUI not installed at $COMFY yet; let the template finish first." >&2; exit 1; }
[[ -f /etc/rp_environment ]] && set +u && source /etc/rp_environment && set -u

clone() {  # clone URL DIR COMMIT|-
    local url=$1 dir=$2 commit=$3
    if [[ ! -d "$NODES/$dir/.git" ]]; then
        git clone -q "$url" "$NODES/$dir"
    fi
    if [[ "$commit" != "-" ]]; then
        git -C "$NODES/$dir" -c advice.detachedHead=false checkout -q "$commit"
    fi
    if [[ -f "$NODES/$dir/requirements.txt" ]]; then
        "$PIP" install -q -r "$NODES/$dir/requirements.txt"
    fi
    echo "node $dir @ $(git -C "$NODES/$dir" log -1 --format=%h)"
}

install_nodes() {
    # ComfyUI-KJNodes, ComfyUI-Manager ship with the template (KJNodes 78cd992 on 2026-11-02).
    clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite ComfyUI-VideoHelperSuite -
    clone https://github.com/mickmumpitz/ComfyUI-Mickmumpitz-Nodes ComfyUI-Mickmumpitz-Nodes 270afbd
    clone https://github.com/drozbay/ComfyUI-WanVaceAdvanced ComfyUI-WanVaceAdvanced 049213c
    clone https://github.com/ClownsharkBatwing/RES4LYF RES4LYF 56e4475
    clone https://github.com/rgthree/rgthree-comfy rgthree-comfy d7297b4
    clone https://github.com/city96/ComfyUI-GGUF ComfyUI-GGUF 6ea2651
    "$PIP" install -q PyWavelets gguf protobuf
    patch_nodes
    write_restart_script
}

patch_nodes() {
    # 1. KJNodes WanVideoNAG on FP8 weights: NAG embeds its negative prompt while
    #    comfy_cast_weights is still off, so a plain Linear forward meets FP8 weights
    #    (mat1/mat2 Half vs Float8_e4m3fn). Run each layer through ComfyUI's own casting
    #    path instead. (A temporary deep copy, the 2026-10-19 approach, crashes on
    #    ComfyUI 0.30 with dynamic VRAM: CUDA invalid argument, then a double free.)
    #    Revert with git -C custom_nodes/ComfyUI-KJNodes checkout nodes/model_optimization_nodes.py
    # 2. Mickmumpitz ControlCrossfadeIterationFix with Reference Only: start_frames is None,
    #    so make it an empty batch and inject nothing on iteration 0. Revert with
    #    git -C custom_nodes/ComfyUI-Mickmumpitz-Nodes checkout nodes/control_crossfade.py
    "$PY" - "$NODES" <<'PY'
import pathlib, sys
nodes = pathlib.Path(sys.argv[1])

def patch(path, mark, old, new):
    p = nodes / path
    text = p.read_text()
    if mark in text:
        print(f"already patched: {path}")
        return
    if text.count(old) != 1:
        sys.exit(f"patch anchor not found exactly once in {path}; upstream changed, re-derive the patch")
    p.write_text(text.replace(old, new))
    print(f"patched: {path}")

patch("ComfyUI-KJNodes/nodes/model_optimization_nodes.py", "FW_AI patch 2026-11-02",
      "        diffusion_model.text_embedding.to(device)\n"
      "        context = diffusion_model.text_embedding(conditioning[0][0].to(device, dtype))\n",
      "        # FW_AI patch 2026-11-02: casting is not switched on yet when NAG patches the\n"
      "        # model, so FP8 weights would meet 16-bit input; use ComfyUI's casting path.\n"
      "        compute_dtype = getattr(model_clone.model, \"manual_cast_dtype\", None) or dtype\n"
      "        if compute_dtype not in (torch.float16, torch.bfloat16, torch.float32):\n"
      "            compute_dtype = torch.bfloat16\n"
      "        context = conditioning[0][0].to(device, compute_dtype)\n"
      "        for layer in diffusion_model.text_embedding:\n"
      "            if hasattr(layer, \"forward_comfy_cast_weights\"):\n"
      "                context = layer.forward_comfy_cast_weights(context)\n"
      "            else:\n"
      "                context = layer(context)\n")

patch("ComfyUI-Mickmumpitz-Nodes/nodes/control_crossfade.py", "FW_AI patch 2026-10-19",
      "        B, H, W, C = control_frames.shape\n        device = control_frames.device\n",
      "        B, H, W, C = control_frames.shape\n        device = control_frames.device\n"
      "        # FW_AI patch 2026-10-19: Reference Only passes start_frames=None; treat it as\n"
      "        # an empty batch so iteration 0 injects nothing instead of crashing.\n"
      "        if start_frames is None:\n"
      "            start_frames = control_frames[:0]\n")
PY
    grep -q "^import torch" "$NODES/ComfyUI-KJNodes/nodes/model_optimization_nodes.py" \
        || { echo "model_optimization_nodes.py does not import torch at top level; check the NAG patch" >&2; exit 1; }
}

write_restart_script() {
    cat > /workspace/restart_comfyui.sh <<'SH'
#!/usr/bin/env bash
# Relaunch ComfyUI the way the template's start.sh does. start.sh does not relaunch it
# after it exits. Launch detached:
#   setsid nohup /workspace/restart_comfyui.sh > /workspace/comfyui_restart.log 2>&1 &
# Stop the old process by PID first (not pkill -f over SSH; it matches the SSH shell).
set +u
[[ -f /etc/rp_environment ]] && source /etc/rp_environment
source /workspace/runpod-slim/ComfyUI/.venv-cu128/bin/activate
cd /workspace/runpod-slim/ComfyUI
ARGS=$(grep -v '^#' /workspace/runpod-slim/comfyui_args.txt 2>/dev/null | tr '\n' ' ')
exec python main.py --listen 0.0.0.0 --port 8188 --enable-cors-header $ARGS
SH
    chmod +x /workspace/restart_comfyui.sh
    echo "wrote /workspace/restart_comfyui.sh"
}

fetch() {  # fetch URL DEST SHA256|-
    local url=$1 dest=$2 sha=$3
    mkdir -p "$(dirname "$dest")"
    if [[ -f "$dest" ]] && { [[ "$sha" == "-" ]] || echo "$sha  $dest" | sha256sum -c --status; }; then
        echo "ok (cached) $dest"
        return
    fi
    curl -fsSL --retry 5 --retry-delay 5 -C - -o "$dest.part" "$url"
    mv "$dest.part" "$dest"
    if [[ "$sha" != "-" ]]; then
        echo "$sha  $dest" | sha256sum -c --quiet || { echo "CHECKSUM MISMATCH $dest" >&2; return 1; }
    fi
    echo "ok $dest ($(stat -c %s "$dest") bytes)"
}

install_models() {
    local HF=https://huggingface.co
    fetch "$HF/Inner-Reflections/VACE_Skyreels_V3_R2V_Merge/resolve/main/wan-14B_vace_skyreels_v3_R2V_e4m3fn_v1.safetensors" \
        "$MODELS/diffusion_models/wan-14B_vace_skyreels_v3_R2V_e4m3fn_v1.safetensors" \
        59511532de0baa48d719ea49f857ada5672d384e5d92e70ea59848ece025d23d &
    fetch "$HF/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors" \
        "$MODELS/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors" - &
    fetch "$HF/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors" \
        "$MODELS/vae/wan_2.1_vae.safetensors" - &
    fetch "$HF/vrgamedevgirl84/Wan14BT2VFusioniX/resolve/main/FusionX_LoRa/Wan2.1_T2V_14B_FusionX_LoRA.safetensors" \
        "$MODELS/loras/Wan2.1_T2V_14B_FusionX_LoRA.safetensors" \
        c653087fa7c9163abdd1a4c627bfc483966c6d78a4426667d1185f860951c30e &
    fetch "https://civitai.com/api/download/models/2066914" \
        "$MODELS/loras/wan/Lenovo.safetensors" \
        64002d78edc3cea47d440c4d7bd7bb9de9c8a67177fe10607632cd6281144631 &
    local failed=0
    for job in $(jobs -p); do wait "$job" || failed=1; done
    [[ $failed -eq 0 ]] || { echo "one or more downloads failed" >&2; exit 1; }
    local te; te=$(stat -c %s "$MODELS/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors")
    [[ "$te" == 6735906897 ]] || { echo "text encoder size $te, expected 6735906897" >&2; exit 1; }
    echo "models complete"
}

case "$WHAT" in
    all) install_nodes; install_models ;;
    nodes) install_nodes ;;
    patch) patch_nodes ;;
    models) install_models ;;
    *) echo "usage: $0 [all|nodes|patch|models]" >&2; exit 2 ;;
esac
