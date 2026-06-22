"""Worker for the multiprocessing part of 14_pipeline_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def heavy_stage(x):
    """A deterministic CPU-bound pipeline stage."""
    return sum(i * i for i in range(x))
