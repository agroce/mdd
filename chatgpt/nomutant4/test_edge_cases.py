from dirs import minimal_dirs

def test_absolute_and_dotdot_and_backslashes():
    inp = [
        "/home/user/project",
        "/home/user/project/module",
        "/home/user/project/module/../other",
        "C:\\Users\\me\\docs",
        "C:/Users/me/docs/sub"
    ]
    out = minimal_dirs(inp)
    assert any(p.endswith("/home/user/project") for p in out)
    assert any("C:/Users/me/docs" in p or p == "C:/Users/me/docs" for p in out)
