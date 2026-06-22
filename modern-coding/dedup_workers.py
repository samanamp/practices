"""Worker for the multiprocessing part of 17_dedup_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def count_distinct(chunk):
    """Number of distinct event ids in a chunk."""
    return len(set(chunk))
