import glob

for filepath in glob.glob(
    "/home/lewis/src/seshat-e2e/e2e/test_suite_multi_selection_part*.py"
):
    with open(filepath, "r") as f:
        content = f.read()

    # Replace test_MUL-XXX_behavior with test_MUL_XXX_behavior
    import re

    content = re.sub(
        r"def test_MUL-(\d+)_behavior", r"def test_MUL_\1_behavior", content
    )

    with open(filepath, "w") as f:
        f.write(content)
    print(f"Fixed {filepath}")
