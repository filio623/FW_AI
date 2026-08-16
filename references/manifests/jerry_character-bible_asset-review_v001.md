**Created:** 2026-05-18
**Modified:** 2026-08-16
**Version:** 1.1

# Jerry Character Bible Asset Review

Source inventory:

- `references/manifests/jerry_external-drive_reference_inventory_v001.md`

Review artifacts: `outputs/review/jerry_asset-triage_v001/` — **expired.**

> `outputs/` is ephemeral. Every `outputs/review/jerry_asset-triage_v001/…` path below
> has since been cleared and no longer resolves. This document is kept because the
> external-drive source paths in the right-hand columns are durable and are the only
> record of where each review artifact came from.
>
> The selections that survived this review were promoted into
> `assets/characters/jerry/character-bible-v001/references/` under stable `JB-###` IDs
> and are tracked in Git. Use those for any current work; use the tables below to trace
> a promoted reference back to its original on `/Volumes/Rob's 4tb FAST FW`.
>
> To regenerate the review artifacts, remount the drive and re-run the contact-sheet
> pass from the source paths listed here.

## Purpose

Identify which external-drive sources should feed Jerry's character bible and creation workflow.

This is still a review pass only:

- No source files were copied, renamed, moved, or extracted from `/Volumes/Rob's 4tb FAST FW`.
- Contact sheets were generated into this workspace as lightweight review artifacts.
- Individual review images were also generated/copied inside `outputs/review/` for easier selection before final asset promotion.
- H.264 proxy movies remain reference-only and should not be treated as alpha-bearing production elements.

## Current Read

The assets split into two useful categories:

1. Character-design references: 2D sheets and storyboard panels that show Jerry's face, emotional range, appeal, and intended shape language.
2. VFX/material references: CGI or comp proxies that show flame motion, scale in plate, lighting, grass interaction, and render behavior.

For Jerry creation, start with the design references. Use the VFX references as constraints, not as the primary look target.

## Contact Sheets Created

| Review Sheet | Original Source | Initial Use |
| --- | --- | --- |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/proxy-video/shot4_ren-small-fire6_proxy_contact.jpg` | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6/Proxy/ren_small_fire6..mov` | Flame motion and isolated element reference. |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/proxy-video/shot4_small-fire-extracted_proxy_contact.jpg` | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/Small Fire_ extracted/Proxy/ren_small_fire6..mov` | Extracted small-fire motion and silhouette reference. |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/proxy-video/shot4_v031_full-proxy_contact.jpg` | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/Proxy/Shot4 V031-1.mov` | Plate scale, grass ignition timing, contact glow. |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/proxy-video/scene4a_2d-animation_v05_contact.jpg` | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Scene 4a_v05.mp4` | Strong Jerry/Sally character and action reference. |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/proxy-video/shot12tt_jerry5_proxy_contact.jpg` | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_12TT_anim_v05/jerry5/Proxy/jerry5..mov` | Isolated rendered Jerry/fire body reference. |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/proxy-video/shot12u_jerry5_proxy_contact.jpg` | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_12U/jerry5/Proxy/jerry5..mov` | Strong isolated rendered flame-body reference. |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/proxy-video/shot6a_blocking_jerry-tom-droplet_contact.jpg` | `/Volumes/Rob's 4tb FAST FW/04 VFX/downloads/Proxy/shot6a_playblast_blocking_wind_jerry_tom_droplet_v15.mov` | Blocking, scale, wind/fire/water interaction reference. |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/proxy-video/exports_4a-comp-v1_contact.jpg` | `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/Renders/4A_Comp_V1.mov` | Plate-integrated comp reference for Scene/Shot 4A. |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/storyboards/storyboards_jerry-selected_contact.jpg` | `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards/13-blue-colored.jpg`, `14-revised-crf.jpg`, `26-looks at her in fear.jpg`, `37a-branch-falls.jpg` | Selected storyboard panels for Jerry scale, expression, Sally relationship, and fire/branch action. |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/storyboards/storyboards_jerry-priority-crops_contact.jpg` | 16 Jerry-focused storyboard crops from `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards/` | Best current storyboard sheet for Jerry character creation: close expressions first, then cropped shared/action panels where Jerry remains the visual subject. |
| `outputs/review/jerry_asset-triage_v001/contact-sheets/storyboards/storyboards_jerry-secondary-crops_contact.jpg` | 16 secondary Jerry/storyboard crops from `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards/` | Lower-priority support sheet for Jerry/Sally interaction, rain/river beats, and action/fire-context panels. |
| `outputs/review/jerry_asset-triage_v001/indexes/storyboard-crops_index.tsv` | Crop index for the two Jerry storyboard crop sheets | Maps each crop tile to its source storyboard panel and priority note. |

## Single-Image Review Set

Use this folder when reviewing individual Jerry references for the real character bible:

- `outputs/review/jerry_asset-triage_v001/single-images/`

Contents:

| Folder | Count | Use |
| --- | ---: | --- |
| `single-images/storyboard-priority/` | 16 | Best Jerry-first storyboard crops for expression, silhouette, and character prompt work. |
| `single-images/storyboard-secondary/` | 16 | Lower-priority shared/action storyboard crops for extra context. |
| `single-images/exr-black-stills/` | 18 | Preferred EXR-derived PNG previews on black, resampled after empty/weak stills were flagged. Use for flame body, material, silhouette, and render behavior. |
| `single-images/composite-footage-stills/` | 17 | Full-frame PNG stills from rough composite/reference footage for plate scale, position, glow, and context. |

Indexes:

- `outputs/review/jerry_asset-triage_v001/single-images/README.md`
- `outputs/review/jerry_asset-triage_v001/indexes/exr-black-stills_index.tsv`
- `outputs/review/jerry_asset-triage_v001/indexes/composite-footage-stills_index.tsv`
- `outputs/review/jerry_asset-triage_v001/indexes/storyboard-crops_index.tsv`

The EXR-derived PNGs were sampled from selected sequences only; no full EXR sequence was converted. After review, `shot_8C` and `shot_8L` EXR samples were moved out of the preferred usable set because they read mostly as dark outline/matte-like frames instead of useful Jerry/fire reference.

## Candidate Ranking

### A. Promote For Jerry Character Bible Review

Use these first when defining Jerry's face, personality, silhouette, and approved prompt language.

| Priority | Source | Why It Matters |
| --- | --- | --- |
| A | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Jerry01.png` | Best first character sheet for Jerry's intended design and poses. |
| A | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/X_Sheet_Jerry02.png` | Companion character sheet for pose/action variation. |
| A | `outputs/review/jerry_asset-triage_v001/single-images/storyboard-priority/` | Individual Jerry-first storyboard images ready for character-bible review and reference selection. |
| A | `outputs/review/jerry_asset-triage_v001/contact-sheets/storyboards/storyboards_jerry-priority-crops_contact.jpg` | Best storyboard contact sheet for Jerry-only/dominant character creation reference. It crops Jerry out of shared panels where useful. |
| A | `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards/13-blue-colored.jpg` | Shows small, appealing Jerry near Sally; good relationship and scale cue. |
| A | `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards/14-revised-crf.jpg` | Shows Jerry in a flying/flame-trail action pose with simple face. |
| A | `/Volumes/Rob's 4tb FAST FW/07 Animation/Story boards/26-looks at her in fear.jpg` | Strong emotional expression panel with Jerry and Sally. |
| A | `/Volumes/Rob's 4tb FAST FW/07 Animation/2D animation/Scene 4a_v05.mp4` | Contact sheet confirms readable Jerry face and action against Sally/plate context. |

### B. Use As Jerry Material / Motion Reference

Use these to constrain AI generation and compositing, but do not let them override the more appealing 2D character design.

| Priority | Source | Why It Matters |
| --- | --- | --- |
| B | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_12U/jerry5/Proxy/jerry5..mov` | Clean isolated flame-body reference with strong internal fire texture and silhouette changes. |
| B | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/shot_12TT_anim_v05/jerry5/Proxy/jerry5..mov` | Clean isolated Jerry/fire render; useful for body/material continuity. |
| B | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/ren_small_fire6/Proxy/ren_small_fire6..mov` | Shot004-specific small-fire motion and isolated silhouette. |
| B | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/Small Fire_ extracted/Proxy/ren_small_fire6..mov` | Alternate extracted small-fire proxy; useful for additional pose/motion frames. |
| B | `outputs/review/jerry_asset-triage_v001/single-images/exr-black-stills/` | Individual black-background PNG stills sampled from selected Jerry/fire EXR sequences; best current EXR still set for flame render/material reference. |

### C. Use As Plate / Interaction Reference

These should inform integration and timing, not Jerry's core design.

| Priority | Source | Why It Matters |
| --- | --- | --- |
| C | `/Volumes/Rob's 4tb FAST FW/04 VFX/VFX Footage/Shot_4/shot_4v031_delivery/Proxy/Shot4 V031-1.mov` | Good for shot004 scale, contact position, grass ignition, and glow behavior. |
| C | `/Volumes/Rob's 4tb FAST FW/05 Exports/Fusion Renders/Renders/4A_Comp_V1.mov` | Good for plate-integrated Scene/Shot 4A reference. Less useful for face/design. |
| C | `/Volumes/Rob's 4tb FAST FW/04 VFX/downloads/Proxy/shot6a_playblast_blocking_wind_jerry_tom_droplet_v15.mov` | Useful for broad blocking and multi-character dynamics, but Jerry is small/distant in the contact sheet. |
| C | `outputs/review/jerry_asset-triage_v001/single-images/composite-footage-stills/` | Individual stills from Shot 4 and 4A composite/reference footage; useful for plate context and scale, not core design. |

## Prompt/Design Takeaways

Early character-bible language should emphasize:

- Small sentient flame, not generic realistic fire.
- Simple readable face with large eyes and expressive brow/mouth.
- Warm orange-yellow body with a brighter inner core.
- Soft, appealing, rounded flame silhouette.
- Flame tail/flicker can stretch during movement.
- Jerry should remain small and vulnerable next to Sally and the environment.

Avoid using the isolated VFX renders alone as Jerry's design source. They are useful for fire material, but the face and emotional appeal come mainly from the 2D/storyboard material.

## Storyboard Crop Pass

The latest storyboard review confirms there is substantially more Jerry material than the initial 4-panel storyboard contact sheet captured.

Use priority order:

1. `outputs/review/jerry_asset-triage_v001/contact-sheets/storyboards/storyboards_jerry-priority-crops_contact.jpg`
2. `outputs/review/jerry_asset-triage_v001/single-images/storyboard-priority/`
3. `outputs/review/jerry_asset-triage_v001/contact-sheets/storyboards/storyboards_jerry-secondary-crops_contact.jpg`
4. `outputs/review/jerry_asset-triage_v001/contact-sheets/storyboards/overview/`

The priority crop sheet intentionally favors Jerry-only or Jerry-dominant panels. Shared Jerry/Sally panels are included only when the crop keeps Jerry readable enough for expression, silhouette, or character prompt work.

## Recommended Next Review Step

Review and promote selected images only from:

1. `X_Sheet_Jerry01.png`
2. `X_Sheet_Jerry02.png`
3. `outputs/review/jerry_asset-triage_v001/single-images/storyboard-priority/`
4. `outputs/review/jerry_asset-triage_v001/single-images/exr-black-stills/`
5. `outputs/review/jerry_asset-triage_v001/single-images/composite-footage-stills/`
6. `Scene 4a_v05.mp4`
7. `shot_12U/jerry5/Proxy/jerry5..mov`
8. `Shot_4/shot_4v031_delivery/ren_small_fire6/Proxy/ren_small_fire6..mov`

Those stills should become the first reviewed candidates for:

- `assets/characters/jerry/source-cgi/`
- `assets/characters/jerry/expressions/`
- `assets/characters/jerry/actions/`
- `assets/storyboards/jerry/`

Do that only after explicitly deciding to copy/curate selected material into `assets/`.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-05-18 | Initial Jerry Character Bible Asset Review. |
| 1.1     | 2026-08-16 | Recorded that the `outputs/review/` artifacts expired and pointed current work at the promoted `character-bible-v001/references/` set. |
