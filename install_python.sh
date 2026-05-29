#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

echo "The script is running from: $SCRIPT_DIR"

cd "$SCRIPT_DIR"

source "$SCRIPT_DIR/.venv/bin/activate"

sh -c 'curl -LsSf https://astral.sh/uv/install.sh | sh' 
sh -c 'uv venv --python 3.12'