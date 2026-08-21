#!/usr/bin/env bash
set -e

NAMESPACE="mlops"
ISVC_NAME="fraud-model"

echo "=== 1. Checking InferenceService Status ==="
READY_STATUS=$(kubectl get inferenceservice $ISVC_NAME -n $NAMESPACE -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}')

if [ "$READY_STATUS" != "True" ]; then
  echo "[-] ERROR: InferenceService $ISVC_NAME is not Ready."
  exit 1
fi
echo "[+] InferenceService $ISVC_NAME is READY."

echo "=== 2. Establishing Port-Forwarding ==="
POD_NAME=$(kubectl get pod -n $NAMESPACE -l serving.kserve.io/inferenceservice=$ISVC_NAME -o jsonpath='{.items[0].metadata.name}')
kubectl port-forward -n $NAMESPACE pod/$POD_NAME 8080:8080 > /dev/null 2>&1 &
PF_PID=$!

cleanup() {
  echo "=== Cleaning up background processes ==="
  kill $PF_PID 2>/dev/null || true
}
trap cleanup EXIT

sleep 2

echo "=== 3. Sending Automated Inference Request ==="
RESPONSE=$(curl -s -X POST http://localhost:8080/v1/models/$ISVC_NAME:predict \
  -H "Content-Type: application/json" \
  -d '{
    "instances": [
      [0.0, 1.2, 0.5, 0.0, 3.1, 0.0, 1.0, 0.2, 0.0, 0.0, 1.0, 0.0, 0.0, 2.5, 0.1, 0.0, 0.0, 1.0, 0.0, 0.5]
    ]
  }')

echo "Response received: $RESPONSE"

echo "=== 4. Validating Response Payload ==="
if echo "$RESPONSE" | grep -q '"predictions"'; then
  echo "[+] SUCCESS: Automated pipeline test passed! Model generated predictions successfully."
else
  echo "[-] FAILURE: Unexpected model response structure."
  exit 1
fi
