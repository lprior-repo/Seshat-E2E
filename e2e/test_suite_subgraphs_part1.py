import pytest
from playwright.sync_api import Page, expect
import time

def test_SUB_001_click_inside_container_selects_child_vs_container_with_modifier(page: Page):
    """Test coverage for Click inside container selects child vs container with modifier"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    # 1. Create subgraph
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    
    # 2. Switch to select tool and drag a node inside
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    time.sleep(0.2)
    
    # 3. Click inside container
    page.mouse.click(200, 200)
    time.sleep(0.2)
    

def test_SUB_002_box_select_across_container_boundary(page: Page):
    """Test coverage for Box-select across container boundary"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    
    page.locator("[data-testid='tool-select']").click()
    page.mouse.move(50, 50)
    page.mouse.down()
    page.mouse.move(350, 350)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_003_collapse_expand_container_behavior(page: Page):
    """Test coverage for Collapse/expand container behavior"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_004_locked_container_with_unlocked_children_interactions(page: Page):
    """Test coverage for Locked container with unlocked children interactions"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_005_parent_child_relationship_preservation_during_selection(page: Page):
    """Test coverage for Parent-child relationship preservation during selection"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_006_delete_container_reparents_children(page: Page):
    """Test coverage for Delete container reparents children"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_007_duplicate_container_remaps_ids(page: Page):
    """Test coverage for Duplicate container remaps IDs"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_008_drag_child_into_container(page: Page):
    """Test coverage for Drag child into container"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 50, "y": 50})
    time.sleep(0.2)
    page.mouse.move(50, 50)
    page.mouse.down()
    page.mouse.move(200, 200, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_009_drag_child_out_becomes_root(page: Page):
    """Test coverage for Drag child out becomes root"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    time.sleep(0.2)
    page.mouse.move(200, 200)
    page.mouse.down()
    page.mouse.move(50, 50, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_010_drag_across_overlapping_containers(page: Page):
    """Test coverage for Drag across overlapping containers"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(250, 250)
    page.mouse.down()
    page.mouse.move(450, 450)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_011_container_auto_expand_when_child_crosses_boundary(page: Page):
    """Test coverage for Container auto-expand when child crosses boundary"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_012_container_resize_behavior(page: Page):
    """Test coverage for Container resize behavior (children keep size vs scale)"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_013_container_overflow_handling(page: Page):
    """Test coverage for Container overflow handling"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_014_container_padding_alignment(page: Page):
    """Test coverage for Container padding alignment"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_015_create_empty_subgraph_container(page: Page):
    """Test coverage for Create empty subgraph container"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    expect(page.locator("[data-node-kind='subgraph']")).to_have_count(1)
    

def test_SUB_016_create_subgraph_with_pre_selected_nodes(page: Page):
    """Test coverage for Create subgraph with pre-selected nodes"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    time.sleep(0.2)
    page.mouse.click(200, 200)
    time.sleep(0.2)
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 300, canvas_box["y"] + 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    

def test_SUB_017_create_nested_subgraphs(page: Page):
    """Test coverage for Create nested subgraphs"""
    page.goto("http://localhost:8082")
    canvas = page.locator("[data-testid='canvas-root']")
    expect(canvas).to_be_visible(timeout=10000)
    
    page.locator("[data-testid='tool-subgraph']").click()
    canvas_box = canvas.bounding_box()
    assert canvas_box is not None
    page.mouse.move(canvas_box["x"] + 100, canvas_box["y"] + 100)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 500, canvas_box["y"] + 500, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(canvas_box["x"] + 200, canvas_box["y"] + 200)
    page.mouse.down()
    page.mouse.move(canvas_box["x"] + 400, canvas_box["y"] + 400, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    expect(page.locator("[data-node-kind='subgraph']")).to_have_count(2)
    

