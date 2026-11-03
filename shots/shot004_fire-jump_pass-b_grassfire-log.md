**Created:** 2026-11-03
**Modified:** 2026-11-03
**Version:** 1.0

# Shot004 Pass B Grass-Fire Test Log

Every Pass B (grass ignition) test run, newest at the bottom. This is an append-only log: add a new entry for each run and never edit an old one. The plan, the current state and the ranked next steps are in `shots/shot004_fire-jump_comp-and-pass-b-plan.md`, Pass B. Entries for tests 1–6 were moved here from that plan's test table on 2026-11-03, unchanged in substance.

## How a test is run and kept

- James builds and runs the graph on the Pod. Before each run the agent diffs the saved or queued graph against the previous test, so each test changes one thing.
- Each kept run has three records: the clip in `assets/elements/by-shot/shot004_fire-jump/benchmark/`, the graph extracted from it in `workflows/comfyui/shot004-benchmark/` (same name, `.workflow.json`), and an entry here. Raw outputs and comparison sheets are in `outputs/shot004/pass-b_grassfire/inpaint_v001/` (`testN.mp4`, `testN.png`, `testN_vs_testM.png`).
- Compare tests only on the same GPU type. On one GPU type and install, a rerun of the same graph and seed is pixel-identical (test 5), so an A/B there is exact. A different GPU gives a nearby but different sample.

## Measures

- **Fire size and place:** fire pixels (bright, red-dominant) as a share of the 912×512 window and of the mask; the share of the fire that run 9's Jerry would cover once comped; fire pixels outside the mask.
- **Plate outside the mask:** mean change outside the mask, and the dark ring: mean luma change against the plate in the band 2–60 px inside the mask edge.
- **Look:** read by eye against Jerry (soft, translucent, peach-white heart, orange and gold tongues) and against real grass fire (blades burning, scorch, embers, smoke).
- Tests 1–6 were measured in one analysis session. From test 7 on the scripts were rebuilt after that session was lost. The fire threshold is now red ≥ 180 and red − blue ≥ 60, which gives sizes within about 0.5 points of the earlier numbers. Ring values use a slightly different band, so compare test 7 ring numbers only with the test 4 and 6 numbers given in its entry.

## Fixed setup

Graph: `workflows/comfyui/shot004-working/pass-b_grassfire/shot004_fire-jump_grassfire-inpaint_mick13_v001.json`; inputs in `assets/elements/by-shot/shot004_fire-jump/scorch-contact/`. Seed 1218565630, 512p, 81 frames, mask from frame 25 to full by frame 50. Settings before test 1 are in the plan, Candidate 2 setup.

## Prompts

- **Prompt 1** (tests 1–2): "l3n0v0, Dry grass at the base of the clump catches fire where a small flame touches the ground. The fire spreads quickly outward and upward through the grass, orange and yellow flames climbing each blade, blades curling and blackening as they burn, thin grey smoke rising, glowing embers drifting up. Realistic outdoor grass fire in natural daylight, filmed with a real camera."
- **Prompt 2** (tests 3–6): "l3n0v0, A fire suddenly ignites at the base of the grass clump and within a second engulfs the whole clump of dry grass. Tall flames climb up every blade and rise high above the tips, with grey smoke curling upward and glowing embers drifting in the air. The flames are soft and translucent, with a bright peach-white glow at the heart and orange and gold flame tongues licking upward, thin dark smoke wisps and tiny sparks. Grass blades blacken and curl as they burn. Realistic outdoor fire in natural daylight, filmed with a real camera."
- **Prompt 3** (test 7): "l3n0v0, A fire catches at the base of the grass clump and over the next second spreads along the dry blades. Low, flickering flames run up the individual blades; each blade glows orange as it burns, then blackens and curls. The flames are soft and translucent, with a peach-white glow at the heart and thin orange and gold tongues, light wisps of dark smoke and a few tiny sparks. A natural, realistic grass fire, filmed with a real camera in natural daylight."

## Test 1 — 2026-11-02

- **Change:** New graph: inputs v001, settings above
- **Run:** 610 s (L4); prompt 1.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test1_seed1218565630_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test1_seed1218565630_v001.workflow.json`.
- **Ignition:** Pass. A spark at Jerry's landing contact on frame 26, spreading from frame 28
- **Fire size and place:** Fail. A Jerry-sized fire at the base of the clump: at most 7.5% of the window and 11–14% of the mask; the rest of the mask was redrawn as grass. 56–100% of the fire sits where Jerry is, so he would hide most of it
- **Plate outside the mask:** Pass outside, fail at the edge. Outside: ~2/255, the re-encode level; 7 fire pixels in 81 frames. Inside, the redrawn grass is darker than the plate (luma −8 to −13 from 2 to 60 px inside the edge on frame 80), so the mask outline shows as a dark ring (James); Compose + Match did not correct it
- **Look:** Mixed. Flames weave through the blades, with blades in front and a scorched base, and the window blends into the plate with no visible seam. But the flames are saturated, hard-edged and sticker-like, with no smoke and no spread up the blades, and their colour does not match Jerry
- **Next:** prompt rewrite (below)

## Test 2 — 2026-11-02

- **Change:** Test 1 plus `JB-010` as Reference Image 2 (James), `vace_ref_strength` still 0
- **Run:** 647 s (L4); prompt 1.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test2-jb010_seed1218565630_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test2-jb010_seed1218565630_v001.workflow.json`.
- **Ignition:** Pass, same as test 1
- **Fire size and place:** Fail, ≈ test 1: 1.7–6.8% of the window, 59–84% of it under Jerry. A different sample after ignition (PSNR 19–25 dB against test 1, 43 dB or more before frame 25), not a style change
- **Plate outside the mask:** Pass outside; the same dark ring
- **Look:** Same sticker-like flames; a bluish-white smoke puff at the base late in the shot
- **Next:** With `vace_ref_strength` 0 an added reference only reshuffles the sample. To pass style it needs a strength above 0, which risks Jerry's shape. Back to test 1's state for the prompt rewrite

## Test 3 — 2026-11-03

- **Change:** Test 1 with the prompt rewrite (whole clump engulfed, tall flames, smoke, Jerry's flame words); `JB-010` bypassed. On an A100, so not seed-for-seed comparable with tests 1–2
- **Run:** 280 s (A100); prompt 2.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test3-prompt2_seed1218565630_eu-ro-a100_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test3-prompt2_seed1218565630_eu-ro-a100_v001.workflow.json`.
- **Ignition:** Pass
- **Fire size and place:** Fail, a little better: 0.9–6.4% of the window, 11–13% of the mask; wider, two-lobed flames, so less of it under Jerry (42–76%). Climbs higher early (top row 90 vs 123 on frame 40) but not by the end. 107 fire pixels outside the mask
- **Plate outside the mask:** Pass outside; the dark ring is unchanged (−10.6 and −12.8 luma inside the edge on frames 50 and 80)
- **Look:** Brighter, whiter flames, close to Jerry's average colour (fire pixels RGB 239/177/95 against Jerry's 224/158/93), but hard-edged and cut-out, not soft and translucent like Jerry. The blades stay intact thin dark lines in front of the flames: the fire sits behind the grass instead of the grass burning (James)
- **Next:** loosen the edges inside the mask

## Test 4 — 2026-11-03

- **Change:** Test 3 with `vace_strength` 1.0 → 0.6 (same A100)
- **Run:** 191 s (A100); prompt 2.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test4-prompt2-str060_seed1218565630_eu-ro-a100_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test4-prompt2-str060_seed1218565630_eu-ro-a100_v001.workflow.json`.
- **Ignition:** Pass
- **Fire size and place:** Fail, better: from frame 50 the fire is 8–9% of the window and 15–17% of the mask (test 3: 6% and 11–12%), still 54–77% under Jerry. A different sample (PSNR 13–15 dB against test 3). Inside the mask the grass follows the plate's edges less (edge agreement 0.24–0.28 against 0.33–0.36)
- **Plate outside the mask:** Pass outside; the dark ring is unchanged (−11.8 and −12.7 luma)
- **Look:** Fuller flames, but still cut-out, and the blades are still dark lines in front of them. James: not much different
- **Next:** gray inside the mask, or a keyframe in the control video

## Test 5 (repeat) — 2026-11-03

- **Change:** Meant as gray inside the mask, but the DRIVING VIDEO loader still pointed at the Canny control, so the graph was test 4's exactly
- **Run:** 190 s (A100); prompt 2.
- **Kept:** not kept.
- **Ignition:** —
- **Fire size and place:** Every frame pixel-identical to test 4 (max difference 0)
- **Plate outside the mask:** —
- **Look:** —
- **Next:** Not kept. It shows that on one GPU type and install a rerun reproduces exactly, so one-knob A/B on the A100 is exact. Rerun as test 6 with the gray control

## Test 6 — 2026-11-03

- **Change:** Test 4 with flat gray instead of Canny edges inside the mask (same A100)
- **Run:** 190 s (A100); prompt 2.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test6-gray-prompt2-str060_seed1218565630_eu-ro-a100_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test6-gray-prompt2-str060_seed1218565630_eu-ro-a100_v001.workflow.json`.
- **Ignition:** Pass
- **Fire size and place:** Fail on look, not size: 3–10% of the window, 9–19% of the mask, about as large as test 4, and less of it under Jerry mid-shot (47–49% on frames 50–66). 157 fire pixels outside the mask
- **Plate outside the mask:** Pass outside; the dark ring stays (−11.7 and −10.7 luma)
- **Look:** The interaction James wanted: the fire replaces the blades where it burns instead of sitting behind intact ones, with embers falling and a scorched, glowing base. But the flames are a thick, opaque, blown-out yellow-white mass with a hard orange outline, wild and far from Jerry's soft, translucent fire (James: too thick and wild)
- **Next:** calmer prompt on the gray control; then the keyframe

## Test 7 — 2026-11-03

- **Change:** Test 6 with prompt 3 (James): drops "engulfs the whole clump" and "tall flames … rise high above the tips", asks for low flickering flames running up individual blades, keeps Jerry's flame words. Checked: only the prompt changed.
- **Run:** 192 s (A100); prompt 3.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test7-gray-prompt3-str060_seed1218565630_eu-ro-a100_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test7-gray-prompt3-str060_seed1218565630_eu-ro-a100_v001.workflow.json`.
- **Ignition:** Pass, later and smaller: 1.3% of the window on frame 32 (test 6: 3.0%).
- **Fire size and place:** Mixed. One peak at frame 50 (13.5% of the window, 25% of the mask, the largest of any test), then it shrinks to 5.7% by frame 80 (test 6: 10.0% and 7.4%). Under Jerry 40–100% (frame 50: 40%). 40 fire pixels outside the mask over 81 frames (test 6: 133). Inside the mask the output follows the plate's grass edges more (edge agreement 0.43–0.53 against 0.23–0.43 in test 6), so more of the grass is left as it was.
- **Plate outside the mask:** Pass outside; the dark ring stays (−15.0 and −11.9 luma on frames 50 and 80, against −15.8 and −14.8 for test 6 by the same measure).
- **Look:** Calmer and smoother: blown-out white inside the mask fell from 11–14% to about 5%, and the flame has a soft gradient from a yellow-white heart to orange edges. But it is no longer a grass fire. It is one smooth ribbon of flame floating above the grass, close to a second Jerry, with no blades burning, no scorch at the base and no embers. The interaction from test 6 is gone.
- **Reading:** Jerry's flame words ("soft and translucent, peach-white glow at the heart, orange and gold tongues"), once the "engulf" and "tall flames" words are gone, pull the model toward the l3n0v0 creature-like flame sheet. The words that make it a grass fire make it wild (test 6). A prompt cannot do both, so the style should come from a picture (the keyframe) or the comp grade, and the prompt should only describe physical grass fire.
- **Next:** prompt 4 on the gray control: prompt 1's physical grass-fire wording without "small flame", no Jerry style words. Then the keyframe.

## Test 8 — 2026-11-03

- **Change:** Test 6 with a new seed (`seed_1` in Iter Seed Batch, node 3462: 1218565630 → 1218565804), James. Prompt 2 restored. Checked: only the seed changed. The first of the seed checks in the plan.
- **Run:** 192 s (A100); prompt 2.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test8-gray-prompt2-str060_seed1218565804_eu-ro-a100_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test8-gray-prompt2-str060_seed1218565804_eu-ro-a100_v001.workflow.json`.
- **Ignition:** Pass, but it starts as a large white smoke puff (frames 32–50) with the flame inside it.
- **Fire size and place:** Larger and earlier than test 6: 9.8% of the window on frame 40 (test 6: 4.4%), 13.0% on frame 50, 9.3% on frame 80; 15–25% of the mask from frame 40. More of it under Jerry (62–91% from frame 50). No fire pixels outside the mask (test 6: 133).
- **Plate outside the mask:** Pass outside. The ring measure reads +13.1 on frame 50 because the smoke inside the mask is brighter than the plate, and −8.4 on frame 80 (test 6: −15.8 and −14.8).
- **Look:** Very different from test 6 at the same settings. Flames are separate vertical tongues with soft edges, much less blown out (white 3–5% of the mask against 11–14%), with blades crossing in front of them. Closer to Jerry's tongues than test 6. But a thick white-lavender smoke cloud fills much of the mask from frame 32 to about 60, reading like steam, and there is less scorch and fewer embers than test 6.
- **Reading:** The seed changes the result as much as any single knob tried so far (tests 3–7). Single runs have been compared as if the change caused the difference; from here each setting needs at least two seeds before it is judged.
- **Next:** a third seed of test 6, then compare prompt 4 over the same seeds.

## Test 9 — 2026-11-03

- **Change:** Test 6 with a third seed (`seed_1` 1218565630 → 1218565905), James. Checked: only the seed changed.
- **Run:** 190 s (A100); prompt 2.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test9-gray-prompt2-str060_seed1218565905_eu-ro-a100_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test9-gray-prompt2-str060_seed1218565905_eu-ro-a100_v001.workflow.json`.
- **Ignition:** Pass, the earliest and largest of the three seeds: 5.6% of the window on frame 32 (tests 6 and 8: 3.0% and 1.7%).
- **Fire size and place:** 10–12% of the window from frame 40 to 80, the steadiest of the three; 51–77% under Jerry. 888 fire pixels outside the mask, all on frames 26–40, where the fire runs ahead of the mask while it is still small.
- **Plate outside the mask:** Pass outside, apart from those early pixels. Ring −5.2 and +4.3 luma on frames 50 and 80.
- **Look:** A wide, bowl-shaped sheet of opaque flame, the most blown out of the three (white 12–24% of the mask, against 11–14% for test 6 and 3–5% for test 8), with a little dark smoke at the edges. The blades are dark lines in front of the flames again rather than burning. James: less interaction with the grass, a little too wild.
- **Reading over tests 6, 8 and 9 (same settings, three seeds):** size and coverage are consistent (about 10–13% of the window by frame 50). The look is consistently thick, opaque, wild fire. What changes with the seed is the smoke (none, a heavy cloud, a little) and whether the blades burn or stay in front. These settings will not give Jerry's look by reseeding; the next change has to constrain the fire's shape or show the model the look.
- **Next:** see the plan, Pass B tests.

## Test 10 — 2026-11-03

- **Change:** Test 6 (first seed, 1218565630) with two changes, James: `vace_strength` 0.6 → 0.8, and "opaque, blown out, fireball, smoke cloud" added to the end of the NAG negative prompt (node 3262). The two cannot be separated in this run.
- **Run:** 191 s (A100); prompt 2.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test10-gray-prompt2-str080-nagneg2_seed1218565630_eu-ro-a100_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test10-gray-prompt2-str080-nagneg2_seed1218565630_eu-ro-a100_v001.workflow.json`.
- **Ignition:** Pass, as test 6.
- **Fire size and place:** Nearly test 6: the same sample and composition, slightly smaller (8.5% of the window on frames 50–66 against 8.5–10.0%); 47–63% under Jerry; 42 fire pixels outside the mask (test 6: 133). Inside the mask the output follows the plate's blade edges a little more (edge agreement 0.29–0.34 against 0.23–0.27).
- **Plate outside the mask:** Pass outside; the ring is unchanged (−15.3 and −16.1 luma, same measure as tests 7–9).
- **Look:** Test 6 again, a little tidier, with the blades slightly more present and a scorched, ember-lit base. Still thick and blown out: white in 8–14% of the mask, as in test 6, so the "opaque, blown out" negatives did not reduce it.
- **Reading:** Within 0.6–0.8 and with these negatives the result is set by the seed and the inputs, not by these knobs.
- **Next:** the combined mask (full strength on the blades, half on the space around them) with edges on gray.

## Test 11 — 2026-11-03

- **Change:** Test 10 with the combined mask and its control (James's idea): MASK `shot004_grassfire_mask-start25-full50-blades4-field050-soft_912x512_81f_v001.mp4` (full strength on the blades, 0.5 on the rest of the spread) and DRIVING VIDEO `shot004_grassfire_control-plate-canny-gray-start25-full50_912x512_81f_v001.mp4` (blade edges on gray inside the spread). Checked: only the two loaders changed. A first attempt loaded the Canny-on-black control by mistake and was stopped before it finished; it is not counted.
- **Run:** 194 s (A100); prompt 2.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test11-cannygray-blades4-field050-str080-nagneg2_seed1218565630_eu-ro-a100_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test11-cannygray-blades4-field050-str080-nagneg2_seed1218565630_eu-ro-a100_v001.workflow.json`.
- **Ignition:** Pass, earlier and larger: 6.1% of the window on frame 32 (test 10: 2.7%).
- **Fire size and place:** 7–11% of the window, 43–78% under Jerry; 27 fire pixels outside the mask.
- **Plate outside the mask:** Fail at the mask. The half-strength area came out as a flat, light gray veil, about 45 luma brighter than the plate (difference from the plate there 44–49, against 3.4 outside the mask), so the whole outline of the spread shows (James: the mask shows up as an artifact).
- **Look:** The flames themselves are the softest yet: white in only 0.2–2.4% of the mask (test 10: 8–14%), more translucent, with the blades as dark lines in front. But the blades do not burn (James: no interaction), and the gray veil spoils the frame.
- **Reading:** With a mask between 0 and 1 the VACE node keeps that share of the control as it is. The control showed flat gray there, so the model half-kept the gray, and Compose + Match then pasted that area at half strength. Whatever sits under a partial mask must be the plate, not gray, so that "half keep" means half keep the grass.
- **Next:** test 11b: the same mask with the plate, not gray, in the half-strength area, and gray with edges only on the blades.

## Test 11b — 2026-11-03

- **Change:** Test 11 with the plate, not gray, in the half-strength area: DRIVING VIDEO `shot004_grassfire_control-plate-canny-gray-blades4-start25-full50_912x512_81f_v001.mp4` (gray with edges only on the full-strength blade strips, plate everywhere else; `--field-fill plate`). Same mask. Checked: only the DRIVING VIDEO changed.
- **Run:** about 190 s (A100); prompt 2.
- **Kept:** `benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test11b-cannygray-bladesonly-field050-platefield-str080-nagneg2_seed1218565630_eu-ro-a100_v001.mp4` and `shot004-benchmark/shot004_fire-jump_grassfire-inpaint_mick13_test11b-cannygray-bladesonly-field050-platefield-str080-nagneg2_seed1218565630_eu-ro-a100_v001.workflow.json`.
- **Ignition:** Weak and late: 0.3% of the window on frame 32, 2.6% on frame 40.
- **Fire size and place:** Small: about 3% of the window from frame 50 (test 10: 7–8.5%), 40–56% under Jerry. 63 fire pixels outside the mask.
- **Plate outside the mask:** The veil is gone: the half-strength area stays within about 4 luma of the plate (difference 7.5–7.9). New artifact on the blade strips: the model redrew the gray strips and their white edges as pale blue-gray tubes over the blades, about 16–19 luma brighter than the plate (James: still mask artifacts).
- **Look:** The flames that do appear run along the blades in thin tongues, the closest yet to fire climbing individual blades. But they are small, and the tubes spoil the frame.
- **Reading:** Under the full-strength strips the model copied the control's pattern instead of drawing fire. The strips are about 9 px wide, close to the model's 8 px working grid, and with half of the spread on "keep" the model leans toward copying. Thin, fine-grained masks do not work with this model; masks need to be regions at least a few grid cells wide. Stop the combined-mask branch here.
- **Next:** test 12, the keyframe as a reference, on test 10's setup.
