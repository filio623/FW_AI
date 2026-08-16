#!/usr/bin/env bash
# Create the FW_AI ComfyUI development Pod, wait for it, and record the Pod ID.
#
#   scripts/runpod-pod-up.sh              # RTX 4090, 2-hour termination guard
#   HOURS=4 scripts/runpod-pod-up.sh      # longer guard
#   GPU="NVIDIA RTX A6000" DC=US-TX-1 VOLUME= scripts/runpod-pod-up.sh
#
# Models and the ComfyUI install live on the network volume, so a terminated Pod
# loses nothing. See mcp/runpod.md.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="$ROOT_DIR/.env"

GPU="${GPU:-NVIDIA GeForce RTX 4090}"
TEMPLATE="${TEMPLATE:-cw3nka7d08}"          # official ComfyUI - CUDA 12.8
DC="${DC:-US-IL-1}"
VOLUME="${VOLUME-ccv3wj09mn}"               # fw-ai-comfyui, 100GB, pinned to US-IL-1
PORTS="${PORTS:-8188/http,22/tcp}"
HOURS="${HOURS:-2}"
NAME="${NAME:-fw-ai-comfyui-dev}"

TERM_AT="$(date -u -v+"${HOURS}"H +%Y-%m-%dT%H:%M:%SZ)"
echo "GPU:              $GPU"
echo "Data center:      $DC"
echo "Network volume:   ${VOLUME:-<none>}"
echo "Auto-terminate:   $TERM_AT (${HOURS}h)"
echo

args=(
  --name "$NAME"
  --template-id "$TEMPLATE"
  --gpu-id "$GPU"
  --cloud-type SECURE
  --data-center-ids "$DC"
  --ports "$PORTS"
  --terminate-after "$TERM_AT"
)
[[ -n "$VOLUME" ]] && args+=(--network-volume-id "$VOLUME")

created="$("$ROOT_DIR/scripts/runpod-with-auth.sh" runpodctl pod create "${args[@]}")"
POD_ID="$(printf '%s' "$created" | python3 -c 'import json,sys; print(json.load(sys.stdin)["id"])')"
COST="$(printf '%s' "$created" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("costPerHr","?"))')"
echo "Created pod $POD_ID at \$$COST/hr"

# Record the Pod ID in the ignored .env so the API helper can reach it.
if [[ -f "$ENV_FILE" ]] && grep -qE '^[# ]*RUNPOD_POD_ID=' "$ENV_FILE"; then
  python3 - "$ENV_FILE" "$POD_ID" <<'PY'
import re, sys
p, pod = sys.argv[1], sys.argv[2]
t = open(p).read()
t = re.sub(r'(?m)^[# ]*RUNPOD_POD_ID=.*$', f'RUNPOD_POD_ID={pod}', t, count=1)
open(p, 'w').write(t)
PY
else
  printf '\nRUNPOD_POD_ID=%s\n' "$POD_ID" >> "$ENV_FILE"
fi
echo "Recorded RUNPOD_POD_ID in .env"

URL="https://${POD_ID}-8188.proxy.runpod.net"
echo
echo -n "Waiting for ComfyUI"
for _ in $(seq 1 60); do
  if python3 - "$URL" <<'PY' >/dev/null 2>&1
import ssl, sys, certifi
from urllib.request import Request, urlopen
r = Request(sys.argv[1] + "/system_stats")
r.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
urlopen(r, timeout=10, context=ssl.create_default_context(cafile=certifi.where())).read()
PY
  then
    echo
    echo "ComfyUI is up:  $URL"
    exit 0
  fi
  echo -n "."
  sleep 10
done

echo
echo "Pod $POD_ID created, but ComfyUI did not answer within 10 minutes." >&2
echo "Check: scripts/runpod-with-auth.sh runpodctl pod get $POD_ID" >&2
exit 1
