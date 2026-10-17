"""Call the Blender Lab MCP server from a shell, for sessions without the `blender` MCP tools.

Run with the Python that `uv tool` installed alongside blender-mcp (it has the `mcp` package):

    PY=~/.local/share/uv/tools/blender-mcp/bin/python
    $PY scripts/blender/mcp_call.py < edit.py                    # execute_blender_code, code on stdin
    $PY scripts/blender/mcp_call.py TOOL '{"arg": "value"}'       # any tool with JSON arguments
    $PY scripts/blender/mcp_call.py --schema TOOL [TOOL ...]      # print tool docs and input schema
    $PY scripts/blender/mcp_call.py --screenshot VIEW_3D out.png  # save an area screenshot

Needs a running Blender with the MCP add-on bridge on localhost:9876 (see mcp/blender.md).
Code passed to execute_blender_code must assign a dict to `result`.
"""

import asyncio
import base64
import json
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main(argv):
    async with stdio_client(StdioServerParameters(command="blender-mcp")) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            if argv and argv[0] == "--schema":
                for tool in (await session.list_tools()).tools:
                    if tool.name in argv[1:]:
                        print(tool.name, tool.description, json.dumps(tool.inputSchema, indent=1))
                return

            if argv and argv[0] == "--screenshot":
                area, path = argv[1], argv[2]
                res = await session.call_tool("get_screenshot_of_area_as_image", {"area_ui_type": area})
                for item in res.content:
                    if getattr(item, "type", "") == "image":
                        with open(path, "wb") as fh:
                            fh.write(base64.b64decode(item.data))
                        print("saved", path)
                        return
                sys.exit("no image returned: %s" % [getattr(c, "text", c) for c in res.content])

            if argv:
                tool, arguments = argv[0], json.loads(argv[1]) if len(argv) > 1 else {}
            else:
                tool, arguments = "execute_blender_code", {"code": sys.stdin.read()}
            res = await session.call_tool(tool, arguments)
            for item in res.content:
                print(getattr(item, "text", item))
            if res.isError:
                sys.exit(1)


asyncio.run(main(sys.argv[1:]))
