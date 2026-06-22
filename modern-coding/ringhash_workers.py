"""Worker for the multiprocessing part of 16_consistent_hashing_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled).
Uses a STABLE hash (hashlib) so placement matches across processes."""
import bisect
import hashlib


def _h(s):
    return int(hashlib.md5(str(s).encode()).hexdigest()[:8], 16)


def assign_chunk(item):
    """Assign a chunk of keys to ring nodes. item = (keys, ring); ring is sorted [(hash, node)]."""
    keys, ring = item
    ks = [h for h, _ in ring]
    out = {}
    for key in keys:
        i = bisect.bisect(ks, _h(key)) % len(ring)
        out[key] = ring[i][1]
    return out
