def minimal_directories(dirs):
    """
    Given a list of directory paths, return the minimal subset
    such that every original path is contained in (or equal to)
    one of the returned directories.
    """
    dirs = sorted(dirs)
    result = []
    for d in dirs:
        if not any(d == r or d.startswith(r + "/") for r in result):
            result.append(d)
    return result
