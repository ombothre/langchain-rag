#!/bin/bash
set -euxo pipefail

# Start Ollama server in the background
ollama serve &
OLLAMA_PID=$!

echo "Waiting for Ollama API to become responsive..."
until curl -s http://localhost:11434/api/tags | grep -q '"models"'; do
  echo "Ollama not ready yet..."
  sleep 1
done

# Pull phi3 with up to 5 retries if not already present
if ! ollama list | grep -q phi3; then
  echo "phi3 model not found — starting pull with retries..."
  for i in {1..5}; do
    echo "Attempt $i to pull phi3..."
    if ollama pull phi3; then
      echo "✅ phi3 pulled successfully on attempt $i"
      break
    elif [[ $i -eq 5 ]]; then
      echo "Failed to pull phi3 after 5 attempts"
      exit 1
    else
      echo "Pull attempt $i failed, retrying in 5 seconds..."
      sleep 5
    fi
  done
else
  echo "phi3 already pulled"
fi

wait $OLLAMA_PID
