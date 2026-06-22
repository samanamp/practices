"""Worker for the multiprocessing part of itinerary_reconstruction_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled).
Self-contained Eulerian reconstruction (Hierholzer, lexicographically smallest)."""
from collections import defaultdict


def reconstruct_one(item):
    """Reconstruct one chest. Returns (name, route) or (name, None) if no Eulerian path
    uses every ticket exactly once."""
    name, cards = item
    if not cards:
        return name, []
    graph = defaultdict(list)
    out_deg, in_deg = defaultdict(int), defaultdict(int)
    for s, d in cards:
        graph[s].append(d)
        out_deg[s] += 1
        in_deg[d] += 1
    for s in graph:
        graph[s].sort(reverse=True)          # pop() takes the lexicographically smallest

    vertices = set(out_deg) | set(in_deg)
    starts = [v for v in vertices if out_deg[v] - in_deg[v] == 1]
    ends = [v for v in vertices if in_deg[v] - out_deg[v] == 1]
    if len(starts) > 1 or len(ends) > 1:
        return name, None
    if len(starts) == 1:
        start = starts[0]
    else:
        if ends:
            return name, None
        start = min(v for v in vertices if out_deg[v] > 0)

    local = {k: list(v) for k, v in graph.items()}
    route, stack = [], [start]
    while stack:
        v = stack[-1]
        if local.get(v):
            stack.append(local[v].pop())
        else:
            route.append(stack.pop())
    route.reverse()
    if len(route) - 1 != len(cards):
        return name, None                    # disconnected / degree-impossible
    return name, route
