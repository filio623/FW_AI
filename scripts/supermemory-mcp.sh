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

if [[ -z "${SUPERMEMORY_API_KEY:-}" ]]; then
  echo "SUPERMEMORY_API_KEY is not set in $ENV_FILE" >&2
  exit 1
fi

export SUPERMEMORY_AUTH_HEADER="Bearer ${SUPERMEMORY_API_KEY}"
export SUPERMEMORY_PROJECT_HEADER="${SUPERMEMORY_PROJECT:-ai-video-workflows}"

exec npx -y mcp-remote@latest \
  https://mcp.supermemory.ai/mcp \
  --header 'Authorization:${SUPERMEMORY_AUTH_HEADER}' \
  --header 'x-sm-project:${SUPERMEMORY_PROJECT_HEADER}'
