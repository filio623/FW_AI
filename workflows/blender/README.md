# Blender Workflows

Run logs for Blender scenes, rigs, and simulations. Working `.blend` files live with their assets (for example `assets/characters/jerry/source-cgi/`). Simulation caches and renders go to `outputs/`.

Blender is driven through the official Blender Lab MCP server; see `mcp/blender.md`. Headless build, bake, render, and MCP-client scripts live in `scripts/blender/`.

## Active Tests

- `jerry/jerry_fire-rig_log_v001.md`: Jerry as a rigged body that emits Mantaflow fire, with an idle cycle.
