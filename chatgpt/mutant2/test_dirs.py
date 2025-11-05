import pytest
from dirs import minimal_dirs

def test_no_containment():
    dirs = ["A/B", "C/D", "E/F"]
    expected = ["A/B", "C/D", "E/F"]
    assert minimal_dirs(dirs) == expected

def test_simple_containment():
    dirs = ["A/B", "A/B/C"]
    expected = ["A/B"]
    assert minimal_dirs(dirs) == expected

def test_partial_prefix_not_containment():
    dirs = ["A/BC", "A/B"]
    expected = ["A/BC", "A/B"]
    assert minimal_dirs(dirs) == expected

def test_containment_is_one_way():
    dirs = ["A/B", "A/B/C"]
    assert minimal_dirs(dirs) == ["A/B"]
    dirs_reversed = ["A/B/C", "A/B"]
    assert minimal_dirs(dirs_reversed) == ["A/B"]

def test_siblings_all_kept():
    dirs = ["A/B", "A/C"]
    expected = ["A/B", "A/C"]
    assert minimal_dirs(dirs) == expected

def test_mixed_case():
    dirs = ["A/B", "A/B/C", "A/C/A", "A/C/B"]
    expected = ["A/B", "A/C/A", "A/C/B"]
    assert minimal_dirs(dirs) == expected

def test_deeper_and_unordered_input():
    dirs = ["A/B/C/D", "A/B", "A/C/B/A", "A/C/B"]
    expected = ["A/B", "A/C/B"]
    assert minimal_dirs(dirs) == expected

def test_duplicates_removed():
    dirs = ["A/B", "A/B", "A/B/C"]
    expected = ["A/B"]
    assert minimal_dirs(dirs) == expected

def test_empty_input():
    assert minimal_dirs([]) == []
