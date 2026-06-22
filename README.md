# practices — notebooks, runnable in any browser

This repo serves all of the practice notebooks as a [JupyterLite](https://jupyterlite.readthedocs.io)
site: a full Jupyter environment that runs **entirely in the browser** via
WebAssembly (Pyodide). No server, no install — open the URL and run cells.

**`numpy`, `pandas`, and `matplotlib` are preloaded into every kernel** at
startup, so you don't need a `%pip install` cell to use them.

## Run it

Everything runs in the cloud — no local install. Pick by track:

### `ml-coding` + `paper-math` → JupyterLite (in-browser)

**▶️ https://samanamp.github.io/practices/lab/index.html**

Runs entirely in the browser via WebAssembly (Pyodide) — no server, no install,
works on a phone or a borrowed laptop. `numpy`, `pandas`, and `matplotlib` are
preloaded into every kernel. The file browser on the left shows all three
folders; double-click any `.ipynb` and run it. Edits are saved in the browser's
local storage — use **File → Download** to export a changed notebook back out.

### `modern-coding` → Binder / Colab (real threads)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/samanamp/practices/main?urlpath=lab/tree/modern-coding)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samanamp/practices)

These drills use real threads (`ThreadPoolExecutor`) and processes
(`ProcessPoolExecutor`), which the browser-only Pyodide runtime can't provide.

- **Binder** (recommended): clones the whole repo, so threads, processes, **and**
  the sibling `*_workers.py` imports all work with zero setup. First launch builds
  the image (~1–3 min); later launches are fast.
- **Colab**: opens only the single notebook, so the `*_workers.py` modules and
  `ProcessPoolExecutor` steps won't work until you pull the repo. Run this once in
  a cell at the top:
  ```python
  !git clone https://github.com/samanamp/practices && cp practices/modern-coding/*_workers.py .
  ```

## Contents

| Folder | What | Where to run it |
| --- | --- | --- |
| `ml-coding/` | NumPy tensor / vectorization drills | ✅ This JupyterLite site |
| `paper-math/` | Intuition-first math notebooks | ✅ This JupyterLite site |
| `modern-coding/` | Concurrency / systems coding drills | ▶️ [Binder / Colab](modern-coding/README.md) — needs real threads |

`modern-coding` uses `ThreadPoolExecutor`/`ProcessPoolExecutor`, which the
browser-only Pyodide runtime can't provide (no OS threads). Run that track on
**Binder** (recommended — clones the repo so threads, processes, and the sibling
`*_workers.py` imports all work) via the badge in
[`modern-coding/README.md`](modern-coding/README.md). The other two tracks are a
perfect fit for JupyterLite and run right here in the browser.

## Build / preview locally

```bash
python -m venv .venv && source .venv/bin/activate   # if you don't already have one
pip install -r requirements.txt
./build.sh                       # writes the static site to _output/
python -m http.server -d _output 8000
# open http://localhost:8000/  (custom landing page; JupyterLite itself is at /lab/)
```

`build.sh` does two notable things:

- **Stages** the three notebook folders under a temporary `content/` directory
  before building — JupyterLite flattens the *contents* of each folder it's
  given, so the wrapper preserves the three folder names (and avoids collisions
  between the identically-named `dayNN` notebooks in `ml-coding` and
  `paper-math`).
- Runs **`gen_index.py`** after the build to replace JupyterLite's default root
  page with `site/index.template.html` — the custom landing page with
  Lite/Binder/Colab buttons and a listing of every notebook, generated from the
  folders so it never goes stale. Edit the look in the template; the per-notebook
  rows are generated.

## Deploy (GitHub Pages)

`.github/workflows/deploy.yml` builds the site and publishes it on every push to
`main`. After the first push, enable Pages once:

**Repo → Settings → Pages → Build and deployment → Source: GitHub Actions.**

The site URL appears in the workflow's `deploy` job summary.

**Custom domain (CNAME):** with Actions-based Pages, set the domain under
**Settings → Pages → Custom domain** and add the DNS record at your registrar —
it persists across deploys (no `CNAME` file in the artifact needed). The landing
page and all in-app links are relative, so the site works unchanged whether
it's served from `…github.io/practices/` or the root of your own domain.

## Caveats (the Pyodide runtime is not full CPython)

- **`modern-coding/` doesn't run here — use Binder.** Pyodide has no real OS
  threads, so `ThreadPoolExecutor`/`ProcessPoolExecutor` exercises can't work in
  the browser. That track runs on Binder instead; see
  [`modern-coding/README.md`](modern-coding/README.md). The `ml-coding` and
  `paper-math` tracks run fine right here.
- **Packages must have a Pyodide/WASM build.** numpy/pandas/matplotlib/scipy/
  scikit-learn all do. Anything needing native threads or a GPU (PyTorch,
  TensorFlow) does not — use Colab for those.

The original folders remain plain notebooks you can still open in local Jupyter
(`run-jupyter.sh`); this setup is purely additive.
