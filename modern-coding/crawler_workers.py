"""Worker for the multiprocessing part of crawler_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled)."""


def parse_page(item):
    """Parse one page: normalize/dedupe its outlinks (stand-in for CPU-bound HTML parsing).
    item = (url, raw_links). Returns (url, clean_links)."""
    url, raw = item
    seen, out = set(), []
    for link in raw:
        if link == url or link in seen:
            continue
        seen.add(link)
        out.append(link)
    return url, out
