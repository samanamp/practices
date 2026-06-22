"""Worker for the multiprocessing part of 29_two_phase_commit_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def decide(votes):
    """Coordinator decision for one transaction given participant votes: commit iff all yes."""
    return "commit" if all(votes) else "abort"
