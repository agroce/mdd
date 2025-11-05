from dirs import minimal_dirs

def test_duplicates_and_trailing_slash_and_dots():
    inp = [
        "A/B", "A/B/", "A/B/C", "A//B/./C",
        "A/C", "A/C/.", "A/C/B", "A/C/B/"
    ]
    out = minimal_dirs(inp)
    assert set(out) == {"A/B", "A/C"}
