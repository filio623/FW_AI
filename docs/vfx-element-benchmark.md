**Created:** 2026-10-13
**Modified:** 2026-10-17
**Version:** 1.6

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

## Already Scored

| Run | Tool | Trajectory | Look | Black | Decision |
|---|---|---|---|---|---|
| VACE all-in-one, 2026-10-08 | `WanVaceToVideo` on plate + screen blend | No. Ground fire, mask grew to the frame | No | No | Killed. Do not rerun. |
| Pass A `00003`, 2026-10-11 | VACE, strength 1, fire-on-black, red mask | Yes, 17 frames | No. Copied the Houdini fire | Yes | Keep the graph. Change strength only. |
| Seedance 2.5 video edit, 2026-10-11 | Higgsfield, 480p | No. 16–19% of frame width off the landing | Yes | Yes | Look reference only. Not the driver. |
| Kling Omni Edit, 2026-10-13 | `KlingOmniProEditVideoNode`, seeds 436 and 602 | Held the source clip, then restyled late | Fail. Starts as the Houdini fire and becomes the still only toward the end | Not measured | Do not keep prompting this node for a frame-1 swap. Next local knob is VACE strength 0.5. Then Wan 2.7 Video Edit. |
| Pass A strength 0.5, 2026-10-17 | VACE, same mask and still | Fire moves up-right but splits and smears | Fail. Soft blobs, not `JB-001` | Pass | Strength sweep closed. Next is silhouette control, not 0.35 or 0.7. |
| Pass A silhouette, 2026-10-17 | VACE, white mask as `control_video`, strength left at 0.5 | Small blob plus a gray ghost of the mask | Fail. Not `JB-001`. The white shape was drawn as gray smoke | Pass | Stock VACE cannot carry the still. Local knob tests are done. |

## Queue

Local stock-VACE knobs are closed. Strength `1` copied the Houdini fire.
Strength `0.5` smeared the path and still missed `JB-001`. A white-mask
control video was drawn as gray smoke. Do not queue `0.35`, `0.7`, or
another mask tweak on `WanVaceToVideo`.

Next, one cloud edit, same motion clip and same still:

1. `Wan2VideoEditApi` (Wan 2.7 Video Edit). Shut the Pod down first if the only work is this API call.
2. `RunwayAleph2VideoToVideoNode` only if Wan 2.7 fails path or look.

Kling Omni Edit and Kling Motion Control are already scored. Do not retry them for this job.

If those edits fail, the next local branch is the SkyReels V3 R2V × Wan VACE merge, which is a new model and a new graph, not a setting on the current one. SkyReels V4 is a paper with no public weights.

A winner still has to pass path, look, and black on a short clip before any full-length rerun or Pass B.

## Promote, Then Pass B

A winner is a short clip that passes all three checks. Only then:

- Rerun that one setup at full length.
- Comp it over the plate with Screen or Add.
- Start Pass B as its own element: grass ignition and ground glow, masked, not baked into the character pass.

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
