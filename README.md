# practices — notebooks, runnable in any browser

This repo serves all of the practice notebooks as a [JupyterLite](https://jupyterlite.readthedocs.io)
site: a full Jupyter environment that runs **entirely in the browser** via
WebAssembly (Pyodide). No server, no install — open the URL and run cells.

**`numpy`, `pandas`, and `matplotlib` are preloaded into every kernel** at
startup, so you don't need a `%pip install` cell to use them.

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

## Use it

Once deployed (see below), open the Pages URL. The file browser on the left
shows `ml-coding/`, `paper-math/`, and `modern-coding/`. Double-click any
`.ipynb` and run it. Your edits are saved in the browser's local storage; use
**File → Download** to export a changed notebook back out.

## Build / preview locally

```bash
python -m venv .venv && source .venv/bin/activate   # if you don't already have one
pip install -r requirements.txt
./build.sh                       # writes the static site to _output/
python -m http.server -d _output 8000
# open http://localhost:8000/lab/index.html
```

`build.sh` stages the three notebook folders under a temporary `content/`
directory before building — JupyterLite flattens the *contents* of each folder
it's given, so the wrapper is what preserves the three folder names (and avoids
collisions between the identically-named `dayNN` notebooks in `ml-coding` and
`paper-math`).

## Deploy (GitHub Pages)

`.github/workflows/deploy.yml` builds the site and publishes it on every push to
`main`. After the first push, enable Pages once:

**Repo → Settings → Pages → Build and deployment → Source: GitHub Actions.**

The site URL appears in the workflow's `deploy` job summary.

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
