# Conventions for generating coding-interview practice problems

This folder holds practice for **Amazon FAR**-style first-round interviews: multi-step problems
where the interviewer keeps adding constraints, almost always ending in concurrency/parallelism.
When the user asks for "another problem" / "more questions," follow this spec exactly.

## Structure (per problem = one Jupyter notebook)

Five parts, mirroring `morse_code_practice.ipynb`:

- **Part 1–3 (core):** a single domain built up incrementally. Each part reuses the previous
  part's code without rewriting it. Part 3 introduces concurrency (threaded producer/consumer
  over a bounded `queue.Queue`, sentinel-based shutdown).
- **Part 4 (stretch):** harder correctness/edge-case variant. Favor an **incremental / streaming**
  reformulation and a recurring **noise- or error-tolerance** theme (threshold classification,
  malformed input, partial data, clock/jitter drift). The user specifically likes this theme.
- **Part 5 (stretch):** **scale & parallelism** — multiplexing, thread pools, and a CPU-bound
  `concurrent.futures.ProcessPoolExecutor` step.

## Hard requirements

- **Language: Python.**
- **Difficulty:** a notch above a fair first-round (medium-plus). The user prefers to over-prepare.
- **Drill all four axes** across the parts: incremental design, edge cases & correctness,
  performance & scale, concurrency depth.
- Each part has: a markdown cell (spec + "say-this-out-loud" assumptions + discussion bullets the
  interviewer is fishing for), a **stub** cell (`raise NotImplementedError`), and a **test** cell.
- Provide collapsed **`ref_`-prefixed reference solutions** at the bottom that actually pass.
- **Multiprocessing workers must live in a real `.py` module** next to the notebook (spawned
  processes can't pickle functions defined in a notebook). Document why in the module docstring.
- **Validate before handing off:** run the reference solutions (the `ProcessPoolExecutor` path
  must be run from a file/module dir, not piped stdin) and confirm every part's tests pass.

## Process

- Pick a **fresh domain** each time (e.g. rate limiter, log aggregator, LRU/TTL cache, chunked
  file transfer, in-memory pub/sub, tokenizer/parser) — keep the multi-step + concurrency shape.
- Confirm the domain with the user before writing a whole notebook if it's ambiguous.
- **Naming:** notebooks are numbered `NN_<domain>_practice.ipynb` in suggested order; a new problem
  takes the next number (currently up to `30_`, so next is `31_`). The worker module stays
  **unprefixed** as `<domain>_workers.py` (a module name can't start with a digit), and the notebook
  imports it by that bare name.
- Update this folder's `README.md` problem table when a new notebook is added.
