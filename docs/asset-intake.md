**Created:** 2026-05-18
**Updated:** 2026-11-04

# Asset Intake

Use this checklist when uploading film assets into the workspace.

## Intake Checklist

1. Put raw uploads in `inbox/`.
2. Identify the asset type: script, storyboard, plate, element, character reference, external reference, audio, editorial, or review export.
3. Identify shot or sequence when applicable.
4. Preserve original filenames for raw source media when useful.
5. Create a curated copy with project naming when the file becomes active.
6. File it where it belongs: the shot folder if one shot uses it (`shots/<shot>/plates/`, `reference/` or a pass folder), `characters/<name>/` or `source/` if it is project-wide; add a line to that folder's README.
7. Update `docs/asset-inventory.md` for source media and anything restored from the NAS.

## Naming Pattern

Shot-specific:

`shot###_short-description_asset-type_v###.ext`

Reusable:

`subject_purpose_descriptor_v###.ext`

Examples:

- `shot004_fire-jump_plate_main_v001.mov`
- `shot004_fire-jump_storyboard_panel-03_v001.png`
- `jerry_fire_approved-look_front_v001.png`
- `grass-ignition_contact-pass_test_v002.mov`
- `fire-and-water_script_v001.pdf`

## Versioning

- Use `v001`, `v002`, `v003` for creative or technical revisions.
- Use `original` in the name only for preserved source files.
- Avoid overwriting source, approved, or delivered files.

## Shot Folder Linkage

When a file belongs to a shot, the shot's README lists where it is:

- Plate path.
- Storyboard path.
- Required character assets.
- VFX element paths.
- Latest composite or review export.
