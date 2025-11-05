def minimal_dirs(dirs):
    """
    Given a list of directory paths, return the smallest subset such that
    all given directories are contained in one of them.

    Example:
    ["A/B", "A/B/C", "A/C/A", "A/C/B"] -> ["A/B", "A/C/A", "A/C/B"]
    """
    unique_dirs = sorted(set(dirs))
    result = []
    for d in unique_dirs:
        if not any(d.startswith(other + "/") for other in result):
            result.append(d)
    return result
