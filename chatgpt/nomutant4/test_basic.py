from dirs import minimal_dirs

def test_example_from_prompt():
    inp = ["A/B", "A/B/C", "A/C/A", "A/C/B"]
    out = minimal_dirs(inp)
    assert set(out) == {"A/B", "A/C/A", "A/C/B"}
