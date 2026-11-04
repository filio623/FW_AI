**Created:** 2026-11-04
**Updated:** 2026-11-04

# Shot004 Comp Log

Append-only log of comp versions and comp checks for shot 004, one entry per saved comp or check, newest at the bottom. Comp files live in `assets/elements/by-shot/shot004_fire-jump/comps/`; renders and review sheets in `outputs/shot004/comp/`. How the comps are built: `plan.md`, Comp. The first three entries were written on 2026-11-04 from the plan and the Pass B log.

## s004-c-001 — 2026-11-02 — Blender Comp v001 (run 8 over the plate)

- **Change:** baseline. Plate → ground glow → Pass B slot (empty) → Jerry (run 8 `s004-a` baseline, core over + Screen glow + bloom) → ridge holdout → neutral grade.
- **Tool:** Blender 5.2.1 compositor, built by `scripts/blender/shot004_comp_build.py`; 4096×2160, frames 1–81.
- **Inputs:** `plates/FW_test_scene.mp4`; run 8 clip `benchmark/shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo_seed1218565630_v001.mp4`.
- **Kept:** `comps/shot004_fire-jump_comp-blender_run8_v001.blend`; preview `outputs/shot004/comp/blender/shot004_fire-jump_comp-blender_run8_preview_v001.mp4`.
- **Result:** placement matches the ffmpeg preview; Jerry reads hot and opaque; the ground glow follows him without flicker. Once opaque, run 8's darker interior patches read as two eyes and a mouth on about frames 45–70; a thin blue-violet line along Jerry's bottom edge after landing.
- **Verdict:** James: Blender is the comp tool for now (2026-11-02).
- **Next:** NAG face negatives (Pass A run 9), the smaller guide.

## s004-c-002 — 2026-11-02 — Fusion Comp v001 (same comp in Resolve)

- **Change:** the same layers built in DaVinci Resolve Studio's Fusion page, for a tool comparison (James).
- **Tool:** `scripts/resolve/shot004_comp_fusion.py` run with ResolvePython; Resolve project `FW_AI_shot004_comp`, timeline `shot004_comp_v001`.
- **Kept:** `comps/shot004_fire-jump_comp-fusion_run8_v001.setting` and `.drp`; renders archived to `outputs/_archive/2026-11-04/shot004/comp/fusion/`; side by side `outputs/shot004/comp/blender-vs-fusion_v001.mp4`.
- **Result:** placement matches; ground glow within about 10% of Blender's; Jerry slightly more yellow; renders about 8 s per frame against Blender's 2 s.
- **Verdict:** James: stay in Blender; Fusion kept for reference; Resolve stays the likely place for a final grade.

## s004-c-003 — 2026-11-04 — Blender comp with Pass B from Seedance S3

- **Change:** `s004-c-001` with the Pass B slot filled by the grass fire from Seedance S3 (`s004-b-020`).
- **Tool:** S3 turned into a layer by `scripts/build_shot004_grassfire_layer.py` (registered onto the plate, median error 1.3 px; fire light kept as a gain on the plate; fire taken by a change matte inside a zone; retimed `--map 20:25,72:54,96:80`, about 1.8× to frame 54), added by `scripts/blender/shot004_comp_add_passb.py`.
- **Kept:** comp `comps/shot004_fire-jump_comp-blender_run8-passb-s3_v002.blend`; layer `scorch-contact/layers/shot004_fire-jump_grassfire-layer-s3_v001/`; render `outputs/shot004/comp/blender/passb_s3/` (preview `shot004_fire-jump_comp-blender_run8-passb-s3_preview_v001.mp4`, sheet `passb_s3_preview_sheet.png`).
- **Result:** works as a layer: the fire starts under Jerry on his landing (frame 26), spreads through the clump by about frame 54 and burns to the end; the ground warms and keeps the plate's texture; no mask outline, no dark ring. Soft (480p scaled 4.4×); one early flame shoots up fast behind Jerry (frames 30–36) from the 1.8× retime.
- **Verdict:** James (2026-11-04): the fire is in the world; Jerry's texture does not match the fire (smooth CG orb against photographic fire); colour can be adjusted.
- **Next:** comp Kling K1 (`s004-b-021`) the same way; Jerry comp-setting variants; regenerate Jerry with the smaller guide.
