**Created:** 2026-11-02
**Modified:** 2026-11-03
**Version:** 2.8

# Shot004 Fire Jump Comp And Pass B Plan

The plan for turning the shot 004 Pass A element (Jerry on black) into a layered comp over the plate, and for generating the remaining layers. The Pass A test queue and its scores stay in `docs/vfx-element-benchmark.md`; this file covers everything that sits on top of a Pass A element.

## Decisions (2026-11-02, James)

- **Comp tool: Blender first.** The agent builds the comp as a Blender compositor node tree by script, renders a preview, checks it, and hands over a `.blend` that James can open and adjust node by node. Blender 5.2.1 is installed and the Blender MCP bridge is set up (`mcp/blender.md`).
- **Fusion and Resolve later, if needed.** James has DaVinci Resolve Studio 21.1.1, so external scripting is available, and the same comp could be authored as a Fusion graph. Resolve's color tools are the main reason to move there. Final grading may be a separate Resolve step either way.
- **After the side-by-side (2026-11-02): stay in Blender for now.** It renders about four times faster and is simpler to rebuild by script. The Fusion version is kept for reference (see Fusion Comp v001); Resolve stays the likely place for the final grade.
- **Pass B grass ignition is AI-first.** The production grass-fire render `ren_grassfire_cpu..mov` is a rough first attempt, kept as a timing and behavior reference. It is not the element. The goal is an AI version that looks better.
- **Quick previews** can still be made with `ffmpeg` (Screen blend). Placement math is in `docs/findings.md`, 2026-11-01.

## Current Inputs

| Layer | File | Status |
|---|---|---|
| Plate | `assets/elements/by-shot/shot004_fire-jump/plates/FW_test_scene.mp4` (4096×2160, 24 fps, 84 frames, 10-bit) | Staged test plate; its provenance relative to the original `4 base plate.mov` is unverified. |
| Jerry (Pass A) | `assets/elements/by-shot/shot004_fire-jump/benchmark/shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo_seed1218565630_v001.mp4` (run 8, 912×512, 24 fps, 81 frames) | Current best. Too large (see below). |
| Houdini fire (reference) | `assets/elements/by-shot/shot004_fire-jump/fire/shot004_fire-jump_ren-small-fire6_source_v001.mov` (decodes 1920×1014, covers the whole plate) | Motion source for Pass A. |
| Grass fire (reference only) | `ren_grassfire_cpu..mov` on the NAS backup | Not restored. |
| Delivered comp (reference) | `assets/elements/by-shot/shot004_fire-jump/comps/Shot4 V031-1.mp4` (1920×1080, 24 fps, 84 frames) | Local copy, file-dated 2026-10-08; its relation to the NAS `Shot4 V031-1.mov` is unverified. Ignition timing below. |
| Comp (Blender) | `assets/elements/by-shot/shot004_fire-jump/comps/shot004_fire-jump_comp-blender_run8_v001.blend` | v001, 2026-11-02. See Blender Comp v001. |

Placing a Mick 1.3 512p clip on the plate scaled to 1920×1014: scale ×2.0192 to 1842×1034, crop 10 px off the top, place at x +39.

## Layer Stack

```mermaid
flowchart BT
  P["Plate"] --> G["Ground glow<br/>(grade driven by Jerry's light map)"]
  G --> B["Pass B: grass ignition<br/>(AI)"]
  B --> J["Jerry<br/>(core 'over' + Screen glow)"]
  J --> H["Ridge holdout<br/>(plate ridge cut back over Jerry)"]
  H --> F["Final grade"]
```

Every layer is a separate input or node, so Jerry, the grass fire, or the glow can be swapped or regenerated without rebuilding the rest (the shot plan's core rule).

## Layers: Method And Status

### Jerry (Pass A element)

- Review of run 8 over the plate (2026-11-01): placement and black are correct; Jerry reads as a pale glowing orb and slightly translucent; he is 20–50% larger than the Houdini fire.
- **Size:** rebuild the gray-in-mask guide with about 4–8 px of growth and a rounded top (benchmark step 8c, item 4). **Growth after landing (James, 2026-11-02):** Jerry grows slightly as the grass catches and grows with him. He should not inflate the way the Houdini fire does: its area roughly triples from landing to the last frame, about 1.7× in linear size. Build the guide at the Houdini fire's size up to landing, then damp the post-landing growth to about 1.2–1.3× linear by the last frame. Make the factor a setting in the guide builder so it can be tuned after a test, and time it to the grass ignition so Jerry and the grass grow together.
- **Guide builder (2026-11-02):** `scripts/build_shot004_guide.py`, run with `/usr/local/bin/python3` (numpy, OpenCV). Per frame: red channel > 20, holes filled; an opening with a 14 px disk removes flame tongues and the tip; the largest piece is replaced by its convex hull; after scaling, a second opening at 0.3 × the body's smaller side domes the top; then 6 px of growth. Up to frame 28 (bottom settles on the ground) the body keeps the fire's size. After it, width and height each follow the fire's own growth raised to one exponent, so the body's linear size (√(w·h)) reaches `--post-scale` at `--grow-end` and keeps the fire's timing. Measured on the rounded body, the fire grows 1.91× from frame 28 to 80; at 1.25 the exponent is 0.346 and the body grows 1.24×. Settings: `--grow`, `--round`, `--round-frac`, `--landing`, `--post-scale`, `--grow-end` (default the last frame; set it nearer frame 48–54 to finish growing with the grass), `--soft` (mask edge, sigma 3 as before). Each run writes the guide, the mask, and a JSON report of the settings and per-frame sizes.
- **Default candidate, awaiting James's approval** (in `outputs/shot004/pass-a_jerry/guide_v002/candidates/`, not yet an asset): `grow6-round14-30-post125`. Against the grow16 guide it is 0.83× linear at frame 0, 0.80× at landing, and 0.60× by frame 80. Against the fire mask it is 1.16× at frame 0 (6 px of growth on a small body), 1.09× at landing, and 0.73× at frame 80, where the fire is a tall column. Variants built for comparison: `grow4`, `grow8`, `post120`, `post130`, and `round-frac 0`. Previews: `outputs/shot004/pass-a_jerry/guide_v002/guide_v002_outlines_a.png`, `guide_v002_fill_a.png`, `guide_v002_on-run8_a.png`, `guide_v002_preview_v001.mp4`. On approval it is copied into `fire/` under its `_v001` name, indexed in `docs/asset-inventory.md`, and uploaded to the volume's `input/`. The GPU run then changes one input, the guide, but that input changes size, top shape, and post-landing growth together; if the result is mixed, the variants separate them.
- **Translucency:** comp first. Use an opacity matte from Jerry's bright core comped "over" the plate, plus a Screen or Add copy for the glow, plus a hotter grade. Generation fallback: prompt for a denser, brighter core, or NAG negatives. Done in Blender Comp v001; it exposed a face problem in run 8 (see below).
- Remaining GPU tests are in benchmark step 8c: NAG with negatives, 720p, smaller guide.

### Ridge holdout

At the start position a dirt ridge in front of Jerry should hide part of him, as in the Houdini version. Cut the ridge out of the plate as a foreground matte (hand roto in Blender or Fusion, or AI segmentation such as SAM2) and layer it back over Jerry. Comp only. Done in Blender Comp v001 as a hand-placed mask.

### Ground glow

A comp effect, not AI. Take Jerry's element brightness, blur it heavily and tint it orange, and use that light map to brighten and warm the plate where the light falls, limited by a soft ground mask with a strength control. It moves and flickers with Jerry automatically. Upgrade path if it looks flat: a rough ground surface in Blender with a point light following Jerry's path, rendered as a light pass. Done in Blender Comp v001.

### Pass B: grass ignition (AI)

What it must do: ignition starts where and when Jerry lands and spreads through the grass. Most of the growth in flame comes from the grass catching; Jerry grows only slightly with it (see Size above). Checks, as in the benchmark: ignition starts at the landing frame, stays inside the grass region, plate intact outside it.

Candidates, cheapest and most controllable first:

1. **AI enhancement of the production grass-fire render.** Feed `ren_grassfire_cpu` as the VACE driving video with flame references and a photographic-flame prompt, on black. Pass A run 1 showed that an RGB driving video is traced almost exactly. That was a failure for Jerry, but here it keeps the production timing and shape while the model replaces the texture. Output is an element on black for Screen or Add, like Jerry. Needs the render restored from the NAS.
2. **Inpainting on the clean plate.** Mick 1.3's native mode: DRIVING VIDEO = the clean plate, MASK = the grass region, animated to start at the landing spot on the landing frame and spread outward, prompt for dry grass catching fire, match mode "Compose + Match", which keeps the plate outside the mask and fixes the colour seam. Use the clean plate, never the plate with Jerry comped in, or the model redraws Jerry and bakes him into the grass layer. Can also scorch and blacken the grass, which an element on black cannot. Caution: the first stock-VACE plate test (2026-10-08) failed with colour artefacts and a growing static mask; Mick's animated-mask setup is different but expect iteration.
3. **Loose flame and smoke elements** from Wan-Alpha (text-to-video with real alpha), comped by hand as extra detail. Parked in the benchmark until 1 or 2 is scored.
4. **MiniMax H3 inpainting** (found 2026-11-02). H3 is the open-weight video model Mickmumpitz built his 2026-10-28 short film on; his Performance Capture 2.2 and AI renderer graphs also use it. It generates 5–15 s in one pass at a native 1344×768 and inpaints video through a mask with its Fun ControlNet Union patch (ComfyUI 0.35+, Union 2.0 0.38+; the `EU-RO-1` Pod runs 0.30.0). Its minimum length is 5 s (124 frames), so the 84-frame shot would be padded and trimmed. Local commercial use needs a paid MiniMax license through Comfy; Comfy Cloud generations include commercial rights, and Comfy Cloud already has the H3 nodes and models, so the first H3 test can run there with the same plate crop and mask as candidate 2.

#### Candidate 2 setup, test 1 (2026-11-02)

Inputs from `scripts/build_shot004_grassfire_inputs.py`, saved in `assets/elements/by-shot/shot004_fire-jump/scorch-contact/` (`_v001`, with a JSON report of the settings):

- **Window.** A 1824×1024 window of the 4096×2160 plate, top-left at plate (1838, 488), scaled ×0.5 to 912×512. Inpainting this window instead of the whole frame keeps twice the detail: the result goes back on the plate at ×2, where a full-frame 512p run would need ×4.3. It holds the grass clump and Jerry from the landing on.
- **Mask** (`…_mask-start25-full50-soft_…`). Empty to frame 24. From frame 25, when Jerry touches down, it spreads from his landing contact (window pixel 490, 450) through a burn zone, the grass clump and the air above it, and covers it by frame 50, then holds to the end. It climbs faster than it spreads sideways, its front and outline are irregular, and it stays 24 px inside the window, so flames never meet the window's edge where the inpaint joins the untouched plate. About 53% of the window at full spread. Timing, spread curve, climb and raggedness are settings.
- **DRIVING VIDEO** (`…_control-plate-canny-start25-full50_…`). The plate outside the mask; inside it, the plate's Canny edges on black. This is Mickmumpitz's recipe from his OfficeFlood example (`MICKMUMPITZ_AIVFX_EXAMPLE-FILES.zip`, `010_OfficeFlood`): the blade edges keep the grass's structure while the model draws fire into it.
- **Start image** (`…_start-frame_…`): the window's frame 0, the plate before any fire. Not committed: plate stills are ignored like the plate.

Graph: `workflows/comfyui/shot004-working/pass-b_grassfire/shot004_fire-jump_grassfire-inpaint_mick13_v001.json`, on the Pod as `shot004/pass-b_grassfire/`. It is the Jerry graph (run 9 state) with these changes: the three inputs above; Reference Image 2 (`JB-010`) bypassed; image mode `Start + Reference` and match mode `Compose + Match`; `vace_strength` 1.0 and `vace_ref_strength` 0, as in the OfficeFlood run; a grass-fire prompt with `l3n0v0`; the NAG negatives swapped from face words to "cartoon, CGI, animation, fireball, glowing orb, character, face, text, watermark"; output prefix `shot004_grassfire`. Seed, steps, sampler, LoRAs, 512p and 81 frames are unchanged. Because this is the first run of a new graph, it is a baseline, not a one-knob test.

#### Pass B tests

Every test run, with its change, scores, look and the kept clip, is in the append-only log `shots/shot004_fire-jump_pass-b_grassfire-log.md`. This section holds only the current state and the next steps.

**State after test 10 (2026-11-03).** Size and placement are close enough; the look is not.

- **Test 6** (flat gray inside the mask, prompt 2) is the best so far for interaction: the fire replaces the blades where it burns, with embers and a scorched base. Its flames are a thick, opaque, wild yellow-white mass, far from Jerry's.
- **Test 7** (prompt 3, calmer, with Jerry's flame words) is smoother and softer but turned into one floating ribbon of flame, like a second Jerry, with no grass burning. Worse overall (James).
- **Tests 8 and 9** (test 6 with two more seeds): the size is the same every time; the smoke and whether the blades burn change with the seed; the flames stay thick and wild. Reseeding will not give Jerry's look.
- **Test 10** (`vace_strength` 0.8 and more negatives): almost test 6. These knobs are not where the look is.

Reading: Jerry's flame words pull the model toward a creature-like flame, while the "engulf, tall flames" words make it wild. The prompt should describe only physical grass fire; the fire's shape should be constrained by the inputs (mask, control); the match to Jerry's look should come from a picture and from the comp grade.

**Keyframes (2026-11-03).** Four Higgsfield edits of the full plate frame by James's colleague, in `assets/elements/by-shot/shot004_fire-jump/scorch-contact/keyframes/` (README there). Each was registered back onto the plate (about 2 px error at 4K) and cut to the Pass B window, so they line up with the inputs pixel for pixel. `k2` and `k4` are the closest to the goal: soft, translucent flame tongues among the plate's own blades, blades blackening in front, embers. `k3` is calmer; `k1` redrew the blades and has one large flame wave.

Fix for the dark ring, in the comp rather than the generation: take from the inpaint only what changed. A change matte (per-pixel difference from the plate window, ramped from 22 to 45 of 255, grown 6 px, blurred 6 px, times the mask) keeps the fire, the scorch and the blades in front of the fire, and drops grass the model merely redrew darker. On frames 50 and 80 it cut the darkening in the band 2–60 px inside the edge from −12.7 and −11.0 to −1.9 and −1.8 luma. The Blender comp's Pass B layer should use it.

**Next tests, one change each, on the A100, first seed (1218565630), against test 10 unless noted:**

1. **Done, stopped: combined mask (tests 11, 11b).** Test 11 gave a gray veil; test 11b fixed the veil but the thin blade strips came out as pale tubes and the fire shrank to about 3% of the window. Thin masks are below what the model can draw in; see the log. Test 11b was: **combined mask with the plate under the half-strength area** (`…_control-plate-canny-gray-blades4-start25-full50_…`, built with `--field-fill plate`; same mask). Test 11 put gray there and came out with a gray veil (see the log). Then test 12 on the better of tests 10 and 11b.
   Test 11 (done): **combined mask.** Full strength on the blades, half strength on the space around them, and the blade edges on gray in the DRIVING VIDEO (`…_mask-start25-full50-blades4-field050-soft_…`, `…_control-plate-canny-gray-start25-full50_…`, built with `--inside canny-gray --field 0.5`). Compose + Match pastes with this mask, so the field comes out half plate; if that ghosts, feed the paste a solid mask (graph v002).
2. **Done: test 12, keyframe `k2` as Reference Image 2 at `vace_ref_strength` 0.4.** About the same as test 10; the reference barely reaches the result.
3. **Done: test 13, `vace_ref_strength` 1.0.** About test 12. A reference image is not the lever in this graph.
4. **Done: test 14, `k2` inside the DRIVING VIDEO on frames 49–52** (mask 0 there, match mode pass-through). From frame 53 the best look so far: soft peach tongues among the blades, embers, no blown-out white. Before frame 49 the whole mask fills with a glowing peach dome (the "poof"); the keyframe frames hold still.
5. **Done on an RTX 4090 (no A100 in stock): test 14r** (test 14 unchanged, the 4090 baseline) **and test 15, the keyframe on three groups** (33–36, 41–44, 49–52). Test 15 removes the poof: the fire grows in `k2`'s look from frame 30. But its outline is the spread's outline (a glowing block), because `k2`'s flames reach far past the spread and are cut, and it moves about half as much, with a hold on each group.
6. **S1 done (2026-11-03): Seedance 2.0 First-Last-Frame works.** Natural ignition at the base at 0.5 s, the clump burning by 1–1.5 s, soft translucent flames among the blades, no blown-out white (James: looks pretty good). Open: the fire runs off the window's edges, the whole frame warms toward `k2`'s grade, and it was 480p. **Next, S2:** full-frame 16:9 first frame (`keyframes/shot004_grassfire_plate-full169_f025_1920x1080_v001.png`) and `k2` on the plate's background (`…_keyframe-k2_full169-platebg_1920x1080_v001.png`), 720p, no `l3n0v0`; then 1080p or 4K for the final (4K maps 1:1 onto the 16:9 crop of the plate). How S1 was set up: First frame: the clean plate window at frame 25 (`keyframes/shot004_grassfire_plate-window_f025_1824x1024_v001.png`); last frame: `k2` registered to the window (`…_keyframe-k2_window_1824x1024_v001.png`). A video model trained on real footage invents the ignition and spread itself, so there is no mask to shape the fire; the camera is locked off, so only the fire area is comped back with the change matte and the timing is set in the comp. Only stills go to the service, which the plate rule allows. Start at Seedance 2.0 Fast, 720p, 4 s, audio off.
   In parallel on the GPU, optional: test 16, the SkyReels graph with a static zone (no growing front) sized to `k2`'s fire and `k2` at frames 57–60 (`--growth static --zone-from-key --key-frames 57-60`; inputs in the Pod's `input/`).
7. **Earlier choice, parked:** make the spread cover the keyframe's fire (bigger fire, up to the window's edges; may need the taller 720p window), or have the keyframes remade with the fire limited to the clump. Then: fewer groups (two) for more motion; seeds; check the change matte against pass-through's whole-frame change (9–11 outside the mask).
7. **Comp:** grade the kept result toward the keyframe's colours, roll off its highlights, and use the change matte.
8. Later: **taller window, 720p** (input set v002) for finer flames, once the look is right; **the production grass-fire render as the guide** (candidate 1) once it is restored from the NAS; prompt 4 (physical grass-fire wording only).

The VAE is not a lever: it only encodes and decodes the frames and has no effect on the fire's look.

Smoke or heat distortion and scorch are listed in the shot plan's required layers. Scorch comes free with candidate 2; heat distortion is a comp effect.

## Blender Comp v001 (2026-11-02)

`assets/elements/by-shot/shot004_fire-jump/comps/shot004_fire-jump_comp-blender_run8_v001.blend`, built by `scripts/blender/shot004_comp_build.py` (Blender 5.2.1). Rebuild with:

```sh
/Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup \
  --python scripts/blender/shot004_comp_build.py -- assets/elements/by-shot/shot004_fire-jump/comps/shot004_fire-jump_comp-blender_run8_v001.blend
```

Rebuilding overwrites the file, so save hand edits as `_v002` first. Starting values are in the script's `LOOK` table; every tunable node is labelled `CTRL …`. 4096×2160 at 100%, frames 1–81 (Jerry's length; the plate has 84). Frame 1 is plate frame 0 and run 8 frame 0. Renders at about 2 s per frame on the M2 Pro GPU. To inspect one node, `scripts/blender/comp_tap.py` renders its output to EXR without saving the `.blend`.

| Layer | Nodes and starting values |
|---|---|
| Plate | Image node, movie, 84 frames. View transform Standard. |
| Ground glow | Jerry luminance → Fast Gaussian blur 900 px → map range 0–0.08 to 0–1 → × tint (1.0, 0.42, 0.10). Lit plate = plate × (1 + 2.5 × tint × light), limited by mask `ground_glow_limit` (row 500 down to the ridge, blurred 220 px), so the ridge's camera side stays dark. Raises the dirt under Jerry about 1.6–2.4× in red. |
| Pass B slot | A reroute (`Pass B in`) between the lit plate and Jerry; insert the grass ignition there. |
| Jerry | Run 8 → Transform ×4.3077 about the centre, bicubic (the 2026-11-01 placement math; the compositor centres images, so no offset) → saturation 1.2 → gain (1.25, 1.0, 0.78) → dark-patch fill (Lighten with a 140 px blur of itself, amount 1.0). Core over: matte = luminance blurred 30 px, mapped 0.03–0.22 to 0–1, × opacity 0.85. Then the same Jerry Screened on top, plus Fog Glow bloom (threshold 0.25, strength 0.6). |
| Ridge holdout | Mask `ridge_holdout`, a polygon along the defocused ridge top (rows 1778–1815 at 4096 wide, traced from the focus fall-off on frame 0; the camera is locked), blurred 28 px; mixes the lit plate back over Jerry. Hides the bottom ~90 px of Jerry at the start, frames 1–12. |
| Final grade | Neutral Color Balance → Group Output and Viewer. |

Review of the full render (`outputs/shot004/comp/blender/shot004_fire-jump_comp-blender_run8_preview_v001.mp4`, 2048×1080):

- Placement matches the ffmpeg preview within a few pixels on frames 1 and 33. Jerry now reads as hot and opaque, and the ground glow gives a warm pool on the dirt and grass that follows him without visible flicker (the largest frame-to-frame change in a ground patch is 2.7 of 255, during the jump).
- **Face problem in run 8.** Once Jerry is opaque and hot, the darker interior patches of run 8 read as two eyes and a mouth on about frames 45–70. Over the plate with Screen alone they read as pale cloud, which hid this. The dark-patch fill reduces it but does not remove it, and it softens the flame texture. This is a generation problem, and the reason to run benchmark step 8c item 1 (NAG negatives "face, eyes, nose, mouth") before trusting a look; the smaller guide may also change it.
- A thin blue-violet line sits along Jerry's bottom edge on some frames after landing (visible at frames 49 and 65).
- Blender's movie decode of the plate is about 1.5–2 of 255 brighter than ffmpeg's `rgb24` conversion across the frame. It is a decode difference, not a comp change; compare comps against Blender's own plate.

Blender 5.2 compositor details that cost time: the comp is `scene.compositing_node_group`, a node group with an Image output (there is no Composite node); the render percentage does not scale image inputs, so render at 100%; the Mix node clamps its factor to 0–1 unless `clamp_factor` is off; mask coordinates are x = px / width and y = (height / 2 − row) / width + 0.5.

## Fusion Comp v001 (2026-11-02)

James asked for the same comp in DaVinci Resolve Studio's Fusion page to compare the two tools. Built by `scripts/resolve/shot004_comp_fusion.py` through Resolve's scripting interface (External scripting = Local), run with Resolve's bundled Python:

```sh
"/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Applications/ResolvePython" \
  scripts/resolve/shot004_comp_fusion.py \
  --setting assets/elements/by-shot/shot004_fire-jump/comps/shot004_fire-jump_comp-fusion_run8_v001.setting \
  [--render-preview DIR --frames 0-80]
```

- **Where it lives:** Resolve project `FW_AI_shot004_comp` (Local Database; it was "New Project 4"), project and timeline at 4096×2160, 24 fps. Timeline `shot004_comp_v001` has the plate on V1 and run 8 on V2, turned into one Fusion clip, so MediaIn1 is the plate and MediaIn2 is Jerry. The node tree is also saved as `assets/elements/by-shot/shot004_fire-jump/comps/shot004_fire-jump_comp-fusion_run8_v001.setting`, which can be pasted into any comp; after pasting, wire MediaIn2 → `Jerry_Place`, MediaIn1 → `Glow_PlateXLight` (Background) and `Glow_Add` (Background), and `Final_Grade` → MediaOut1.
- **Project file in the repo:** `assets/elements/by-shot/shot004_fire-jump/comps/shot004_fire-jump_comp-fusion_run8_v001.drp`, a Resolve project export (File → Import Project in Resolve's Project Manager). It holds the timeline and the Fusion clip with the full node tree; the media are linked by absolute path, so relink if the repo moves.
- **Rerunning the script rebuilds the comp** and deletes every tool except the MediaIns and MediaOut, so hand edits are lost. Before tuning by hand, copy the Fusion clip or the timeline in Resolve.
- **Nodes:** four underlays group the layers (`Layer_Jerry_Element`, `Layer_Ground_Glow`, `Layer_Jerry_Comp`, `Layer_Ridge_Holdout`). Tools are named for their job (`Jerry_Place`, `Jerry_DarkFill`, `Jerry_CoreKey`, `Glow_GroundMask`, `PassB_Slot`, `Ridge_Mask`, `Final_Grade`, and so on), and the two masks are Polyline masks whose points can be dragged in the viewer.
- **Same layers, different maths:** Fusion in Resolve works on the Rec.709 values it receives, not scene linear as Blender's compositor does, so its grade, matte thresholds, and glow strength are separate values, tuned until the two matched. Resolve hands Jerry to Fusion already fitted to the timeline height (×4.21875), so `Jerry_Place` adds only ×1.0213 to reach the same ×4.3077 placement.
- **Match against the Blender comp** (`outputs/shot004/comp/fusion/shot004_fire-jump_comp-fusion_run8_preview_v001.mp4`; side by side in `outputs/shot004/comp/blender-vs-fusion_v001.mp4`): placement matches; ground glow just under Jerry is within about 10% of Blender's (red ×2.0–2.2 against ×2.1–2.4), a little weaker 150 px out; Jerry's body is slightly more yellow; the ridge holdout covers the same area. The dark-patch fill softens the face patches a little more than Blender's, but they still read as a face on frames 45–70.

| | Blender compositor | Fusion page (Resolve) |
|---|---|---|
| Build by script | `bpy`, headless; no app open | Resolve must be open with scripting on; several API traps (see `docs/findings.md`, 2026-11-02) |
| Render, 4096×2160 | ~2 s per frame on the M2 Pro GPU | ~8 s per frame, rendered through a temporary Saver |
| Working space | Scene linear | Rec.709 as received, unless Resolve colour management is set up |
| Masks | Mask editor, a separate editor | Polyline points in the viewer, as in any Fusion comp |
| Grading | Compositor nodes only | Color page on the same clip |
| File in the repo | `.blend`, opens by itself | `.setting` text; the live comp is in the Resolve database |

## Ignition Timing In The Delivered Comp

From the local `Shot4 V031-1.mp4`: the fire lands around frame 23, the grass catches at once, spreads upward and outward through about frame 48, peaks around frames 42–54, and has burned down by about frame 66, while the main fire keeps growing taller to the end. The Houdini source settles on the ground at frames 25–28, so the delivered comp may sit the fire 2–3 frames earlier, or its source differs; confirm against the NAS `.mov` when restored. The delivered comp also carries other elements (a silver shape lower left, smoke near the start), so compare only the fire, grass, and glow.

## Files To Fetch From The NAS

James will copy these when he is at the NAS. Put them in `assets/inbox/`; they are classified and renamed from there. NAS restore prefix: `/Volumes/FW_Backup/Robs-Mac-Studio.local/Volumes/Rob's 4tb FAST/`.

| Priority | NAS path (under the prefix) | Use |
|---|---|---|
| 1 | `04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_grassfire_cpu/` (Proxy `.mov`; any EXR or full-res frames too) | Pass B reference and the input for candidate 1 |
| 2 | The original base plate (`4 base plate.mov`); exact NAS location not yet recorded, likely under `04 VFX/VFX Footage/Shot_4/` | The real plate for the final comp |
| 3 | `04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/Proxy/Shot4 V031-1.mov` | The delivered comp; a local `.mp4` copy already covers timing and glow reference, so this only confirms provenance |
| 3 | `.../shot_4v031_delivery/ren_steam/` and `.../ren_wetmap/` | Smoke and scorch reference |

## Open Questions For James

- ~~After landing, should Jerry keep the same size while the grass carries the growth?~~ Answered 2026-11-02: Jerry grows slightly as the grass catches and grows with him (see Size).
- Ignition frame: the local `Shot4 V031-1.mp4` shows ignition at landing, about frame 23 (see Ignition Timing). Confirm against the NAS `.mov` once restored.
- Guide: approve `grow6-round14-30-post125`, or pick a variant (growth 4 or 8 px, post-landing 1.2 or 1.3, growth ending at the grass peak instead of the last frame).

## Order Of Work

Not GPU-bound:

1. ~~Build the smaller, rounded guide and mask (local, free).~~ Built 2026-11-02; candidate awaiting approval (see Size).
2. ~~Build the first Blender comp with what is on hand: plate, run 8, ridge holdout, ground glow. Render a preview for review and hand over the `.blend`.~~ Blender Comp v001, 2026-11-02.
3. When the NAS files arrive: restore and index them, then compare with the delivered comp.

GPU, on the rebuilt `EU-RO-1` volume (see `mcp/runpod.md`):

4. Pass A, benchmark step 8c: smaller guide with run 9's settings; 720p later.
5. Pass B: candidate 2 test 1 (above), then candidate 1 once the grass-fire render is restored.
6. Swap the winners into the Blender comp; final grading in Resolve if wanted.

Later (James, 2026-11-02), not now:

- Update ComfyUI, either in place with a rollback or as a second install beside the current one. Needed before MiniMax H3 can run on the Pod. Why the Pod runs 0.30.0, and what an update risks, is in `mcp/runpod.md` (ComfyUI version).
- Try MiniMax H3 for the grass fire (candidate 4), probably on Comfy Cloud first.
- A fire-style LoRA (James, 2026-11-02): one trained look for every AI fire in the film, Jerry and grass alike. Train it on fire material (flame close-ups, approved renders, matching real fire), not on whole Jerry bodies, so it carries the look without pulling every fire into his teardrop shape; a Jerry character LoRA stays a separate option (benchmark Stage 4). A LoRA only works on the base model it was trained for, so decide between the Wan 2.1 14B family and MiniMax H3 first, and approve the target look first.

Ideas for later shots (hand-drawn paths, motion from Blender or After Effects, compositing in Blender, inpainting) are in `references/mickmumpitz-library.md` under Creature on a Path.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-11-02 | Initial Shot004 Fire Jump Comp And Pass B Plan. |
| 1.1     | 2026-11-02 | Recorded James's answer: Jerry grows slightly after landing alongside the grass fire. Set the guide's damped post-landing growth target. |
| 1.2     | 2026-11-02 | Built the guide builder and a candidate smaller guide (awaiting approval), built Blender Comp v001 with ground glow and ridge holdout, recorded the face problem the opaque comp exposes in run 8, and recorded the local delivered comp copy and its ignition timing. |
| 1.3     | 2026-11-02 | Built Fusion Comp v001 in Resolve Studio from the same layers and geometry and compared it with Blender Comp v001. |
| 1.4     | 2026-11-02 | Recorded the decision to stay in Blender for now, and the Resolve project export `.drp`. |
| 1.5     | 2026-11-02 | Added MiniMax H3 inpainting as Pass B candidate 4. |
| 1.6     | 2026-11-02 | Recorded the grass-fire inpaint inputs and graph for candidate 2 test 1, and James's notes for later: a ComfyUI update or second install, and MiniMax H3. |
| 1.7     | 2026-11-02 | Added James's fire-style LoRA idea to the later list. |
| 1.8     | 2026-11-02 | Scored Pass B candidate 2 test 1 and listed the next tests. |
| 1.9     | 2026-11-02 | Recorded the dark ring along the mask edge in test 1 and the change-matte fix for the comp. |
| 1.10    | 2026-11-02 | Scored Pass B test 2 (`JB-010` added at reference strength 0). |
| 1.11    | 2026-11-02 | Recorded the test 3 prompt for the next session. |
| 1.12    | 2026-11-03 | Scored Pass B test 3 (prompt rewrite, A100). |
| 1.13    | 2026-11-03 | Scored Pass B test 4 (`vace_strength` 0.6). |
| 1.14    | 2026-11-03 | Logged test 5: an unchanged rerun of test 4, pixel-identical. |
| 1.15 | 2026-11-03 | Updated `outputs/` paths to the per-shot layout (`outputs/<shot>/<pass or comp>/`). |
| 1.16 | 2026-11-03 | Scored Pass B test 6 (gray inside the mask). |
| 2.0 | 2026-11-03 | Major revision; 1.16 archived to `docs/archive/shot004_fire-jump_comp-and-pass-b-plan-v1.16.md`. Moved the Pass B test table into the new append-only `shots/shot004_fire-jump_pass-b_grassfire-log.md` (tests 1–7 there), and replaced the stale next-test list with the state after test 7 and a ranked list of levers. |
| 2.1 | 2026-11-03 | Updated Pass B state after test 10; recorded the Higgsfield keyframes; replaced the next-test list with the sequence for tests 11–16. |
| 2.2 | 2026-11-03 | Recorded test 11's gray-veil result and queued test 11b (plate under the half-strength area). |
| 2.3 | 2026-11-03 | Recorded test 11b and stopped the combined-mask branch; test 12 runs on test 10's setup. |
| 2.4 | 2026-11-03 | Recorded test 12; set tests 13 (reference strength 1.0) and 14 (keyframe inside the control, pass-through). |
| 2.5 | 2026-11-03 | Recorded tests 13 and 14 (keyframe in the clip: first real change of look); set test 15 (keyframe on three groups). |
| 2.6 | 2026-11-03 | Recorded tests 14r and 15 (4090); next choice: spread to fit the keyframe, or keyframes limited to the clump. |
| 2.7 | 2026-11-03 | Set the next Pass B step: Seedance 2.0 first-last-frame from the clean plate to k2, via the ComfyUI API node; test 16 (static zone) optional. |
| 2.8 | 2026-11-03 | Recorded Seedance S1 (first-last-frame works); set S2 (full frame, plate background). |
