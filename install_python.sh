#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE}")" &> /dev/null && pwd)

echo "The script is running from: $SCRIPT_DIR"

cd "$SCRIPT_DIR"

# Detect OS and set the correct virtual environment activation path
case "$OSTYPE" in
    msys*|cygwin*|mingw*)
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ;;
    *)
        sh -c 'curl -LsSf https://astral.sh/uv/install.sh | sh'
    ;;
esac

sh -c 'uv venv'
sh -c 'uv sync'