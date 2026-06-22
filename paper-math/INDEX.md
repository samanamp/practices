# paper-math curriculum & review ledger

Goal: in ~180 short days (30 min/day), go from "comfortable with basic algebra" to **reading ML
papers comfortably**. The curriculum is **milestone-driven**: instead of abstract topics, each
stretch of days *builds toward a concrete thing you can implement and recognize in papers*. Every
day is a named building block for the current milestone, so it always feels like it's going
somewhere.

Pick the next undone day, write it, then update this file (ledger + mark done).

## Why milestones
The math you need to read the architecture sections of modern papers is mostly **forward-pass**
math, and it stacks neatly: the dot product underlies cosine similarity, which underlies attention.
So we chase those first (motivating, no calculus yet). Calculus/gradients arrive later, as their own
milestone ("make it *learn*"), once you actually want to understand training.

---

## Milestone 1 — Cosine similarity & a tiny RAG retriever
*Payoff:* implement the retrieval step of RAG and read "we rank passages by cosine similarity"
with full understanding. Each day introduces exactly the math the milestone needs.

| Day | New concept | Why it's needed |
|-----|-------------|-----------------|
| 01 ✅ | Summation Σ + moves: linearity, sum-over-axis, factoring a double sum | the language all of it is written in |
| 02 | Vectors & embeddings — a list of numbers as a point/direction in $\mathbb{R}^d$ | what we're comparing |
| 03 | Dot product $a\cdot b=\sum_i a_i b_i$ (builds straight on day 1) | the core similarity operation |
| 04 | Squares, sum of squares, and the L2 norm $\lVert x\rVert=\sqrt{\sum_i x_i^2}$ | a vector's length/magnitude |
| 05 | Geometry: $a\cdot b=\lVert a\rVert\lVert b\rVert\cos\theta$ — the angle reading | dot product ↔ "how aligned" |
| 06 | Unit vectors & normalization $x/\lVert x\rVert$ | strip magnitude, keep direction |
| 07 | **Cosine similarity** $=\dfrac{a\cdot b}{\lVert a\rVert\lVert b\rVert}\in[-1,1]$ (mini-capstone) | the RAG ranking score |
| 08 | One query vs many docs → a vector of similarities (matrix–vector; reuse axis-sums) | scoring a whole corpus |
| 09 | **Top-k retrieval** with argmax/argsort (Milestone 1 capstone: a tiny RAG retriever) | the actual retrieval step |

## Milestone 2 — Attention scores
*Payoff:* implement scaled dot-product attention and see exactly how it relates to cosine
similarity. Builds entirely on Milestone 1.

| Day | New concept | Why it's needed |
|-----|-------------|-----------------|
| 10 | **max & argmax** — hard "pick the winner," and its *itch*: all-or-nothing and **not differentiable** | motivates needing a *soft* version |
| 11 | Matrix multiplication as a batch of dot products ($QK^\top$ = every query–key score at once) | the score matrix |
| 12 | The exponential $e^x$ — positive, and *amplifies* gaps | the ingredient that makes softmax peaky |
| 13 | **Softmax = a *soft* argmax** — exp-then-normalize; recovers argmax in the limit; **temperature** as the sharpness knob (T→0 one-hot, T→∞ uniform — sweep it and watch) | raw scores → a probability distribution / attention weights |
| 14 | Softmax properties: shift-invariance ⇒ *why* we subtract the max (stability); monotonic; differentiable ⇒ *why* we use it instead of argmax | makes it usable & trainable |
| 15 | Weighted average / convex combination $\sum_i w_i v_i$ (ties to day-1 linearity) | softmax weights → aggregate the values |
| 16 | Why divide by $\sqrt d$: dot products grow with dimension (variance $\sim d$), saturating softmax | the "scaled" in scaled attention |
| 17 | **Scaled dot-product attention** $\text{softmax}(QK^\top/\sqrt d)\,V$ (Milestone 2 capstone) | the whole mechanism |
| 18 | Cosine-vs-attention: attention = softmax over (scaled) dot-product similarities; unit-normalized Q,K ⇒ scores *are* cosine sims ("cosine attention", Swin v2) | tie the two milestones together |

## Milestone 3 — A full attention block (incl. LayerNorm, intuition-first)
*Payoff:* read a Transformer block diagram end to end. Note the LayerNorm prerequisites: **mean /
variance / standardization are forward-pass descriptive stats, taught here when first needed — not
the probability milestone (M5).**

| Day | New concept | Why it's needed |
|-----|-------------|-----------------|
| 19 | Mean of a vector (descriptive stat — center of a cloud of numbers) | prerequisite for normalization |
| 20 | Variance & std (spread); **standardization / z-score** $(x-\mu)/\sigma$ → mean 0, std 1 | re-center & re-scale to a common footing |
| 21 | The *itch*: activation scale **drifts** across deep layers (explode/vanish), destabilizing training | why we normalize at all |
| 22 | **LayerNorm** — standardize each token's feature vector, then learned scale $\gamma$ & shift $\beta$; *effect:* stable, scale-insensitive, deeper stacks trainable | the normalization in a Transformer block |
| 23 | Placement (pre- vs post-norm) & LayerNorm vs BatchNorm (across features vs across batch; why transformers use LN) | reading the block diagram |
| 24 | Residual connection $x+\text{sublayer}(x)$ — the *itch* (deep nets degrade) & effect | the skip arrow in the diagram |
| 25 | Multi-head attention — attention in parallel subspaces, concatenated | the rest of the block |
| 26 | **Capstone: read a full Transformer block end to end** | M3 payoff |

## Later milestones (sketch — flesh out when we get there)
- **M4 — Make it learn (calculus arrives):** derivatives as slope, the chain rule = backprop,
  gradients of a loss, gradient descent. Capstone: hand-derive softmax/attention gradients.
- **M5 — Probability for ML:** random variables, expectation/variance *as distributions*, the
  Gaussian, Bayes. (Builds on the descriptive mean/variance from M3.)
- **M6 — Generative models:** entropy/KL/ELBO → read & derive the math behind VAEs and diffusion.

(Targets ~180 days total; pacing is loose — one solid building block per day beats rushing.)

---

## Spaced-repetition rule
Concept introduced on day **D** → review on **D+1, D+3, D+7, D+16, D+35**. Compute today's due
reviews from the "Introduced" column below; cap the Review section at 2 items (if more are due,
take the 2 most overdue and bump the rest by +1 day).

## Ledger
Record each day's new concept here when written.

| Day | Status | New concept | Introduced (D) | Review-on days |
|-----|--------|-------------|----------------|----------------|
| 01  | ✅ done | Summation Σ + linearity, sum-over-axis, factoring a double sum | 1 | 2, 4, 8, 17, 36 |
| 02  | ✅ done | Vectors & embeddings ($\mathbb{R}^d$); meaning-as-geometry, analogy arithmetic | 2 | 3, 5, 9, 18, 37 |
| 03  | ✅ done | Dot product $a\cdot b=\sum_i a_i b_i$; sign = alignment; $a\cdot a$ | 3 | 4, 6, 10, 19, 38 |
| 04  | ✅ done | Squares, sum of squares, L2 norm $\lVert x\rVert$; distance; row norms | 4 | 5, 7, 11, 20, 39 |
| 05  | ✅ done | Geometry $a\cdot b=\lVert a\rVert\lVert b\rVert\cos\theta$; recover the angle | 5 | 6, 8, 12, 21, 40 |
| 06  | ✅ done | Unit vectors & normalization $x/\lVert x\rVert$; normalized dot = cosθ | 6 | 7, 9, 13, 22, 41 |
| 07  | ✅ done | **Cosine similarity** (mini-capstone); scale-invariance, symmetry | 7 | 8, 10, 14, 23, 42 |
| 08  | ✅ done | Query vs corpus → score vector; matrix–vector $\hat D\hat q$ (vectorization) | 8 | 9, 11, 15, 24, 43 |
| 09  | ✅ done | **Top-k retrieval** (argmax/argsort) — Milestone 1 capstone: a RAG retriever | 9 | 10, 12, 16, 25, 44 |
| 10  | ✅ done | max & argmax; one-hot; discontinuity (the *itch* for softmax) | 10 | 11, 13, 17, 26, 45 |
| 11  | ✅ done | Matrix multiply = batched dot products; $QK^\top$ score matrix; Gram | 11 | 12, 14, 18, 27, 46 |
| 12  | ✅ done | The exponential $e^x$ — positive, amplifies; shifted/stable exp | 12 | 13, 15, 19, 28, 47 |
| 13  | ✅ done | **Softmax = soft argmax**; temperature dial; argmax limit | 13 | 14, 16, 20, 29, 48 |
| 14  | ✅ done | Softmax properties: shift-invariance ⇒ subtract-max; log-sum-exp; differentiable | 14 | 15, 17, 21, 30, 49 |
| 15  | ✅ done | Weighted average / convex combination $\sum_i w_i v_i = w^\top V$; batched $WV$ | 15 | 16, 18, 22, 31, 50 |
| 16  | ✅ done | Why $\div\sqrt d$: $\mathrm{Var}(q\cdot k)\approx d$; un-saturating softmax | 16 | 17, 19, 23, 32, 51 |
| 17  | ✅ done | **Scaled dot-product attention** $\mathrm{softmax}(QK^\top/\sqrt d)V$ — M2 capstone | 17 | 18, 20, 24, 33, 52 |
| 18  | ✅ done | **Cosine ↔ attention**: softmax over cosine sims; cosine attention (Swin v2) | 18 | 19, 21, 25, 34, 53 |
| 19  | ⬜ next | M3 — mean of a vector (descriptive stat, toward LayerNorm) | | |

_(extend one row per day as you go)_

> **Milestone 1 complete (days 1–9):** read & build cosine-similarity RAG retrieval.
> **Milestone 2 complete (days 10–18):** read scaled dot-product attention, and see why it *is* cosine similarity with a softmax on top.
