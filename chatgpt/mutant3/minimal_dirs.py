from pathlib import PurePosixPath
from typing import Iterable, Set, List

def _lexical_normalize(path: str) -> str:
    """Purely lexical normalization of path segments: collapse '.' and '..',
    preserve absolute vs relative. Does not consult the filesystem.
    Returns a normalized POSIX-style path string.
    """
    p = PurePosixPath(path)
    is_abs = p.is_absolute()
    segs = list(p.parts)
    if is_abs:
        segs = segs[1:]  # drop leading root indicator '/'
    parts: List[str] = []
    for part in segs:
        if part == '.':
            continue
        if part == '..':
            if parts and parts[-1] != '..':
                parts.pop()
            else:
                parts.append('..')
        else:
            parts.append(part)
    if not parts:
        return '/' if is_abs else '.'
    norm = '/'.join(parts)
    if is_abs:
        norm = '/' + norm
    return norm

def minimal_dirs(paths: Iterable[str]) -> Set[str]:
    """Return the minimal set (as a set of strings) of directories from `paths`
    such that every input path is either in the returned set or a descendant
    of some returned path.

    Behavior and design choices:
    - Purely lexical, no filesystem access.
    - POSIX-style semantics via pathlib.PurePosixPath.
    - Normalizes '.' and '..' lexically.
    - Preserves absolute vs relative semantics; '/A' is distinct from 'A'.
    - Output is a set (order not guaranteed). Duplicates are removed.
    """
    normalized = [_lexical_normalize(p) for p in paths]
    # ensure parents are considered before children: sort by part-count
    normalized.sort(key=lambda p: len(PurePosixPath(p).parts))
    kept: List[str] = []
    for p in normalized:
        p_parts = PurePosixPath(p).parts
        # If any already-kept path is a prefix (by path parts) of p, p is covered.
        if not any(PurePosixPath(k).parts == p_parts[:len(PurePosixPath(k).parts)] for k in kept):
            kept.append(p)
    return set(kept)
