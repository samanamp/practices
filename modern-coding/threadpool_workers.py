"""Worker for the multiprocessing part of 09_threadpool_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def cpu_task(n):
    """A deterministic CPU-bound job: sum of squares below n."""
    return sum(i * i for i in range(n))
