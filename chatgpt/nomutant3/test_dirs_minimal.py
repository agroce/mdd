# test_dirs_minimal.py

from dirs_minimal import minimal_dirs

def test_single_directory_returns_itself():
    assert minimal_dirs(["A/B"]) == ["A/B"]

def test_parent_directory_removes_subdirectory():
    assert minimal_dirs(["A", "A/B"]) == ["A"]

def test_multiple_unrelated_directories():
    paths = ["A/B", "C/D"]
    assert minimal_dirs(paths) == ["A/B", "C/D"]

def test_deeply_nested_structure():
    paths = ["A/B/C/D", "A/B"]
    assert minimal_dirs(paths) == ["A/B"]

def test_example_case_from_specification():
    paths = ["A/B", "A/B/C", "A/C/A", "A/C/B"]
    expected = ["A/B", "A/C/A", "A/C/B"]
    assert minimal_dirs(paths) == expected
