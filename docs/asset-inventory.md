**Created:** 2026-05-18
**Modified:** 2026-10-18
**Version:** 1.9

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

## FW_test (historical, not present in this checkout)

`FW_test/` is not in this checkout and is ignored by Git. The section below is the
2026-05-18 survey of that folder, kept because it is the only durable record of the
Scene 4 source media and its technical metadata. Treat every path here as a
description of material to be restored from the external production drive, not as a
path that currently resolves.

To restore: locate the sources through `references/manifests/external-drive_inventory_v001.md`
and promote anything needed into `assets/plates/by-shot/` or `assets/elements/`
under proper `_vNNN` names, recording the promotion in this file.

Surveyed contents:

- `FW_test/Scene 4/4 base plate.mov`: base environmental plate.
- `FW_test/Scene 4/FW_test_scene.mov`: likely existing scene composite or reference.
- `FW_test/Scene 4/Shot4 V031-1.mp4`: likely review/export reference.
- `FW_test/Scene 4/ren_grassfire_cpu..mov`: grass fire render.
- `FW_test/Scene 4/ren_small_fire6..mov`: fire character render.
- `FW_test/Scene 4/ren_small_waterCHAR8..mov`: water character render.
- `FW_test/Scene 4/ren_small_waterSplash..mov`: water splash render.
- `FW_test/Scene 4/ren_steam..mov`: steam render.

As of 2026-05-18 these files had not been moved into `assets/`. The original
`FW_test/` paths remain absent; a fire source was restored on 2026-08-18 and
a separate Scene 4 test reference was staged later (indexed below). The
original `4 base plate.mov` has not been restored into this checkout.

## Restored Shot004 Fire Element

Copied from the NAS backup of the production drive, not from `FW_test/`:

`/Volumes/FW_Backup/Robs-Mac-Studio.local/Volumes/Rob's 4tb FAST/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6/Proxy/ren_small_fire6..mov`

- `assets/elements/by-shot/shot004_fire-jump/fire/ren_small_fire6..mov`: preserved production filename.
- `assets/elements/by-shot/shot004_fire-jump/fire/shot004_fire-jump_ren-small-fire6_source_v001.mov`: same bytes, project-named. H.264, 1920x1080, 24 fps, 87 frames, 3.625s, `yuv420p`.
- `assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_control_832x448_81f_v001.mp4`: rebuilt 832x448, 24 fps, 81-frame control proxy (pad-to-fit, first 81 frames). The expired `outputs/` copy was never on the production drive.
- `assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_trajectory-dot_832x448_81f_v001.mp4`: path-only control. Weighted luma centroid of the 832x448 proxy as a ~56px warm dot on black, 24 fps, 81 frames. Built 2026-09-03 to test Fun Control following jump timing without filling the CGI silhouette.
- `assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_trajectory-streak_832x448_81f_v001.mp4`: stronger path control. Same centroid with a ~72px head and 10-frame fading trail.
- `assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_control-shrunk40_832x448_81f_v001.mp4`: original fire silhouette scaled 40% around its centroid on black. Middle ground between full CGI body and path-only.

## Shot004 VACE Test Reference

- `assets/elements/by-shot/shot004_fire-jump/plates/FW_test_scene.mp4`: staged 4096x2160, 24 fps, 84-frame Scene 4 reference used for the VACE test; provenance relative to the surveyed `.mov` is unverified. This is not the original `4 base plate.mov`.
- `assets/elements/by-shot/shot004_fire-jump/plates/shot004_fw-test-scene_plate-proxy_1280x672_49f_v001.mp4`: 1280x672, 24 fps, first 49 frames of the staged MP4, Lanczos-scaled and H.264 CRF 18; used as the low-memory finishing/composite input on the A40 Pod. It is a test proxy, not a full-resolution delivery plate.

### Benchmark clips

Scored test outputs, not approved elements. Mp4s are gitignored. Extracted graphs are in `workflows/comfyui/shot004-benchmark/`. The index and the keeping rule are in `docs/vfx-element-benchmark.md`.

- `assets/elements/by-shot/shot004_fire-jump/benchmark/`: local copies of the rejected VACE proxy, the Pass A strength `1` / `0.5` / silhouette clips, two Kling Omni Edit clips, the October 11 17-frame clip, the ComfyUI Seedance 2.0 reference test, and four Wan 2.7 Video Edit runs (seed 42; seed 2126129005, the paid fallback element; seed 508 with prompt v2 and `JB-010`; seed 2126129005 with `JB-010`).

Media files are gitignored. The original base plate, grass fire, steam, and water passes are still only on the backup.

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

## Tracked Character Assets

These are committed to the repository and resolve in any checkout.

- `assets/characters/jerry/character-bible-v001/references/`: the promoted Jerry bible set, 27 images under stable `JB-###` IDs, split into `primary-body/`, `motion-poses/`, `material/`, `secondary-training/`, `source-ref-only/`, and `performance-2d-ref-only/`. Indexed by `reference_gallery.md` and `selection_manifest.tsv`. This is the durable replacement for the expired `outputs/review/jerry_asset-triage_v001/` review pass.
- `assets/characters/jerry/look-references/external-v001/`: 14 external look references defining the current no-face Jerry body direction.
- `assets/characters/jerry/higgsfield-candidates/run001`–`run005`: casting-run stills, assessed in `docs/jerry-character-bible_v001.md`.
- `assets/characters/jerry/approval-review/v001/`: Jerry approval review pack.
- `assets/characters/tom/approval-review/v001`–`v003/`: Tom review rounds, v003 current.
- `assets/characters/jerry/source-cgi/jerry_fire-rig_v001.blend`: Blender 5.2.1 Jerry fire rig (rigged emitter body, core-glow volume, Mantaflow fire, embers, idle cycle). The fluid cache is not tracked; rebake into `outputs/jerry_fire-rig_v001/cache_fluid/`. Run log: `workflows/blender/jerry/jerry_fire-rig_log_v001.md`.
- `assets/characters/jerry/source-cgi/jerry_fire-rig_idle-test-r09_f0064_v001.png`: 960x540 r09 test still from that rig. Not approved.

Empty scaffold folders (`approved/`, `actions/`, `expressions/`, `training-candidates/`) exist for both characters and are held open with `.gitkeep`, as does Tom's `source-cgi/`. Nothing is approved into `approved/` yet for either character.

## Active Shot Asset Logs

- `shots/shot004_fire-jump_workflow-test-plan_v001.md`: current shot004 planning note.

## Script

- `assets/scripts/Fire and Water, A love Story 2023 (1).pdf`: current uploaded screenplay PDF. PDF version 1.4, 8 pages, title metadata `Fire and Water, A love Story 2023`.
- `assets/scripts/fire-and-water_script_extracted.md`: searchable text extracted from the screenplay PDF with `pypdf`. Lightly normalized; check against the PDF before final script breakdown.

## Notes

`ffmpeg` and `ffprobe` are now installed. Use them for detailed inspection and reference-frame extraction.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Asset Inventory. |
| 1.1     | 2026-08-16 | Marked the `FW_test` survey as historical and not present in this checkout, and indexed the tracked Jerry and Tom character assets. |
| 1.2     | 2026-08-18 | Restored the shot004 small-fire motion source from `/Volumes/FW_Backup` and rebuilt the 832x448 control proxy into `assets/elements/by-shot/shot004_fire-jump/fire/`. |
| 1.3     | 2026-09-03 | Added the shot004 fire trajectory-dot control proxy for path-only Fun Control tests. |
| 1.4     | 2026-09-03 | Added streak and 40%-shrunk fire control proxies after the tiny dot proved too weak. |
| 1.5     | 2026-10-08 | Indexed the staged Scene 4 reference and 49-frame proxy used for low-memory VACE finishing; clarified which original plates remain off-repo. |
| 1.6     | 2026-10-17 | Indexed the Jerry Blender fire rig `.blend` and its r09 test still in `source-cgi/`. |
| 1.7     | 2026-10-17 | Indexed the local shot004 benchmark clips copied off the RunPod volume. |
| 1.8     | 2026-10-17 | Indexed the two Wan 2.7 Video Edit benchmark clips. |
| 1.9     | 2026-10-18 | Indexed Wan 2.7 runs 3 and 4 and marked seed 2126129005 as the paid fallback. |
