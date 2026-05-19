# Asset Intake

Use this checklist when uploading film assets into the workspace.

## Intake Checklist

1. Put raw uploads in `assets/inbox/`.
2. Identify the asset type: script, storyboard, plate, element, character reference, external reference, audio, editorial, or review export.
3. Identify shot or sequence when applicable.
4. Preserve original filenames for raw source media when useful.
5. Create a curated copy with project naming when the file becomes active.
6. Update `docs/asset-inventory.md`.
7. Add or update shot notes in `shots/` for shot-specific assets.

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

When a file belongs to a shot, link it from the shot note:

- Plate path.
- Storyboard path.
- Required character assets.
- VFX element paths.
- Latest composite or review export.
