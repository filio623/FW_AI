**Created:** 2026-05-19
**Modified:** 2026-05-19
**Version:** 1.0

# Scene 4 Jerry Fire Video Test Log v001

Date started: 2026-05-19

Status: first Higgsfield Seedance 2.0 baseline completed.

## Goal

Test whether Higgsfield can generate a baked preview of Jerry's fire element/motion over the Scene 4 base footage, using the approved Jerry character-bible references.

This is not expected to produce a final alpha element. Treat it as a motion/look benchmark before building a more controlled ComfyUI workflow.

## Source Media

- Base footage: `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/FW_test_scene.mov`
  - 4096x2160
  - 24 fps
  - 3.5 seconds
- Rough reference: `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/Shot4 V031-1.mp4`
  - 1920x1080
  - 24 fps
  - 3.5 seconds
- Isolated fire motion reference: `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/ren_small_fire6..mov`
  - 1920x1080
  - 24 fps
  - 3.63 seconds

## Character References

- Character-bible folder: `assets/characters/jerry/character-bible-v001/`
- Primary body refs:
  - `assets/characters/jerry/character-bible-v001/references/primary-body/JB-001_upright-compact-idle.png`
  - `assets/characters/jerry/character-bible-v001/references/primary-body/JB-009_small-upright-idle.png`
  - `assets/characters/jerry/character-bible-v001/references/primary-body/JB-010_round-idle-glow.png`
- Motion ref:
  - `assets/characters/jerry/character-bible-v001/references/motion-poses/JB-004_fast-right-comet.png`
- Material ref:
  - `assets/characters/jerry/character-bible-v001/references/material/JB-012_upright-wild-flicker_material-ref.png`

## Core Constraints

- Generate Jerry's fire element only.
- Do not generate Sally/water droplet.
- Do not bake in eyes, mouth, brows, nose, smile, or other facial features.
- Preserve the base plate as much as the model allows.
- Do not overwrite source footage.

## Run 001

- Date: 2026-05-19
- Model: Higgsfield Seedance 2.0 (`seedance_2_0`)
- Job ID: `1814d06e-b8d5-41a1-a0ff-7eabe31319de`
- Status: failed
- Command summary:
  - Used the original 4K base plate as video input.
  - Used the rough comp as a second video input.
  - Used four Jerry character-bible stills as image references.
  - Requested 16:9, 1080p, 5 seconds, `mode=std`.
- Input media:
  - `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/FW_test_scene.mov`
  - `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/Shot4 V031-1.mp4`
- Reference images:
  - `assets/characters/jerry/character-bible-v001/references/primary-body/JB-001_upright-compact-idle.png`
  - `assets/characters/jerry/character-bible-v001/references/primary-body/JB-010_round-idle-glow.png`
  - `assets/characters/jerry/character-bible-v001/references/motion-poses/JB-004_fast-right-comet.png`
  - `assets/characters/jerry/character-bible-v001/references/material/JB-012_upright-wild-flicker_material-ref.png`
- Duration: 5 seconds requested
- Aspect ratio: 16:9
- Resolution: 1080p
- Output URL: none
- Local copy: none
- Cost: not captured
- Notes: The CLI accepted the mixed-media command and uploaded both videos plus the image references, but the generated job returned `status=failed` with no result URL. `higgsfield generate get` did not find the failed job afterward, so no deeper error detail was available.
- Decision: Do not use this full mixed-reference bundle as the next default. Simplify inputs first, then add references back one at a time.

## Run 002

- Date: 2026-05-19
- Model: Higgsfield Seedance 2.0 (`seedance_2_0`)
- Job ID: `692244d8-18cc-4def-bea3-eb2b511dd8a3`
- Status: completed
- Command summary:
  - Used a local 1080p H.264 proxy of the Scene 4 base plate as the only video input.
  - Did not include the rough comp or Jerry still references.
  - Requested 16:9, 1080p, 5 seconds, `mode=std`.
- Input media:
  - Source: `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/FW_test_scene.mov`
  - Local proxy: `outputs/higgsfield/scene4_jerry-fire-test_v001/source_proxies/FW_test_scene_1080p24_v001.mp4`
- Reference images: none in this simplified run
- Duration:
  - Requested: 5 seconds
  - Output: 5.06 seconds
- Aspect ratio: 16:9
- Resolution:
  - Requested: 1080p
  - Output: 1920x1080
- Frame rate: 24 fps
- Output URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260519_205732_692244d8-18cc-4def-bea3-eb2b511dd8a3.mp4`
- Local copy: `outputs/higgsfield/scene4_jerry-fire-test_v001/scene4_jerry_seedance2_simplified-video-only_run002.mp4`
- Cost: not captured for the completed job; prior estimate for Seedance 2.0 1080p 5s std was 45 credits.
- Notes:
  - Output downloaded successfully.
  - Output container: MP4, H.264 video, AAC audio, 1920x1080, 24 fps, 5.06 seconds.
  - This run is a baseline to test whether Seedance can modify the plate with a simple video-only input.
- Review notes:
  - Fire motion does not follow the intended reference action from `Shot4 V031-1.mp4`.
  - Intended action: Jerry starts lower-middle frame, bounces back into the grass, and ignites it.
  - Generated action: fire comes in from frame right, bounces left, then exits/ends without matching the intended fire path.
  - Jerry look is too blurry and does not match the approved character-bible reference images closely enough.
- Decision: Useful as a first baseline only. Next run should prioritize motion fidelity and character fidelity separately instead of relying on text prompt alone.

## Review Aids

- Rough comp contact sheet: `outputs/higgsfield/scene4_jerry-fire-test_v001/review_refs/shot4_rough-comp_contact_v001.jpg`
- Isolated fire render contact sheet: `outputs/higgsfield/scene4_jerry-fire-test_v001/review_refs/ren_small_fire6_contact_v001.jpg`
- Seedance Run 002 contact sheet: `outputs/higgsfield/scene4_jerry-fire-test_v001/review_refs/seedance_run002_contact_v001.jpg`
- Seedance Run 003 contact sheet: `outputs/higgsfield/scene4_jerry-fire-test_v001/review_refs/seedance_run003_fire-motion-plus-jb001_contact_v001.jpg`
- Seedance Run 004 contact sheet: `outputs/higgsfield/scene4_jerry-fire-test_v001/review_refs/seedance_run004_plate-motion-jb001_contact_v001.jpg`
- Seedance Run 006 contact sheet: `outputs/higgsfield/scene4_jerry-fire-test_v001/review_refs/seedance_run006_plate-motion-jb001_hierarchy_contact_v001.jpg`

## Run 003 Attempts

### Kling 3.0 Motion-First Attempt

- Date: 2026-05-19
- Model: Higgsfield Kling 3.0 (`kling3_0`)
- Status: failed before job result
- Command summary:
  - Used `ren_small_fire6..mov` as a motion/reference video.
  - Used `JB-001_upright-compact-idle.png` as `--start-image`.
  - Requested 16:9, 5 seconds, `mode=std`, `sound=off`.
- Result: HTTP 500 Internal Server Error.
- Output URL: none
- Decision: Do not treat as a creative failure. This appears to be a backend/CLI media-shape failure for video plus start-image in this endpoint.

### Wan 2.7 Motion-First Attempt

- Date: 2026-05-19
- Model: Higgsfield Wan 2.7 (`wan2_7`)
- Status: failed before job result
- Command summary:
  - Used `ren_small_fire6..mov` as a motion/reference video.
  - Used `JB-001_upright-compact-idle.png` as an image reference.
  - Requested 16:9, 1080p, 5 seconds.
- Result: HTTP 500 Internal Server Error.
- Output URL: none
- Decision: Same as Kling 3.0; likely a backend/CLI media-shape issue for this combined-media path.

## Run 003

- Date: 2026-05-19
- Model: Higgsfield Seedance 2.0 (`seedance_2_0`)
- Job ID: `69c359a2-9863-4ce0-88c9-849df2bf150c`
- Status: completed
- Command summary:
  - Used the isolated fire render as the motion/timing video reference.
  - Used one Jerry character-bible reference as `--start-image`.
  - Did not include the base plate.
  - Requested 16:9, 1080p, 5 seconds, `mode=std`.
- Input media:
  - Motion video: `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/ren_small_fire6..mov`
  - Start image: `assets/characters/jerry/character-bible-v001/references/primary-body/JB-001_upright-compact-idle.png`
- Duration:
  - Requested: 5 seconds
  - Output: 5.06 seconds
- Aspect ratio: 16:9
- Resolution:
  - Requested: 1080p
  - Output: 1920x1080
- Frame rate: 24 fps
- Output URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260519_215038_69c359a2-9863-4ce0-88c9-849df2bf150c.mp4`
- Local copy: `outputs/higgsfield/scene4_jerry-fire-test_v001/scene4_jerry_seedance2_fire-motion-plus-jb001_run003.mp4`
- Cost: not captured for the completed job; prior estimate for Seedance 2.0 1080p 5s std was 45 credits.
- Notes:
  - Output downloaded successfully.
  - Output container: MP4, H.264 video, AAC audio, 1920x1080, 24 fps, 5.06 seconds.
  - Job metadata confirms media roles: `ren_small_fire6..mov` was submitted as `video`; `JB-001` was submitted as `start_image`.
- Review notes:
  - Character and animation are much better than Run 002.
  - The result used a completely different generated background and did not preserve the Scene 4 plate.
  - This is expected for this test because the Scene 4 base plate was intentionally not included; Run 003 isolated motion and character identity only.
  - The next production-relevant question is how to combine the improved Jerry motion/look with the real plate, either as a baked plate-aware preview or as a separable VFX element with matte/alpha.
- Decision: Successful as a motion/look isolation test, not a plate integration test.

## Run 004

- Date: 2026-05-19
- Model: Higgsfield Seedance 2.0 (`seedance_2_0`)
- Job ID: `f5807e08-6e63-4140-854a-8c9bf4a541a3`
- Status: completed
- Command summary:
  - Used the Scene 4 1080p H.264 proxy as the first video input and instructed the model to treat it as the locked background plate.
  - Used `ren_small_fire6..mov` as the second video input and instructed the model to treat it only as Jerry motion/timing reference.
  - Used `JB-001_upright-compact-idle.png` as `--start-image` for Jerry identity.
  - Requested 16:9, 1080p, 5 seconds, `mode=std`.
- Input media:
  - Plate video: `outputs/higgsfield/scene4_jerry-fire-test_v001/source_proxies/FW_test_scene_1080p24_v001.mp4`
  - Motion video: `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/ren_small_fire6..mov`
  - Start image: `assets/characters/jerry/character-bible-v001/references/primary-body/JB-001_upright-compact-idle.png`
- Duration:
  - Requested: 5 seconds
  - Output: 5.06 seconds
- Aspect ratio: 16:9
- Resolution:
  - Requested: 1080p
  - Output: 1920x1080
- Frame rate: 24 fps
- Output URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260520_005549_f5807e08-6e63-4140-854a-8c9bf4a541a3.mp4`
- Local copy: `outputs/higgsfield/scene4_jerry-fire-test_v001/scene4_jerry_seedance2_plate-motion-jb001_run004.mp4`
- Cost: not captured for the completed job; prior estimate for Seedance 2.0 1080p 5s std was 45 credits.
- Notes:
  - Output downloaded successfully.
  - Output container: MP4, H.264 video, AAC audio, 1920x1080, 24 fps, 5.06 seconds.
  - Job metadata confirms media roles: first plate proxy as `video`, second fire-motion reference as `video`, and `JB-001` as `start_image`.
- Review notes:
  - Win: this is the first completed CLI run that successfully used all three reference categories in one request: plate, motion video, and Jerry image.
  - Issue: the model appears to have used the `ren_small_fire6..mov` fire animation element as the primary visual source for Jerry's fire look, not only as motion reference.
  - Intended behavior: use `JB-001` / Jerry character-bible imagery as the primary source for modeling Jerry's fire body and material, while using `ren_small_fire6..mov` only for timing, path, bounce, and landing motion.
- Decision: Successful input-routing proof, but not yet the correct visual hierarchy. Next prompt/test should explicitly down-rank the fire render as motion-only and up-rank the Jerry still as the visual identity/material source.

## Run 005

- Date: 2026-05-19
- Model: Higgsfield Seedance 2.0 (`seedance_2_0`)
- Job ID: `abbc4ef8-f25c-41b4-ae38-636ea870981e`
- Status: `ip_detected`
- Command summary:
  - Same plate-aware structure as Run 004.
  - Strengthened prompt hierarchy: plate is locked, Jerry image is primary look/material source, fire motion video is motion-only.
  - Passed `JB-001_upright-compact-idle.png` as both `--start-image` and `--image` to reinforce Jerry identity over the fire-motion clip.
- Input media:
  - Plate video: `outputs/higgsfield/scene4_jerry-fire-test_v001/source_proxies/FW_test_scene_1080p24_v001.mp4`
  - Motion video: `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/ren_small_fire6..mov`
  - Start/image reference: `assets/characters/jerry/character-bible-v001/references/primary-body/JB-001_upright-compact-idle.png`
- Duration: 5 seconds requested
- Aspect ratio: 16:9
- Resolution: 1080p
- Output URL: none
- Local copy: none
- Notes:
  - Higgsfield accepted the media shape through submission and generation.
  - The duplicate Jerry `--image` was represented in job metadata as a second `start_image` role using the same uploaded media ID.
  - The job returned `ip_detected`, not a creative output. This likely reflects Higgsfield's IP/provenance filter, not a normal model-quality failure.
- Decision: Do not retry the identical duplicate-image setup blindly. If continuing this branch, try a safer visual-hierarchy prompt with one Jerry start image, or use a different Jerry bible still/material reference instead of duplicating the exact same image.

## Run 006

- Date: 2026-05-19
- Model: Higgsfield Seedance 2.0 (`seedance_2_0`)
- Job ID: `8bc3f306-27e9-4d07-baef-bec780c06c4c`
- Status: completed
- Command summary:
  - Same plate-aware structure as Run 004.
  - Kept the stronger visual hierarchy prompt from Run 005.
  - Removed the duplicate Jerry `--image` to avoid the Run 005 `ip_detected` failure.
  - Avoided using the character name in the prompt and referred to the subject as the original flame character.
- Input media:
  - Plate video: `outputs/higgsfield/scene4_jerry-fire-test_v001/source_proxies/FW_test_scene_1080p24_v001.mp4`
  - Motion video: `/Users/robbiefilios/Documents/FW_AI_Workflow/FW_test/Scene 4/ren_small_fire6..mov`
  - Start image: `assets/characters/jerry/character-bible-v001/references/primary-body/JB-001_upright-compact-idle.png`
- Duration:
  - Requested: 5 seconds
  - Output: 5.06 seconds
- Aspect ratio: 16:9
- Resolution:
  - Requested: 1080p
  - Output: 1920x1080
- Frame rate: 24 fps
- Output URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260520_031025_8bc3f306-27e9-4d07-baef-bec780c06c4c.mp4`
- Local copy: `outputs/higgsfield/scene4_jerry-fire-test_v001/scene4_jerry_seedance2_plate-motion-jb001_hierarchy-run006.mp4`
- Cost: not captured for the completed job; prior estimate for Seedance 2.0 1080p 5s std was 45 credits.
- Notes:
  - Output downloaded successfully.
  - Output container: MP4, H.264 video, AAC audio, 1920x1080, 24 fps, 5.06 seconds.
  - Job metadata confirms media roles: plate proxy as `video`, fire-motion reference as `video`, and `JB-001` as `start_image`.
  - Removing the duplicate image avoided the Run 005 `ip_detected` status.
- Decision: Pending visual review. Compare directly against Run 004 to see whether prompt-only hierarchy improved the character look while retaining plate and motion.

## Higgsfield Access Notes

- Current Codex session has Supermemory MCP resources only; no Higgsfield MCP server is configured.
- Local notes confirm Higgsfield is currently available through the authenticated CLI, not MCP: `mcp/higgsfield.md`.
- The CLI can run Seedance 2.0 mixed `video` + `start_image` jobs, but Kling 3.0 and Wan 2.7 returned HTTP 500 for comparable combined-media tests.
- The Higgsfield web UI may expose a dedicated Motion Control workflow with clearer separate slots for character image, motion video, and video editing/plate input than the CLI currently exposes.
- If a Higgsfield MCP or richer API is available later, evaluate whether it supports true multi-slot inputs: plate video, motion/reference video, character/reference image, first/last frame, and output/matte controls.

## Next Higgsfield Test Recommendation

Based on Run 002, the next useful tests should isolate one variable at a time:

1. Motion-first: use `ren_small_fire6..mov` or `Shot4 V031-1.mp4` as the motion reference, with one Jerry image reference only.
2. Character-first: create a stronger single Jerry keyframe from the character-bible stills, then use that as `--start-image` or `--image`.
3. Plate-last: only once motion and look are closer, reintroduce the base plate as context. Treat plate integration as a later baked-preview test, not the first constraint.
4. Element path: test whether Run 003 can be used as an element source by extracting or generating a matte, then compositing over `FW_test_scene.mov`.
5. Web UI/MCP path: test Higgsfield Motion Control in the UI, if available, with separate fields for character image and motion video; look for a distinct video-edit or plate-preservation mode before spending more CLI credits on full plate integration.
6. Visual hierarchy test: rerun the plate-aware shape with stronger language that the motion video is low-priority for appearance and must not determine Jerry's material, silhouette, color, or flame texture. Consider passing Jerry as both `--start-image` and `--image` if the CLI accepts it, while keeping the motion source as a single `--video`.
