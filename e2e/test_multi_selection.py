import pytest
from playwright.sync_api import Page, expect
import time


def test_multi_selection(page: Page):
    """
    Implements MUL-001 to MUL-018: Multi-Selection
    Tests creating multiple nodes, dragging a marquee to select them,
    and verifying they can be moved together.
    """
    page.goto("http://localhost:8082")

    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)

    icon = page.locator("[data-testid='icon-item']").first
    expect(icon).to_be_visible(timeout=10000)

    # Create two nodes
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    time.sleep(0.5)
    icon.drag_to(canvas, target_position={"x": 400, "y": 200})
    time.sleep(0.5)

    nodes = page.locator("[data-node-kind='node']")
    expect(nodes).to_have_count(2)

    canvas_box = canvas.bounding_box()
    assert canvas_box is not None

    # Drag a marquee selection around both nodes
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 500, canvas_box["y"] + 300, steps=10)
    page.mouse.up()

    time.sleep(0.5)

    # Select one of the nodes and drag it to move the whole selection
    node1 = nodes.nth(0)
    node1_box = node1.bounding_box()
    assert node1_box is not None

    node2_before = nodes.nth(1).bounding_box()
    assert node2_before is not None

    page.mouse.move(node1_box["x"] + 10, node1_box["y"] + 10)
    page.mouse.down()
    page.mouse.move(node1_box["x"] + 110, node1_box["y"] + 110, steps=10)
    page.mouse.up()

    time.sleep(0.5)

    # Verify both nodes moved
    node1_after = nodes.nth(0).bounding_box()
    node2_after = nodes.nth(1).bounding_box()

    assert node1_after is not None
    assert node2_after is not None

    assert abs(node1_after["x"] - node1_box["x"] - 100) < 20
    assert abs(node2_after["x"] - node2_before["x"] - 100) < 20
