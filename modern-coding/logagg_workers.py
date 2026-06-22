"""Worker for the multiprocessing part of log_aggregator_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""

_LEVELS = ("DEBUG", "INFO", "WARN", "ERROR")


def count_file(item):
    """Map step: one file (list of raw lines) -> (level_counts, time_bucket_counts).
    Malformed lines are skipped. Returns plain dicts (picklable)."""
    lines, bucket = item
    levels, buckets = {}, {}
    for ln in lines:
        parts = ln.split(" ", 2)
        if len(parts) < 3:
            continue
        ts_s, level, _msg = parts
        if not ts_s.lstrip("-").isdigit() or level not in _LEVELS:
            continue
        ts = int(ts_s)
        levels[level] = levels.get(level, 0) + 1
        b = (ts // bucket) * bucket
        buckets[b] = buckets.get(b, 0) + 1
    return levels, buckets
