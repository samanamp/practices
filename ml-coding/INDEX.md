# ML Coding Practice — Curriculum & Index

Day-based, vectorized-only NumPy, grounded in real systems / papers. **Forward passes come paired
with their backward pass** (gradients validated by finite differences) — backward is usually the
harder, more interview-relevant half. Each day: 1 warmup + ~2 medium + ~2 hard, with **≥1 pure
tensor-manipulation trick**. Conventions in `CLAUDE.md`.

Legend: ✅ done · 🔜 next · ⬜ planned

---

## Completed days

| Day | Theme | Questions |
|---|---|---|
| `day01_practice.ipynb` ✅ | Attention I | cosine top-k retrieval `[warmup]` · scaled dot-product attention `[medium]` · LayerNorm/RMSNorm `[medium]` · multi-head causal attention `[hard]` · conv2d/im2col `[trick]` |
| `day02_practice.ipynb` ✅ | Attention II (backward) | softmax backward `[warmup]` · softmax-CE fwd+bwd `[medium]` · attention backward dQ/dK/dV `[medium]` · causal attention fwd+bwd `[hard]` · MHA backward via einsum `[hard·trick]` (all gradients finite-diff checked) |
| `day03_practice.ipynb` ✅ | Attention III (efficient) | online softmax `[warmup]` · FlashAttention forward `[medium]` · KV-cache decode `[medium]` · causal FlashAttention block-sparse `[hard]` · sliding-window attention via stride view `[hard·trick]` |
| `day04_practice.ipynb` ✅ | MLP / MoE I | GELU fwd+bwd `[warmup]` · MLP block fwd+bwd `[medium]` · SwiGLU fwd+bwd `[medium]` · top-k MoE routing `[hard]` · MoE via grouped einsum `[hard·trick]` |
| `day05_practice.ipynb` ✅ | Quantization I | affine quant/dequant `[warmup]` · calibration/qparams `[medium]` · per-channel weight quant `[medium]` · fake-quant + STE backward `[hard]` · 4-bit pack/unpack `[hard·trick]` |
| `day06_practice.ipynb` ✅ | Attention IV (positional) | sinusoidal PE `[warmup]` · RoPE `[medium]` · ALiBi bias `[medium]` · RoPE attention + relative-pos `[hard]` · RoPE via complex numbers `[hard·trick]` |
| `day07_practice.ipynb` ✅ | MoE II (backward) | top-1 routing `[warmup]` · Switch aux loss `[medium]` · aux-loss gradient `[medium]` · MoE combine fwd+bwd `[hard]` · capacity dispatch via cumsum `[hard·trick]` |
| `day08_practice.ipynb` ✅ | Quantization II (PTQ) | percentile calib `[warmup]` · MSE-optimal scale `[medium]` · int8 GEMM `[medium]` · dynamic vs static `[hard]` · fused requant (zero-point trick) `[hard·trick]` |
| `day09_practice.ipynb` ✅ | Quantization III (LLM) | NF4 `[warmup]` · SmoothQuant `[medium]` · AWQ scale search `[medium]` · GPTQ error feedback `[hard]` · QLoRA double-quant `[hard·trick]` |
| `day10_practice.ipynb` ✅ | Quantization IV (QAT) | STE fake-quant `[warmup]` · LSQ step-size grad `[medium]` · per-channel backward `[medium]` · one QAT step `[hard]` · stochastic rounding `[hard·trick]` |

---

## Planned days (next up)

Concrete schedule for the remaining days. Each follows the format (1 warmup + ~2 medium + ~2 hard,
≥1 tensor trick, forward paired with backward, finite-diff-checked, paper-grounded). Order is a
suggestion — themes are independent, so they can be reordered.

### Day 6 ✅ — Attention IV: positional schemes
- sinusoidal positional encoding `[warmup]`
- RoPE: apply rotary embeddings to Q/K (pair-rotation) — Su 2021, arXiv:2104.09864 `[medium]`
- ALiBi: linear distance bias added to scores — Press 2021, arXiv:2108.12409 `[medium]`
- RoPE end-to-end in attention + relative-position equivalence `[hard]`
- RoPE via complex-number view (`reshape`/`view_as_complex`-style) `[hard · trick]`

### Day 7 ✅ — MoE II: backward & load balancing
- top-1 routing one-hot + tokens-per-expert counts `[warmup]`
- Switch load-balancing auxiliary loss (Fedus 2021) `[medium]`
- aux-loss gradient wrt gate logits (note: hard-assignment `f_e` is constant) `[medium]`
- MoE block backward: router + per-expert grads (builds on Day-4 MLP backward) `[hard]`
- capacity factor + token dropping via a scatter/capacity mask `[hard · trick]`

### Day 8 ✅ — Quant II: PTQ & calibration
- percentile calibration (clip outliers before choosing scale) `[warmup]`
- MSE-optimal scale search `[medium]`
- int8 GEMM: int32 accumulation + zero-point correction + requantization `[medium]`
- static vs dynamic activation quant pipeline matching the float matmul `[hard]`
- per-channel requant fused with the GEMM via `einsum` `[hard · trick]`

### Day 9 ✅ — Quant III: LLM methods
- NF4: nearest-codebook nonuniform quant (QLoRA, Dettmers 2023) `[warmup]`
- SmoothQuant activation→weight migration (Xiao 2022, arXiv:2211.10438) `[medium]`
- AWQ activation-aware per-channel scale search (Lin 2023, arXiv:2306.00978) `[medium]`
- GPTQ-style sequential error compensation (Frantar 2022, arXiv:2210.17323) `[hard]`
- GGUF k-quant super-block (block scales + nibble) pack/unpack `[hard · trick]`

### Day 10 ✅ — Quant IV: QAT & backward
- STE recap with a learnable scale `[warmup]`
- LSQ learned step size, forward + backward (Esser 2019, arXiv:1902.08153) `[medium]`
- per-channel fake-quant backward `[medium]`
- one quantization-aware training step (fake-quant weights+acts, STE backward) `[hard]`
- stochastic rounding `[hard · trick]`

### Day 11 🔜 — Backward / autodiff I: manual VJPs
- matmul VJP `[warmup]`
- BatchNorm forward + backward (Ioffe & Szegedy 2015) — the classic hard one `[medium]`
- LayerNorm backward `[medium]`
- conv2d backward (`dx`, `dW`) `[hard]`
- tiny reverse-mode autodiff tape over a few ops, gradient-checked `[hard · trick]`

### Day 12 — Losses & their gradients
- label-smoothed cross-entropy fwd+bwd `[warmup]`
- focal loss fwd+bwd (Lin 2017, arXiv:1708.02002) `[medium]`
- InfoNCE / contrastive loss (van den Oord 2018, arXiv:1807.03748) fwd+bwd `[medium]`
- BPR / triplet loss with in-batch hard-negative mining `[hard]`
- NDCG ranking metric, fully vectorized `[hard · trick]`

### Day 13 — Classic ML
- standardize / z-score whiten `[warmup]`
- k-means assignment + update step (Lloyd) `[medium]`
- PCA via SVD + whitening `[medium]`
- GMM E-step (responsibilities via logsumexp) `[hard]`
- RBF-kernel Gram matrix + Nyström sketch `[hard · trick]`

### Day 14 — Sequence decoding
- greedy + temperature sampling `[warmup]`
- top-k / top-p (nucleus) filtering `[medium]`
- repetition penalty / logit processors `[medium]`
- beam search, vectorized over beams `[hard]`
- batched gather for beam expansion / inverse-permutation `[hard · trick]`

### Day 15 — RL: returns & advantages
- discounted returns via reverse cumulative scan `[warmup]`
- GAE advantages (Schulman 2015, arXiv:1506.02438) `[medium]`
- importance-sampling ratios + PPO clipped objective `[medium]`
- n-step returns / TD(λ), vectorized `[hard]`
- per-episode masking so nothing leaks across episode boundaries `[hard · trick]`

### Day 16 (optional) — Diffusion
- DDPM closed-form `q(x_t | x_0)`, noise schedule, ε-objective (Ho 2020, arXiv:2006.11239).

---

## Theme: Attention (multi-day)

- **Day 1 ✅** — basics (SDPA, MHA, causal mask, LayerNorm/RMSNorm).
- **Day 2 ✅** — backward & training: softmax VJP, softmax-CE fused gradient, attention backward
  (`dQ/dK/dV`), causal attention fwd+bwd, full MHA backward via einsum (finite-diff checked).
- **Day 3 ✅** — efficient/long-context: online softmax, FlashAttention forward + causal block-sparse
  (Dao 2022, arXiv:2205.14135), KV-cache decode, sliding-window attention via `sliding_window_view`.
- **Day 6 ✅** — positional schemes: sinusoidal PE, RoPE (Su 2021, arXiv:2104.09864) via
  rotation/complex, ALiBi (Press 2021, arXiv:2108.12409), relative-position equivalence.

## Theme: MLP / MoE (multi-day)

- **Day 4 ✅** — MLP/MoE I: GELU fwd+bwd, MLP block fwd+bwd, SwiGLU fwd+bwd (Shazeer 2020,
  arXiv:2002.05202), top-k MoE routing (Shazeer 2017 / Fedus 2021), MoE via grouped einsum (GShard,
  Lepikhin 2020).
- **Day 7 ✅** — MoE II: top-1 routing, Switch aux loss + its gradient, MoE combine fwd+bwd, capacity
  token dropping, load-balancing aux loss + its gradient. *Backward-heavy.*
- **⬜ MoE at scale:** expert-parallel reshaping, segmented matmul (`np.add.at` / `reduceat`),
  megablocks-style block-sparse view. *Trick-heavy.*

## Theme: Quantization (multi-day) — recommended arc

Yes, this deserves several days; it's deep and very on-trend for LLM-serving roles.

- **Day 5 ✅ — Quant I — fundamentals:** affine quant/dequant, symmetric vs asymmetric, per-channel
  weight quant, fake-quant + STE backward (Bengio 2013 / Jacob 2017), 4-bit pack/unpack (QLoRA/GGUF).
- **Day 8 ✅ — Quant II — PTQ & calibration:** min/max vs percentile vs MSE-optimal scale; per-channel weight
  quant; int8 matmul with int32 accumulation + requantization; dynamic vs static activation quant.
- **Day 9 ✅ — Quant III — LLM methods:** SmoothQuant activation/weight migration (Xiao 2022,
  arXiv:2211.10438); AWQ activation-aware scaling (Lin 2023, arXiv:2306.00978); GPTQ error
  compensation idea (Frantar 2022, arXiv:2210.17323); NF4 + double-quant (QLoRA, Dettmers 2023,
  arXiv:2305.14314); GGUF/k-quant block layout. *Trick-heavy (bit-packing, block reshape).*
- **Day 10 ✅ — Quant IV — QAT & backward:** straight-through estimator (Bengio 2013, arXiv:1308.3432) forward
  fake-quant + STE backward; LSQ learned step size (Esser 2019, arXiv:1902.08153). *Backward-heavy.*

---

## Cross-cutting theme: backward pass / autodiff

Woven through every theme, but also stands alone:

- **⬜ Manual VJPs:** matmul, softmax, LayerNorm/BatchNorm (the classic hard one), GELU, conv.
- **⬜ Tiny reverse-mode autodiff** over a handful of ops; gradient-check the whole graph.
- Validation pattern everywhere: compare analytic grad to central finite differences.

## Cross-cutting: pure tensor-manipulation tricks (≥1 per day)

im2col ✅. Backlog: `as_strided` Toeplitz/Hankel · segment ops (`add.at`/`reduceat`) · einsum tensor
contractions/bilinear · broadcasting puzzles · argsort/inverse-permutation/ranking · unfold/fold ·
gather/scatter without one-hot · top-k & Gumbel-top-k sampling.

---

## Themes yet to cover (backlog / candidate days)

- **Losses:** softmax-CE fwd/bwd (`grad = p − onehot`), InfoNCE/contrastive (van den Oord 2018,
  arXiv:1807.03748), BPR, focal loss, label smoothing.
- **Normalization deep-dive:** BatchNorm fwd+bwd, GroupNorm, train vs eval stats.
- **Classic ML:** k-means assign+update, PCA/SVD whitening, GMM E-step, logistic regression GD.
- **Retrieval/ranking:** MIPS, ANN intuition, NDCG/MRR vectorized, reranking.
- **Sequence decoding:** greedy/temperature/top-k/top-p sampling, beam search, n-gram.
- **RL:** discounted returns, GAE advantages (Schulman 2015, arXiv:1506.02438), importance ratios.
- **Diffusion (optional):** DDPM noise schedule / closed-form `q(x_t|x_0)` (Ho 2020, arXiv:2006.11239).
