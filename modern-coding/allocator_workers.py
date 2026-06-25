"""Self-contained memory-allocator worker for the multiprocessing part of the notebook.

Why a separate module? `ProcessPoolExecutor` on macOS/Windows uses the *spawn*
start method: each worker re-imports the target by module path. Functions and
classes defined inside a Jupyter notebook live in an interactive ``__main__``
that workers cannot import, so they fail to unpickle. Putting the worker in a
real .py file fixes that. Keep it dependency-free and picklable.

The `Allocator` here is a standalone copy of the reference allocator (first-fit
or best-fit free list with coalescing) so each spawned process can run a full
fragmentation simulation without touching the notebook.
"""
import random


class Allocator:
    """Fixed-capacity allocator over the address range [0, capacity).

    Free space is a list of (offset, size) blocks kept sorted by offset and
    coalesced, so adjacent holes always merge. `allocated` maps a base address
    to its size, which is what `free` needs to return a block to the pool.
    """

    def __init__(self, capacity, policy="first"):
        if capacity < 0:
            raise ValueError("capacity must be >= 0")
        self.capacity = capacity
        self.policy = policy  # "first" or "best"
        self.free_list = [(0, capacity)] if capacity > 0 else []
        self.allocated = {}  # base address -> size

    def _find(self, size, align):
        """Return (index, aligned_start, pad) of a usable free block, or None."""
        best = None
        for i, (off, sz) in enumerate(self.free_list):
            astart = (off + align - 1) // align * align
            pad = astart - off
            if pad + size <= sz:
                if self.policy == "first":
                    return (i, astart, pad)
                waste = sz - (pad + size)
                if best is None or waste < best[0]:
                    best = (waste, i, astart, pad)
        if best is None:
            return None
        _, i, astart, pad = best
        return (i, astart, pad)

    def malloc(self, size, align=1):
        if not isinstance(size, int) or size <= 0 or size > self.capacity:
            return None
        if not isinstance(align, int) or align < 1 or (align & (align - 1)) != 0:
            return None
        found = self._find(size, align)
        if found is None:
            return None
        i, astart, pad = found
        off, sz = self.free_list[i]
        leftovers = []
        if pad > 0:  # alignment gap before the allocation
            leftovers.append((off, pad))
        tail_off = astart + size
        tail_sz = (off + sz) - tail_off
        if tail_sz > 0:  # remainder after the allocation
            leftovers.append((tail_off, tail_sz))
        self.free_list[i:i + 1] = leftovers
        self.allocated[astart] = size
        return astart

    def free(self, address):
        if address not in self.allocated:
            raise KeyError("free of unallocated address: %r" % (address,))
        size = self.allocated.pop(address)
        self._insert_free(address, size)

    def _insert_free(self, off, size):
        lo, hi = 0, len(self.free_list)
        while lo < hi:  # binary search for sorted insertion point
            mid = (lo + hi) // 2
            if self.free_list[mid][0] < off:
                lo = mid + 1
            else:
                hi = mid
        self.free_list.insert(lo, (off, size))
        # coalesce with the right neighbour, then the left
        i = lo
        while i + 1 < len(self.free_list) and \
                self.free_list[i][0] + self.free_list[i][1] == self.free_list[i + 1][0]:
            o, s = self.free_list[i]
            _, s2 = self.free_list[i + 1]
            self.free_list[i:i + 2] = [(o, s + s2)]
        while i > 0 and \
                self.free_list[i - 1][0] + self.free_list[i - 1][1] == self.free_list[i][0]:
            o, s = self.free_list[i - 1]
            _, s2 = self.free_list[i]
            self.free_list[i - 1:i + 1] = [(o, s + s2)]
            i -= 1

    def stats(self):
        sizes = [s for _, s in self.free_list]
        free = sum(sizes)
        return {
            "capacity": self.capacity,
            "free": free,
            "used": self.capacity - free,
            "largest_free": max(sizes) if sizes else 0,
            "num_free_blocks": len(sizes),
        }


def simulate(params):
    """Replay a random malloc/free workload against a fresh allocator.

    CPU-bound: many ops over many seeds. Deterministic per seed, so the same
    params always produce the same metrics — that is what lets the notebook
    assert the parallel run matches the serial run.

    params: (seed, capacity, n_ops, max_alloc, free_prob)
    returns: dict of metrics.
    """
    seed, capacity, n_ops, max_alloc, free_prob = params
    rng = random.Random(seed)
    a = Allocator(capacity, policy="best")
    live = []  # currently-allocated base addresses
    used = 0
    ok = fail = 0
    peak = 0
    for _ in range(n_ops):
        if live and rng.random() < free_prob:
            addr = live.pop(rng.randrange(len(live)))
            used -= a.allocated[addr]
            a.free(addr)
        else:
            size = rng.randint(1, max_alloc)
            addr = a.malloc(size)
            if addr is None:
                fail += 1
            else:
                live.append(addr)
                used += size
                ok += 1
                peak = max(peak, used)
    st = a.stats()
    return {
        "seed": seed,
        "alloc_ok": ok,
        "alloc_fail": fail,
        "peak_used": peak,
        "largest_free": st["largest_free"],
        "free": st["free"],
    }
