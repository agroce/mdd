from pathlib import PurePosixPath
from typing import Iterable, List

def normalize(p: str) -> str:
    # Normalize a POSIX-style path (removes redundant '.' and '..' where possible,
    # removes duplicate slashes, and removes trailing slash except for root "/").
    pp = PurePosixPath(p)
    return str(pp)

def is_ancestor(ancestor: str, descendant: str) -> bool:
    a = PurePosixPath(ancestor)
    d = PurePosixPath(descendant)
    try:
        # Python 3.9+: is_relative_to is convenient
        return d.is_relative_to(a) and d != a
    except AttributeError:
        # Fallback for older versions: compare parts
        a_parts = a.parts
        d_parts = d.parts
        if len(d_parts) <= len(a_parts):
            return False
        return d_parts[:len(a_parts)] == a_parts

def reduce_paths(paths: Iterable[str]) -> List[str]:
    """
    Return a minimal set of paths such that none of the returned paths
    is a descendant of another returned path.
    Paths are normalized (duplicates / trailing slashes removed).
    Stable lexicographic ordering is preserved on normalized paths.
    """
    normalized = sorted({normalize(p) for p in paths})
    kept = []
    for p in normalized:
        # keep p if no existing kept path equals p or is an ancestor of p
        if not any(p == k or is_ancestor(k, p) for k in kept):
            kept.append(p)
    return kept
