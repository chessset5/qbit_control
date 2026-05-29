#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

echo "The script is running from: $SCRIPT_DIR"

cd "$SCRIPT_DIR"

source "$SCRIPT_DIR/.venv/bin/activate"

uvx isort --py=312 .
uvx black --target-version=py312 .