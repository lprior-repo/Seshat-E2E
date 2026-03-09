# Seshat End-to-End Tests

This repository contains the comprehensive, 255+ case Python Playwright test suite for the Seshat diagramming tool.

## Setup

```bash
# Provide the path to your local Seshat app repository if it is not located at ../../seshat/diagram_tool
export SESHAT_DIR="/path/to/your/seshat/repo/diagram_tool"

./run_e2e.sh
```

The script will automatically build your Dioxus app, launch it on a background server via `dx serve`, and run the comprehensive UI assertions against it natively in Chromium using Python Playwright.
