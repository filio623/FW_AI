# ComfyUI Model Notes

## Current Project Findings

- SD 1.5 txt2img works locally with `v1-5-pruned-emaonly-fp16.safetensors`.
- Wan2.2 5B FP16 files loaded successfully after incomplete downloads were resumed.
- Local Wan2.2 5B pure text-to-video produced weak prompt adherence and blurry output for the robot/bunny test.
- Wan2.2 14B FP8 high/low-noise models failed on Apple MPS with unsupported `Float8_e4m3fn`.
- Prefer FP16/BF16-compatible model files for Apple MPS.

## Practical Implication

For the short film, use local ComfyUI primarily for:

- First frames and keyframes.
- Video-to-video refinement from CGI/proxy animation.
- ControlNet/IPAdapter/reference-conditioned experiments.
- Alpha/matte element generation.
- Interaction passes that can be composited.

Do not assume local text-to-video from noise will provide final-quality, art-directable shot elements.
