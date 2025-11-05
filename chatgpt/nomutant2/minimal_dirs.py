def minimal_dirs(paths):
    """
    Given a list of directory paths, return the minimal subset such that
    every input path is contained in or equal to one of the returned paths.
    """
    paths = sorted(paths)
    result = []
    for p in paths:
        if not any(p.startswith(r + "/") for r in result):
            result.append(p)
    return result
