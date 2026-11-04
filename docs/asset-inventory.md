**Created:** 2026-05-18
**Updated:** 2026-11-04

# Asset Inventory

Index of the film's source media: what exists, where the original lives, and what has been restored into the repo. What each restored or generated file is, is recorded in the README of the folder that holds it; this file does not repeat those lists.

## Where media lives (as of 2026-11-04)

- `shots/<shot>/`: everything one shot uses (`plates/`, `reference/`, per-pass `inputs/`, `keyframes/`, `layers/`, `runs/`, `comps/`).
- `characters/<name>/`: character references, review packs, candidates, CGI.
- `source/`: screenplay. `inbox/`: uploads waiting to be sorted.
- Off the repo: the NAS backup of the production drive, `/Volumes/FW_Backup/Robs-Mac-Studio.local/Volumes/Rob's 4tb FAST`, indexed by `library/manifests/`. Any move to or from it updates its manifest.
- Until 2026-11-04 media lived under `assets/`; old-to-new paths: `docs/archive/restructure_2026-11-04_moves.tsv`.

Heavy media (video, frame sequences, plate stills, keyframes) is gitignored and exists only on this Mac and the NAS. A backup routine is an open item (`docs/todo.md`).

## Shot 004 source media

Production files of the delivered shot (`04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/` on the NAS unless noted). Technical data from `ffprobe`, 2026-05-18.

| File | Format | Status |
|---|---|---|
| `4 base plate.mov` | ProRes, 4096x2160, 24 fps, 87 frames, `yuv444p12le` | NAS only; exact location not recorded. The working plate is the staged `shots/shot004_fire-jump/plates/FW_test_scene.mp4`, whose relation to it is unverified. |
| `FW_test_scene.mov` | HEVC, 4096x2160, 24 fps, 84 frames, `yuv420p10le` | Surveyed in `FW_test/Scene 4/` (absent here); an MP4 of the same scene is the working plate. |
| `Shot4 V031-1` (`.mov` on the NAS, `.mp4` surveyed) | H.264, 1920x1080, 24 fps, 84 frames | Delivered comp. Local copy: `shots/shot004_fire-jump/reference/shot004_fire-jump_comp-houdini-delivered-v031_1920x1080_v001.mp4`. |
| `ren_small_fire6..mov` | H.264, 1920x1080 (displays 1920x1014), 24 fps, 87 frames | Restored 2026-08-18 from `ren_small_fire6/Proxy/` to `shots/shot004_fire-jump/reference/`. EXR sequence and a 112-frame extracted alternate stay on the NAS. |
| `ren_grassfire_cpu..mov` | H.264, 1920x1080, 24 fps, 86 frames | NAS only; wanted as the Pass B timing reference. |
| `ren_steam..mov` | H.264, 1920x1080, 24 fps, 82 frames | NAS only. |
| `ren_small_waterCHAR8..mov` | H.264, 1920x1080, 24 fps, 86 frames | NAS only. |
| `ren_small_waterSplash..mov` | H.264, 1920x1080, 24 fps, 33 frames | NAS only. |

The H.264 renders are `yuv420p` with no alpha: use them as motion, timing, scale and look references, and extract mattes separately if needed.

`FW_test/` (surveyed 2026-05-18, not in this checkout) held working copies of these same files under `Scene 4/`. To restore anything, locate it through `library/manifests/external-drive_inventory_v001.md`, file it in the shot folder that uses it under a `_vNNN` name, and add a row here.

## Characters

Character material is tracked in the repo under `characters/` and listed in each folder's README. Nothing is approved into a separate `approved/` set yet for either character; Jerry's approved reference set is `characters/jerry/character-bible-v001/` (frozen bible `characters/jerry/bible_v001.md`).

Several files exist twice by design: the bible set and Tom's working references are copies of originals kept in the look references, review packs and training candidates, and each copy is part of a provenance record (original → review pack → bible). Git stores identical files once, so the copies cost local disk only.

## Screenplay

- `source/screenplay/Fire and Water, A love Story 2023 (1).pdf`: the uploaded screenplay, 8 pages.
- `source/screenplay/fire-and-water_script_extracted.md`: searchable text extracted with `pypdf`; check against the PDF before a final breakdown.
