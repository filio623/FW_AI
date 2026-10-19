**Created:** 2026-10-13
**Modified:** 2026-10-19
**Version:** 3.2

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
| Cost | Pod minutes (queue to finish, from ComfyUI history) or API credits | Written in the score row. "Pod time" alone is not a cost. |

A run can pass trajectory and fail look. That is a useful result. Do not
"fix" it by changing the prompt, the mask, and the model in the same queue.

**Replication.** One run does not prove or kill a setting. Wan 2.7 seed 42
failed look and seed `2126129005` passed on identical settings. A setting
passes when at least 2 of 3 seeds pass all three checks. A setting is dead
when 3 seeds fail the same check. Score every seed as its own row.

**Resolution changes the sample.** A seed at 1080P is not the same picture
as that seed at 720P, because the noise shape changes with the latent size.
Treat a resolution change as a new sample that also needs replication.

**Cost.** Paid partner nodes charge every run and every seed, on every
shot. A Pod test costs $0.59/hr while the Pod is up, whatever runs. A
local workflow that wins is therefore much cheaper for the rest of the
film than a paid one that wins. Prefer the cheapest test that answers
the question: replicate at 720P before paying for 1080P, and try a free
upscale before a paid resolution bump.

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
| Wan 2.7 Video Edit, 2026-10-18, run 3 | Three changes from run 2 at once: prompt v2 (names both references, keeps smoke and sparks, asks for crisp detail), `JB-010` added as `image2`, seed `508` | Fail. 25–27% of frame width off mid-jump, no flame on frame 0; lands in place | Partial. A pale pinkish-white ball with an orange tip: recognizably Jerry, but rounder and less saturated than `JB-001`. User: "about 75% there" | Mostly pass. A faint band on frame 0 (≤20/255 over 3.8%), clean after | Confounded; cannot say which change hurt. |
| Wan 2.7 Video Edit, 2026-10-18, run 4 | Run 2 settings and seed `2126129005`, plus `JB-010` as `image2` (meant as a reproducibility check; `image2` was still wired) | Fail. 15–17% off mid-jump; lands ~12% low | Fail. A smooth white teardrop with a red rim, no flame texture or smoke; stays small instead of growing on landing. User: worse | Pass-ish. A faint glow halo, ≤13/255 over ~1–2% | Same seed plus one extra image gave an unrelated sample: it differs from run 2 about as much as run 3 (a different seed) does. Seed-locked one-knob A/B does not work on Wan 2.7. |
| Mick 1.3 SkyReels, 2026-10-19, run 1 | Mickmumpitz 1.3 ADV with the VACE × SkyReels merge, FusionX, 5 steps, CFG 1; Houdini fire RGB as DRIVING VIDEO and as MASK (red); `JB-001` Reference Only; NAG and Lenovo bypassed; 512p | Pass, but traced: ≤1.2% of frame size off on every tenth, with area matching the source | Fail. User: "looks the same as the reference video." It redrew the Houdini fire with a round, dark-cored variation | Pass. ≤2/255 everywhere | The driving video must be a guide signal, not the element's RGB. |
| Mick 1.3 SkyReels, 2026-10-19, run 2 | Run 1, but DRIVING VIDEO = flat mid-gray blob on black (fire mask grown 16 px) and MASK = the same shape, white and soft. Prompt "small faceless fire spirit…" | Pass. ≤1.4% horizontal | Fail. Its own glowing round body with a flame crown, close to `JB-001`, but with eyes and a nose from frame 0 | Pass | Gray-in-mask stopped the copying. "Spirit" and "faceless" invited a face; NAG is bypassed, so no negative prompt. |
| Mick 1.3 SkyReels, 2026-10-19, run 3 | Run 2 with the prompt "A round ball of fire: a smooth, softly glowing…" | Pass. ≤1.2% / ≤5.1% (taller than the source) | Fail. An opaque matte peach sphere with a small flame crown | Pass | No face, but "ball" and "smooth" were taken literally. |
| Mick 1.3 SkyReels, 2026-10-19, run 4 | Run 3 with prompt v3: "A teardrop-shaped fireball made entirely of soft, translucent flames, with a bright peach-white glow at its heart…" | Pass. ≤1.1% / ≤4.6% | Close. A teardrop body made of flame with a pale glowing interior and an ember band low down; no face. Center a little milky; less smoke and spark than `JB-001`. User: "better, not perfect but getting there" | Pass. ≤2/255 | First SkyReels look that reads as Jerry. |
| Mick 1.3 SkyReels, 2026-10-19, run 5 | Run 4 with a new seed (`seed_1` 1218565630, through the restored seed wire) | Pass. ≤0.9% / ≤1.9%, tightest of any run | Close. Same character; flame strands visible through the center. Edge slightly clean and bubble-like | Pass. ≤3/255 | Replicates run 4: 2 of 2 seeds pass path, black, and face, with a close look. The setup passes the 2-of-3 rule. |
| Mick 1.3 SkyReels, 2026-10-19, run 6 | Run 5 plus `JB-010` as Reference Image 2, same seed | Pass. ≤0.9% / ≤1.8% | Close. Very similar to run 5; slightly warmer, with a bit more spark and grain at the edge. User: "pretty similar" | Pass. ≤2/255 | One added image moved the picture less than a seed change did. Unlike Wan 2.7, one-knob A/B works on this setup. |

## Queue

Local stock-VACE knobs are closed. Strength `1` copied the Houdini fire.
Strength `0.5` smeared the path and still missed `JB-001`. A white-mask
control video was drawn as gray smoke. Do not queue `0.35`, `0.7`, or
another mask tweak on `WanVaceToVideo`.

The queue runs in stages. Work a stage top to bottom. Move to the next
stage only when the current one has no winner. Within a stage, a cloud
test and a Pod test may run in the same session because they spend
different budgets, but each is still one knob and one score row.

Pod-only tests are not gated by stage order. Step 8 (VACE × SkyReels
merge) and step 10 (ATI) may run alongside Stage 1. Their per-run cost
is Pod time, and an open-weight winner is the cheapest path for the film.

### Stage 1: Confirm the Wan 2.7 candidate

Questions: is the pass repeatable, and can it be sharp enough?

1. ~~`Wan2VideoEditApi` (Wan 2.7 Video Edit).~~ Seed 42 failed look. Seed `2126129005` passed path, look, and black but is soft. Pass A candidate.
2. ~~Replication.~~ Runs 3 and 4 (2026-10-18) both failed path and look. Run 4 showed that one extra reference image at the same seed produces an unrelated sample, so every Wan 2.7 change is a fresh draw and needs several paid runs to judge.
3. **Upscale the candidate after generation.** SeedVR2 (quality) and FlashVSR (speed) on the Pod, 2×, on `shot004_fire-jump_wan27-videoedit_seed2126129005_v001.mp4`. No generation cost and the frozen inputs do not change. Score as a finishing variant: look and black must still pass; measure detail against `JB-001` at equal height. Still open; Pod time only.
4. ~~1080P, 3 seeds.~~ Closed with Stage 1, not run.
5. ~~Crop variant.~~ Closed with Stage 1, not run. Still a valid idea for any later winner that is soft because the flame is small in frame.

Stage 1 result (2026-10-18): no winner. One good run out of four (about $2.70) misses the 2-of-3 rule, and seed-locked tuning does not isolate a change. Wan 2.7 tuning stops here. Keep `shot004_fire-jump_wan27-videoedit_seed2126129005_v001.mp4` as the paid fallback element. Wan 2.7 renders at 30 fps and 1280×720 from the 24 fps 832×448 input; conform both before any comp.

Wan 2.7 notes for any later use: Alibaba rewrites the prompt by default (`prompt_extend`, on unless disabled) and supports a separate `negative_prompt`; the ComfyUI node exposes neither. Our first prompt said "no smoke" although both references have smoke.

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
8. **VACE × SkyReels V3 R2V merge, Pass A graph, model swap only.** Pod. Same graph as `00003` (strength 1, red mask, `JB-001` reference); change the diffusion model to `wan-14B_vace_skyreels_v3_R2V_e4m3fn_v1.safetensors` and nothing else. Hypothesis: stock VACE locked the path but could not carry the still; R2V training targets reference identity. The model is on volume `avw5iclb48` in `models/diffusion_models/` (downloaded and checksum-verified 2026-10-18). The saved Pass A canvas on the volume is in the silhouette state and has a live Kling Omni Edit node; see `mcp/runpod.md` before running it. Mickmumpitz's own graphs run this merge differently (`WanVacePhantomSimpleV2`, FusionX LoRA, 5 steps, CFG 1, `res_2s`/`beta57`, NAG); a model swap in our graph tests the merge outside that tuned setup. 17 frames.
8b. **Mickmumpitz 1.3 ADV with the merge, gray-in-mask inputs.** Pod, 2026-10-19, runs 1–6 above. Graph `workflows/comfyui/shot004-benchmark/shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218565630_v001.workflow.json`; inputs `assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_control-graymask-grow16_832x448_81f_v001.mp4` (DRIVING VIDEO) and `…_mask-grow16-soft_832x448_81f_v001.mp4` (MASK); prompt v3; `vace_strength` 1.5; NAG and Lenovo bypassed; 512p (912×512, 24 fps, 81 frames, the same timing as the source); ~330 s Pod time per run. This is the first local setup to pass path, black, and face on two seeds with a close look. Step 8 (a model swap in the stock Pass A graph) has not been run and is no longer needed to answer the merge question. Next, one knob each at seed `1218565630`: `vace_strength` 1.0 for a looser edge; the Lenovo LoRA (with `l3n0v0`); then a fixed NAG with "face, eyes, solid sphere" as negatives. After that, the comp check over the plate under "Promote, Then Pass B".
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
| `.../shot004_fire-jump_wan27-videoedit_seed508-promptv2-jb010_v001.mp4` | `.../shot004_fire-jump_wan27-videoedit_seed508-promptv2-jb010_v001.workflow.json` | Wan 2.7 run 3: prompt v2, `JB-001` + `JB-010`, seed 508. |
| `.../shot004_fire-jump_wan27-videoedit_seed2126129005-jb010_v001.mp4` | `.../shot004_fire-jump_wan27-videoedit_seed2126129005-jb010_v001.workflow.json` | Wan 2.7 run 4: run 2 settings plus `JB-010`. |
| `.../shot004_fire-jump_mick13-skyreels_rgb-drive_seed1218564478_v001.mp4` | `.../shot004_fire-jump_mick13-skyreels_rgb-drive_seed1218564478_v001.workflow.json` | Mick 1.3 SkyReels run 1: fire RGB as driving video; traced the source. |
| `.../shot004_fire-jump_mick13-skyreels_graymask-spiritprompt_seed1218564478_v001.mp4` | `.../shot004_fire-jump_mick13-skyreels_graymask-spiritprompt_seed1218564478_v001.workflow.json` | Run 2: gray-in-mask; face appeared. |
| `.../shot004_fire-jump_mick13-skyreels_graymask-ballprompt_seed1218564478_v001.mp4` | `.../shot004_fire-jump_mick13-skyreels_graymask-ballprompt_seed1218564478_v001.workflow.json` | Run 3: opaque sphere. |
| `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218564478_v001.mp4` | `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218564478_v001.workflow.json` | Run 4: prompt v3, first close look. |
| `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218565630_v001.mp4` | `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218565630_v001.workflow.json` | Run 5: prompt v3, second seed. The current local reference setup. |
| `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010_seed1218565630_v001.mp4` | `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010_seed1218565630_v001.workflow.json` | Run 6: run 5 plus `JB-010`. |

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
| 2026-10-18 | Wan 2.7 Video Edit run 3 | `Wan2VideoEditApi` 720P | prompt v2, `JB-010` added, seed 508 (three changes) | 81 in, 101 out | ~$0.68 Comfy credits (price formula; balance not checked); 196 s | Fail | Partial; user ~75% | Mostly pass | `shot004_fire-jump_wan27-videoedit_seed508-promptv2-jb010_v001.mp4` | reproducibility check |
| 2026-10-18 | Wan 2.7 Video Edit run 4 | `Wan2VideoEditApi` 720P | `JB-010` added at seed `2126129005` | 81 in, 101 out | ~$0.68 Comfy credits (price formula; balance not checked); 215 s | Fail | Fail | Pass-ish, faint halo | `shot004_fire-jump_wan27-videoedit_seed2126129005-jb010_v001.mp4` | stop Wan 2.7 tuning; SkyReels merge |
| 2026-10-19 | Mick 1.3 SkyReels run 1 | Mick 1.3 ADV + merge, 512p | new graph; fire RGB as driving video and mask | 81 in, 81 out (24 fps, 912×512) | 349 s Pod (incl. model load) | Pass, traced | Fail, copy | Pass | `shot004_fire-jump_mick13-skyreels_rgb-drive_seed1218564478_v001.mp4` | gray-in-mask inputs |
| 2026-10-19 | Mick 1.3 SkyReels run 2 | same | driving video and mask → gray-in-mask clips | 81 / 81 | 336 s Pod | Pass | Fail, face | Pass | `…_graymask-spiritprompt_seed1218564478_v001.mp4` | prompt without character words |
| 2026-10-19 | Mick 1.3 SkyReels run 3 | same | prompt "round ball of fire…" | 81 / 81 | 330 s Pod | Pass | Fail, opaque sphere | Pass | `…_graymask-ballprompt_seed1218564478_v001.mp4` | prompt v3 |
| 2026-10-19 | Mick 1.3 SkyReels run 4 | same | prompt v3 | 81 / 81 | 330 s Pod | Pass | Close | Pass | `…_graymask-promptv3_seed1218564478_v001.mp4` | new seed |
| 2026-10-19 | Mick 1.3 SkyReels run 5 | same | `seed_1` 1218565630 (seed wire restored) | 81 / 81 | 330 s Pod | Pass | Close | Pass | `…_graymask-promptv3_seed1218565630_v001.mp4` | `JB-010` as 2nd ref |
| 2026-10-19 | Mick 1.3 SkyReels run 6 | same | `JB-010` added | 81 / 81 | 354 s Pod | Pass | Close, ≈ run 5 | Pass | `…_graymask-promptv3-jb010_seed1218565630_v001.mp4` | `vace_strength` 1.0, then Lenovo |

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
| 3.0 | 2026-10-18 | Major revision; 2.0 archived to `docs/archive/vfx-element-benchmark-v2.0.md`. Cut Stage 1 cost: one or two 720P seeds for replication and a free Pod upscale before any 1080P run, which is now conditional. Pod-only tests (VACE × SkyReels merge, ATI) may run alongside Stage 1. Added a cost rule and required Pod minutes in score rows. |
| 3.1 | 2026-10-18 | Scored Wan 2.7 runs 3 and 4. Closed Stage 1 with no winner, stopped Wan 2.7 tuning, and kept run 2 as the paid fallback. Recorded the hidden prompt rewrite and that the SkyReels merge is now on the volume, and noted how Mickmumpitz's graphs run that merge. |
| 3.2 | 2026-10-19 | Scored Mickmumpitz 1.3 SkyReels runs 1–6. Fire RGB as the driving video traced the source; gray-in-mask inputs plus prompt v3 gave the first local setup that passes path, black, and face on two seeds with a close look. Added step 8b and its next knobs, and indexed the clips. |
