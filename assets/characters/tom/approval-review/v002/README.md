# Tom Approval Review v002

Date: 2026-05-21

Status: corrected review pack only. Nothing in this folder is approved yet.

## What Changed From v001

Robbie reviewed `v001` and noted:

- Contact sheets are useful for context but should not be review candidates.
- Many EXR-derived PNGs appeared blank, empty, or alpha-only.
- `TB-015` and `TB-016` were useful as material references, but better single images are still desired.
- The Tom X-sheet should not be part of core body images right now.

This `v002` pack replaces the review candidates with single, flattened JPG images:

- `TB2-001` through `TB2-007`: single source stills from comp/reference movies.
- `TB2-008` through `TB2-010`: flattened big-fire material stills from EXR sources.

## Review Rule

Use the `TB2-###` IDs in `approval_manifest.tsv` and `review_gallery.md` when giving notes.

Possible decisions:

- `primary`: main Tom body/look anchor.
- `material`: fire, glow, smoke, edge, or scale support.
- `source-only`: context, scale, or plate integration only.
- `reject`: do not use for Tom.

Do not move anything into `assets/characters/tom/approved/` or assemble `assets/characters/tom/character-bible-v001/` until review decisions are recorded.
