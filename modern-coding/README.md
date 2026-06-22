# Modern Coding Practice

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/samanamp/practices/main?urlpath=lab/tree/modern-coding)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samanamp/practices)

> **Run these in the cloud — not on the JupyterLite site.** These drills use real
> threads (`ThreadPoolExecutor`) and processes (`ProcessPoolExecutor`), which the
> browser-only JupyterLite (Pyodide) runtime can't provide. Use the buttons above:
>
> - **Binder** (recommended): clones the whole repo, so threads, processes, **and**
>   the sibling `*_workers.py` imports all work with zero setup. First launch builds
>   the image (~1–3 min); later launches are fast.
> - **Colab**: opens only the single notebook, so the `*_workers.py` modules and
>   `ProcessPoolExecutor` steps won't work until you pull the repo. Run this once in
>   a cell at the top:
>   ```python
>   !git clone https://github.com/samanamp/practices && cp practices/modern-coding/*_workers.py .
>   ```

Practice for **Amazon FAR**-style first-round coding interviews: one problem domain that the
interviewer keeps piling constraints onto, almost always ending in a concurrency/parallelism
component. The goal is to rehearse *building a solution that survives added constraints* — not
to memorize one algorithm.

## How these interviews run

You're given a small problem. Once it works, the interviewer adds a twist, then another. They're
watching whether you:

1. Pin down ambiguity **before** coding (inputs, error cases, scale).
2. Pick data structures that won't need to be ripped out at the next step.
3. Keep the code testable as it grows.
4. Reason about concurrency correctly (threads vs processes, backpressure, shutdown, ordering).

## Problems

| Notebook | Domain | Arc (Parts 1→5) |
|---|---|---|
| `01_morse_code_practice.ipynb` | Morse encode/decode → timed signal | encode/decode → on/off signal → threaded link → streaming noise-tolerant decode → multiplexed bus + multiprocessing |
| `02_rate_limiter_practice.ipynb` | Request rate limiting | token bucket → sliding window → thread-safe shared limiter → clock-skew/bad-input robustness → per-key sharding + parallel replay |
| `03_log_aggregator_practice.ipynb` | Log ingestion & aggregation | parse line → k-way merge → concurrent multi-source ingest → out-of-order/late/malformed tolerance → parallel map-reduce |
| `04_lru_ttl_cache_practice.ipynb` | Caching | LRU → TTL expiry → thread-safe access → cache-stampede / single-flight → sharded cache + parallel warmup |
| `05_chunked_transfer_practice.ipynb` | Chunked file transfer | split/reassemble → checksums + manifest → concurrent send/recv → unreliable channel (drop/reorder/dup/corrupt) → parallel multi-file verify |
| `06_itinerary_reconstruction_practice.ipynb` | Boarding-pass itinerary | reconstruct chain → uniqueness check → concurrent multi-chest ingest → Eulerian reconstruction (repeated tickets) → reconstruct many chests in parallel |
| `07_pubsub_practice.ipynb` | Pub/sub broker | topic fan-out → wildcard matching → concurrent broker (queues) → at-least-once ack/redeliver/dedup → sharded broker + parallel aggregation |
| `08_crawler_practice.ipynb` | Concurrent web crawler | extract links → BFS crawl → concurrent crawl (frontier + termination) → robust crawl (dead links/depth) → parallel fetch/parse |
| `09_threadpool_practice.ipynb` | Parallel task runner | Future → sequential runner → worker-pool parallel runner → retries/fail-fast → process pool |
| `10_connection_pool_practice.ipynb` | Connection pool | basic pool → validate-on-acquire → thread-safe blocking pool → timeouts/eviction/double-release → sharded pools + parallel warmup |
| `11_kvstore_wal_practice.ipynb` | KV store + write-ahead log | get/put/delete → replay log → thread-safe store (atomic incr) → crash recovery (torn log) → sharded store + parallel compaction |
| `12_dag_scheduler_practice.ipynb` | DAG task scheduler | ready tasks → topological order → concurrent execution (deps + termination) → failure propagation → parallel cost precompute |
| `13_ledger_practice.ipynb` | Account ledger | transfers → replay log → concurrent transfers (deadlock-free lock ordering) → idempotent atomic batches → sharded ledger + parallel replay |
| `14_pipeline_practice.ipynb` | Streaming pipeline | one stage → compose stages → concurrent pipeline (bounded queues/backpressure) → error routing → parallel CPU stage |
| `15_circuit_breaker_practice.ipynb` | Retry + circuit breaker | retry/backoff → breaker state machine → thread-safe breaker → guarded calls → per-endpoint registry + parallel replay |
| `16_consistent_hashing_practice.ipynb` | Consistent hashing ring | build ring + lookup → minimal-movement rebalance → thread-safe ring → replication → parallel assignment |
| `17_dedup_practice.ipynb` | Exactly-once / dedup | basic deduper → TTL deduper → thread-safe (exactly-once) → bounded-memory LRU deduper → sharded parallel distinct count |
| `18_heavy_hitters_practice.ipynb` | Top-K heavy hitters | count → top-k → concurrent counter → Misra–Gries approximate → parallel map-reduce top-k |
| `19_filesystem_practice.ipynb` | In-memory filesystem | core ops → recursive rm/find → thread-safe FS → atomic move + errors → parallel disk-usage |
| `20_bloom_filter_practice.ipynb` | Bloom filter | add/contains → optimal sizing → thread-safe → counting (deletable) → parallel build + union |
| `21_merkle_tree_practice.ipynb` | Merkle tree | root → full tree + diff → concurrent leaf hashing → inclusion proofs → parallel leaf hashing |
| `22_crdt_counter_practice.ipynb` | CRDT G-Counter | counter → merge (per-replica max) → concurrent increments → merge many replicas → parallel merge-reduce |
| `23_order_book_practice.ipynb` | Order book / matching | resting book → price-time matching → thread-safe book → cancel + validation → parallel per-symbol replay |
| `24_mvcc_store_practice.ipynb` | MVCC versioned store | versioned reads → snapshot view → concurrent MVCC → tombstone delete + GC → parallel point-in-time reads |
| `25_trie_autocomplete_practice.ipynb` | Trie autocomplete | trie → top-k autocomplete → thread-safe trie → deletion → parallel frequency precompute |
| `26_reservoir_sampling_practice.ipynb` | Reservoir sampling | Algorithm R → streaming reservoir → thread-safe → merge partitions → parallel sampling |
| `27_union_find_practice.ipynb` | Union-Find (DSU) | find/union → components → thread-safe (RLock) → redundant-edge detect → parallel connectivity |
| `28_lfu_cache_practice.ipynb` | LFU cache | LFU + LRU tie-break → compute-on-miss → thread-safe → frequency aging → parallel hit-rate sim |
| `29_two_phase_commit_practice.ipynb` | Two-phase commit | coordinator/vote → recovery (in-doubt) → concurrent txns → failure handling → parallel decision replay |
| `30_count_min_sketch_practice.ipynb` | Count-Min Sketch | add/estimate → sizing/error bound → thread-safe → merge (union) → parallel build |

Notebooks are numbered in suggested order; new problems continue the sequence (`09_…`). Worker
modules stay **unprefixed** — a Python module name can't start with a digit — and keep their
`<domain>_workers.py` name (the notebooks `import` them by that name).

Each notebook is **5 parts**: a 3-part incremental core (concurrency arrives at Part 3) plus **2
stretch parts** that push harder — Part 4 on error/noise tolerance, Part 5 on scale + multiprocessing.

## Suggested order

Treat each part as a fresh 10–15 min round:

1. Read the part's markdown and say the spec/assumptions out loud (as you would to an interviewer).
2. Fill in the stubs.
3. Run the part's test cell until it's green.
4. Only then reveal the collapsed `ref_`-prefixed reference cells at the bottom to compare.
5. Read the "discussion" bullets — those are the points the interviewer is fishing for.

Don't peek at the reference solutions early; the value is in the struggle.

## How new problems are generated

The conventions for generating more problems live in **`CLAUDE.md`** (auto-loaded by any Claude
Code session/agent working in this folder). In short: Python, difficulty a notch above a fair
first-round, same 3-core-parts + 2-stretch structure, runnable tests + passing reference solutions,
and a recurring **noise/error-tolerance** theme. See `CLAUDE.md` for the full spec.

## Files

- `*_practice.ipynb` — the practice notebooks (stubs + per-part tests + collapsed reference cells).
- `*_workers.py` — multiprocessing workers for each notebook's Part 5 (`morse_workers`,
  `ratelimit_workers`, `logagg_workers`, `cachewk_workers`, `transfer_workers`, `itinerary_workers`,
  `pubsub_workers`, `crawler_workers`, `threadpool_workers`, `connpool_workers`, `kvstore_workers`,
  `dagsched_workers`, `ledger_workers`, `pipeline_workers`, `breaker_workers`, `ringhash_workers`,
  `dedup_workers`, `heavyhitters_workers`, `fs_workers`, `bloom_workers`, `merkle_workers`,
  `crdt_workers`, `orderbook_workers`, `mvcc_workers`, `trie_workers`, `reservoir_workers`,
  `dsu_workers`, `lfu_workers`, `tpc_workers`, `cms_workers`). Worker code must live in a real module so
  spawned processes can import it (notebook-defined functions can't be pickled under the `spawn` start
  method).
- `CLAUDE.md` — generation conventions for future problems.

All reference solutions were validated end-to-end at authoring time (every part's tests pass,
including the `ProcessPoolExecutor` paths).
