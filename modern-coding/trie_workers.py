"""Worker for the multiprocessing part of 25_trie_autocomplete_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def count_words(chunk):
    """Frequency count for a chunk of words (becomes insertion weights for the trie)."""
    counts = {}
    for w in chunk:
        counts[w] = counts.get(w, 0) + 1
    return counts
