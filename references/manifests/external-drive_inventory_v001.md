**Created:** 2026-05-18
**Modified:** 2026-08-18
**Version:** 1.1

# External Drive Inventory

External source (original inventory path):

`/Volumes/Rob's 4tb FAST FW`

Current mounted restore copy (NAS backup of that drive):

`/Volumes/FW_Backup/Robs-Mac-Studio.local/Volumes/Rob's 4tb FAST`

Paths below were recorded against the original volume name. On the backup, replace `/Volumes/Rob's 4tb FAST FW` with the restore-copy prefix above. Folder layout under `01 Projects/` through `zUnorganized/` matches.

## Summary

This drive appears to contain the main Fire and Water production archive. Treat it as a read-only source unless a copy operation is explicitly planned.

Approximate drive usage: `2.3T`.

Top-level production areas:

- `01 Projects/`: Resolve project exports and project files.
- `02 Footage/`: main Fire and Water assembly footage and render folders.
- `03 Audio/`: music, sound effects, temp music/fx mix.
- `04 VFX/`: VFX footage, EXR renders, shot folders, Houdini/Nuke-related material.
- `05 Exports/`: reference exports, 2D/3D/music refs, Fusion renders.
- `07 Animation/`: storyboards, 2D animation, PNG animation exports, animation reference.

## User Triage Guidance

Use this scope before doing deeper inventory:

- Ignore `01 Projects/`; it contains project files.
- Mostly ignore `02 Footage/`; it has footage plates, is very large, and generally does not contain character information.
- Ignore `03 Audio/`.
- Investigate `04 VFX/`; likely contains rough VFX for all characters, including EXRs and proxy files.
- Investigate `05 Exports/`; likely contains useful reference exports from early VFX, animation, and shot tests.
- Ignore `06 Photo/`.
- Investigate only these parts of `07 Animation/` for now:
  - `07 Animation/2D animation/`
  - `07 Animation/Story boards/`
- Skip `07 Animation/png Anim/` for now.
- Skip `07 Animation/Videos of Rob for animation ref/` for now.
- Ignore `08 BTS/`, `09 Cache Clips/`, and later miscellaneous folders for now.

Practical rule: prefer proxy movies, reference exports, 2D animation sheets, and storyboard panels before touching large EXR sequences.

File type counts from a broad scan:

- EXR: about 18,610
- WAV: about 12,795
- PNG: about 7,081
- JPG: about 1,606
- MOV: about 1,102
- BRAW: about 445
- MP4: about 232
- PDF: about 134
- PSD: about 27

## Large Areas

- `02 Footage/Fire and Water 8-20 assembly/`: about `1.7T`
- `04 VFX/`: about `112G`
- `05 Exports/`: about `106G`
- `07 Animation/`: about `73G`

## High-Value Character Sources

### Jerry PNG Animation

Likely useful for Jerry character bible, motion reference, and AI image/video conditioning:

- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_03/Jerry`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_04/PNGs/Jerry`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_04A/PNGs/Jerry`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene 12N/Jerry`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene N2/Jerry`

Observed count:

- `Scene_04A/PNGs/Jerry`: 71 files.

### Sally PNG Animation

Likely useful for Sally character bible and later generation tests:

- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_04A/PNGs/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/12A/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene 12A-2/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene 12B/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene 12D/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene 12E/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene 12H/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene 12K-2/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene 12Q-2/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene 12Q/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene K1/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene L/Sally`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/png Anim/Scene_12.1/PNGs/Scene M/Sally`

Observed count:

- `Scene_04A/PNGs/Sally`: 71 files.

### Animation Sheets

- `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Jerry01.png`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Jerry02.png`
- `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Sally.png`

These are likely high-value character bible references.

## Storyboards

Path:

- `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards`

File type counts inside storyboards:

- MOV: 328
- JPG: 128
- JPEG: 21
- PSD: 15
- XML: 2
- PNG: 2
- MP3: 1

Recommendation: do not hand-rename these. Generate contact sheets and a manifest first, then only copy/rename selected panels.

## Shot004 / Scene 4 Sources

Likely relevant to the current fire/grass workflow test:

- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_grassfire_cpu`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_steam`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_waterCHAR8`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_waterSplash`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_wetmap`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_4A`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_4A/ren_small_fire6`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_4A/ren_small_waterCHAR8`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_4A/ren_grass`

The existing `FW_test/Scene 4/` folder in this repo appears to be a small extracted subset of this larger drive material.

## Other Character/VFX Sources Seen

Possible Jerry, Tom, Sally/water, wind, rain, and interaction folders:

- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/render_dn/ren_jerry`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8H/render_dn/Tom_DN`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8G/render/Combined__tom_v001`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8G/render_dn/Drop_DN`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_6A/ren_wind_shot_6A`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_6A/ren_small_fire_shot_6A`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_6A/ren_droplet_6A`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_5G/ren_small_fire_shot_5G`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/jerry_8L_V1`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/jerry_8L_V3`
- `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/ren_big_fire_shot 8L`

## Recommended Workflow

Do not copy the whole drive or whole EXR trees into this repo.

Recommended next steps:

1. Inventory `04 VFX/` at the folder/proxy level and identify useful character reference clips.
2. Inventory `05 Exports/` for early VFX and animation reference exports.
3. Inventory `07 Animation/2D animation/` for character sheets and short animation refs.
4. Inventory `07 Animation/Story boards/` for storyboard panels and animatics.
5. Generate contact sheets from selected storyboard and 2D animation media.
6. Copy only selected stills/proxies into this repo.
7. Keep EXR sequences on the external drive until a shot needs them.
8. For EXR sequences, create low-res proxy movies or selected stills instead of copying full sequences.

## Current Bias

For Jerry casting, start from:

- `07 Animation/2D animation/X_Sheet_Jerry01.png`
- `07 Animation/2D animation/X_Sheet_Jerry02.png`
- `04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6`
- `05 Exports/` clips or stills that show Jerry clearly, after inventory.
- `07 Animation/Story boards/` panels that show Jerry's design, poses, or emotional beats.

These should provide a practical first character-bible source set without importing the entire archive.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial External Drive Inventory. |
| 1.1     | 2026-08-18 | Recorded the current NAS restore copy at `/Volumes/FW_Backup/Robs-Mac-Studio.local/Volumes/Rob's 4tb FAST`. |
