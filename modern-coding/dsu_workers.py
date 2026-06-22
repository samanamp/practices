"""Worker for the multiprocessing part of 27_union_find_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def spanning_forest(item):
    """Reduce one chunk of edges to a spanning forest (the edges that actually merged components).
    item = (n, edges). Returns the kept edges."""
    n, edges = item
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    keep = []
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            keep.append((a, b))
    return keep
