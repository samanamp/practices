"""Worker for the multiprocessing part of chunked_transfer_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled).
Self-contained: re-derives checksums with zlib so it needs nothing from the notebook."""
import zlib


def verify(item):
    """Verify one file: every chunk\'s CRC and the whole-file checksum. Returns (name, ok)."""
    name, manifest, chunks = item
    for seq, payload, crc in chunks:
        if zlib.crc32(payload) != crc:
            return name, False
    data = b"".join(p for _, p, _ in sorted(chunks))
    ok = len(data) == manifest["length"] and zlib.crc32(data) == manifest["checksum"]
    return name, ok
