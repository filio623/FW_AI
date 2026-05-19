#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
RESPONSES = ROOT / "memories" / "responses"
API_URL = "https://api.supermemory.ai/v3/documents"


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def post_document(payload: dict, api_key: str) -> dict:
    body = json.dumps(payload).encode("utf-8")
    req = Request(
        API_URL,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    with urlopen(req, timeout=60) as response:
        raw = response.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add a local markdown/text document to Supermemory."
    )
    parser.add_argument("file", help="Path to the text/markdown file to add")
    parser.add_argument("--custom-id", help="Stable customId for dedupe/update")
    parser.add_argument("--title", help="Human-readable title")
    parser.add_argument("--type", default="project-memory", help="Metadata type")
    parser.add_argument("--source", default="codex", help="Metadata source")
    args = parser.parse_args()

    if not ENV_FILE.exists():
        raise SystemExit(f"Missing .env at {ENV_FILE}")

    env = load_env(ENV_FILE)
    api_key = env.get("SUPERMEMORY_API_KEY") or os.environ.get("SUPERMEMORY_API_KEY")
    if not api_key:
        raise SystemExit("SUPERMEMORY_API_KEY is not set")

    container_tag = env.get("SUPERMEMORY_CONTAINER_TAG", "ai-video-workflows")
    project = env.get("SUPERMEMORY_PROJECT", container_tag)

    path = (ROOT / args.file).resolve() if not Path(args.file).is_absolute() else Path(args.file)
    if not path.exists():
        raise SystemExit(f"Missing input file: {path}")

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    custom_id = args.custom_id or path.stem.replace(" ", "-")
    title = args.title or path.stem.replace("-", " ")

    payload = {
        "content": path.read_text(),
        "containerTag": container_tag,
        "customId": custom_id,
        "taskType": "memory",
        "entityContext": (
            "AI short-film VFX project workspace for generating consistent fire and "
            "water characters as compositable elements over live-action plates."
        ),
        "metadata": {
            "project": project,
            "source": args.source,
            "type": args.type,
            "title": title,
            "date": now[:10],
            "workspace": "FW_AI_Workflow",
            "filepath": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
        },
    }

    try:
        result = post_document(payload, api_key)
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Supermemory HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise SystemExit(f"Supermemory request failed: {exc}") from exc

    RESPONSES.mkdir(parents=True, exist_ok=True)
    response_path = RESPONSES / f"{custom_id}-{now.replace(':', '').replace('+', 'Z')}.json"
    response_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    print(f"Added Supermemory document: {custom_id}")
    print(f"Response saved: {response_path.relative_to(ROOT)}")
    if "id" in result:
        print(f"Document id: {result['id']}")


if __name__ == "__main__":
    main()
