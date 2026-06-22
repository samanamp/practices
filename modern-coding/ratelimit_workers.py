"""Worker for the multiprocessing part of rate_limiter_practice.ipynb.
Must be a real module so spawned processes can import it (notebook-defined
functions can't be pickled under the 'spawn' start method)."""


def replay(item):
    """Replay one key's request log against a fresh token bucket; return (key, allowed)."""
    key, events, capacity, refill = item
    tokens, last, allowed = float(capacity), None, 0
    for now, cost in events:
        if last is None:
            last = now
        elapsed = max(0.0, now - last)
        last = max(last, now)
        tokens = min(capacity, tokens + elapsed * refill)
        if tokens >= cost:
            tokens -= cost
            allowed += 1
    return key, allowed
