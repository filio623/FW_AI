# Jerry External Drive Reference Inventory

Date: 2026-05-18

Source drive:

`/Volumes/Rob's 4tb FAST FW`

## Scope

This is a narrow first-pass inventory for Jerry character casting and fire-character reference.

Rules followed:

- Treated the external drive as read-only.
- Did not copy, rename, move, or extract source media.
- Ignored `01 Projects/`, `03 Audio/`, `06 Photo/`, `08 BTS/`, and later folders.
- Mostly ignored `02 Footage/`.
- Skipped `07 Animation/png Anim/` and `07 Animation/Videos of Rob for animation ref/`.
- Focused on `04 VFX/`, `05 Exports/`, `07 Animation/2D animation/`, and `07 Animation/Story boards/`.

Scan methods:

- Directory and filename inventory with `find`.
- Video metadata with `ffprobe`.
- Image dimensions with `sips`.
- Limited visual spot checks of still images in place.

## Highest-Value Jerry Sources

### 2D Character Sheets

These are the best starting references for Jerry's designed shape language before looking at rendered VFX.

| Priority | Path | Type | Notes |
| --- | --- | --- | --- |
| High | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Jerry01.png` | PNG, 3300x2550 | Jerry character/action sheet. High-value casting and pose reference. |
| High | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Jerry02.png` | PNG, 3300x2550 | Jerry character/action sheet. High-value casting and pose reference. |
| Medium | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Screen Shot 2024-05-20 at 11.04.32 AM.png` | PNG, 1504x686 | Candidate still in same folder. Needs visual review before promotion. |

### Storyboard Panels Spot-Checked

These panels show Jerry clearly enough to be useful for expression, scale, and relationship reference.

| Priority | Path | Type | Notes |
| --- | --- | --- | --- |
| High | `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards/13-blue-colored.jpg` | JPG | Jerry appears small and smiling near campfire with Sally/water character on leaf. Good scale and relationship cue. |
| High | `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards/14-revised-crf.jpg` | JPG | Jerry in motion/flying with simple face and trailing flame shape. Good silhouette and action reference. |
| High | `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards/26-looks at her in fear.jpg` | JPG | Jerry appears close enough for facial expression; Sally also visible. Good emotional reference. |
| Medium | `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards/37a-branch-falls.jpg` | JPG | Fire/branch action reference, but not a clear Jerry character reference from the spot check. |

The full storyboard folder contains many additional panels and animatic movies. Next pass should generate a contact sheet or visually review top-level JPG/JPEG panels before selecting more.

## 2D Animation Movies

These are useful for motion, pose timing, and broad character behavior. They are not as direct as the still sheets for casting, but they can guide Jerry action states.

| Priority | Path | Metadata | Notes |
| --- | --- | --- | --- |
| High | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Scene 4a_v05.mp4` | H.264, 4096x2160, 24fps, 71 frames, 2.96s | Scene 4A animation. Relevant to the current shot004/4A fire-jump area. |
| High | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Proxy/Scene 4a_v03.mov` | H.264, 1920x1080, 24fps, 70 frames, 2.92s | Lighter proxy for Scene 4A review. |
| Medium | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Scene 05_v05.mp4` | H.264, 4096x2160, 24fps, 346 frames, 14.42s | Candidate broader Jerry/Sally scene reference; needs scrub. |
| Medium | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Scene 6_v04.mp4` | H.264, 4096x2160, 24fps, 78 frames, 3.25s | Candidate for Jerry/wind/Tom interaction timing; needs scrub. |
| Medium | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Scene 08_Ending_v02.mp4` | H.264, 4096x2160, 24fps, 417 frames, 17.38s | Candidate later-sequence reference; needs scrub. |
| Medium | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Scene_12N_v01.mp4` | H.264, 4096x2160, 24fps, 203 frames, 8.46s | Candidate late-story Jerry/fire reference; needs scrub. |
| Low | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Scene12_V05 (1).mp4` | H.264, 4096x2160, 24fps, 1862 frames, 77.58s | Long sequence. Use only after narrower clips are exhausted. |

## VFX Proxy Movies And Element Renders

### Shot 4 / Shot 4A

These are the strongest VFX sources for the immediate Jerry fire-jump workflow. The proxy movies are H.264/yuv420p and should be treated as visual, motion, timing, and scale reference, not alpha-bearing source.

| Priority | Path | Metadata | Notes |
| --- | --- | --- | --- |
| High | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6/Proxy/ren_small_fire6..mov` | H.264, 1920x1080, 24fps, 87 frames, 3.63s | Small fire/Jerry element proxy for shot 4. Primary VFX reference. |
| High | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/Small Fire_ extracted/Proxy/ren_small_fire6..mov` | H.264, 1920x1080, 24fps, 112 frames, 4.67s | Extracted small-fire proxy. Useful if it isolates Jerry better than the main proxy. |
| High | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/Proxy/Shot4 V031-1.mov` | H.264, 1920x1080, 24fps, 84 frames, 3.50s | Full shot 4 review/proxy. Useful for Jerry scale in plate and grass ignition timing. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_grassfire_cpu/Proxy/ren_grassfire_cpu..mov` | H.264, 1920x1080, 24fps, 86 frames, 3.58s | Interaction pass reference, not Jerry casting, but useful for fire/grass behavior. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/3D shotblast/Proxy/Shot4_V031-1.mov` | H.264, 1920x1080, 24fps, 84 frames, 3.50s | Duplicate or parallel shotblast proxy for shot 4 review. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/3D shotblast/Proxy/Shot4av02-1.mov` | H.264, 1920x1080, 24fps, 70 frames, 2.92s | Shot 4A proxy. Useful for adjacent action/timing. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/3D shotblast/Proxy/Shot_4a_animv07.mov` | H.264, 1920x1080, 24fps, 71 frames, 2.96s | Shot 4A animation proxy. Useful for motion blocking. |

Related EXR sequences to leave on the drive until needed:

| Path | Count | Notes |
| --- | ---: | --- |
| `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6/` | 112 EXR | Main shot 4 small-fire render sequence. |
| `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/Small Fire_ extracted/` | 112 EXR | Extracted small-fire sequence. |
| `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_4A/ren_small_fire6/` | 72 EXR | Shot 4A small-fire render sequence; no proxy found in that folder during this pass. |

### Named Jerry / Small-Fire VFX Folders

These are useful because the folder names explicitly identify Jerry or small fire. Several are EXR-only at the scanned depth, so they should not be copied wholesale.

| Priority | Path | Type / Count | Notes |
| --- | --- | --- | --- |
| High | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_12TT_anim_v05/jerry5/Proxy/jerry5..mov` | H.264, 1920x1080, 24fps, 73 frames, 3.04s | Named Jerry proxy. Strong candidate for clear VFX character reference. |
| High | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_12U/jerry5/Proxy/jerry5..mov` | H.264, 1920x1080, 24fps, 150 frames, 6.25s | Named Jerry proxy. Longer and likely useful for motion reference. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_12TT_anim_v05/jerry5/` | 73 EXR | Underlying Jerry render sequence. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_12U/jerry5/` | 150 EXR | Underlying Jerry render sequence. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/jerry_8L_V1/` | 68 EXR | Named Jerry render folder; no proxy found in first pass. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/jerry_8L_V3/` | 68 EXR | Named Jerry render folder; no proxy found in first pass. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_8C/jerry_8C/` | 38 EXR | Named Jerry render folder; no proxy found in first pass. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_5j/jerry_5j/` | 70 EXR | Named Jerry render folder; no proxy found in first pass. |

### Broader Rough VFX Clips

These are useful for context, blocking, and character interaction, but are less direct than the named Jerry proxies.

| Priority | Path | Metadata | Notes |
| --- | --- | --- | --- |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/3D shotblast/shot6a_playblast_blocking_wind_jerry_tom_droplet_v15.mp4` | H.264, 1920x1080, 24fps, 133 frames, 5.54s | Explicitly names Jerry, Tom, wind, and droplet. Strong blocking/reference candidate. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/downloads/Proxy/shot6a_playblast_blocking_wind_jerry_tom_droplet_v15.mov` | H.264, 1920x1080, 24fps, 133 frames, 5.54s | Proxy version of same shot6A blocking clip. |
| Medium | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_8L/Shot_8L/shot_8L_anim_v05.mov` | ProRes, 1920x1012, 24fps, 67 frames, 2.79s | Shot-level animation reference near named Jerry 8L folders. Needs visual scrub. |
| Low | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_2C/shot_2C.mov` | ProRes, 1920x1012, 24fps, 35 frames, 1.46s | Adjacent named `jerry2` folder exists under shot_2C; needs visual scrub before promotion. |

## 05 Exports Candidates

`05 Exports` is mostly useful for finished or semi-finished reference exports, not isolated Jerry casting. It is still worth keeping these as review candidates because they may show Jerry in the plate with final-ish scale and color.

| Priority | Path | Metadata | Notes |
| --- | --- | --- | --- |
| High | `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/Renders/4A_Comp_V1.mov` | ProRes, 4096x2160, 24fps, 71 frames, 2.96s | High-resolution comp export for 4A. Best 05 export candidate for the current shot family. |
| Medium | `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/4/4 Full Comp_V1/` | 83 EXR | Shot 4 full-comp EXR sequence. Do not copy wholesale; make selected review stills only after approval. |
| Medium | `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/Renders/5G_Comp_V1.mov` | ProRes, 4096x2160, 24fps, 36 frames, 1.50s | Candidate if scene 5G shows Jerry clearly. Needs scrub. |
| Medium | `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/Renders/5J_Comp_V1.mov` | ProRes, 4096x2160, 24fps, 53 frames, 2.21s | Candidate if scene 5J shows Jerry clearly. Needs scrub. |
| Medium | `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/Renders/6_Comp_V1.mov` | ProRes, 4096x2160, 24fps, 78 frames, 3.25s | Candidate if scene 6 shows Jerry/wind/Tom clearly. Needs scrub. |
| Medium | `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/Renders/6A_Comp_V1.mov` | ProRes, 4096x2160, 24fps, 123 frames, 5.13s | Candidate if scene 6A shows Jerry/wind/Tom clearly. Needs scrub. |

Other export folders worth searching only after these:

- `/Volumes/Rob's 4tb FAST FW/05 Exports/For 2D reference/`
- `/Volumes/Rob's 4tb FAST FW/05 Exports/Full Export REF/`
- `/Volumes/Rob's 4tb FAST FW/05 Exports/For 3d reference/`

## Recommended First Selection Queue

Use this order for the next triage pass:

1. `X_Sheet_Jerry01.png` and `X_Sheet_Jerry02.png` for design anchors.
2. Storyboard panels `13-blue-colored.jpg`, `14-revised-crf.jpg`, and `26-looks at her in fear.jpg` for emotion, scale, and relationship cues.
3. Shot 4 small-fire proxies: `ren_small_fire6..mov`, `Small Fire_ extracted/Proxy/ren_small_fire6..mov`, and `Shot4 V031-1.mov`.
4. Named Jerry proxies: `shot_12TT_anim_v05/jerry5/Proxy/jerry5..mov` and `shot_12U/jerry5/Proxy/jerry5..mov`.
5. Scene 4A 2D animation: `Scene 4a_v05.mp4` and `Proxy/Scene 4a_v03.mov`.
6. Shot6A blocking clip: `shot6a_playblast_blocking_wind_jerry_tom_droplet_v15`.
7. 05 export `4A_Comp_V1.mov`, then only scrub the other Fusion comp movies if more plate-integrated reference is needed.

## Notes For Future Handling

- Do not import full EXR trees yet.
- For the next pass, generate review contact sheets or selected stills only from the high-priority clips after explicit approval.
- Store curated copies later under `assets/characters/jerry/source-cgi/`, `assets/characters/jerry/actions/`, `assets/characters/jerry/expressions/`, or `assets/storyboards/jerry/` according to the Jerry development plan.
- Treat H.264 proxy movies as reference only. They do not preserve alpha.
