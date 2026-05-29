#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE}")" &> /dev/null && pwd)

echo "The script is running from: $SCRIPT_DIR"

cd "$SCRIPT_DIR"

# Detect OS and set the correct virtual environment activation path
case "$OSTYPE" in
  msys*|cygwin*|mingw*)
    VENV_ACTIVATE="$SCRIPT_DIR/.venv/Scripts/activate"
    ;;
  *)
    VENV_ACTIVATE="$SCRIPT_DIR/.venv/bin/activate"
    ;;
esac

# Verify the activate script exists before sourcing it
if [ -f "$VENV_ACTIVATE" ]; then
    source "$VENV_ACTIVATE"
else
    echo "Error: Virtual environment activation script not found at $VENV_ACTIVATE" >&2
    exit 1
fi

uv run "$SCRIPT_DIR/main.py"
