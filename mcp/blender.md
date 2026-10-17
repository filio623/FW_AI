**Created:** 2026-10-17
**Modified:** 2026-10-17
**Version:** 1.2

# Blender MCP

Official Blender Lab MCP server: a natural-language interface to a running Blender session's Python API, plus the bundled Python API reference and user manual. Source: [blender.org/lab/mcp-server](https://www.blender.org/lab/mcp-server/), code at `https://projects.blender.org/lab/blender_mcp`.

Not the community `ahujasid/blender-mcp` project, which uses the same `blender-mcp` name. A plain `uvx blender-mcp` or `pip install blender-mcp` does not install this server.

## Security

The server runs model-written Python inside Blender with no guards. Blender Python can read the whole filesystem, including this repository's `.env`, and can reach the network. Blender recommends a VM or a machine without sensitive data. Keep Blender closed, or stop the bridge, when you are not using it.

## Current Status

Verified 2026-10-17:

- Blender 5.2.1 LTS at `/Applications/Blender.app`. The add-on needs 5.1 or newer.
- Add-on `mcp` 1.0.3 from the Blender Lab extensions repository (`lab_blender_org`, `https://lab.blender.org/`). Enabled, matches the `mcp-1.0.3.zip` release byte for byte.
- Add-on prefs: host `localhost`, port `9876`, Auto Start on. Blender's system **Online Access** must stay on, or the bridge refuses to start.
- Server `blender-mcp` 1.0.3 installed with `uv tool`, executable at `~/.local/bin/blender-mcp`.
- OMP: `.omp/mcp.json` defines the `blender` stdio server, with a 300 s request timeout for renders.

## Architecture

```text
MCP client  <- stdio ->  blender-mcp  <- TCP localhost:9876 ->  Blender add-on
```

The add-on must be running inside Blender before tool calls succeed. The server process starts without it, but every Blender-backed tool fails until the bridge is listening.

## Install And Upgrade

Server, pinned to a release tag:

```sh
uv tool install "blender-mcp @ git+https://projects.blender.org/lab/blender_mcp.git@v1.0.3#subdirectory=mcp"
```

Add-on, with Blender closed:

```sh
B=/Applications/Blender.app/Contents/MacOS/Blender
$B -c extension sync
$B -c extension list            # shows "mcp [outdated: X -> Y]" under lab.blender.org
$B -c extension remove lab_blender_org.mcp
$B -c extension install -e lab_blender_org.mcp
```

`extension install` skips a package that is already installed, and `extension update` upgrades every outdated extension in every repository, so use remove plus install to upgrade only this add-on. Removing the add-on resets its prefs; the values above are the defaults.

Keep the add-on and server on the same release.

## Running

- **Interactive:** open Blender. Auto Start launches the bridge about one second after startup. Start or stop it manually from Preferences → Add-ons → MCP.
- **Headless:** `/Applications/Blender.app/Contents/MacOS/Blender -b -c blender_mcp` starts the bridge in background mode. Do not add `--factory-startup`, because that skips user add-ons and fails with `Unrecognized command: "blender_mcp"`. Background mode rejects deferred tools such as screenshots.
- OMP connects to the server at session start. Run `/mcp reload` if Blender was started after the session.
- Without the `blender` MCP tools loaded in a session, `scripts/blender/mcp_call.py` drives a running Blender through the same server. Run it with `~/.local/share/uv/tools/blender-mcp/bin/python`; its docstring has the usage.

## Headless Scripts

`scripts/blender/` holds tools that do not need the bridge:

- `fluid_bake.py`: frees and rebakes every Mantaflow domain in a `.blend` (or `--domain NAME`), then saves it.
- `render_frames.py`: renders frames or `A-B` ranges with Cycles on Metal to `OUTDIR/f####.png`, with `--samples` and `--percent`.
- `jerry_fire_rig_build.py`: rebuilds the Jerry fire rig; see `workflows/blender/jerry/jerry_fire-rig_log_v001.md`.

## Tools

26 tools in 1.0.3:

- Code: `execute_blender_code`. Assign a **dict** to `result`; any other type returns `The result variable must be a dict`, though `stdout` still comes back.
- Scene inspection: `get_objects_summary`, `get_object_detail_summary`, `get_blendfile_summary_datablocks`, `_missing_files`, `_of_linked_libraries`, `_path_info`, `_usage_guess`.
- Viewing: `get_screenshot_of_window_as_image`, `get_screenshot_of_area_as_image`, `get_screenshot_of_window_as_json`, `render_viewport_to_path`, `render_thumbnail_to_path`.
- Navigation: `jump_to_tab_by_name`, `jump_to_tab_by_space_type`, `jump_to_view3d_object_by_name`, `jump_to_view3d_object_data_by_name`.
- Docs: `get_python_api_docs`, `search_api_docs`, `search_manual_docs`.
- The `*_for_cli` variants are for background mode.

## Verified Behavior (2026-10-17)

A smoke test against a headless bridge, using the MCP Python client over stdio, passed. `initialize` succeeded, `list_tools` returned 26 tools, `execute_blender_code` ran and printed `5.2.1 LTS` with the default `Camera`, `Cube`, and `Light`, and `get_objects_summary` returned the scene, collections, and active object.

## Interactive Session Pitfalls (2026-10-17)

Seen while building `jerry_fire-rig_v001.blend` (`workflows/blender/jerry/jerry_fire-rig_log_v001.md`):

- With Blender behind other windows, `execute_blender_code` timed out with `Blender connection timed out at localhost:9876`. The port stayed open and Blender sat at 0% CPU. Suspected cause, unconfirmed: macOS App Nap throttling the add-on's timer.
- Switching the viewport to Cycles rendered shading with a baked fire domain froze the UI at 0% CPU. It was force-quit.
- A request that times out may still be queued inside a stalled Blender and run later, including its `save_mainfile`. Force-quit a hung session instead of waiting, so stale edits cannot overwrite the file.
- Heavy work (fluid bakes, renders) is safer headless: `Blender -b FILE --python script.py`. Edit the same `.blend` headless too, then reopen it in the UI to inspect. Keep the UI viewport in Solid shading.
- Set a bone-parented object's `matrix_world` with the armature in `pose_position = "REST"`. In an animated pose, the inverse of the current pose gets baked into the child's local transform.

---

## Changelog

| Version | Date       | Description |
|---------|------------|-------------|
| 1.0     | 2026-10-17 | Initial Blender MCP: official Blender Lab server and add-on 1.0.3, OMP stdio config, upgrade path, and smoke-test results. |
| 1.1     | 2026-10-17 | Added interactive-session pitfalls: bridge timeouts while Blender was backgrounded, the rendered-viewport freeze, stale queued requests, and the headless workflow. |
| 1.2     | 2026-10-17 | Indexed the `scripts/blender/` headless tools and the `mcp_call.py` client. |
