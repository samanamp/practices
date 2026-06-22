"""Worker for the multiprocessing part of 26_reservoir_sampling_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""
import random


def sample_chunk(item):
    """Reservoir-sample one chunk (Algorithm R). item = (chunk, k, seed).
    Returns (reservoir, chunk_length)."""
    chunk, k, seed = item
    rng = random.Random(seed)
    res = []
    for i, x in enumerate(chunk):
        if i < k:
            res.append(x)
        else:
            j = rng.randint(0, i)
            if j < k:
                res[j] = x
    return res, len(chunk)
