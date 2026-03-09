#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
E2E_DIR="$DIR/e2e"
SESHAT_DIR="${SESHAT_DIR:-$DIR/../seshat/diagram_tool}"

echo "Running E2E tests against Seshat at: $SESHAT_DIR"

if [ ! -d "$SESHAT_DIR" ]; then
	echo "Error: Seshat directory not found at $SESHAT_DIR"
	exit 1
fi

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
pip install pytest-xdist

# Install playwright browsers
echo "Installing Playwright browsers..."
playwright install chromium

# Start the Dioxus app in the background
echo "Building and starting Dioxus app..."
cd "$SESHAT_DIR"
dx build --platform web --release

# Serve the static files with a bulletproof Python HTTP server that can handle xdist concurrency
cd "$DIR/../seshat/target/dx/diagram_tool/release/web/public"
python3 -m http.server 8082 >"$E2E_DIR/http_server.log" 2>&1 &
SERVER_PID=$!

# Ensure server is killed when script exits
trap "kill $SERVER_PID || true" EXIT

echo "Waiting for server to start on port 8082..."
for i in {1..40}; do
	if curl -s http://localhost:8082 >/dev/null; then
		echo "Server is up!"
		break
	fi
	sleep 1
	if [ $i -eq 40 ]; then
		echo "Server failed to start in time. Check $E2E_DIR/dx_serve.log"
		cat "$E2E_DIR/dx_serve.log"
		exit 1
	fi
done

# Run tests (Limit to 4 parallel workers so we don't overwhelm the Dioxus dev server listen backlog)
echo "Running pytest..."
cd "$E2E_DIR"
pytest test_suite_*.py -n 4 -q

echo "E2E tests completed successfully!"
