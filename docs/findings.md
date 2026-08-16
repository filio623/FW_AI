**Created:** 2026-05-18
**Modified:** 2026-05-18
**Version:** 1.0

# Findings

## 2026-05-17

- Higgsfield `wan2_7` produced a strong robot/bunny benchmark from prompt alone.
- Local ComfyUI SD 1.5 text-to-image works.
- Local ComfyUI Wan2.2 5B video tests were not production-usable for prompt-adherent text-to-video from pure noise.
- Wan2.2 FP8 diffusion weights are not compatible with Apple MPS due to unsupported `Float8_e4m3fn`.
- For the short film, prioritize element generation, alpha/matte workflows, and compositing passes over full-shot AI video.

## 2026-05-19

- Scene 4 / shot004 should be developed as layered VFX, not a single baked AI video: Jerry element, matte/alpha, glow/contact light, grass ignition, smoke/heat, scorch, and preview comp should remain separately revisable.
- Current local ComfyUI install exposes useful video nodes, including `Wan22FunControlToVideo`, `LoadVideo`, `GetVideoComponents`, `CreateVideo`, and multiple cloud/API video nodes.
- Current local model inventory does not include ControlNet model files. ControlNet and IPAdapter workflows will need additional model installs before they can be serious production branches.
- First local ComfyUI element-control workflow created and validated: `workflows/comfyui/shot004_jerry-wan22-funcontrol-element_v001.json`.
- Use a generation proxy resolution around 832x448 for first Wan2.2 tests, then composite/evaluate against the 4K plate in Fusion/Resolve. Keep the original `FW_test_scene.mov` as the final plate source.
