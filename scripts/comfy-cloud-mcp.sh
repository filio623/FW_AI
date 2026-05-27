#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT_DIR/.env"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Missing .env at $ENV_FILE" >&2
  exit 1
fi

set -a
source "$ENV_FILE"
set +a

MCP_URL="${COMFY_CLOUD_MCP_URL:-https://cloud.comfy.org/mcp}"

if [[ -z "${COMFY_API_KEY:-}" ]]; then
  echo "COMFY_API_KEY is not set in $ENV_FILE" >&2
  exit 1
fi

exec npx -y mcp-remote@latest \
  "$MCP_URL" \
  --header 'X-API-Key:${COMFY_API_KEY}'
