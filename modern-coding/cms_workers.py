"""Worker for the multiprocessing part of 30_count_min_sketch_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled).
Uses a STABLE hash (hashlib) so cells match across processes."""
import hashlib


def _h(item, r, w):
    return int(hashlib.md5(("%d:%s" % (r, item)).encode()).hexdigest(), 16) % w


def build_table(item):
    """Build one chunk's CMS table. item = (chunk, width, depth). Returns the table (list of rows)."""
    chunk, width, depth = item
    table = [[0] * width for _ in range(depth)]
    for x in chunk:
        for r in range(depth):
            table[r][_h(x, r, width)] += 1
    return table
