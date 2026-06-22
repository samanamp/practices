"""Worker for the multiprocessing part of 13_ledger_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def replay_shard(item):
    """Replay one shard's transfer log to final balances. item = (initial_balances, txns);
    each txn is (src, dst, amount). Overdrafting transfers are skipped."""
    initial, txns = item
    bal = dict(initial)
    for src, dst, amt in txns:
        if bal[src] >= amt:
            bal[src] -= amt
            bal[dst] += amt
    return bal
