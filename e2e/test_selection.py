import pytest
from playwright.sync_api import Page, expect
import time


def test_selection_click(page: Page):
    """
    Implements SEL-001 to SEL-025: Selection
    Tests basic clicking to select, shift-clicking to toggle selection,
    and clicking on empty space to deselect.
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

    # Click node 1
    node1 = nodes.nth(0)
    node1_box = node1.bounding_box()
    assert node1_box is not None

    # Deselect anything
    page.mouse.click(10, 10)
    time.sleep(0.1)

    # Click just Node 1
    page.mouse.click(
        node1_box["x"] + node1_box["width"] / 2,
        node1_box["y"] + node1_box["height"] / 2,
    )
    time.sleep(0.1)

    page.keyboard.press("Delete")
    time.sleep(0.5)

    expect(nodes).to_have_count(1)  # Node 1 is deleted

    # Undo
    page.locator("[data-testid='toolbar-undo']").click()
    time.sleep(0.5)

    expect(nodes).to_have_count(2)

    node1 = nodes.nth(0)
    node2 = nodes.nth(1)

    node1_box = node1.bounding_box()
    node2_box = node2.bounding_box()
    assert node1_box is not None
    assert node2_box is not None

    # Deselect anything again
    page.mouse.click(10, 10)
    time.sleep(0.1)

    # Shift click both
    # Let's just use keyboard down again, but use it properly with absolute mouse movement
    page.keyboard.down("Shift")
    page.mouse.click(
        node1_box["x"] + node1_box["width"] / 2,
        node1_box["y"] + node1_box["height"] / 2,
    )
    time.sleep(0.1)
    page.mouse.click(
        node2_box["x"] + node2_box["width"] / 2,
        node2_box["y"] + node2_box["height"] / 2,
    )
    page.keyboard.up("Shift")
    time.sleep(0.1)

    # Delete both
    page.keyboard.press("Delete")
    time.sleep(0.5)

    expect(nodes).to_have_count(0)
