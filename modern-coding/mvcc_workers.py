"""Worker for the multiprocessing part of 24_mvcc_store_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def answer_queries(item):
    """Answer point-in-time reads. item = (histories, queries); histories: key -> [(ver, val)] asc;
    queries: list of (key, version). Returns list of (key, version, value-as-of)."""
    histories, queries = item
    out = []
    for key, version in queries:
        val = None
        for ver, v in histories.get(key, []):
            if ver <= version:
                val = v
            else:
                break
        out.append((key, version, val))
    return out
