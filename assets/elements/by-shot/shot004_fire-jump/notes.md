# Shot004 Fire Jump VFX Elements

## Restored working files

Copied 2026-08-18 from the NAS backup of the production drive:

`/Volumes/FW_Backup/Robs-Mac-Studio.local/Volumes/Rob's 4tb FAST/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6/Proxy/ren_small_fire6..mov`

- `fire/ren_small_fire6..mov`: preserved production filename. H.264, 1920x1080, 24 fps, 87 frames, 3.625s, `yuv420p`. No embedded alpha.
- `fire/shot004_fire-jump_ren-small-fire6_source_v001.mov`: same bytes, project-named source.
- `fire/shot004_ren-small-fire6_control_832x448_81f_v001.mp4`: rebuilt control proxy. H.264, 832x448, 24 fps, 81 frames, 3.375s. Scaled with pad-to-fit (letterboxed/pillarboxed) so the fire is not cropped. First 81 frames of the 87-frame source.
- `fire/shot004_ren-small-fire6_trajectory-dot_832x448_81f_v001.mp4`: path-only control from the 832x448 proxy. Luma centroid as a soft ~56px warm dot on black. Same 81 frames / 24 fps. Built 2026-09-03.
- `fire/shot004_ren-small-fire6_trajectory-streak_832x448_81f_v001.mp4`: stronger path control. Centroid with ~72px head and 10-frame trail.
- `fire/shot004_ren-small-fire6_control-shrunk40_832x448_81f_v001.mp4`: fire silhouette scaled 40% around centroid on black.

The 832x448 file that used to live in `outputs/` was never on the production drive. It was regenerated here.

Do not copy the EXR sequence unless a later pass needs it. Leave it on the backup at `.../ren_small_fire6/*.exr`.

An extracted alternate (112 frames) remains on the backup at `.../Small Fire_ extracted/Proxy/ren_small_fire6..mov` and has not been copied.

## Intended Organization

- `fire/`: fire character, flame-only, and fire interaction elements.
- `water/`: water character elements if needed for this shot.
- `smoke-steam/`: steam, smoke, heat haze, and vapor passes.
- `splashes/`: splash or water interaction passes.
- `scorch-contact/`: grass ignition, scorch, contact light, shadows, and glow passes.
- `mattes/`: alpha, holdout, roto, and utility mattes for generated elements.

## Known Source Candidates

Still on the backup, not yet copied:

- `.../ren_grassfire_cpu/Proxy/ren_grassfire_cpu..mov`
- `.../ren_small_waterCHAR8/`
- `.../ren_small_waterSplash/`
- `.../ren_steam/`
- Historical `FW_test/Scene 4/` copies of those same renders.
