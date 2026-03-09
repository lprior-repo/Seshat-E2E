import pytest
from playwright.sync_api import Page, expect
import time


def test_clipboard_copy_paste(page: Page):
    """
    Implements CLP-001 to CLP-010: Clipboard
    Tests copying a node and pasting it back onto the canvas.
    """
    page.goto("http://localhost:8082")

    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)

    icon = page.locator("[data-testid='icon-item']").first
    expect(icon).to_be_visible(timeout=10000)

    # Create a node
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    time.sleep(0.5)

    nodes = page.locator("[data-node-kind='node']")
    expect(nodes).to_have_count(1)

    # Click to select it
    page.mouse.click(200, 200)

    # Copy
    page.keyboard.press("Control+C")
    time.sleep(0.1)

    # Move mouse somewhere else
    page.mouse.move(400, 400)

    # Paste
    page.keyboard.press("Control+V")
    time.sleep(0.5)

    # We should have 2 nodes now
    expect(nodes).to_have_count(2)
