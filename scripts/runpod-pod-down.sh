#!/usr/bin/env bash
# Terminate the FW_AI ComfyUI Pod and clear its ID from .env.
#
#   scripts/runpod-pod-down.sh            # terminate the pod recorded in .env
#   scripts/runpod-pod-down.sh <pod-id>   # terminate a specific pod
#
# Safe to run whenever you stop working: ComfyUI and all downloaded models live
# on the network volume, which is NOT deleted by this script. Only the ~$7/month
# volume charge continues. See mcp/runpod.md.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT_DIR/.env"

POD_ID="${1:-}"
if [[ -z "$POD_ID" && -f "$ENV_FILE" ]]; then
  POD_ID="$(grep -E '^RUNPOD_POD_ID=' "$ENV_FILE" | head -1 | cut -d= -f2- | tr -d '[:space:]')"
fi

if [[ -z "$POD_ID" ]]; then
  echo "No pod id given and no RUNPOD_POD_ID set in .env." >&2
  echo "Running pods:" >&2
  "$ROOT_DIR/scripts/runpod-with-auth.sh" runpodctl pod list >&2
  exit 1
fi

echo "Terminating pod $POD_ID ..."
"$ROOT_DIR/scripts/runpod-with-auth.sh" runpodctl pod delete "$POD_ID"

# Comment the Pod ID back out so stale ids are never reused.
if [[ -f "$ENV_FILE" ]]; then
  python3 - "$ENV_FILE" <<'PY'
import re, sys
p = sys.argv[1]
t = open(p).read()
t = re.sub(r'(?m)^RUNPOD_POD_ID=.*$', '# RUNPOD_POD_ID=', t, count=1)
open(p, 'w').write(t)
PY
  echo "Cleared RUNPOD_POD_ID in .env"
fi

echo
echo "Pod terminated. The network volume and everything on it is untouched."
"$ROOT_DIR/scripts/runpod-with-auth.sh" runpodctl pod list
