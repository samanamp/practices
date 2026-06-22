"""Worker for the multiprocessing part of 10_connection_pool_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def expensive_handshake(key):
    """A deterministic CPU-bound 'connection handshake' for a key."""
    return sum(i * i for i in range(key))
