from reduce_paths import reduce_paths

paths = ["A/B"]
assert reduce_paths(paths) == ["A/B"]

paths = ["A/B", "A/B/C"]
assert reduce_paths(paths) == ["A/B"]

paths = ["A/B/C", "A/B", "A/C/A", "A/C/B"]
assert reduce_paths(paths) == ["A/B", "A/C/A", "A/C/B"]

paths = ["A/B/", "A/B", "A/B/C/", "A/B/C"]
assert reduce_paths(paths) == ["A/B"]

# root should dominate everything under it
paths = ["/", "/a", "/a/b", "/a/b/"]
assert reduce_paths(paths) == ["/"]

# relative and ./ should normalize to same forms
paths2 = ["./a", "./a/b", "a/b", "a"]
assert reduce_paths(paths2) == ["a"]
