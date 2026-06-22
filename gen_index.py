#!/usr/bin/env python3
"""Generate _output/index.html (the public landing page) from the notebook folders.

Run AFTER `jupyter lite build`: it overwrites JupyterLite's default root index
with a custom landing page that links to JupyterLite / Binder / Colab and lists
every notebook. Regenerated on every build, so the listing never goes stale.

Links are relative (e.g. `lab/index.html`) so the page works both at
https://samanamp.github.io/practices/ and at a custom domain served from root.
"""
import glob
import html
import json
import os
import re

REPO = "samanamp/practices"
BRANCH = "main"
TEMPLATE = "site/index.template.html"
OUT = "_output/index.html"

# dir, display title, one-line blurb, runtime: "lite" (browser) or "cloud" (Binder/Colab)
TRACKS = [
    ("ml-coding", "ml-coding",
     "NumPy tensor &amp; vectorization drills — masking, broadcasting, numerical stability.", "lite"),
    ("paper-math", "paper-math",
     "Intuition-first math, 30 minutes a day, toward reading ML papers.", "lite"),
    ("modern-coding", "modern-coding",
     "Amazon FAR-style multi-step coding drills that end in real threads &amp; processes.", "cloud"),
]


def notebook_title(path):
    """First markdown heading in the notebook, cleaned of light markdown/LaTeX."""
    try:
        nb = json.load(open(path))
    except Exception:
        nb = {"cells": []}
    md = next((c for c in nb.get("cells", []) if c.get("cell_type") == "markdown"), None)
    src = "".join(md.get("source", [])) if md else ""
    for line in src.splitlines():
        m = re.match(r"\s*#+\s+(.*)", line)
        if m:
            t = re.sub(r"[*`]", "", m.group(1)).strip()
            t = re.sub(r"\$(.*?)\$", r"\1", t)
            return t
    return os.path.splitext(os.path.basename(path))[0].replace("_", " ")


def nb_row(track_dir, runtime, path):
    fname = os.path.basename(path)
    rel = f"{track_dir}/{fname}"
    title = html.escape(notebook_title(path))
    if runtime == "lite":
        links = f'<a class="run" href="lab/index.html?path={rel}">Open &#9656;</a>'
    else:
        binder = f"https://mybinder.org/v2/gh/{REPO}/{BRANCH}?urlpath=lab/tree/{rel}"
        colab = f"https://colab.research.google.com/github/{REPO}/blob/{BRANCH}/{rel}"
        links = (f'<a class="run" href="{binder}">Binder</a>'
                 f'<a class="run" href="{colab}">Colab</a>')
    return (f'<li><span class="nb-name">{title}</span>'
            f'<span class="nb-file">{html.escape(fname)}</span>'
            f'<span class="nb-run">{links}</span></li>')


def track_section(track_dir, title, blurb, runtime):
    paths = sorted(glob.glob(f"{track_dir}/*.ipynb"))
    rows = "\n".join(nb_row(track_dir, runtime, p) for p in paths)
    if runtime == "lite":
        tag = '<span class="tag lite">Runs in JupyterLite</span>'
    else:
        tag = '<span class="tag cloud">Needs real threads &rarr; Binder / Colab</span>'
    return (f'<section class="track">'
            f'<div class="track-head"><h2>{title}</h2>{tag}</div>'
            f'<p class="track-blurb">{blurb}</p>'
            f'<ul class="nb-list">\n{rows}\n</ul>'
            f'<p class="count">{len(paths)} notebooks</p>'
            f'</section>')


FALLBACK_CONFIG = (
    '<script id="jupyter-config-data" type="application/json" '
    'data-jupyter-lite-root=".">{}</script>'
)


def lite_root_config_block():
    """Extract the `jupyter-config-data` <script> from JupyterLite's own root
    index (which we are about to overwrite). JupyterLite's apps fetch this page
    when resolving the lite root, so our landing page must carry the same block
    or `/lab/` etc. fail to launch with a `textContent of null` error.
    """
    try:
        existing = open(OUT).read()
    except FileNotFoundError:
        return FALLBACK_CONFIG
    m = re.search(r'<script[^>]*id="jupyter-config-data".*?</script>', existing, re.S)
    return m.group(0) if m else FALLBACK_CONFIG


def main():
    config_block = lite_root_config_block()  # read before we overwrite OUT
    sections = "\n".join(track_section(*t) for t in TRACKS)
    total = sum(len(glob.glob(f"{t[0]}/*.ipynb")) for t in TRACKS)
    summary = html.escape(f"{total} notebooks across {len(TRACKS)} tracks.")
    page = (open(TEMPLATE).read()
            .replace("<!--JUPYTER_CONFIG-->", config_block)
            .replace("<!--SUMMARY-->", summary)
            .replace("<!--TRACKS-->", sections))
    with open(OUT, "w") as f:
        f.write(page)
    print(f"Wrote {OUT} ({total} notebooks listed); lite-root config "
          f"{'preserved' if config_block != FALLBACK_CONFIG else 'FALLBACK used'}")


if __name__ == "__main__":
    main()
