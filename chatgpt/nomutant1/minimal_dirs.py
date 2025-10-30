def minimal_dirs(dirs):
    """
    Given a list of directories, return the smallest subset that contains all
    directories, i.e., remove directories that are subdirectories of others.
    """
    dirs = sorted(dirs)
    result = []
    for d in dirs:
        # Only add if no existing result is parent of d
        if not any(d.startswith(r + "/") for r in result):
            result.append(d)
    return result
