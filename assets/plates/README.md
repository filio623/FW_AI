# Plates

Original and working plate media.

## Folders

- `source/`: untouched camera plates or supplied base renders.
- `by-shot/`: curated shot folders with source references, proxies, stills, and notes.
- `proxies/`: transcoded working files for AI tools, editorial, or quick review.

## Per-Shot Layout

Use this shape when a shot has enough material to justify a folder:

```text
assets/plates/by-shot/shot004_fire-jump/
├── source/
├── proxies/
├── stills/
├── mattes/
└── notes.md
```

Do not overwrite source plates. New versions should increment `v###`.
