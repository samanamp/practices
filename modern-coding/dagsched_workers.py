"""Worker for the multiprocessing part of 12_dag_scheduler_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def node_cost(n):
    """A deterministic CPU-bound 'cost' for a node."""
    return sum(i * i for i in range(n))
