#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
E2E_DIR="$DIR/e2e"

echo "Running E2E tests..."

# Check if python3 is installed
if ! command -v python3 &>/dev/null; then
	echo "Python 3 is required but not installed."
	exit 1
fi

# Setup venv if it doesn't exist
if [ ! -d "$E2E_DIR/venv" ]; then
	echo "Creating virtual environment..."
	python3 -m venv "$E2E_DIR/venv"
fi

# Activate venv
source "$E2E_DIR/venv/bin/activate"

# Install requirements
echo "Installing python dependencies..."
pip install -r "$E2E_DIR/requirements.txt"

# Install playwright browsers
echo "Installing Playwright browsers..."
playwright install chromium

# Run tests
echo "Running pytest..."
cd "$E2E_DIR"
pytest test_drag_drop.py -v -s

echo "E2E tests completed successfully!"
