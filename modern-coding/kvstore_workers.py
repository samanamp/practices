"""Worker for the multiprocessing part of 11_kvstore_wal_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def compact_log(log):
    """Reduce one shard's write-ahead log to its final {key: value} state."""
    d = {}
    for entry in log:
        if entry[0] == "put":
            d[entry[1]] = entry[2]
        elif entry[0] == "delete":
            d.pop(entry[1], None)
    return d
