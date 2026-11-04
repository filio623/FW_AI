# Shot 004 reference media

Media the shot is measured against; none of it is an element in the comp. Heavy media is gitignored; this README is the record.

## Contents

- `ren_small_fire6..mov`: the delivered Houdini fire element, production file name kept. H.264, 1920x1080, 24 fps, 87 frames, 3.625 s, `yuv420p`, no alpha. The motion source for Pass A.
- `shot004_fire-jump_ren-small-fire6_source_v001.mov`: the same bytes under the project name.
- `shot004_fire-jump_comp-houdini-delivered-v031_1920x1080_v001.mp4`: the delivered Houdini comp (1920x1080, 84 frames; production name `Shot4 V031-1.mp4`, the NAS original is `Shot4 V031-1.mov`). Timing reference: the fire lands around frame 23, the grass catches and spreads through about frame 48.

## Source and history

- 2026-08-18: `ren_small_fire6` copied from the NAS backup `/Volumes/FW_Backup/Robs-Mac-Studio.local/Volumes/Rob's 4tb FAST/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6/Proxy/`. Its EXR sequence stays on the backup; an extracted 112-frame alternate (`.../Small Fire_ extracted/Proxy/ren_small_fire6..mov`) was not copied.
- 2026-10-08: delivered comp copy added (renamed 2026-11-04).
- Still on the backup, not copied: `ren_grassfire_cpu` (Pass B reference), `ren_small_waterCHAR8`, `ren_small_waterSplash`, `ren_steam`. Restore list: `../plan.md`, Files to fetch from the NAS.
- 2026-11-04: moved here from `assets/elements/by-shot/shot004_fire-jump/fire/` and `comps/` (shot-first layout).
