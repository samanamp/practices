"""Worker for the multiprocessing part of 28_lfu_cache_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""
from collections import defaultdict, OrderedDict


def simulate(item):
    """Replay an access trace through an LFU cache of the given capacity; return the hit count.
    On a miss the key is inserted with value=key. item = (capacity, accesses)."""
    capacity, accesses = item
    key_val, key_freq, freq_keys, min_freq, hits = {}, {}, defaultdict(OrderedDict), 0, 0

    def touch(key):
        nonlocal min_freq
        f = key_freq[key]
        del freq_keys[f][key]
        if not freq_keys[f]:
            del freq_keys[f]
            if min_freq == f:
                min_freq = f + 1
        key_freq[key] = f + 1
        freq_keys[f + 1][key] = None

    for key in accesses:
        if key in key_val:
            hits += 1
            touch(key)
        elif capacity > 0:
            if len(key_val) >= capacity:
                ek, _ = freq_keys[min_freq].popitem(last=False)
                del key_val[ek]
                del key_freq[ek]
            key_val[key] = key
            key_freq[key] = 1
            freq_keys[1][key] = None
            min_freq = 1
    return hits
