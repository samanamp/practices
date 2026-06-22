#!/usr/bin/env bash
# Build the static JupyterLite site into _output/.
#
# The notebooks live in three top-level folders. JupyterLite copies the
# *contents* of each listed directory into the site root, which would flatten
# the three folders together (and collide the duplicate dayNN/README names in
# ml-coding and paper-math). To preserve structure we stage them under a single
# `content/` wrapper and point the build at that.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"

PYTHON="${PYTHON:-python}"

# Also drop the doit cache: it tracks task state, and a stale cache will skip
# re-merging jupyter-lite.json (the package preload config) on a clean rebuild.
rm -rf content _output .jupyterlite.doit.db
mkdir -p content
cp -R modern-coding ml-coding paper-math content/

# Don't ship local Jupyter checkpoint copies into the site.
find content -name '.ipynb_checkpoints' -type d -prune -exec rm -rf {} +

"$PYTHON" -m jupyterlite_core build

# Replace JupyterLite's default root page with our custom landing page
# (CTAs for Lite/Binder/Colab + a generated listing of every notebook).
"$PYTHON" gen_index.py
cp site/favicon.svg _output/favicon.svg

echo "Built site at: $HERE/_output  (open _output/index.html via a local server)"
