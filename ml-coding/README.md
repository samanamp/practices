# ML / Tensor-Programming Practice (day-based)

Practice for **tensor-programming interviews** (CoderPad-style ML coding rounds). The real interview
hands you the **hard vectorized** problem — so there are **no scalar/loop versions** here. Every
question goes straight to vectorized NumPy, grounded in a real system or a paper.

## Format: one notebook = one ~1-hour practice day

Each `dayNN_practice.ipynb` has:

- **1 warmup** — quick, but still vectorized and real.
- **~2 medium + ~2 hard** (≈5 questions, a one-hour load).
- **≥1 pure tensor-manipulation trick** (stride tricks, einsum, fancy indexing) — not easy.
- **Forward paired with backward** — when a question is a layer/op/loss, it also asks for the
  gradient (VJP), checked against finite differences. Backward is the harder, more interview-relevant
  half, so some questions are backward-only.

Every question's markdown cell gives the **real-world/paper context, a reference, and why it
matters**, plus the spec, shapes, and a "no loops" reminder. Each has a stub, a test, and a collapsed
`ref_` reference solution. Tests are deterministic and check invariants (shapes, sums-to-1,
masked==0, equivariance, a loop-oracle, numerically-extreme cases). Loops appear only inside tests, as
an obviously-correct oracle to validate the vectorized solution against.

## Days

| Notebook | Theme | Questions |
|---|---|---|
| `day01_practice.ipynb` | Attention I | cosine top-k retrieval `[warmup]` · scaled dot-product attention `[medium]` · LayerNorm/RMSNorm `[medium]` · multi-head causal attention `[hard]` · conv2d via `sliding_window_view` (im2col) `[hard · trick]` |
| `day02_practice.ipynb` | Attention II (backward) | softmax backward `[warmup]` · softmax cross-entropy fwd+bwd `[medium]` · attention backward dQ/dK/dV `[medium]` · causal attention fwd+bwd `[hard]` · multi-head attention backward via einsum `[hard · trick]` |
| `day03_practice.ipynb` | Attention III (efficient) | online softmax `[warmup]` · FlashAttention forward `[medium]` · KV-cache decode `[medium]` · causal FlashAttention (block-sparse) `[hard]` · sliding-window attention via `sliding_window_view` `[hard · trick]` |
| `day04_practice.ipynb` | MLP / MoE I | GELU fwd+bwd `[warmup]` · MLP block fwd+bwd `[medium]` · SwiGLU fwd+bwd `[medium]` · top-k MoE routing `[hard]` · MoE via grouped einsum `[hard · trick]` |
| `day05_practice.ipynb` | Quantization I | affine quant/dequant `[warmup]` · calibration `[medium]` · per-channel weight quant `[medium]` · fake-quant + STE backward `[hard]` · 4-bit pack/unpack `[hard · trick]` |
| `day06_practice.ipynb` | Attention IV (positional) | sinusoidal PE `[warmup]` · RoPE `[medium]` · ALiBi bias `[medium]` · RoPE attention + relative-position `[hard]` · RoPE via complex numbers `[hard · trick]` |
| `day07_practice.ipynb` | MoE II (backward) | top-1 routing `[warmup]` · Switch aux loss `[medium]` · aux-loss gradient `[medium]` · MoE combine fwd+bwd `[hard]` · capacity dispatch via cumsum `[hard · trick]` |
| `day08_practice.ipynb` | Quantization II (PTQ) | percentile calibration `[warmup]` · MSE-optimal scale `[medium]` · int8 GEMM `[medium]` · dynamic vs static `[hard]` · fused requant `[hard · trick]` |
| `day09_practice.ipynb` | Quantization III (LLM) | NF4 `[warmup]` · SmoothQuant `[medium]` · AWQ scale search `[medium]` · GPTQ error feedback `[hard]` · QLoRA double-quant `[hard · trick]` |
| `day10_practice.ipynb` | Quantization IV (QAT) | STE fake-quant `[warmup]` · LSQ step-size grad `[medium]` · per-channel backward `[medium]` · one QAT step `[hard]` · stochastic rounding `[hard · trick]` |

See **`INDEX.md`** for the full curriculum — themes (Attention, MLP/MoE, Quantization), the
backward-pass thread, the tensor-trick backlog, and what's left to cover.

Papers referenced so far: Vaswani et al. 2017 (attention), Ba et al. 2016 (LayerNorm),
Zhang & Sennrich 2019 (RMSNorm), Chellapilla et al. 2006 (im2col), Dao et al. 2022 (FlashAttention),
Beltagy et al. 2020 (Longformer), Hendrycks & Gimpel 2016 (GELU), Shazeer 2020 (SwiGLU),
Shazeer 2017 / Fedus 2021 / Lepikhin 2020 (MoE), Bengio 2013 + Jacob 2017 (STE/quant-aware training),
Dettmers et al. 2023 (QLoRA/NF4), Su 2021 (RoPE), Press 2021 (ALiBi), Xiao 2022 (SmoothQuant),
Lin 2023 (AWQ), Frantar 2022 (GPTQ), Esser 2019 (LSQ).

## How to use a day

Time-box ~60 min. Per question: restate the spec/shapes, write the **vectorized** solution (no
element loops), run the test until green, then reveal the `ref_` cell to compare. The context bullets
are the "say-this-out-loud" material an interviewer probes for.

## How new days are generated

Conventions live in `CLAUDE.md` (auto-loaded by any Claude Code session/agent here): vectorized-only
NumPy, 1 warmup + ~2 medium + ~2 hard, ≥1 tensor trick, reality/paper-grounded with citations,
deterministic tests, passing references.

## Environment

```
python3 -m pip install numpy
```

All reference solutions are validated at authoring time (every question's tests pass).
