**Created:** 2026-09-07
**Modified:** 2026-10-08
**Version:** 1.8
**Archived:** 2026-10-08
**Original path:** docs/mickmumpitz-vfx-setup.md

# [ARCHIVED] Mickmumpitz AI-VFX Setup Handoff

Historical 2026-09-18 Superhero lab handoff. The `US-IL-1` volume and its Pod were retired; the commands and "next" steps below are not live. Resume current shot004 work via `shots/shot004_fire-jump_workflow-test-plan_v001.md` and `mcp/runpod.md`.

## Status (2026-09-18)

- Fun Control is **closed for learning**.
- **No Pod is running.** Last terminate `1d3rdrcwv5kfos`. Resume: `scripts/runpod-pod-up.sh` (Illinois 4090).
- Superhero Simple lab is in progress. Mask from plate works; suit reads. **Body still 180° flips** when the left arm goes up — even with `vace_ref_strength` 0.8. Next experiment: **PLATE as DRIVING**, not the pose skeleton.
- Load `workflows/comfyui/mickmumpitz/shot004_jerry-vace-simple-fp8_v001.json`. 576p / 81 frames. FusionX on, Lenovo LoRA on disk (optional).
- Volume still tight (~22 GB free). Skip Qwen / extra SAM3/Depth weights.
- Get/Set/Label: frontend-only. Hard-refresh.

## Superhero lab (current)

**Preprocess:** `INPUT VIDEO` = `060_Superhero_PLATE.mp4` (not `DRIVINGVIDEO` — that file has a pose skeleton overlay; SAM then mattes junk). Bypass TRACK, Image Composite Masked, and the grey DRIVING-VIDEO combine. Cap 81, 576p. Real matte: `MASK_00005.mp4` (~22% white / ~78% black). Copied to `input/MASK_00005.mp4`. `MASK-PLATE_00004.mp4` is QC of the isolated guy — **do not** load it as MASK (ImageToMask on that = no restyle).

**Simple slots that worked for the suit:**

| Slot | File |
|---|---|
| DRIVING | `060_Superhero_DRIVINGVIDEO.mp4` (skeleton — causes the flip) |
| MASK | `MASK_00005.mp4` |
| Start / Ref 1 | `Gemini_Generated_Image_dq24yidq24yidq24.png` |
| Mode | Start + Reference |
| `vace_strength` | 1.0 |
| `vace_ref_strength` | 0.8 (must set **inside** the Sampler subgraph on `WanVacePhantomSimpleV2`; 0 = still only locks frame 0) |

**Positive prompt:**

```text
A young man with short messy blond hair in a blue and gold superhero armor suit, chest emblem, armored shoulders and legs, standing in a destroyed city street, cracked pavement, smoke, wrecked cars, collapsing buildings. Same person as the reference still, photoreal cinematic, dramatic daylight, dust in the air. He performs the same body motion as the driving video.
```

**Negative prompt:**

```text
watercolor, painting, illustration, cartoon, white t-shirt, casual clothes, parking lot, empty parking, clean buildings, extra person, extra limbs, deformed face, blurry, text, logo, watermark
```

**Runs:** `AI-VFX_00005` = MASK-PLATE by mistake + ref 0 → original plate. `AI-VFX_00006` = MASK_00005 + skeleton drive + ref 0 → suit, then flip. Same flip after ref 0.8.

**Next queue:** same mask / still / prompt / ref 0.8. **DRIVING VIDEO** → `060_Superhero_PLATE.mp4`. Pose skeletons are front/back ambiguous on an arm raise; RGB plate has facing. If it still flips: Gemini still is a screaming wide stance vs parking-lot arm raise — use a front-on still closer to the plate pose.

Office Flood after Superhero holds orientation. Jerry after that.

## Do not

- Do **not** attach Mickmumpitz RunPod template `hb55l4frnh` (`mickmumpitz/ai-vfx:latest`) to volume `fw-ai-comfyui` (`ccv3wj09mn`). Different image, auto-download, 120 GB min, FileBrowser `admin`/`adminadmin12`. Would fight `/workspace/runpod-slim/ComfyUI` and the Fun Control/Jerry weights.
- His template is only OK as a **throwaway sandbox** on a **new** 120 GB volume, no project plates. Prefer staying on our volume.

## Files already in the repo

`workflows/comfyui/mickmumpitz/`

| File | Role |
|---|---|
| `shot004_jerry-vace-simple-fp8_v001.json` | **Simple graph, FP8 path — load this** |
| `260330_MICKMUMPITZ_AI-VFX_1-0_SMPL.json` | Original Simple (GGUF wired). Keep as reference. |
| `260330_MICKMUMPITZ_AI-VFX_PREPROCESS_1-0.json` | Masks, depth, canny, pose, plate |
| `260330_AI-VFX-STARTIMAGE_1-0.json` | Qwen Image Edit start/ref helper; extra models; later |

Paid `_ADV` graphs were not downloaded. Correct.

Watch: [Mickmumpitz 2026 Masterclass](https://www.youtube.com/watch?v=_n0ir5V5tX4). Written: [free guide](https://mickmumpitz.ai/posts/free-guide-epic-154092216). Video post: [free workflows](https://mickmumpitz.ai/posts/new-video-free-154315215).

## Next Pod session

1. `scripts/runpod-pod-up.sh` — Illinois 4090, volume `ccv3wj09mn`.
2. Hard-refresh. Load `shot004_jerry-vace-simple-fp8_v001.json`.
3. MASK `MASK_00005.mp4`, still Gemini `dq24yi…`, prompt as above, `vace_ref_strength` 0.8 on **WanVacePhantomSimpleV2**.
4. **Change only drive** to `060_Superhero_PLATE.mp4`.
5. Do not Queue Fun Control. Skip Qwen.

## Jerry inputs already on the volume `input/`

- `jerry_JB-001_upright-compact-idle.png`
- Fire controls in `assets/elements/by-shot/shot004_fire-jump/fire/` (also uploaded): full CGI proxy, trajectory-dot, **trajectory-streak**, 40%-shrunk.

Do not spend the next session on more Fun Control seeds.

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-09-07 | Handoff after Fun Control close; Mickmumpitz Simple/Preprocess/StartImage in repo; do not mix his RunPod template with `fw-ai-comfyui`. |
| 1.1     | 2026-09-07 | Pod `ijzpkfsy5sqmt6` attached; RES4LYF + Mickmumpitz nodes cloned; FP8 merge download started. |
| 1.2     | 2026-09-07 | Installed RMBG, DepthCrafter, controlnet_aux, CoTracker, Impact, calcuis/gguf; Simple execution nodes confirmed; frontend-only Get/Set/Label noise documented. |
| 1.3     | 2026-09-08 | Terminated `ijzpkfsy5sqmt6`; relaunched `v3chqyqw2kowkx`; skipped re-downloads; next work is Simple remap + 576p mask study. |
| 1.4     | 2026-09-08 | Added `shot004_jerry-vace-simple-fp8_v001.json`: FP8 UNETLoader into FusionX, GGUF bypassed, Linux `wan/` path. |
| 1.5     | 2026-09-08 | Pod `1a2lj3lfp7wnju`; uploaded Superhero + Office Flood drive/mask/refs to `input/mick/`. |
| 1.6     | 2026-09-08 | Terminated `1a2lj3lfp7wnju`. Next sit-down: pod up, load FP8 Simple, Superhero drive+mask. |
| 1.7     | 2026-09-18 | Superhero matte from plate (`MASK_00005`); suit reads; 180° flip on arm raise with skeleton drive even at ref 0.8. Documented prompt. Next: plate as driving. Lenovo LoRA on volume. |
| 1.8     | 2026-10-08 | Retired the old Illinois-volume setup handoff after VACE shot004 became the active review path; preserved the lab record in the archive. |
