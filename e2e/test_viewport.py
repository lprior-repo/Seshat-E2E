import pytest
from playwright.sync_api import Page, expect
import time


def test_viewport_panning(page: Page):
    """
    Implements CAM-001 to CAM-012: Viewport
    Tests panning the viewport by holding spacebar and dragging.
    """
    page.goto("http://localhost:8082")

    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)

    icon = page.locator("[data-testid='icon-item']").first
    expect(icon).to_be_visible(timeout=10000)

    # Create a node
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    time.sleep(0.5)

    node = page.locator("[data-node-kind='node']").first
    node_box_before = node.bounding_box()
    assert node_box_before is not None

    canvas_box = canvas.bounding_box()
    assert canvas_box is not None

    # Press space and pan
    page.keyboard.down(" ")
    page.mouse.move(canvas_box["x"] + 200, canvas_box["y"] + 200)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    page.keyboard.up(" ")

    time.sleep(0.5)

    node_box_after = node.bounding_box()
    assert node_box_after is not None

    # The node should appear to have moved on the screen relative to the pan
    assert abs(node_box_after["x"] - node_box_before["x"] - 100) < 20
    assert abs(node_box_after["y"] - node_box_before["y"] - 100) < 20
