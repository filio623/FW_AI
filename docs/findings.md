# Findings

## 2026-05-17

- Higgsfield `wan2_7` produced a strong robot/bunny benchmark from prompt alone.
- Local ComfyUI SD 1.5 text-to-image works.
- Local ComfyUI Wan2.2 5B video tests were not production-usable for prompt-adherent text-to-video from pure noise.
- Wan2.2 FP8 diffusion weights are not compatible with Apple MPS due to unsupported `Float8_e4m3fn`.
- For the short film, prioritize element generation, alpha/matte workflows, and compositing passes over full-shot AI video.
