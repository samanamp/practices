# Conventions for generating ML / tensor-programming practice (day-based)

This folder holds practice for **tensor-programming interviews** (CoderPad-style ML coding rounds).
The real interview hands you the **hard vectorized** problem — nobody asks for a scalar/loop version.
So **do not write scalar versions**. Every question goes straight to vectorized NumPy.

## Structure: one notebook = one ~1-hour practice day

`dayNN_practice.ipynb`. Each day contains a small set of questions, escalating:

- **1 warmup** — quick to get going, but still vectorized and real (no toy/scalar stuff).
- **~2 medium** and **~2 hard** (as many as the day needs; ~5 total is a good 1-hour load).
- **≥1 "pure tensor-manipulation trick"** per day — stride tricks, einsum contractions, fancy
  indexing, broadcasting gymnastics, scatter/gather. **Make it genuinely hard**, not a one-liner.

## Every question must be grounded in reality or a paper

- Prefer problems that show up in real systems (retrieval, attention, normalization, conv, NMS,
  recommender scoring, RL advantages, beam search, mixture-of-experts routing, etc.).
- **If it's from a paper, cite it** (authors, title, year, arXiv id) and add a sentence on **why it
  matters / what's important about it**. Put this in the question's markdown cell.

## Hard requirements

- **NumPy** (`import numpy as np`). Solutions are vectorized: **no Python loops over elements.**
  (Loops are fine *inside test cells* as an obviously-correct oracle to validate the vectorized
  solution against — that's how we replace the scalar version.)
- **Difficulty:** medium-plus to hard; the user prefers to over-prepare and finds vectorized hard.
- **Pair forward with backward.** Whenever a question implements a forward pass (a layer, op, or
  loss), include or immediately follow it with the **backward pass** (gradients / VJP) where it's
  instructive — backward is usually the harder, more interview-relevant half. Validate gradients with
  a **finite-difference numerical check** in the test cell (that's the gradient analogue of the
  loop-oracle). Some questions are backward-only (derive `dQ/dK/dV`, BatchNorm backward, STE, etc.).
- Each question = a markdown cell (real/paper context + reference + why it matters + spec + shapes +
  "no loops" reminder), a **stub** cell (`raise NotImplementedError`), and a **test** cell.
- Collapsed **`ref_`-prefixed reference solutions** at the bottom that actually pass.
- Tests are **deterministic** (`np.random.default_rng(<int>)`), use `np.allclose` + explicit expected
  values + at least one property/invariant check (shapes, sums-to-1, masked==0, equivariance, a
  loop-oracle, a numerically-extreme case).
- **Validate before handing off:** run every question's test against the references and confirm they
  pass (a build-and-validate script is the easy way; delete it afterward).

## Process

- Each day picks a coherent theme. The **curriculum, themes, and what's left to cover live in
  `INDEX.md`** — pick the next day from there, then update `INDEX.md` (mark done) and `README.md`.
- Active themes: **Attention** (multi-day), **MLP / MoE** (multi-day), **Quantization** (multi-day),
  plus cross-cutting **backward-pass / autodiff** woven through all of them. Don't repeat a problem
  already covered.
- Tag each question `[warmup] / [medium] / [hard]` and mark the tensor-trick one.
- Update `README.md` when a new day is added.

## Environment

NumPy required (`python3 -m pip install numpy`; numpy 2.4.6 installed in /opt/miniconda3 on
2026-06-18). No multiprocessing in this track.
