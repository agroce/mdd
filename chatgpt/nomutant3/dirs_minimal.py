# dirs_minimal.py (final)

from typing import List

def minimal_dirs(paths: List[str]) -> List[str]:
    """
    Given a list of directory paths, return the minimal subset such that
    every original path is contained within one of them.
    """
    result = []
    for path in sorted(paths):
        # Only add if no existing result is a prefix (i.e., parent directory)
        if not any(path == p or path.startswith(p + "/") for p in result):
            result.append(path)
    return result
