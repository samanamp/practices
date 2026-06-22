"""Worker for the multiprocessing part of 22_crdt_counter_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def merge_states(states):
    """Merge a chunk of G-Counter states: per-replica maximum. Returns a plain dict."""
    out = {}
    for s in states:
        for k, v in s.items():
            out[k] = max(out.get(k, 0), v)
    return out
