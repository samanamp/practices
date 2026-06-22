# paper-math

A gentle, ~180-day, 30-minutes-a-day path from "comfortable with basic algebra" to **reading ML
papers comfortably**. Each day is one notebook: a short lecture note on one new idea, a few small
exercises, and a quick spaced-repetition review of earlier days.

The curriculum is **milestone-driven** — every stretch of days builds toward a concrete thing you
can implement and recognize in papers:

- **Milestone 1 — Cosine similarity & a tiny RAG retriever** (days 1–9)
- **Milestone 2 — Scaled dot-product attention** (days 10–18)
- **Milestone 3 — A full attention block** incl. LayerNorm (days 19–26)
- then calculus/backprop → probability → VAEs & diffusion.

Every concept is taught **intuition first, formula last**: what problem it solves, the picture, the
formula as the natural answer, the knobs/effect, and where papers use it.

See `INDEX.md` for the full milestone roadmap and review ledger, and `CLAUDE.md` for how days are built.

## Days

| Day | Topic | Milestone |
|-----|-------|-----------|
| [01](day01_practice.ipynb) | Summation notation Σ (+ three moves) | M1 · cosine & RAG |
| [02](day02_practice.ipynb) | Vectors & embeddings | M1 · cosine & RAG |
| [03](day03_practice.ipynb) | The dot product | M1 · cosine & RAG |
| [04](day04_practice.ipynb) | Length: the L2 norm | M1 · cosine & RAG |
| [05](day05_practice.ipynb) | Geometry: dot = ‖a‖‖b‖cosθ | M1 · cosine & RAG |
| [06](day06_practice.ipynb) | Unit vectors & normalization | M1 · cosine & RAG |
| [07](day07_practice.ipynb) | Cosine similarity (mini-capstone) | M1 · cosine & RAG |
| [08](day08_practice.ipynb) | Query vs many documents | M1 · cosine & RAG |
| [09](day09_practice.ipynb) | Top-k retrieval (capstone: a RAG retriever) | M1 · cosine & RAG |
| [10](day10_practice.ipynb) | max & argmax (the itch for softmax) | M2 · attention |
| [11](day11_practice.ipynb) | Matrix multiply = batched dot products (QKᵀ) | M2 · attention |
| [12](day12_practice.ipynb) | The exponential eˣ | M2 · attention |
| [13](day13_practice.ipynb) | Softmax = soft argmax (+ temperature) | M2 · attention |
| [14](day14_practice.ipynb) | Softmax stability & differentiability | M2 · attention |
| [15](day15_practice.ipynb) | Weighted average / convex combination | M2 · attention |
| [16](day16_practice.ipynb) | Why divide by √d | M2 · attention |
| [17](day17_practice.ipynb) | Scaled dot-product attention (capstone) | M2 · attention |
| [18](day18_practice.ipynb) | Cosine similarity ↔ attention | M2 · attention |

_(one row per day as they're added)_
