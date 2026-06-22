"""Worker for the multiprocessing part of 23_order_book_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""
from collections import deque, defaultdict


def replay_orders(item):
    """Replay one symbol's order log through a fresh book; return (symbol, total_traded_volume).
    Each order is ("limit", side, price, qty, oid) or ("market", side, qty)."""
    symbol, orders = item
    bids, asks, traded = defaultdict(deque), defaultdict(deque), 0
    for o in orders:
        if o[0] == "limit":
            _, side, price, qty, oid = o
            (bids if side == "buy" else asks)[price].append((oid, qty))
        else:
            _, side, qty = o
            levels = asks if side == "buy" else bids
            pick = min if side == "buy" else max
            rem = qty
            while rem > 0:
                prices = [p for p, d in levels.items() if d]
                if not prices:
                    break
                best = pick(prices)
                q = levels[best]
                while rem > 0 and q:
                    oid, oqty = q[0]
                    take = min(rem, oqty)
                    traded += take
                    rem -= take
                    if take == oqty:
                        q.popleft()
                    else:
                        q[0] = (oid, oqty - take)
                if not q:
                    del levels[best]
    return symbol, traded
