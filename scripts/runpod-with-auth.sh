#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT_DIR/.env"
RUNPOD_CONFIG="${RUNPOD_CONFIG:-$HOME/.runpod/config.toml}"

if [[ -z "${RUNPOD_API_KEY:-}" && -f "$ENV_FILE" ]]; then
  set -a
  source "$ENV_FILE"
  set +a
fi

if [[ -z "${RUNPOD_API_KEY:-}" && -f "$RUNPOD_CONFIG" ]]; then
  RUNPOD_API_KEY="$(python3 - "$RUNPOD_CONFIG" <<'PY'
from pathlib import Path
import sys
import tomllib

config = tomllib.loads(Path(sys.argv[1]).read_text())
default = config.get("default", {})
candidates = (
    config.get("apikey"),
    config.get("api_key"),
    default.get("apikey") if isinstance(default, dict) else None,
    default.get("api_key") if isinstance(default, dict) else None,
)
print(next((value for value in candidates if isinstance(value, str) and value), ""))
PY
)"
fi

if [[ -z "${RUNPOD_API_KEY:-}" ]]; then
  echo "RunPod authentication is missing." >&2
  echo "Run 'flash login' or set RUNPOD_API_KEY in the ignored .env file." >&2
  exit 1
fi

if [[ "$#" -eq 0 ]]; then
  echo "Usage: scripts/runpod-with-auth.sh <command> [args...]" >&2
  exit 2
fi

export RUNPOD_API_KEY
exec "$@"
