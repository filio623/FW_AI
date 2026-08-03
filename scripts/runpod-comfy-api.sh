#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT_DIR/.env"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  source "$ENV_FILE"
  set +a
fi

COMFYUI_PORT="${RUNPOD_COMFYUI_PORT:-8188}"
if [[ -n "${RUNPOD_COMFYUI_URL:-}" ]]; then
  COMFYUI_URL="${RUNPOD_COMFYUI_URL%/}"
elif [[ -n "${RUNPOD_POD_ID:-}" ]]; then
  COMFYUI_URL="https://${RUNPOD_POD_ID}-${COMFYUI_PORT}.proxy.runpod.net"
else
  echo "Set RUNPOD_POD_ID or RUNPOD_COMFYUI_URL in the ignored .env file." >&2
  exit 1
fi

COMMAND="${1:-}"
case "$COMMAND" in
  url)
    printf '%s\n' "$COMFYUI_URL"
    ;;
  status)
    curl -fsS "$COMFYUI_URL/system_stats" | jq .
    ;;
  queue)
    curl -fsS "$COMFYUI_URL/queue" | jq .
    ;;
  object-info)
    curl -fsS "$COMFYUI_URL/object_info" | jq .
    ;;
  history)
    PROMPT_ID="${2:-}"
    if [[ -n "$PROMPT_ID" ]]; then
      curl -fsS "$COMFYUI_URL/history/$PROMPT_ID" | jq .
    else
      curl -fsS "$COMFYUI_URL/history" | jq .
    fi
    ;;
  upload)
    FILE="${2:-}"
    if [[ -z "$FILE" || ! -f "$FILE" ]]; then
      echo "Usage: scripts/runpod-comfy-api.sh upload <file>" >&2
      exit 2
    fi
    curl -fsS -X POST "$COMFYUI_URL/upload/image" \
      -F "image=@$FILE" \
      -F "overwrite=true" | jq .
    ;;
  submit)
    WORKFLOW="${2:-}"
    if [[ -z "$WORKFLOW" || ! -f "$WORKFLOW" ]]; then
      echo "Usage: scripts/runpod-comfy-api.sh submit <api-workflow.json>" >&2
      exit 2
    fi
    jq -n --slurpfile prompt "$WORKFLOW" '{prompt: $prompt[0]}' \
      | curl -fsS -X POST "$COMFYUI_URL/prompt" \
          -H 'Content-Type: application/json' \
          --data-binary @- \
      | jq .
    ;;
  *)
    echo "Usage: scripts/runpod-comfy-api.sh {url|status|queue|object-info|history [prompt-id]|upload <file>|submit <workflow.json>}" >&2
    exit 2
    ;;
esac
