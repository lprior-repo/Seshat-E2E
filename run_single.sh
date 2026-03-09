#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
E2E_DIR="$DIR/e2e"
SESHAT_DIR="${SESHAT_DIR:-$DIR/../seshat/diagram_tool}"

source "$E2E_DIR/venv/bin/activate"

cd "$SESHAT_DIR"
dx build --platform web --release

cd "$DIR/../seshat/target/dx/diagram_tool/release/web/public"
python3 -m http.server 8082 >"$E2E_DIR/http_server.log" 2>&1 &
SERVER_PID=$!

trap "kill $SERVER_PID || true" EXIT

for i in {1..40}; do
	if curl -s http://localhost:8082 >/dev/null; then
		break
	fi
	sleep 1
done

cd "$E2E_DIR"
pytest test_suite_H_snapping.py test_suite_J_undo.py -n 4 -q
