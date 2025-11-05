from typing import Iterable, List
from pathlib import PurePosixPath

def _normalize(p: str) -> str:
    """
    Normalize path string:
    - Convert backslashes to forward slashes (accept Windows-style input).
    - Remove '.' components and redundant separators via PurePosixPath.
    - Return normalized posix string; return '' for '.' (current dir).
    """
    p = p.replace("\\", "/")
    pp = PurePosixPath(p)
    s = pp.as_posix()
    if s == ".":
        return ""
    return s

def _is_ancestor(ancestor: str, descendant: str) -> bool:
    """
    Return True if 'ancestor' path string is equal to or a parent directory of 'descendant'.
    Both strings are POSIX-normalized already (or will be passed through PurePosixPath).
    """
    if ancestor == descendant:
        return True
    if ancestor == "":
        # treat empty string as current dir that contains everything
        return True
    a_parts = PurePosixPath(ancestor).parts
    d_parts = PurePosixPath(descendant).parts
    if len(a_parts) > len(d_parts):
        return False
    return tuple(a_parts) == tuple(d_parts[:len(a_parts)])

def minimal_dirs(paths: Iterable[str]) -> List[str]:
    """
    Return the minimal subset of the input paths that cover all the input paths.

    Behavior:
    - Normalizes input paths (remove redundant separators and '.' and handle '..').
    - Accepts both forward- and backslash separators in input.
    - Removes duplicates.
    - Deterministic output: sorted by path depth (shallow first) and then lexicographically.
    """
    normalized = { _normalize(p) for p in paths }
    # Sort by number of parts (shallow first), then lexicographically for determinism.
    def comp_key(p: str):
        parts = PurePosixPath(p).parts
        return (len(parts), p)
    candidates = sorted(normalized, key=comp_key)
    survivors = []
    for p in candidates:
        if any(_is_ancestor(s, p) for s in survivors):
            continue
        survivors.append(p)
    return survivors
