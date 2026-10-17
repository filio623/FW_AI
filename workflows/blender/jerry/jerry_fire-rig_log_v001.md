**Created:** 2026-10-17
**Modified:** 2026-10-17
**Version:** 1.2

# Jerry Blender Fire Rig Log

Date started: 2026-10-17

## Goal

Build Jerry in Blender as an animatable character with real simulated fire, matching the body references in `docs/jerry-character-bible_v001.md` (`JB-001`, `JB-002`, `JB-010`, material `JB-012`). The body is face-free; the face stays a separate layer.

This is a character-build test, not a shot 004 generation input. The scored motion driver remains `assets/elements/by-shot/shot004_fire-jump/fire/shot004_ren-small-fire6_control_832x448_81f_v001.mp4` until `docs/vfx-element-benchmark.md` records a replacement.

## Asset

- Working file: `assets/characters/jerry/source-cgi/jerry_fire-rig_v001.blend` (Blender 5.2.1).
- Test still: `assets/characters/jerry/source-cgi/jerry_fire-rig_idle-test-r09_f0064_v001.png`.
- Fluid cache: `outputs/jerry_fire-rig_v001/cache_fluid/` (relative path in the file, about 683 MB, ephemeral). Rebake before rendering in a fresh checkout.
- Build script: `scripts/blender/jerry_fire_rig_build.py` rebuilds the r09 `.blend` from an empty scene. Its constants at the top are the current settings below.

## Rebuild, Bake, Render

Run from a scratch folder under `outputs/`; noise-upres bakes write a 24 MB `waveletNoiseTile.bin` into the working directory.

```sh
R=/Users/jamesfilios/Software_Projects/FW_AI
B=/Applications/Blender.app/Contents/MacOS/Blender
cd $R/outputs/jerry_fire-rig_v001
$B -b --factory-startup --python $R/scripts/blender/jerry_fire_rig_build.py -- \
    --out $R/assets/characters/jerry/source-cgi/jerry_fire-rig_v001.blend --cache $R/outputs/jerry_fire-rig_v001/cache_fluid
$B -b $R/assets/characters/jerry/source-cgi/jerry_fire-rig_v001.blend --python $R/scripts/blender/fluid_bake.py
$B -b $R/assets/characters/jerry/source-cgi/jerry_fire-rig_v001.blend --python $R/scripts/blender/render_frames.py -- renders/idle 25-120 --samples 64
```

Building over the existing `.blend` replaces it. To keep a new look, write a new `_vNNN` file and leave the old one in place.

Verified 2026-10-17: a rebuild rendered against the r09 cache matched r09 frame 64 at 99.5 dB PSNR, so the settings are exact. A fresh bake of the same settings gave 35.7 dB PSNR and SSIM 0.975. Mantaflow bakes are not bit-identical between runs, so flame detail varies from bake to bake while the silhouette holds.

## Design

Four layers, so the outline reads as Jerry while the edges are real fire:

1. `JERRY_body`: teardrop mesh, base radius 0.25 m, about 0.61 m tall. It is not visible to any render ray. Modifier stack: Armature, then Fluid flow, then Embers particles.
2. `JERRY_rig`: bones `root`, `body`, and `tip`. `body` has a Maintain Volume constraint, so scaling Y squashes and stretches. The custom property `flare` (0–2.5, 1 is neutral) drives fuel, heat, core glow, fire emission, and ember brightness.
3. `JERRY_core`: an ellipsoid volume parented to the `body` bone. Emission falls off radially with a noisy edge, and vertical noise strands scroll upward.
4. `JERRY_fire_domain`: Mantaflow gas domain 1.0 × 1.0 × 1.7 m. Plus `JERRY_embers` particles instancing `JERRY_ember`, which sits in an excluded collection.

Animate the bones and `flare`. Every change to animation or sim settings needs a rebake.

## Current Settings (r09)

| Area | Settings |
|---|---|
| Flow | Fire, inflow, mesh source, surface 0.02, volume emission 0, vertex group `fire_emit` (0.3 at the base to 1.0 above z 0.2), initial velocity 1.0, fuel `3.0 * flare`, temperature `0.4 + 0.6 * flare` |
| Domain | res 128, noise upres 2 (strength 0.5, position scale 2), vorticity 0.05, alpha 0.4, beta 1.0, burning rate 1.0, flame smoke 0, flame vorticity 0.35, max temp 1.8, ignition 1.4, dissolve 6 (log), **clipping 0** |
| Fire shader | `flame^0.55` drives the ramp (black, deep red 0.08, orange 0.25, amber 0.5, yellow-white 0.85) and emission `14 * flare`; density 0 |
| Core shader | Falloff 0.55–1.02, edge noise 0.4, strands, emission `3.5 * flare`, volume density 0.12 |
| Embers | 400, 6 mm, lifetime 36 ±60%, gravity −0.18, Brownian 0.5, emitted by the `tip` group, emission `60 * flare` fading with age |
| Idle | Cyclic F-curves: body Y-scale breath (48 f), body lean ±4.5° (64 f), tip whip and curl (64 f), tip flicker stretch (24 f), flare pulse 0.94–1.12 (80 f) |
| Render | Cycles Metal, 64 spp, denoise, 960×540 (50%), AgX Punchy, exposure 1.0, compositor Bloom (threshold 0.35, strength 0.45, size 0.7); motion blur on for embers only, off for the domain and core |
| Camera | 65 mm at (0, −3.9, 0.33) |

Timing on an M2 Pro: bake 140–205 s per 120 frames at res 128, 262–267 s with noise upres. Render 4–5 s per frame at 960×540, 64 spp, after the first frame. The first render compiles kernels and took about 95 s.

## Run Log

| Run | Change | Result |
|---|---|---|
| r01 | First build: full-surface plus volume emission, emission 14 + 6 | Overexposed cream-white candle column about 2× body height; brown smoke patches; stair-stepped base |
| r02 | Top-weighted emission, burning rate 1.6, emission 4 + 3 | Fire starved; dim core only |
| sweep | Res 64, 64 frames: burning rate {0.6, 1.0} × fuel {1.5, 3.0} × volume emission {0, 0.25} | Any volume emission gives the column. No volume emission plus fuel 3.0 gives core plus tongue, closest to JB-001 |
| r03 | Burning rate 0.8, fuel 3.0, base emission 0.3, core strands | First readable fire; core reads as an opaque egg; muddy brown |
| r04 | Translucent core (density 0.12), ramp shifted, burning rate 1.0 | Core and fire merge into one flame body; hard horizontal cut-offs; vertical smear |
| r05 | `clipping` 0, domain motion blur off, AgX Punchy | Cut-offs gone, detail sharper; dark crust around the core |
| r06 | `flame^0.55` gamma, 65 mm lens | Crust lifted but blotchy; base clipped |
| r07 | Noise upres ×2, smoke density 0, brighter core | **Jerry silhouette**: compact rounded base, teardrop, curling tongue |
| r08 | Exposure 1.0, fire 14, core 5 | Brighter; next to JB-001 the turbulence is too busy and there is no glow halo |
| r09 | Lower vorticity, upres strength 0.5, bloom, translucent core | Current. Calmer, with a subtle halo. The body texture is still flaky against the references' smooth flame sheets |

Preview: `outputs/jerry_fire-rig_v001/renders/jerry_fire-rig_v001_idle_r09.mp4` (frames 25–120, ephemeral).

## Assessment (r09)

- Strong: reads as one living flame with Jerry's compact teardrop silhouette and tongue. Face-free. Fully rigged, with squash/stretch, lean, tip whip, and one Flare/Dim control. The sim reacts to the animated body.
- Weak: the flame material is busy and flaky, not the large smooth licking sheets of JB-001 and JB-010. The core is still slightly visible as a pale inner ellipse. Embers barely register at 960×540.
- Decision: the rig and layer design work. The material is not approved.

## Next

1. Emit a few large flame sheets instead of a thin shell: fewer emission regions, or a lower-resolution base sim with stronger upres for the licks.
2. Push the core toward JB-012: larger internal flame strands and no ellipse edge.
3. Pose test: lean, droop, flare, and dim at held poses, to check the silhouette holds under the bible's body-language set.
4. Motion test: a comet dash (`JB-004`/`JB-005`) with an adaptive domain.
5. Final renders: full resolution, EXR multilayer, transparent film, and a face-anchor empty for the separate face layer.

## Working Method

Edit and render headless against the `.blend`. The interactive Blender UI froze when Cycles rendered-viewport shading was switched on with this fire domain, and the MCP bridge stopped responding while Blender sat behind other windows. See `mcp/blender.md`.

---

## Changelog

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 2026-10-17 | Initial Jerry Blender fire rig log. |
| 1.1 | 2026-10-17 | Marked the rig as a character test, not the shot 004 motion driver. |
| 1.2 | 2026-10-17 | Added the promoted build, bake, and render scripts, rebuild commands, and the rebuild verification. |
