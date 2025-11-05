# tests/test_minimal_dirs_full.py
from minimal_dirs import minimal_dirs

def test_example_from_prompt():
    inp = ["A/B", "A/B/C", "A/C/A", "A/C/B"]
    assert set(minimal_dirs(inp)) == {"A/B", "A/C/A", "A/C/B"}

def test_sibling_with_prefix_name_not_child():
    inp = ["A/B", "A/BA"]
    assert set(minimal_dirs(inp)) == {"A/B", "A/BA"}

def test_duplicates_removed():
    inp = ["A/B", "A/B", "A/B/C"]
    assert set(minimal_dirs(inp)) == {"A/B"}

def test_trailing_slash_normalization():
    inp = ["A/B/", "A/B/C"]
    assert set(minimal_dirs(inp)) == {"A/B"}

def test_dot_and_dotdot_normalization():
    inp = ["A/./B", "A/B/C", "A/B/../D"]
    assert set(minimal_dirs(inp)) == {"A/B", "A/D"}

def test_leading_dotdot_preserved():
    inp = ["../A", "../A/B", "C/D"]
    assert set(minimal_dirs(inp)) == {"../A", "C/D"}

def test_absolute_and_relative_distinct():
    inp = ["/A/B", "/A/B/C", "A/B"]
    assert set(minimal_dirs(inp)) == {"/A/B", "A/B"}

def test_current_dir_and_empty_string():
    inp = ["", ".", "./A", "A/B"]
    assert set(minimal_dirs(inp)) == {"."}

def test_root_covers_absolute_children():
    inp = ["/", "/A", "/A/B"]
    assert set(minimal_dirs(inp)) == {"/"}

def test_case_sensitivity():
    inp = ["A/B", "a/b"]
    assert set(minimal_dirs(inp)) == {"A/B", "a/b"}
