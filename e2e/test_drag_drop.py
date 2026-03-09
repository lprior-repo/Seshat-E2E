import pytest
from playwright.sync_api import Page, expect
import time


def test_drag_icon_to_canvas(page: Page):
    page.goto("http://localhost:8082")

    # Wait for elements
    canvas = page.locator("[data-testid='canvas-root']")
    icon = page.locator("[data-testid='icon-item']").first

    expect(canvas).to_be_visible(timeout=10000)
    expect(icon).to_be_visible(timeout=10000)

    # Enable console log tracking
    page.on("console", lambda msg: print(f"PAGE LOG: {msg.text}"))

    # Try native drag and drop
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})

    time.sleep(1)

    canvas_html = canvas.inner_html()
    print(f"Canvas HTML length: {len(canvas_html)}")

    # Let's count how many nodes
    node_count = canvas.locator("[data-testid='node']").count()
    print(f"Number of nodes: {node_count}")
