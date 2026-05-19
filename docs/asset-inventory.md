# Asset Inventory

Use this file as the human-readable index for active assets. Raw uploads may sit in `assets/inbox/` briefly, but anything used for production should be listed here or in the relevant shot note.

## Asset Roots

- `assets/inbox/`: incoming unsorted files.
- `assets/scripts/`: screenplay PDF and script breakdown notes.
- `assets/storyboards/`: storyboard panels and animatics.
- `assets/plates/`: source plates, shot folders, proxies, stills, and mattes.
- `assets/elements/`: separable VFX elements and generated passes.
- `assets/characters/`: character references and approved looks.
- `assets/references/`: visual, motion, and style references.
- `assets/audio/`: music, dialogue, and sound effects.
- `assets/editorial/`: EDL/XML files and reference exports.

## FW_test

Current test folder:

- `FW_test/Scene 4/4 base plate.mov`: base environmental plate.
- `FW_test/Scene 4/FW_test_scene.mov`: likely existing scene composite or reference.
- `FW_test/Scene 4/Shot4 V031-1.mp4`: likely review/export reference.
- `FW_test/Scene 4/ren_grassfire_cpu..mov`: grass fire render.
- `FW_test/Scene 4/ren_small_fire6..mov`: fire character render.
- `FW_test/Scene 4/ren_small_waterCHAR8..mov`: water character render.
- `FW_test/Scene 4/ren_small_waterSplash..mov`: water splash render.
- `FW_test/Scene 4/ren_steam..mov`: steam render.

These files have not been moved yet. Treat `FW_test/Scene 4/` as the preserved incoming source/test folder until shot004 is fully organized under `assets/plates/by-shot/` and `assets/elements/`.

### Technical Metadata

Checked with `ffprobe` on 2026-05-18:

- `4 base plate.mov`: ProRes, 4096x2160, 24 fps, 87 frames, 3.625s, `yuv444p12le`.
- `FW_test_scene.mov`: HEVC, 4096x2160, 24 fps, 84 frames, 3.5s, `yuv420p10le`.
- `Shot4 V031-1.mp4`: H.264, 1920x1080, 24 fps, 84 frames, 3.5s, `yuv420p`.
- `ren_small_fire6..mov`: H.264, 1920x1080, 24 fps, 87 frames, 3.625s, `yuv420p`.
- `ren_grassfire_cpu..mov`: H.264, 1920x1080, 24 fps, 86 frames, 3.583s, `yuv420p`.
- `ren_steam..mov`: H.264, 1920x1080, 24 fps, 82 frames, 3.417s, `yuv420p`.
- `ren_small_waterCHAR8..mov`: H.264, 1920x1080, 24 fps, 86 frames, 3.583s, `yuv420p`.
- `ren_small_waterSplash..mov`: H.264, 1920x1080, 24 fps, 33 frames, 1.375s, `yuv420p`.

Alpha note: the H.264 element/reference renders use `yuv420p`, so they do not contain an embedded alpha channel. Treat them as motion, timing, scale, and visual references unless matte extraction is performed separately.

## Active Shot Asset Logs

- `shots/shot004_fire-jump_workflow-test-plan_v001.md`: current shot004 planning note.

## Script

- `assets/scripts/Fire and Water, A love Story 2023 (1).pdf`: current uploaded screenplay PDF. PDF version 1.4, 8 pages, title metadata `Fire and Water, A love Story 2023`.
- `assets/scripts/fire-and-water_script_extracted.md`: searchable text extracted from the screenplay PDF with `pypdf`. Lightly normalized; check against the PDF before final script breakdown.

## Notes

`ffmpeg` and `ffprobe` are now installed. Use them for detailed inspection and reference-frame extraction.
