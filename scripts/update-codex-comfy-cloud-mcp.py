#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re
import shutil


CONFIG = Path.home() / ".codex" / "config.toml"
LAUNCHER = Path(__file__).resolve().parent / "comfy-cloud-mcp.sh"

BLOCK = f"""
[mcp_servers.comfy_cloud]
command = "{LAUNCHER}"
startup_timeout_sec = 30
tool_timeout_sec = 60
""".strip()


def replace_or_append(text: str) -> str:
    pattern = re.compile(
        r"(?ms)^\[mcp_servers\.comfy_cloud\]\n.*?(?=^\[[^\n]+\]|\Z)"
    )
    if pattern.search(text):
        return pattern.sub(BLOCK + "\n\n", text).rstrip() + "\n"
    return text.rstrip() + "\n\n" + BLOCK + "\n"


def main() -> None:
    if not CONFIG.exists():
        raise SystemExit(f"Missing Codex config: {CONFIG}")
    if not LAUNCHER.exists():
        raise SystemExit(f"Missing Comfy Cloud launcher: {LAUNCHER}")

    original = CONFIG.read_text()
    updated = replace_or_append(original)

    if updated == original:
        print("Codex config already contains the expected Comfy Cloud MCP block.")
        return

    backup = CONFIG.with_suffix(
        CONFIG.suffix + "." + datetime.now().strftime("%Y%m%d-%H%M%S") + ".bak"
    )
    shutil.copy2(CONFIG, backup)
    CONFIG.write_text(updated)
    print(f"Updated {CONFIG}")
    print(f"Backup: {backup}")


if __name__ == "__main__":
    main()
