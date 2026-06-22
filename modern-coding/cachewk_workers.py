"""Worker for the multiprocessing part of lru_ttl_cache_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def compute(key):
    """Pretend-expensive (CPU-bound) value computation. Returns (key, value)."""
    acc = 0
    for _ in range(2000):          # stand-in for real CPU work
        acc += 1
    return key, key * key
