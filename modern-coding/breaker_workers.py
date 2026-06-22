"""Worker for the multiprocessing part of 15_circuit_breaker_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled).
Self-contained breaker replay so it needs nothing from the notebook."""


def replay_calls(item):
    """Replay one endpoint's call log through a fresh breaker; return (endpoint, num_rejected).
    item = (endpoint, log, failure_threshold, reset_timeout); log = list of (now, succeeded_bool)."""
    endpoint, log, ft, rt = item
    state, failures, opened_at, rejected = "CLOSED", 0, None, 0
    for now, ok in log:
        allowed = True
        if state == "OPEN":
            if now - opened_at >= rt:
                state, allowed = "HALF_OPEN", True
            else:
                allowed = False
        if not allowed:
            rejected += 1
            continue
        if ok:
            state, failures, opened_at = "CLOSED", 0, None
        elif state == "HALF_OPEN":
            state, opened_at = "OPEN", now
        else:
            failures += 1
            if failures >= ft:
                state, opened_at = "OPEN", now
    return endpoint, rejected
