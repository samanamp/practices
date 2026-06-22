"""Worker for the multiprocessing part of 20_bloom_filter_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled).
Uses a STABLE hash (hashlib) so bit positions match across processes."""
import hashlib


def _hashes(item, k, size):
    return [int(hashlib.md5(("%d:%s" % (i, item)).encode()).hexdigest(), 16) % size for i in range(k)]


def build_bits(item):
    """Return the set of bit positions for a chunk of items. item = (chunk, k, size)."""
    chunk, k, size = item
    bits = set()
    for x in chunk:
        bits.update(_hashes(x, k, size))
    return bits
