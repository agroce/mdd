import pytest
from min_dirs import minimal_directories

def test_single_directory_returns_itself():
    assert minimal_directories(["A/B"]) == ["A/B"]

def test_single_directory_preserves_length_and_content():
    result = minimal_directories(["A/B"])
    assert len(result) == 1
    assert "A/B" in result

def test_removes_subdirectories_of_other_entries():
    dirs = ["A/B", "A/B/C"]
    result = minimal_directories(dirs)
    assert result == ["A/B"]

def test_does_not_remove_sibling_directories():
    dirs = ["A/B", "A/C"]
    result = minimal_directories(dirs)
    assert sorted(result) == ["A/B", "A/C"]

def test_does_not_remove_parent_if_only_subdir_present():
    dirs = ["A/B/C"]
    result = minimal_directories(dirs)
    assert result == ["A/B/C"]

def test_example_from_specification():
    dirs = ["A/B", "A/B/C", "A/C/A", "A/C/B"]
    expected = ["A/B", "A/C/A", "A/C/B"]
    assert sorted(minimal_directories(dirs)) == sorted(expected)

def test_empty_list_returns_empty():
    assert minimal_directories([]) == []

def test_handles_deep_nesting_correctly():
    dirs = ["A", "A/B", "A/B/C", "A/B/C/D"]
    assert minimal_directories(dirs) == ["A"]

def test_mixed_order_input():
    dirs = ["A/B/C", "A/B", "A/C/B", "A/C/A"]
    expected = ["A/B", "A/C/A", "A/C/B"]
    assert sorted(minimal_directories(dirs)) == sorted(expected)
