#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT / ".env"
BASE_URL = "https://cloud.comfy.org"


def load_env() -> dict[str, str]:
    env = dict(os.environ)
    if ENV_FILE.exists():
        for raw_line in ENV_FILE.read_text().splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            env.setdefault(key.strip(), value.strip().strip("\"'"))
    return env


def request_json(method: str, path: str, api_key: str, body: object | None = None) -> object:
    data = None
    headers = {"X-API-Key": api_key}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = Request(f"{BASE_URL}{path}", data=data, headers=headers, method=method)
    try:
        with urlopen(req, timeout=120) as response:
            raw = response.read().decode("utf-8")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Comfy Cloud HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise SystemExit(f"Comfy Cloud request failed: {exc}") from exc

    return json.loads(raw) if raw else {}


def print_json(value: object) -> None:
    print(json.dumps(value, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description="Small Comfy Cloud API helper.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("user", help="Show authenticated account status.")
    subparsers.add_parser("system-stats", help="Show cloud system statistics.")
    subparsers.add_parser("queue", help="Show cloud queue information.")

    history = subparsers.add_parser("history", help="Show history for one prompt/job ID.")
    history.add_argument("prompt_id")

    submit = subparsers.add_parser("submit", help="Submit a ComfyUI API-format workflow JSON.")
    submit.add_argument("workflow", type=Path)

    args = parser.parse_args()
    env = load_env()
    api_key = env.get("COMFY_API_KEY")
    if not api_key:
        raise SystemExit(f"COMFY_API_KEY is not set in {ENV_FILE}")

    if args.command == "user":
        print_json(request_json("GET", "/api/user", api_key))
    elif args.command == "system-stats":
        print_json(request_json("GET", "/api/system_stats", api_key))
    elif args.command == "queue":
        print_json(request_json("GET", "/api/queue", api_key))
    elif args.command == "history":
        print_json(request_json("GET", f"/api/history/{args.prompt_id}", api_key))
    elif args.command == "submit":
        workflow = json.loads(args.workflow.read_text())
        print_json(request_json("POST", "/api/prompt", api_key, {"prompt": workflow}))


if __name__ == "__main__":
    main()
