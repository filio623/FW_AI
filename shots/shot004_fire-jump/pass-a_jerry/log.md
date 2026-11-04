**Created:** 2026-11-04
**Updated:** 2026-11-04

# Shot004 Pass A Jerry Element Log

Append-only log, one entry per Pass A generation run (the Jerry fire
element on black, Houdini motion, `JB-001` look). Newest entries go at
the bottom; never edit old entries. A scored run's clip lives in
`shots/shot004_fire-jump/pass-a_jerry/runs/`; its extracted
workflow/prompt JSON lives in `shots/shot004_fire-jump/pass-*/runs/`.

## Measures

Frozen inputs (do not swap):

| Role | File | Do not swap |
|---|---|---|
| Motion | `shots/shot004_fire-jump/pass-a_jerry/inputs/shot004_ren-small-fire6_control_832x448_81f_v001.mp4` | A prettier jump that is not this path. The Blender rig in `characters/jerry/source-cgi/` is a separate character test, not this driver, until a scored row says otherwise. |
| Look | `JB-001_upright-compact-idle.png` on the volume `input/` | `JB-010` unless a test is specifically about a second still. The Blender r09 still is not an approved look. |
| Plate | Kept out of Pass A | `FW_test_scene` and the 49-frame proxy |

Short tests use the first 17 frames (`4n+1`). A 4-second cloud test may
use the 96-frame padded clip already made for Higgsfield.

Watch the same three moments every time: start on the ground, mid-jump,
landing.

| Check | How | Pass |
|---|---|---|
| Trajectory | Compare fire centroid to the Houdini control at start, mid, land | Lands in the same place. Drift past ~10% of frame width fails. |
| Look | Side by side with `JB-001` | Reads as that still, not the rough Houdini blob |
| Black | Sample the background away from the flame | Near black (`≤2/255`). Grass, floor, or a box fails. |
| Face | Whole clip | No eyes, mouth, or drawn features |
| Cost | Pod minutes (queue to finish, from ComfyUI history) or API credits | Written per run. "Pod time" alone is not a cost. |

Replication rule: a setting passes when at least 2 of 3 seeds pass all
three checks; it is dead when 3 seeds fail the same check. A resolution
change is a new sample that also needs replication.

## s004-a-001 — 2026-10-08 — VACE all-in-one rejected comp

- **Tool:** `WanVaceToVideo` on plate + screen blend.
- **Kept:** `shots/shot004_fire-jump/pass-a_jerry/runs/shot004_fire-jump_vace-rejected-comp_v001.mp4`; `shots/shot004_fire-jump/pass-a_jerry/runs/shot004_fire-jump_vace-rejected-comp_v001.prompt.json` (prompt only, no workflow block).
- **Result:** Trajectory no (ground fire, mask grew to the frame). Look no. Black no.
- **Verdict:** Killed. Do not rerun.
- **Next:** Pass A `00003`, VACE strength 1, fire-on-black.

## s004-a-002 — 2026-10-11 — Pass A `00003`, VACE strength 1

- **Change:** Fire-on-black with a red mask, strength 1 (vs. the rejected plate/screen blend).
- **Tool:** VACE 14B, strength 1, red mask, 17 frames.
- **Kept:** `.../shot004_fire-jump_passa-strength1_v001.mp4` (decode of latent `00003`); `.../shot004_fire-jump_passa-strength1_v001.workflow.json` (decode graph, not the sampler). Latent also saved as `shot004_vace_latent_00003_.latent`.
- **Result:** Trajectory yes (17 frames). Look no, copied the Houdini fire. Black yes.
- **Verdict:** Pass trajectory/black, fail look. Keep the graph, change strength only.
- **Next:** Strength 0.5.

## s004-a-003 — 2026-10-11 — HF Seedance 2.5 video edit, 480p

- **Tool:** Higgsfield, `video_edit`, 480p, 89 frames, 14 credits.
- **Kept:** Not copied into `assets/`; raw clip at `shots/shot004_fire-jump/outputs/_archive/2026-11-04/pass-a_jerry/higgsfield/shot004_jerry_seedance25-edit_480p_run001.mp4` (local only).
- **Result:** Trajectory fail (16–19% of frame width off the landing). Look pass. Black pass.
- **Verdict:** Look reference only, not the driver.
- **Next:** Not pursued as a path-lock tool.

## s004-a-004 — 2026-10-11 — Pass A 17-frame clip (not recorded which score)

- **Change:** Not recorded; this clip's embedded canvas already shows strength `0.5`, but it is dated 2026-10-11, before the score-table row for strength 0.5 (2026-10-17). No distinct score row names this run; carrying over the Kept Runs description only.
- **Kept:** `.../shot004_fire-jump_passa-oct11_v001.mp4`; `.../shot004_fire-jump_passa-oct11_v001.workflow.json`.
- **Result:** Not recorded.
- **Verdict:** Not recorded.
- **Next:** Not recorded.

## s004-a-005 — 2026-10-13 — Kling Omni Edit, seed 436

- **Tool:** `KlingOmniProEditVideoNode` / `kling-v3-omni`, 720p; prompt asked for the still look, video for scale and motion; output scaled to a 1338×720 class, full clip.
- **Kept:** `.../shot004_fire-jump_kling-omni-edit_seed436_v001.mp4`; `.../shot004_fire-jump_kling-omni-edit_seed436_v001.workflow.json`. (ComfyUI history name `output/video/ComfyUI_00005_.mp4`.)
- **Result:** Trajectory held the source clip, then restyled late (not measured as pass/fail). Look fail, starts as the Houdini fire and becomes the still only toward the end. Black not measured.
- **Verdict:** Do not keep prompting this node for a frame-1 swap.
- **Next:** VACE strength 0.5, then Wan 2.7 Video Edit.

## s004-a-006 — 2026-10-13 — Kling Omni Edit, seed 602

- **Change:** Same setup as seed 436, seed changed to 602.
- **Tool:** `KlingOmniProEditVideoNode` / `kling-v3-omni`, 720p.
- **Kept:** `.../shot004_fire-jump_kling-omni-edit_seed602_v001.mp4`; `.../shot004_fire-jump_kling-omni-edit_seed602_v001.workflow.json`. (ComfyUI history name `output/video/ComfyUI_00006_.mp4`.)
- **Result:** Same as seed 436: held source, restyled late; look fail; black not measured.
- **Verdict:** Do not keep prompting this node for a frame-1 swap.
- **Next:** VACE strength 0.5, then Wan 2.7 Video Edit.

## s004-a-007 — 2026-10-13 — Kling Motion Control

- **Tool:** `KlingMotionControl`.
- **Inputs:** Not recorded (frames/cost/measures all logged as "—"/0 in the score row).
- **Kept:** Not kept.
- **Result:** n/a on trajectory, look, black.
- **Verdict:** Do not retry.
- **Next:** Ruled out; Jerry has no upper body for a skeleton driver.

## s004-a-008 — 2026-10-17 — Pass A strength 0.5

- **Change:** VACE strength 1 → 0.5, same mask and still.
- **Tool:** VACE 14B, strength 0.5 only, 17 frames.
- **Kept:** `.../shot004_fire-jump_passa-strength05_v001.mp4` (ComfyUI history `FW_fire_comp_proxy_00005_.mp4`); `.../shot004_fire-jump_passa-strength05_v001.workflow.json`.
- **Result:** Trajectory partial, fire moves up-right but splits and smears. Look fail, soft blobs, not `JB-001`. Black pass.
- **Verdict:** Fail. Strength sweep closed; do not queue 0.35 or 0.7.
- **Next:** Silhouette control, not another strength value.

## s004-a-009 — 2026-10-17 — Pass A silhouette

- **Change:** Control video swapped to a white mask (`MaskToImage` of the fire mask); strength left at 0.5.
- **Tool:** VACE 14B, white-mask control video, strength 0.5, 17 frames.
- **Kept:** `.../shot004_fire-jump_passa-silhouette_v001.mp4` (ComfyUI history `FW_fire_comp_proxy_00006_.mp4`); `.../shot004_fire-jump_passa-silhouette_v001.workflow.json`.
- **Result:** Trajectory partial, small blob plus a gray ghost of the mask. Look fail, the white shape was drawn as gray smoke, not `JB-001`. Black pass.
- **Verdict:** Fail. Stock VACE cannot carry the still; local knob tests on `WanVaceToVideo` are closed.
- **Next:** Wan 2.7 Video Edit.

## s004-a-010 — 2026-10-17 — Wan 2.7 Video Edit, seed 42

- **Change:** New tool: `Wan2VideoEditApi` (Wan 2.7 Video Edit) in place of VACE.
- **Tool:** `Wan2VideoEditApi`, 720P, 16:9, duration auto, seed 42, `JB-001` as `image1`. Pod. 81 frames in, 101 out (30 fps, 1280×720). $0.68 Comfy credits.
- **Kept:** `.../shot004_fire-jump_wan27-videoedit_seed42_v001.mp4`; `.../shot004_fire-jump_wan27-videoedit_seed42_v001.prompt.json` (API-submitted, prompt only; runnable source is `shots/shot004_fire-jump/pass-a_jerry/workflows/early/shot004_fire-jump_wan27-videoedit_api_v001.json`).
- **Result:** Trajectory pass, ≤2.3% of frame width off the Houdini centroid at every tenth of the clip, landing 1.1%. Look partial/scored fail: a teardrop with a hot white core from frame 1, no late ramp, not `JB-001`'s soft wispy fireball. Black pass, ≤2/255 after frame 0.
- **Verdict:** First run to hold path and a Jerry-like shape together; look still misses the still.
- **Next:** Replicate with a different seed.

## s004-a-011 — 2026-10-17 — Wan 2.7 Video Edit run 2, seed 2126129005

- **Change:** Same graph and prompt as run (seed 42); only the seed changed, to `2126129005` (randomized), queued by hand from the Pod canvas.
- **Tool:** `Wan2VideoEditApi`, 720P, 16:9, duration auto. Pod. 81 frames in, 101 out (30 fps, 1280×720). $0.676 Comfy credits.
- **Kept:** `.../shot004_fire-jump_wan27-videoedit_seed2126129005_v001.mp4`; `.../shot004_fire-jump_wan27-videoedit_seed2126129005_v001.workflow.json` (queued by hand from the canvas; extract is that canvas). The Pass A candidate.
- **Result:** Trajectory pass, ≤5.5% off mid-jump, landing 0.3%, grows after landing like the Houdini fire. Look pass, soft: reads as `JB-001` (smoky edge, sparks, pale glowing core, a tip that leans with the motion), peachier and less saturated than the still; flame 150–400 px tall vs. `JB-001`'s ~1350, ~70–75% of the still's Laplacian detail at equal height; file ~0.7 Mbps. Black pass, only non-black pixels away from the flame are its own smoke/sparks, up to 17/255 over 0.2% of the frame.
- **Verdict:** First run to pass all three checks. Seed alone moved the look from generic to `JB-001`. Sharpness is the open problem.
- **Next:** 1080P, same seed, for sharpness; also a reproducibility check.

## s004-a-012 — 2026-10-18 — Wan 2.7 Video Edit run 3, seed 508

- **Change:** Three changes from run 2 at once: prompt v2 (names both references, keeps smoke and sparks, asks for crisp detail), `JB-010` added as `image2`, seed `508`.
- **Tool:** `Wan2VideoEditApi`, 720P. Pod. 81 frames in, 101 out. ~$0.68 Comfy credits (price formula, balance not checked); 196 s.
- **Kept:** `.../shot004_fire-jump_wan27-videoedit_seed508-promptv2-jb010_v001.mp4`; `.../shot004_fire-jump_wan27-videoedit_seed508-promptv2-jb010_v001.workflow.json`.
- **Result:** Trajectory fail, 25–27% of frame width off mid-jump, no flame on frame 0, lands in place. Look partial, a pale pinkish-white ball with an orange tip, recognizably Jerry but rounder and less saturated than `JB-001`; user: "about 75% there." Black mostly pass, a faint band on frame 0 (≤20/255 over 3.8%), clean after.
- **Verdict:** Confounded; cannot say which of the three changes hurt.
- **Next:** Reproducibility check (run 2 settings/seed, one added image only).

## s004-a-013 — 2026-10-18 — Wan 2.7 Video Edit run 4, seed 2126129005 + `JB-010`

- **Change:** Run 2 settings and seed `2126129005`, plus `JB-010` as `image2` (meant as a reproducibility check; `image2` was still wired).
- **Tool:** `Wan2VideoEditApi`, 720P. Pod. 81 frames in, 101 out. ~$0.68 Comfy credits (price formula, balance not checked); 215 s.
- **Kept:** `.../shot004_fire-jump_wan27-videoedit_seed2126129005-jb010_v001.mp4`; `.../shot004_fire-jump_wan27-videoedit_seed2126129005-jb010_v001.workflow.json`.
- **Result:** Trajectory fail, 15–17% off mid-jump, lands ~12% low. Look fail, a smooth white teardrop with a red rim, no flame texture or smoke, stays small instead of growing on landing; user: worse. Black pass-ish, a faint glow halo, ≤13/255 over ~1–2%.
- **Verdict:** Same seed plus one extra image gave an unrelated sample, differing from run 2 about as much as run 3 (a different seed) does. Seed-locked one-knob A/B does not work on Wan 2.7.
- **Next:** Stage 1 closed with no winner; keep run 2 (`seed2126129005`) as the paid fallback element. Move to the VACE × SkyReels merge (Mickmumpitz 1.3).

## s004-a-014 — 2026-10-19 — Mick 1.3 SkyReels run 1, fire RGB as driving video

- **Change:** New graph: Mickmumpitz 1.3 ADV with the VACE × SkyReels merge.
- **Tool:** FusionX, 5 steps, CFG 1; Houdini fire RGB as DRIVING VIDEO and as MASK (red); `JB-001` Reference Only; NAG and Lenovo bypassed; 512p. Pod, 349 s (incl. model load). 81 frames in, 81 out (24 fps, 912×512).
- **Kept:** `.../shot004_fire-jump_mick13-skyreels_rgb-drive_seed1218564478_v001.mp4`; `.../shot004_fire-jump_mick13-skyreels_rgb-drive_seed1218564478_v001.workflow.json`.
- **Result:** Trajectory pass but traced, ≤1.2% of frame size off on every tenth, area matching the source. Look fail, user: "looks the same as the reference video," redrew the Houdini fire with a round, dark-cored variation. Black pass, ≤2/255 everywhere.
- **Verdict:** The driving video must be a guide signal, not the element's RGB.
- **Next:** Gray-in-mask inputs.

## s004-a-015 — 2026-10-19 — Mick 1.3 SkyReels run 2, gray-in-mask

- **Change:** DRIVING VIDEO → flat mid-gray blob on black (fire mask grown 16 px); MASK → the same shape, white and soft. Prompt "small faceless fire spirit…".
- **Tool:** Same graph as run 1. Pod, 336 s. 81/81 frames.
- **Kept:** `.../shot004_fire-jump_mick13-skyreels_graymask-spiritprompt_seed1218564478_v001.mp4`; `.../shot004_fire-jump_mick13-skyreels_graymask-spiritprompt_seed1218564478_v001.workflow.json`.
- **Result:** Trajectory pass, ≤1.4% horizontal. Look fail, its own glowing round body with a flame crown, close to `JB-001`, but with eyes and a nose from frame 0. Black pass.
- **Verdict:** Gray-in-mask stopped the copying; "spirit"/"faceless" invited a face (NAG bypassed, so no negative prompt).
- **Next:** Prompt without character words.

## s004-a-016 — 2026-10-19 — Mick 1.3 SkyReels run 3, "round ball of fire" prompt

- **Change:** Prompt → "A round ball of fire: a smooth, softly glowing…".
- **Tool:** Same as run 2. Pod, 330 s. 81/81 frames.
- **Kept:** `.../shot004_fire-jump_mick13-skyreels_graymask-ballprompt_seed1218564478_v001.mp4`; `.../shot004_fire-jump_mick13-skyreels_graymask-ballprompt_seed1218564478_v001.workflow.json`.
- **Result:** Trajectory pass, ≤1.2% / ≤5.1% (taller than the source). Look fail, an opaque matte peach sphere with a small flame crown. Black pass.
- **Verdict:** No face, but "ball" and "smooth" were taken literally.
- **Next:** Prompt v3.

## s004-a-017 — 2026-10-19 — Mick 1.3 SkyReels run 4, prompt v3

- **Change:** Prompt v3: "A teardrop-shaped fireball made entirely of soft, translucent flames, with a bright peach-white glow at its heart…".
- **Tool:** Same as run 3. Pod, 330 s. 81/81 frames.
- **Kept:** `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218564478_v001.mp4`; `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218564478_v001.workflow.json`.
- **Result:** Trajectory pass, ≤1.1% / ≤4.6%. Look close, a teardrop body made of flame with a pale glowing interior and an ember band low down, no face; center a little milky, less smoke/spark than `JB-001`; user: "better, not perfect but getting there." Black pass, ≤2/255.
- **Verdict:** First SkyReels look that reads as Jerry.
- **Next:** New seed, for replication.

## s004-a-018 — 2026-10-19 — Mick 1.3 SkyReels run 5, seed 1218565630

- **Change:** New seed (`seed_1` 1218565630, through the restored seed wire).
- **Tool:** Same as run 4. Pod, 330 s. 81/81 frames.
- **Kept:** `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218565630_v001.mp4`; `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218565630_v001.workflow.json`. The current local reference setup.
- **Result:** Trajectory pass, ≤0.9% / ≤1.9%, tightest of any run. Look close, same character, flame strands visible through the center, edge slightly clean/bubble-like. Black pass, ≤3/255.
- **Verdict:** Replicates run 4: 2 of 2 seeds pass path, black, and face, with a close look. Setup passes the 2-of-3 rule.
- **Next:** `JB-010` as second reference image.

## s004-a-019 — 2026-10-19 — Mick 1.3 SkyReels run 6, `JB-010` added

- **Change:** `JB-010` added as Reference Image 2, same seed.
- **Tool:** Same as run 5. Pod, 354 s. 81/81 frames.
- **Kept:** `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010_seed1218565630_v001.mp4`; `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010_seed1218565630_v001.workflow.json`.
- **Result:** Trajectory pass, ≤0.9% / ≤1.8%. Look close, very similar to run 5, slightly warmer, a bit more spark and grain at the edge; user: "pretty similar." Black pass, ≤2/255.
- **Verdict:** One added image moved the picture less than a seed change did; unlike Wan 2.7, one-knob A/B works on this setup.
- **Next:** `vace_strength` 1.5 → 1.0.

## s004-a-020 — 2026-10-19 — Mick 1.3 SkyReels run 7, `vace_strength` 1.0

- **Change:** `vace_strength` 1.5 → 1.0.
- **Tool:** Same as run 6. Pod, 376 s. 81/81 frames.
- **Kept:** `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str100_seed1218565630_v001.mp4`; `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str100_seed1218565630_v001.workflow.json`.
- **Result:** Trajectory pass, ≤1.0% / ≤1.2%. Look mixed, more flame texture inside and taller tongues, but a faint gray-blue cone sticks up through the top in several frames and the bottom edge is dull; user saw the cone. Black pass-ish, ≤4/255.
- **Verdict:** Lower strength lets the flat gray guide show through the grown mask's pointed tip; too low for this guide.
- **Next:** Strength 1.25, with Lenovo LoRA.

## s004-a-021 — 2026-10-19 — Mick 1.3 SkyReels run 8, strength 1.25 + Lenovo

- **Change:** `vace_strength` 1.25 **and** the Lenovo LoRA (`wan/Lenovo.safetensors` at 1.0, `l3n0v0,` at the start of the prompt). Two changes.
- **Tool:** Same base graph as run 6. Pod, 353 s. 81/81 frames.
- **Kept:** `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo_seed1218565630_v001.mp4`; `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo_seed1218565630_v001.workflow.json`. Current best settings (as of 2026-10-19).
- **Result:** Trajectory pass, ≤1.0% / ≤1.8%. Look close, best so far: no cone, more ragged photographic flame tongues on top, fire texture inside, less bubble-like than run 6. Black pass, ≤2/255.
- **Verdict:** Current best settings; confounded, does not show whether 1.25 or Lenovo did the work.
- **Next:** NAG with a negative prompt, then 720p, then the comp check over the plate.

## s004-a-022 — 2026-11-02 — Mick 1.3 SkyReels run 8r, reproduced on `EU-RO-1`/L4

- **Change:** None: run 8's graph and settings rerun unchanged on the rebuilt `EU-RO-1` volume with an L4 GPU (run 8 was an A40).
- **Tool:** Same graph/settings as run 8. Pod, 667 s (L4). 81/81 frames.
- **Kept:** `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo_seed1218565630_eu-ro-l4-repro_v001.mp4`; `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo_seed1218565630_eu-ro-l4-repro_v001.workflow.json`. Baseline for one-knob tests on the new stack.
- **Result:** Trajectory pass, ≤0.6% / ≤3.7% (run 8 by the same measure: ≤0.6% / ≤2.0%). Look close, ≈ run 8: same body, path, and size (area within ±9%); flame tongues differ in detail; per-frame PSNR against run 8 26.5–34.2 dB. Black pass, 0/255 in the corners.
- **Verdict:** Same seed and graph on the new GPU/install gave a nearby sample, not an identical one.
- **Next:** NAG on this setup, compared against run 8r (not run 8).

## s004-a-023 — 2026-11-02 — Mick 1.3 SkyReels run 9, NAG with face negatives

- **Change:** `WanVideoNAG` on (scale 11, alpha 0.25, tau 2.5, node defaults), fed by the negative prompt with "face, eyes, nose, mouth, solid sphere, smooth plastic, ground, environment" appended to Mick's default Chinese negatives. At CFG 1 the negative prompt acts only through NAG, so this is one knob.
- **Tool:** Same graph as run 8r, `EU-RO-1`, L4. Pod, 684 s. 81/81 frames.
- **Kept:** `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo-nag_seed1218565630_eu-ro-l4_v001.mp4`; `.../shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo-nag_seed1218565630_eu-ro-l4_v001.workflow.json`.
- **Result:** Trajectory pass, ≤0.6% / ≤3.4%. Look close, ≈ run 8r: per-frame PSNR against 8r 36.1–38.9 dB, area within −2%/+5%; interior slightly brighter (mean luminance 164 vs 157 on frames 40–71), half as many dark interior pixels (2.2% vs 4.5% below 110/255). Through Blender Comp v001 both 8r and run 9 show only faint dark lobes, weaker than run 8's face; run 9 is a little more even. Black pass, 0/255 in the corners.
- **Verdict:** Small, positive change. Keep NAG on; it costs only seconds.
- **Next:** Smaller guide or 720p (see `shots/shot004_fire-jump/plan.md`).

## Run ID map

| ID | Date | Old name | Kept clip file |
|---|---|---|---|
| s004-a-001 | 2026-10-08 | VACE all-in-one, rejected comp | `shot004_fire-jump_vace-rejected-comp_v001.mp4` |
| s004-a-002 | 2026-10-11 | Pass A `00003`, strength 1 | `shot004_fire-jump_passa-strength1_v001.mp4` |
| s004-a-003 | 2026-10-11 | HF Seedance 2.5 video edit, 480p | not kept in `assets/`; `shots/shot004_fire-jump/outputs/_archive/2026-11-04/pass-a_jerry/higgsfield/shot004_jerry_seedance25-edit_480p_run001.mp4` (local only) |
| s004-a-004 | 2026-10-11 | Pass A 17-frame clip (unlabeled in score tables) | `shot004_fire-jump_passa-oct11_v001.mp4` |
| s004-a-005 | 2026-10-13 | Kling Omni Edit, seed 436 | `shot004_fire-jump_kling-omni-edit_seed436_v001.mp4` |
| s004-a-006 | 2026-10-13 | Kling Omni Edit, seed 602 | `shot004_fire-jump_kling-omni-edit_seed602_v001.mp4` |
| s004-a-007 | 2026-10-13 | Kling Motion Control | not kept |
| s004-a-008 | 2026-10-17 | Pass A strength 0.5 | `shot004_fire-jump_passa-strength05_v001.mp4` |
| s004-a-009 | 2026-10-17 | Pass A silhouette | `shot004_fire-jump_passa-silhouette_v001.mp4` |
| s004-a-010 | 2026-10-17 | Wan 2.7 Video Edit, seed 42 | `shot004_fire-jump_wan27-videoedit_seed42_v001.mp4` |
| s004-a-011 | 2026-10-17 | Wan 2.7 Video Edit run 2, seed 2126129005 | `shot004_fire-jump_wan27-videoedit_seed2126129005_v001.mp4` |
| s004-a-012 | 2026-10-18 | Wan 2.7 Video Edit run 3, seed 508 | `shot004_fire-jump_wan27-videoedit_seed508-promptv2-jb010_v001.mp4` |
| s004-a-013 | 2026-10-18 | Wan 2.7 Video Edit run 4, seed 2126129005 + JB-010 | `shot004_fire-jump_wan27-videoedit_seed2126129005-jb010_v001.mp4` |
| s004-a-014 | 2026-10-19 | Mick 1.3 SkyReels run 1 | `shot004_fire-jump_mick13-skyreels_rgb-drive_seed1218564478_v001.mp4` |
| s004-a-015 | 2026-10-19 | Mick 1.3 SkyReels run 2 | `shot004_fire-jump_mick13-skyreels_graymask-spiritprompt_seed1218564478_v001.mp4` |
| s004-a-016 | 2026-10-19 | Mick 1.3 SkyReels run 3 | `shot004_fire-jump_mick13-skyreels_graymask-ballprompt_seed1218564478_v001.mp4` |
| s004-a-017 | 2026-10-19 | Mick 1.3 SkyReels run 4 | `shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218564478_v001.mp4` |
| s004-a-018 | 2026-10-19 | Mick 1.3 SkyReels run 5 | `shot004_fire-jump_mick13-skyreels_graymask-promptv3_seed1218565630_v001.mp4` |
| s004-a-019 | 2026-10-19 | Mick 1.3 SkyReels run 6 | `shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010_seed1218565630_v001.mp4` |
| s004-a-020 | 2026-10-19 | Mick 1.3 SkyReels run 7 | `shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str100_seed1218565630_v001.mp4` |
| s004-a-021 | 2026-10-19 | Mick 1.3 SkyReels run 8 | `shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo_seed1218565630_v001.mp4` |
| s004-a-022 | 2026-11-02 | Mick 1.3 SkyReels run 8r | `shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo_seed1218565630_eu-ro-l4-repro_v001.mp4` |
| s004-a-023 | 2026-11-02 | Mick 1.3 SkyReels run 9 | `shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo-nag_seed1218565630_eu-ro-l4_v001.mp4` |
