"""Worker for the multiprocessing part of pubsub_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def count_topics(chunk):
    """Count messages per topic in a chunk of a message log. Returns a plain dict."""
    counts = {}
    for topic in chunk:
        counts[topic] = counts.get(topic, 0) + 1
    return counts
