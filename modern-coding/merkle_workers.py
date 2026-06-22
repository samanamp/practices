"""Worker for the multiprocessing part of 21_merkle_tree_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""
import hashlib


def hash_block(b):
    """Stable leaf hash of one data block."""
    if isinstance(b, str):
        b = b.encode()
    return hashlib.sha256(b).hexdigest()
