# VFX Elements

Separable render passes and generated assets used in compositing.

## Folders

- `by-shot/`: shot-specific element collections when a shot has multiple related passes.
- `fire/`: fire character and fire-only effects.
- `water/`: water character and water-only effects.
- `smoke-steam/`: smoke, steam, mist, vapor, and heat haze sources.
- `splashes/`: splash, droplets, spray, ripples, and wetness elements.
- `scorch-contact/`: scorch, grass ignition, contact light, shadows, and interaction passes.
- `mattes/`: alpha, holdout, roto, occlusion, depth, and utility mattes.

Prefer layered, compositable elements over baked full-frame generations.

## Per-Shot Layout

```text
assets/elements/by-shot/shot004_fire-jump/
├── fire/
├── water/
├── smoke-steam/
├── splashes/
├── scorch-contact/
├── mattes/
└── notes.md
```
