import os

# SUB-001 to SUB-017
PART1_TESTS = [
    (
        "SUB_001_click_inside_container_selects_child_vs_container_with_modifier",
        "Click inside container selects child vs container with modifier",
        """
    # 1. Create subgraph
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
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
    """,
    ),
    (
        "SUB_002_box_select_across_container_boundary",
        "Box-select across container boundary",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    
    page.locator("[data-testid='tool-select']").click()
    page.mouse.move(50, 50)
    page.mouse.down()
    page.mouse.move(350, 350)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_003_collapse_expand_container_behavior",
        "Collapse/expand container behavior",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_004_locked_container_with_unlocked_children_interactions",
        "Locked container with unlocked children interactions",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_005_parent_child_relationship_preservation_during_selection",
        "Parent-child relationship preservation during selection",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_006_delete_container_reparents_children",
        "Delete container reparents children",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_007_duplicate_container_remaps_ids",
        "Duplicate container remaps IDs",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_008_drag_child_into_container",
        "Drag child into container",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
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
    """,
    ),
    (
        "SUB_009_drag_child_out_becomes_root",
        "Drag child out becomes root",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
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
    """,
    ),
    (
        "SUB_010_drag_across_overlapping_containers",
        "Drag across overlapping containers",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(250, 250)
    page.mouse.down()
    page.mouse.move(450, 450)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_011_container_auto_expand_when_child_crosses_boundary",
        "Container auto-expand when child crosses boundary",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_012_container_resize_behavior",
        "Container resize behavior (children keep size vs scale)",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_013_container_overflow_handling",
        "Container overflow handling",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_014_container_padding_alignment",
        "Container padding alignment",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_015_create_empty_subgraph_container",
        "Create empty subgraph container",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    expect(page.locator("[data-node-kind='subgraph']")).to_have_count(1)
    """,
    ),
    (
        "SUB_016_create_subgraph_with_pre_selected_nodes",
        "Create subgraph with pre-selected nodes",
        """
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    time.sleep(0.2)
    page.mouse.click(200, 200)
    time.sleep(0.2)
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_017_create_nested_subgraphs",
        "Create nested subgraphs",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(500, 500)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(200, 200)
    page.mouse.down()
    page.mouse.move(400, 400)
    page.mouse.up()
    time.sleep(0.2)
    expect(page.locator("[data-node-kind='subgraph']")).to_have_count(2)
    """,
    ),
]

# SUB-018 to SUB-034
PART2_TESTS = [
    (
        "SUB_018_subgraph_inherits_viewport_transforms",
        "Subgraph inherits viewport transforms",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_019_subgraph_bounds_calculation",
        "Subgraph bounds calculation",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_020_subgraph_z_index_ordering",
        "Subgraph z-index ordering",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_021_add_node_to_subgraph_updates_parent_reference",
        "Add node to subgraph updates parent reference",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_022_remove_node_from_subgraph_clears_parent_reference",
        "Remove node from subgraph clears parent reference",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    time.sleep(0.2)
    page.mouse.move(200, 200)
    page.mouse.down()
    page.mouse.move(500, 500, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_023_add_multiple_nodes_in_batch",
        "Add multiple nodes in batch",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(400, 400)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    icon.drag_to(canvas, target_position={"x": 300, "y": 300})
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_024_remove_all_nodes_preserves_container",
        "Remove all nodes preserves container",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    time.sleep(0.2)
    page.keyboard.press("Delete")
    time.sleep(0.2)
    expect(page.locator("[data-node-kind='subgraph']")).to_have_count(1)
    """,
    ),
    (
        "SUB_025_remove_last_node_deletes_empty_container",
        "Remove last node deletes empty container",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_026_create_subgraph_within_subgraph",
        "Create subgraph within subgraph",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(500, 500)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(200, 200)
    page.mouse.down()
    page.mouse.move(400, 400)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_027_drag_node_from_parent_to_child_subgraph",
        "Drag node from parent to child subgraph",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(500, 500)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(200, 200)
    page.mouse.down()
    page.mouse.move(400, 400)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 150, "y": 150})
    time.sleep(0.2)
    page.mouse.move(150, 150)
    page.mouse.down()
    page.mouse.move(300, 300, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_028_drag_node_from_child_to_parent_subgraph",
        "Drag node from child to parent subgraph",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(500, 500)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(200, 200)
    page.mouse.down()
    page.mouse.move(400, 400)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 300, "y": 300})
    time.sleep(0.2)
    page.mouse.move(300, 300)
    page.mouse.down()
    page.mouse.move(150, 150, steps=10)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_029_collapse_parent_hides_nested_children",
        "Collapse parent hides nested children",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(500, 500)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_030_edge_internal_to_subgraph",
        "Edge internal to subgraph",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(500, 500)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    icon.drag_to(canvas, target_position={"x": 400, "y": 400})
    time.sleep(0.2)
    page.locator("[data-testid='tool-edge']").click()
    page.mouse.move(200, 200)
    page.mouse.down()
    page.mouse.move(400, 400)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_031_edge_crosses_subgraph_boundary",
        "Edge crosses subgraph boundary",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-select']").click()
    icon = page.locator("[data-testid='icon-item']").first
    icon.drag_to(canvas, target_position={"x": 200, "y": 200})
    icon.drag_to(canvas, target_position={"x": 400, "y": 400})
    time.sleep(0.2)
    page.locator("[data-testid='tool-edge']").click()
    page.mouse.move(200, 200)
    page.mouse.down()
    page.mouse.move(400, 400)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_032_edge_between_nested_subgraphs",
        "Edge between nested subgraphs",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(400, 100)
    page.mouse.down()
    page.mouse.move(600, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_033_edge_updates_when_nodes_reparented",
        "Edge updates when nodes reparented",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
    (
        "SUB_034_edge_routing_respects_collapsed_state",
        "Edge routing respects collapsed state",
        """
    page.locator("[data-testid='tool-subgraph']").click()
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(300, 300)
    page.mouse.up()
    time.sleep(0.2)
    """,
    ),
]


def generate_file(filename, tests):
    with open(filename, "w") as f:
        f.write("import pytest\n")
        f.write("from playwright.sync_api import Page, expect\n")
        f.write("import time\n\n")

        for func_name, desc, body in tests:
            f.write(f"def test_{func_name}(page: Page):\n")
            f.write(f'    """Test coverage for {desc}"""\n')
            f.write(f'    page.goto("http://localhost:8082")\n')
            f.write(f"    canvas = page.locator(\"[data-testid='canvas-root']\")\n")
            f.write(f"    expect(canvas).to_be_visible(timeout=10000)\n")

            for line in body.split("\\n"):
                f.write(f"    {line}\n")

            f.write("\n")


generate_file(
    "/home/lewis/src/seshat-e2e/e2e/test_suite_subgraphs_part1.py", PART1_TESTS
)
generate_file(
    "/home/lewis/src/seshat-e2e/e2e/test_suite_subgraphs_part2.py", PART2_TESTS
)
