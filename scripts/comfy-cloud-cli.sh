#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT_DIR/.env"
COMFY_BIN="${COMFY_BIN:-$ROOT_DIR/.venv-comfy-cli/bin/comfy}"

if [[ ! -x "$COMFY_BIN" ]]; then
  echo "Missing comfy CLI at $COMFY_BIN. Install Python 3.12, then run: python3.12 -m venv .venv-comfy-cli && .venv-comfy-cli/bin/python -m pip install git+https://github.com/Comfy-Org/comfy-cli.git" >&2
  exit 1
fi

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Missing .env at $ENV_FILE" >&2
  exit 1
fi

set -a
source "$ENV_FILE"
set +a

if [[ -z "${COMFY_API_KEY:-}" ]]; then
  echo "COMFY_API_KEY is not set in $ENV_FILE" >&2
  exit 1
fi

exec "$COMFY_BIN" "$@"
