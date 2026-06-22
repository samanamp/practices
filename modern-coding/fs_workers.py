"""Worker for the multiprocessing part of 19_filesystem_practice.ipynb.
Real module so spawned processes can import it (notebook functions can\'t be pickled).
A directory node is a dict (name -> child); a file node is the tuple ("file", content)."""


def subtree_size(node):
    """Total bytes (sum of file content lengths) in a subtree."""
    if isinstance(node, tuple) and len(node) == 2 and node[0] == "file":
        return len(node[1])
    if isinstance(node, dict):
        return sum(subtree_size(v) for v in node.values())
    return 0
