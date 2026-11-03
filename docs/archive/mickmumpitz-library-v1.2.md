**Created:** 2026-10-19
**Modified:** 2026-11-01
**Version:** 1.2
**Archived:** 2026-11-03

# [ARCHIVED] Mickmumpitz Workflow Library

A local copy of the Mickmumpitz Patreon workflows and guides, organized per YouTube video. The files live off-repo. This document and `references/manifests/mickmumpitz/` are the durable record of what exists and where.

- YouTube: <https://www.youtube.com/@mickmumpitz> (50 videos as of 2026-10-19)
- Patreon: <https://mickmumpitz.ai/> (James is a member; 131 posts as of 2026-10-19)

## Location

`~/Desktop/VFX workflows/mickmumpitz/`, about 7.0 GB on 2026-10-19 after pruning.

- `INDEX.md`: generated catalog. Each video lists its YouTube link, every matching Patreon post, and every attachment with its library path. Files that were not downloaded are marked.
- `<YYYY-MM-DD>_<video-slug>__<youtube-id>/{free,advanced}/`: one folder per video. Free and advanced attachments are kept apart.
- `_patreon-only/<YYYY-MM-DD>_<post-slug>__p<post-id>/`: posts with attachments that do not belong to a video (Consistent Character Creator betas, film-school PDFs, the RTX node guide, the LTX lip-sync workflow, and similar).
- `_meta/`: the Patreon post manifest and YouTube video list the index was built from, plus `removed_<date>.txt` listing pruned folders. Repo copies of all three are in `references/manifests/mickmumpitz/`.

The repo working copies in `workflows/comfyui/mickmumpitz/` are unchanged. The library is reference material; anything adopted for a shot is copied into `workflows/` and logged there.

## How Posts Map To Videos

Most videos have a free Patreon post that embeds the YouTube link and a locked `[ADVANCED]` or `[EXAMPLE FILES]` post published the same day. `scripts/mickmumpitz-library.py` links a post to a video in this order:

1. By the YouTube link embedded in the post.
2. By the explicit `POST_VIDEO_OVERRIDES` in the script, for 2023–24 posts that name the video without embedding it and for companions posted a day before or after.
3. By sharing a publish date with exactly one video post.

A post that matches none of these goes to `_patreon-only/`. A file attached to several posts is stored once, under the first post that carries it, with a preference for the free post. `INDEX.md` lists it under every post.

10 YouTube videos have no Patreon post. Most are from 2022–23, before the Patreon started. They are listed at the end of `INDEX.md`. The "THIS is the FUTURE OF VFX" posts from 2024-01-17 have no matching video title and stay under `_patreon-only/`.

## What Was Downloaded

On 2026-10-19, 203 files were downloaded through Chrome: every attachment under 50 MB, plus five example packs James chose. The seven AI-VFX files already on the Desktop were moved into the library. They are the 1.0, 1.1 and 1.3 ADV workflows, the 1.0 simple, preprocess and start-image workflows, and the example-files zip with its extracted folder.

| Video | Example pack | Size |
|-------|--------------|------|
| 2026-10-07 AI Performance Capture 2.2 | `PERFCAP_2-2_ADV_EXAMPLE_FILES.zip` | 3.5 GB |
| 2026-08-12 AI Rendering with MiniMax | `260812_AI-RENDERING_MINIMAX_PATREON_FILES.7z` | 0.6 GB |
| 2026-06-19 FREE 3D Movie Pipeline | `AI-RENDERING-EXAMPLE FILES.7z` | 1.0 GB |
| 2026-02-25 AI Renderer 2.0 | `260225_AI-RENDERING_PATREON.zip`, `Example_Blender_Files.zip` | 0.3 GB |
| 2026-03-30 AI VFX pipeline | `MICKMUMPITZ_AIVFX_EXAMPLE-FILES.zip` (already on hand) | 1.0 GB |

Seventeen large packs were left on Patreon, about 23 GB in total. The biggest are the World Generation splat and training datasets (16.4 GB) and the Consistent Character packs (2.9 GB). `INDEX.md` marks each one "not downloaded". To fetch one later, download it from its post and rerun the script.

The library holds a few helper scripts (`.bat`, `.py`, `.js`) from the posts. They have not been run. Review any of them before running it.

## Pruned As Obsolete

On 2026-10-19, 30 folders (287 MB) went to the macOS Trash. Each one was built on a model generation that a later workflow in the library replaces. They are listed in `_meta/removed_2026-10-19.txt`, and `INDEX.md` marks their files "removed as obsolete". The script does not file anything back into them. The triage was based on the models and node packs each graph loads; none was run.

- 2023 workflow sheets and AI Film School PDFs, from the pre-ComfyUI pipeline.
- SD 1.5 and AnimateDiff vid2vid from 2024: Future of VFX, Any Style, and AI Compositing V01. AI-VFX 1.3 replaces them.
- The Wav2Lip lip-sync cleanup. The LTX 2.3 lip-sync workflow (2026-04) replaces it.
- The SDXL and LCM AI renderers, v3 to v7. AI Renderer 2.0 and MiniMax rendering replace them.
- Every Consistent Character Creator generation before 4.0: the 2024 character sheets, CCC v01, PuLID, 3.0, 3.2, 3.5, and the 2025-10 Hyperrealistic Characters set. CCC 4.0 and Krea 2 (2026-07) replace them.
- SDXL, IPAdapter, and ToonCrafter image pipelines: Anime, Storyboard, Shoot Epic Movies, Multiple Characters, Basic Flux ControlNet, and the Shot-by-Shot Scene Builder. The 2026 LTX Movie Builder replaces them.
- 2024 3D set and set-extension projection and Hunyuan3D texturing. These are not relevant to fire and water elements.

To restore a folder, use Finder's Put Back while it is still in the Trash, or download it again from its Patreon post. Then delete its line from the removed list and rerun the script.

## Refreshing

1. Capture a new post manifest from the Patreon post API while logged in, in the same JSON shape as `_meta/mickmumpitz_patreon_manifest_<date>.json`, and refresh the YouTube TSV.
2. Download the new attachments into `~/Downloads/`.
3. Dry run, then apply:

```bash
python3 scripts/mickmumpitz-library.py --manifest "$HOME/Desktop/VFX workflows/mickmumpitz/_meta/mickmumpitz_patreon_manifest_2026-10-19.json" --videos "$HOME/Desktop/VFX workflows/mickmumpitz/_meta/youtube_videos_2026-10-19.tsv" --library "$HOME/Desktop/VFX workflows/mickmumpitz" --source "$HOME/Downloads"
```

Add `--apply` to move the files and rewrite `INDEX.md`. Files are matched by exact name and byte size, so a partial or renamed download is never filed. Copy the new manifest and TSV into `references/manifests/mickmumpitz/`.

## Candidates For FW_AI

These are leads from the workflow file names and the models they load; their contents have not been reviewed yet.

- **AI VFX pipeline 1.0–1.3** (`_n0ir5V5tX4`): the current shot004 Pass A workflow. See `docs/vfx-element-benchmark.md`.
- **Creature on a Path** (`OhKoh0CsVFo`, July 2025): Wan VACE drives a creature from a reference image along a trajectory. The motion guide is red squares on the path, optionally with a DWPose skeleton, plus an animated inpainting mask. It runs on the older Kijai WanVideoWrapper stack (Wan 2.1 T2V 14B fp8, a separate VACE module, the CausVid LoRA, 8 steps), none of which is on the RunPod volume. It comes with an After Effects trajectory exporter (`.js`), a Blender bone tracer (`.py`) and an HTML coordinate converter. Reviewed 2026-11-01. It is not a replacement for the shot 004 Mick 1.3 SkyReels setup, whose gray-blob guide carries shape and size as well as path. Ideas James wants to explore later:
  - Drawing the path by hand (spline in ComfyUI or an online spline tool) for shots with no CG motion source.
  - Importing motion from Blender (bone tracer) or After Effects to build a gray-blob guide for any blocked-out shot.
  - Compositing in Blender, or building AI animation effects that are composited in Blender.
  - Inpainting, as in its animated-mask and inpainted-start-frame options.
- **AI Performance Capture 2.2** (`2MzCkYrvDaI`): actor-to-creature transfer with mattes for Nuke and After Effects. Possibly useful for Jerry and Tom body performance. Facial features stay a separate layer under the character-generation rules.
- **Actor Compositor 2.0 and Mask & Track** (`VaSZGkGff7U`): Wan VACE plate integration.
- **Wan 2.1 Clean Plate Creator** (`pd76XGHCavY`): plate prep. The start-frame and Flux inpainting graphs in the same folder are older and lower priority.
- **Time2Move** (`pUb58eAZ3pc`): stick-puppet motion control for video generation.
- **RTX upscaling** (`NpNagmQI4yg` and `_patreon-only/…installing-rtx-nodes…`): finishing.
- **AI Renderer 2.0, the 3D Movie Pipeline, and MiniMax rendering** (`0WkixvqnPXw`, `7J7hi-Hxpac`, `Q2oVBVQNQ_U`): rendering rough Blender or Houdini layouts into finished frames.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-10-19 | Initial Mickmumpitz Workflow Library. |
| 1.1     | 2026-10-19 | Recorded the 30 folders pruned as obsolete; added Creature on a Path, Time2Move and Mask & Track to the candidates and dropped AI Compositing V01. |
| 1.2     | 2026-11-01 | Reviewed Creature on a Path and recorded James's ideas for later: hand-drawn paths, Blender and After Effects motion import, Blender compositing, and inpainting. |
