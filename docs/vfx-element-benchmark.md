**Created:** 2026-10-13
**Modified:** 2026-10-18
**Version:** 2.0

# VFX Element Benchmark

Working plan for learning which workflow can make a compositable element.
Shot 004 is the fixed benchmark so every run is comparable. It is not a
leaderboard of "best video model."

## Why This Shape

A model that wins a text-to-video ranking can still fail this shot. The
job is narrower: follow a known jump, take Jerry's look, and come back as
a layer. Testing every model on a mixed prompt answers none of those
questions. One job, frozen inputs, one changed knob, then a score.

Do not promote a run to a full-length shot or to grass ignition until it
passes Pass A. Do not spend cloud credits on a tool that cannot take the
motion clip.

## The Job

Pass A only, until one workflow passes.

- Motion comes from the Houdini fire on black.
- Look comes from `JB-001`.
- Background stays black so the result can be screened or added over the plate.
- The plate is not an input to this test.

Pass B (grass ignition, ground glow) starts only after a Pass A winner
comps cleanly over the plate in Resolve or Fusion.

## Frozen Inputs

| Role | File | Do not swap |
|---|---|---|
| Motion | `assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_control_832x448_81f_v001.mp4` | A prettier jump that is not this path. The Blender rig in `assets/characters/jerry/source-cgi/` is a separate character test, not this driver, until a scored row says otherwise. |
| Look | `JB-001_upright-compact-idle.png` on the volume `input/` | `JB-010` unless a test is specifically about a second still. The Blender r09 still is not an approved look. |
| Plate | Kept out of Pass A | `FW_test_scene` and the 49-frame proxy |

Short tests use the first 17 frames (`4n+1`). A 4-second cloud test may
use the 96-frame padded clip already made for Higgsfield. Say which
length you used in the score row.

## What To Measure

Watch the same three moments every time: start on the ground, mid-jump,
landing. Then fill one row in the score table. Taste is not the record.

| Check | How | Pass |
|---|---|---|
| Trajectory | Compare fire centroid to the Houdini control at start, mid, land | Lands in the same place. Drift past ~10% of frame width fails. |
| Look | Side by side with `JB-001` | Reads as that still, not the rough Houdini blob |
| Black | Sample the background away from the flame | Near black (`≤2/255`). Grass, floor, or a box fails. |
| Face | Whole clip | No eyes, mouth, or drawn features |
| Cost | Pod minutes or API credits | Written down before the next run |

A run can pass trajectory and fail look. That is a useful result. Do not
"fix" it by changing the prompt, the mask, and the model in the same queue.

**Replication.** One run does not prove or kill a setting. Wan 2.7 seed 42
failed look and seed `2126129005` passed on identical settings. A setting
passes when at least 2 of 3 seeds pass all three checks. A setting is dead
when 3 seeds fail the same check. Score every seed as its own row.

**Resolution changes the sample.** A seed at 1080P is not the same picture
as that seed at 720P, because the noise shape changes with the latent size.
Treat a resolution change as a new sample that also needs replication.

## Already Scored

| Run | Tool | Trajectory | Look | Black | Decision |
|---|---|---|---|---|---|
| VACE all-in-one, 2026-10-08 | `WanVaceToVideo` on plate + screen blend | No. Ground fire, mask grew to the frame | No | No | Killed. Do not rerun. |
| Pass A `00003`, 2026-10-11 | VACE, strength 1, fire-on-black, red mask | Yes, 17 frames | No. Copied the Houdini fire | Yes | Keep the graph. Change strength only. |
| Seedance 2.5 video edit, 2026-10-11 | Higgsfield, 480p | No. 16–19% of frame width off the landing | Yes | Yes | Look reference only. Not the driver. |
| Kling Omni Edit, 2026-10-13 | `KlingOmniProEditVideoNode`, seeds 436 and 602 | Held the source clip, then restyled late | Fail. Starts as the Houdini fire and becomes the still only toward the end | Not measured | Do not keep prompting this node for a frame-1 swap. Next local knob is VACE strength 0.5. Then Wan 2.7 Video Edit. |
| Pass A strength 0.5, 2026-10-17 | VACE, same mask and still | Fire moves up-right but splits and smears | Fail. Soft blobs, not `JB-001` | Pass | Strength sweep closed. Next is silhouette control, not 0.35 or 0.7. |
| Pass A silhouette, 2026-10-17 | VACE, white mask as `control_video`, strength left at 0.5 | Small blob plus a gray ghost of the mask | Fail. Not `JB-001`. The white shape was drawn as gray smoke | Pass | Stock VACE cannot carry the still. Local knob tests are done. |
| Wan 2.7 Video Edit, 2026-10-17 | `Wan2VideoEditApi` on the Pod, 720P, seed 42, `JB-001` as `image1` | Pass. ≤2.3% of frame width off the Houdini centroid at every tenth of the clip; landing 1.1% | Partial, scored Fail. A teardrop with a hot white core from frame 1, no late ramp. But it is a clean, glossy candle-drop, not `JB-001`'s soft, wispy fireball | Pass. Background ≤2/255 after frame 0 | First run to hold path and a Jerry-like shape together. The look still misses the still. |
| Wan 2.7 Video Edit, 2026-10-17, run 2 | Same graph and prompt, queued by hand from the Pod canvas; only the seed changed (`2126129005`, randomized) | Pass. ≤5.5% of frame width off mid-jump; landing 0.3%. Grows after landing like the Houdini fire | Pass, soft. Reads as `JB-001`: smoky edge, sparks, pale glowing core, a tip that leans with the motion. Peachier and less saturated than the still. Softer than the still: the flame is 150–400 px tall against `JB-001`'s ~1350, and at equal height it keeps ~70–75% of the still's Laplacian detail. The file is ~0.7 Mbps | Pass. The only non-black pixels away from the flame are its own smoke and sparks, up to 17/255 over 0.2% of the frame. No ground or box | First run to pass all three checks. Seed alone moved the look from generic to `JB-001`. Sharpness is the open problem. |

## Queue

Local stock-VACE knobs are closed. Strength `1` copied the Houdini fire.
Strength `0.5` smeared the path and still missed `JB-001`. A white-mask
control video was drawn as gray smoke. Do not queue `0.35`, `0.7`, or
another mask tweak on `WanVaceToVideo`.

The queue runs in stages. Work a stage top to bottom. Move to the next
stage only when the current one has no winner. Within a stage, a cloud
test and a Pod test may run in the same session because they spend
different budgets, but each is still one knob and one score row.

### Stage 1: Confirm the Wan 2.7 candidate

Questions: is the pass repeatable, and can it be sharp enough?

1. ~~`Wan2VideoEditApi` (Wan 2.7 Video Edit).~~ Seed 42 failed look. Seed `2126129005` passed path, look, and black but is soft. Pass A candidate.
2. **1080P, 3 seeds.** Same graph, prompt, and inputs; `resolution` 1080P only. Seeds `2126129005`, `42`, and one new random seed. About $1.01 each, so ~$3.03. Wan 2.7 edit bills input + output seconds (3.375 s + ~3.37 s at $0.15/s), which matches the $0.676 logged at 720P ($0.10/s). Answers sharpness and replication together.
3. **Two more 720P seeds** only if step 2 is inconclusive (~$0.68 each).
4. **Upscale the candidate after generation.** SeedVR2 (quality) and FlashVSR (speed) on the Pod, 2×, on `shot004_fire-jump_wan27-videoedit_seed2126129005_v001.mp4`. No generation cost and the frozen inputs do not change. Score as a finishing variant: look and black must still pass; measure detail against `JB-001` at equal height.
5. **Crop variant.** Source cropped to the jump region and scaled back in comp. Changes the frozen motion input, so score it as a variant. Only if 2–4 leave it soft.

Winner rule for this stage: at least 2 of 3 seeds pass at one resolution, and sharpness is accepted by eye against `JB-001` after any upscale.

### Stage 2: Restyled-first-frame edits

Question: can a tool take `JB-001` from frame 1 while it keeps the path?
Kling Omni Edit reached the look only late. These tools take an explicit
first frame or keyframe, which targets that failure.

Build one new derived input first and freeze it:
`JB-001` scaled to the Houdini fire's frame-0 height and placed on its
frame-0 centroid, on black, at 832×448 and 1280×720
(`shot004_jb001-first-frame_<res>_v001.png`). Every Stage 2 and Stage 3
test uses this file.

6. **Luma Modify Video (Ray 3.2 video-to-video), `adhere` mode, start image = the JB-001 first frame.** Cloud. Third-party rates are about $0.35/s; confirm the price and whether ComfyUI has a node, or use Luma's API directly. Hypothesis: a restyled first frame with adhere strength keeps the path and takes the look from frame 1.
7. **Runway Aleph 2 (`RunwayAleph2VideoToVideoNode`), guidance image = the JB-001 first frame at t = 0.** Cloud. Third-party rate $0.369/s with a 2 s minimum, so a 4 s clip is ~$1.48. Confirm the node exposes guidance images; without them it is a prompt-only restyle.
8. **VACE × SkyReels V3 R2V merge, Pass A graph, model swap only.** Pod. Same graph as `00003` (strength 1, red mask, `JB-001` reference); change the diffusion model to `wan-14B_vace_skyreels_v3_R2V_e4m3fn_v1.safetensors` and nothing else. Hypothesis: stock VACE locked the path but could not carry the still; R2V training targets reference identity. The model is not on volume `avw5iclb48` (it was on the deleted Illinois volume); download it from `Inner-Reflections/VACE_Skyreels_V3_R2V_Merge` first. A Mickmumpitz graph that loads it is at `workflows/comfyui/mickmumpitz/shot004_jerry-vace-simple-fp8_v001.json`. 17 frames.
9. **Same merge, plus the JB-001 first frame as control frame 0** (mask black on frame 0, red mask after). Only after 8 is scored. It reopens first-frame conditioning on a new model, not a stock-VACE mask tweak.

### Stage 3: Image-to-video with a drawn path

Question: if no edit model takes the look, can an I2V model start from
`JB-001` and follow the Houdini path?

Build one more derived input: the Houdini fire centroid per frame as
coordinates (`shot004_houdini-centroid_832x448_81f_v001.json`), taken
from the same measurement used for trajectory scores. The existing
`trajectory-dot` and `trajectory-streak` clips show this path.

10. **ATI (Wan 2.1 I2V 14B, Kijai WanVideoWrapper or the ComfyUI template).** Start image = the JB-001 first frame, one trajectory = the centroid track. Pod. 480P only, so sharpness is a known risk. Watch whether the flame grows on landing, since I2V only animates the start image.
11. **Wan-Move (Wan 2.1, 480P, 5 s).** Same inputs as 10. Run only if ATI follows the path poorly or its look is good but the motion is wrong.
12. **Time-to-Move with Wan 2.2 I2V.** Training-free. Crude animation = the JB-001 first frame dragged along the centroid track (a cut-and-drag clip). Run only if 10 and 11 fail on motion. The cut-and-drag clip is also a possible source video for Wan 2.7 Video Edit; score that as a motion-input variant, not a Stage 1 setting.

### Stage 4: Train the look

13. **Jerry LoRA on Wan 2.1 14B (musubi-tuner or AI Toolkit).** Only if Stages 2–3 lock the path but no local model carries `JB-001`. The primary-body and motion-pose stills (`JB-001`–`JB-006`, `JB-009`–`JB-011`, `JB-013`) are about 10 images, the low end that hosted trainers suggest. Then rerun the best local path-lock graph with the LoRA as the one new knob.

### Parked

- **Wan-Alpha.** Text-to-video only, so it cannot take the motion clip. Moved to Pass B as a source of loose flame and smoke elements with real alpha.
- **Wan 2.7 first/last-frame I2V.** Locks start and landing only; mid-jump path is free. Lower odds than Stage 3.
- **Wan 2.7 reference-to-video and Seedance reference.** Reference-to-video already failed as the path lock. Look studies only.

Kling Omni Edit and Kling Motion Control are already scored. Do not retry them for this job. SkyReels V4 is a paper with no public weights.

A winner still has to pass path, look, and black on a short clip before any full-length rerun or Pass B. Third-party prices above were looked up on 2026-10-17; confirm on the node or the provider before queuing.

## Promote, Then Pass B

A winner is a short clip that passes all three checks. Only then:

- Rerun that one setup at full length.
- Comp it over the plate with Screen or Add.
- Start Pass B as its own element: grass ignition and ground glow, masked, not baked into the character pass.

Pass B gets the same method: frozen inputs (plate proxy, grass mask, landing frame from the Pass A winner), one knob per run, and its own checks (ignition starts at the landing frame, stays inside the grass mask, plate intact outside it). First candidates: VACE inpainting inside the grass mask over the plate, and Wan-Alpha flame and smoke elements comped by hand. Glow, contact shadow, and scorch start as comp work in Resolve or Fusion before any generation.

## Do Not Test For This Job

- Veo text-to-video or image-to-video. No motion-video input, so it cannot lock this jump.
- Kling Motion Control and other skeleton drivers. Jerry has no upper body.
- Seedance or Wan reference-to-video as the path lock. Already failed that job. Fine as a look study.
- A new model because a chatbot ranked it this week.
- Pass B, 4K, or an 81-frame run before a 17-frame pass.

## How To Work A Session

1. Read the Queue above. Do not reopen a closed knob.
2. Pod up only if the next test needs the local 14B model. Partner API tests do not need the A40.
3. Duplicate the workflow. Do not edit `shot004_fire-vace14b_sample-latent_v001`.
4. Change one control. Queue once.
5. If the run is scored, copy the output mp4 to `assets/elements/by-shot/shot004_fire-jump/benchmark/` under a shot-first `_vNNN` name, and extract its embedded workflow JSON into `workflows/comfyui/shot004-benchmark/`. Add a row to the index below. Do not save an unscored rerun.
6. Stop. The next session starts at the next unchecked item, not a new idea.

## Kept Runs

Scored clips are the research set. The mp4 holds the picture and the canvas that was open when it was saved. The extracted JSON is the part Git can track, because `*.mp4` is gitignored. The JSON is the whole canvas, including nodes that did not feed the saved video. Follow the Save Video wire before you conclude what a run did.

| Clip | Graph extract | What it is |
|---|---|---|
| `assets/elements/by-shot/shot004_fire-jump/benchmark/shot004_fire-jump_vace-rejected-comp_v001.mp4` | `workflows/comfyui/shot004-benchmark/shot004_fire-jump_vace-rejected-comp_v001.prompt.json` | 2026-10-08 rejected proxy. Prompt only; no workflow block. |
| `.../shot004_fire-jump_passa-strength1_v001.mp4` | `.../shot004_fire-jump_passa-strength1_v001.workflow.json` | Decode of latent `00003`, the strength `1` path lock. The extract is the decode graph, not the sampler. |
| `.../shot004_fire-jump_passa-oct11_v001.mp4` | `.../shot004_fire-jump_passa-oct11_v001.workflow.json` | 2026-10-11 17-frame clip. Embedded canvas already shows strength `0.5`. |
| `.../shot004_fire-jump_passa-strength05_v001.mp4` | `.../shot004_fire-jump_passa-strength05_v001.workflow.json` | 2026-10-17 strength `0.5`. Look failed. |
| `.../shot004_fire-jump_passa-silhouette_v001.mp4` | `.../shot004_fire-jump_passa-silhouette_v001.workflow.json` | 2026-10-17 white mask as control. Look failed. |
| `.../shot004_fire-jump_kling-omni-edit_seed436_v001.mp4` | `.../shot004_fire-jump_kling-omni-edit_seed436_v001.workflow.json` | Kling Omni Edit seed 436. |
| `.../shot004_fire-jump_kling-omni-edit_seed602_v001.mp4` | `.../shot004_fire-jump_kling-omni-edit_seed602_v001.workflow.json` | Kling Omni Edit seed 602. |
| `.../shot004_fire-jump_seedance20-ref_v001.mp4` | `.../shot004_fire-jump_seedance20-ref_v001.workflow.json` | ComfyUI Seedance 2.0 Fast reference test, seed 825222339. Not the Higgsfield Seedance 2.5 run. |
| `.../shot004_fire-jump_wan27-videoedit_seed42_v001.mp4` | `.../shot004_fire-jump_wan27-videoedit_seed42_v001.prompt.json` | Wan 2.7 Video Edit, seed 42, 720P. API-submitted, so prompt only; the runnable source is `workflows/comfyui/shot004_fire-jump_wan27-videoedit_api_v001.json`. |
| `.../shot004_fire-jump_wan27-videoedit_seed2126129005_v001.mp4` | `.../shot004_fire-jump_wan27-videoedit_seed2126129005_v001.workflow.json` | Wan 2.7 Video Edit, seed 2126129005, 720P. Queued by hand from the canvas; the extract is that canvas. The Pass A candidate. |

The Higgsfield Seedance 2.5 clip is not in this checkout. Its score row still points at `outputs/higgsfield/shot004_jerry_seedance25-edit_480p_run001.mp4`.

## Score Rows

| Date | Run | Tool | Knob changed | Frames | Cost | Trajectory | Look | Black | File | Next |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-11 | Pass A 00003 | VACE 14B | strength 1, red mask | 17 | Pod time | Pass | Fail | Pass | `shot004_vace_latent_00003_.latent` | strength 0.5 |
| 2026-10-11 | HF Seedance 2.5 | video_edit 480p | — | 89 | 14 credits | Fail | Pass | Pass | `outputs/higgsfield/shot004_jerry_seedance25-edit_480p_run001.mp4` | not the driver |
| 2026-10-13 | Kling Motion Control | `KlingMotionControl` | — | — | 0 | n/a | n/a | n/a | — | do not retry |
| 2026-10-13 | Kling Omni Edit 00005 / 00006 | `kling-v3-omni` 720p | prompt asked for still look, video for scale and motion | full clip, scaled to 1338×720 class | Comfy credits | Held, not measured | Fail. Look ramps in late | Not measured | `output/video/ComfyUI_00005_.mp4` seed 436, `ComfyUI_00006_.mp4` seed 602 | VACE strength 0.5, then Wan 2.7 Video Edit |
| 2026-10-17 | Pass A strength 0.5 | VACE 14B | strength 0.5 only | 17 | Pod time | Partial. Splits | Fail | Pass | `FW_fire_comp_proxy_00005_.mp4` | silhouette as control video |
| 2026-10-17 | Pass A silhouette | VACE 14B | control video = MaskToImage of the fire mask; strength stayed 0.5 | 17 | Pod time | Partial. Gray ghost of the mask | Fail | Pass | `FW_fire_comp_proxy_00006_.mp4` | stop local VACE knobs |
| 2026-10-17 | Wan 2.7 Video Edit | `Wan2VideoEditApi` 720P, 16:9, duration auto | new tool; seed 42, `JB-001` as reference image | 81 in, 101 out (30 fps, 1280×720) | $0.68 Comfy credits | Pass | Fail. Generic teardrop, not the still | Pass | `shot004_fire-jump_wan27-videoedit_seed42_v001.mp4` | Runway Aleph |
| 2026-10-17 | Wan 2.7 Video Edit run 2 | `Wan2VideoEditApi` 720P, 16:9, duration auto | seed `2126129005` only | 81 in, 101 out (30 fps, 1280×720) | $0.676 Comfy credits | Pass | Pass, soft | Pass, own smoke ≤17/255 | `shot004_fire-jump_wan27-videoedit_seed2126129005_v001.mp4` | 1080P same seed for sharpness |

---

## Changelog

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-10-13 | Initial VFX Element Benchmark. Frozen shot004 Pass A inputs, measurements, scored baselines, and the one-knob queue. |
| 1.1 | 2026-10-13 | Scored Kling 3.0 Omni Edit as a late look-swap, not a frame-1 replacement. Next knob remains VACE strength 0.5. |
| 1.2 | 2026-10-17 | Scored the strength 0.5 Pass A run as a failed look transfer and closed the strength sweep. |
| 1.3 | 2026-10-17 | Scored the silhouette control run. Stock VACE drew the mask as gray smoke and did not take the Jerry still. |
| 1.4 | 2026-10-17 | Closed the local VACE queue after the silhouette run. Next test is Wan 2.7 Video Edit. |
| 1.5 | 2026-10-17 | Added the scored-run file rule and indexed the clips copied off the volume. |
| 1.6 | 2026-10-17 | Kept the Blender Jerry rig off the shot 004 motion driver until a scored row replaces the Houdini clip. |
| 1.7 | 2026-10-17 | Scored Wan 2.7 Video Edit: path and black pass, look fails as a generic teardrop. Indexed the clip and moved the queue to Runway Aleph. |
| 1.8 | 2026-10-17 | Scored Wan 2.7 run 2 (seed 2126129005) as the first pass on all three checks, soft. Made it the Pass A candidate, queued sharpness tests, and put Runway Aleph on hold. |
| 2.0 | 2026-10-18 | Major revision; 1.8 archived to `docs/archive/vfx-element-benchmark-v1.8.md`. Added the 2-of-3 seed replication rule. Replaced the queue with a staged test matrix: Wan 2.7 confirmation, restyled-first-frame edits (Luma Modify, Runway Aleph 2, VACE × SkyReels merge), I2V path tools (ATI, Wan-Move, Time-to-Move), and a Jerry LoRA. Parked Wan-Alpha for Pass B and outlined the Pass B method. |
