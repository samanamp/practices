"""Worker for the multiprocessing part of 18_heavy_hitters_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def count_chunk(chunk):
    """Frequency count of one chunk of items. Returns a plain dict."""
    counts = {}
    for x in chunk:
        counts[x] = counts.get(x, 0) + 1
    return counts
