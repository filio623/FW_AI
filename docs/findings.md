**Created:** 2026-05-18
**Modified:** 2026-09-18
**Version:** 1.3

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

## 2026-08-30

- Official Wan2.2 Fun Control tutorial weights, both `lightx2v` LoRAs, `wan_2.1_vae`, and the sample start image / pose video are on network volume `fw-ai-comfyui`. The tutorial graph was loaded but not queued.
- Illinois 4090 was out of stock; an RTX 6000 Ada (48 GB, $0.84/hr) in `US-IL-1` ran the same volume. Fun Control 14B fp8 fits that card.
- RunPod Direct can land 14B files in `models/unet/` while a parallel download lands the same filename in `models/diffusion_models/`. ComfyUI treats those folders as one UNET pool, so a second copy is wasted space. One duplicate low-noise 14B was deleted; volume usage after that was ~48 GB of 100 GB.

## 2026-09-07

- Fun Control learning closed. `Wan22FunControlToVideo` has no control-strength slider; concat control is structure. Canny or the full `ren_small_fire6` CGI made Jerry fill the old body. A ~56px centroid dot was too weak (idle bounce). A fat centroid streak was usable as path-only control.
- Jerry tests used the official 14B Fun Control template with `JB-001` + fire controls, not `shot004_jerry-wan22-funcontrol-element_v001.json` (5B TI2V). Next hands-on chapter is Mickmumpitz / VACE-1.3B.

## 2026-09-18

- Mick Superhero: matte from **plate** (`MASK_00005`), not the pose `DRIVINGVIDEO` and not `MASK-PLATE` (QC RGB). Suit restyle works. Pose-skeleton drive still 180° flips the body on the left-arm raise at `vace_ref_strength` 0.8. Next: plate as driving.
- Load Video only lists `input/`; Preprocess writes `output/AIVFX-PREPROCESS/`. Copy mattes into `input/` before Simple.
- CoTracker on 4K×395 Superhero frames killed ComfyUI (502). Bypass TRACK. Lenovo LoRA (`Lenovo.safetensors`) is on the volume.
