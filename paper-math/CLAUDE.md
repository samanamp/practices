# Conventions for generating math-from-zero practice (180-day arc)

This folder teaches the **math needed to read ML papers**, starting from (almost) nothing and
building up over ~180 short days. **Assume comfort with basic algebra and notation** (variables,
fractions, powers, rearranging an equation) — don't re-teach those — but **define every symbol
beyond that the first time it appears.** This is *not* interview practice and *not* research-grade
rigor: the bar is "open a paper and follow any derivation it hand-waves." Ramp slowly from there;
each day earns its 30 minutes with a real, usable idea rather than a triviality.

The whole thing must stay **light and enjoyable enough to do for 30 minutes a day, every day.**
No rush. The 180-day payoff is: read papers comfortably. Optimize for not-quitting over speed.

## The daily shape (one notebook = one ~30-min day)
`dayNN_practice.ipynb`, four sections in order:

1. **Review (~5 min, "warm-up").** 1–2 short exercises recalling concepts from earlier days
   (see spaced-repetition rule below). On day 1 there's nothing to review — say so.
2. **Lecture note (~10 min).** A short, friendly markdown mini-lecture on **one** new concept.
   Open with **one line naming the current milestone and how today's idea is a building block
   toward it** (motivation matters more than coverage). Plain language first, jargon second. Build
   intuition, then one tiny **worked numeric example** done by hand. Define every symbol. A cheap
   matplotlib picture is welcome when it helps.
3. **Exercises (~15 min).** 2–4 small exercises on today's concept, escalating *gently* from
   "can you read this notation" to "can you use it." Each exercise = a markdown prompt, a **stub**
   cell (`raise NotImplementedError`), and a **test** cell. **At least one exercise must probe the
   *effect*, not just the formula** — sweep a knob and observe (e.g. softmax temperature), or break
   an assumption and watch the tool fix it (e.g. feed mis-scaled inputs to LayerNorm and show the
   output is invariant). Reproducing the formula alone doesn't build "where/why to use it."
4. **Collapsed `ref_` solutions** at the bottom: worked-out answer (LaTeX where it's a derivation)
   **and** the reference implementation that passes.

## The practice loop (self-validating)
Where a concept has a closed form, the exercise is: understand it → implement it → a **numerical
oracle** confirms it (Monte-Carlo expectation, finite-difference gradient, brute-force loop, or
autodiff). Pure-notation exercises just check the computed value. This mirrors the sibling
`ml-coding` folder's "closed form vs. oracle" style — keep it, but **much gentler**.

## How to teach a building block — intuition first, formula LAST
This is the core pedagogy: the owner wants to know *what a tool does, when to reach for it, and what
breaks without it* — never just the formula. Every concept's lecture hits these five beats **in order**:
1. **The itch** — the real thing that's clumsy or broken *without* this tool (motivation before machinery).
2. **The picture** — a geometric / visual mental model.
3. **The formula** — *derived as the natural answer* to beat 1, not dropped from the sky.
4. **The knobs & effect** — behavior at the extremes, what it controls, what changes if you remove it
   (e.g. softmax temperature T→0 vs ∞; LayerNorm's learned γ, β; what explodes without normalization).
5. **In the wild** — where papers use it and how to recognize it.

A formula introduced before its "itch" is a bug in the lecture. When a concept's intuition needs
prerequisites (e.g. LayerNorm needs mean/variance/standardization), give them their own earlier days —
**descriptive stats of a vector (mean, variance, std) are forward-pass math and belong wherever first
needed; they are NOT the probability milestone** (random variables/distributions, which stays in M5).

## Spaced repetition (the thing that makes 180 days stick)
- Each new concept is **introduced on day D** and reviewed on days **D+1, D+3, D+7, D+16, D+35**.
- `INDEX.md` records the introduced-on day for every concept; due reviews for "today" are computed
  from those offsets. Keep the Review section to **≤2 exercises**; if more are due, take the 2
  most-overdue and bump the rest by +1 day. Review exercises are short variants, not re-teaches.

## Hard requirements
- **NumPy** (`import numpy as np`); autodiff/matplotlib allowed where they're the natural tool.
- Tone is warm and encouraging. Difficulty ramps slowly, but the floor assumes basic algebra —
  don't spend a day on something a comfortable-with-algebra reader already knows.
- Tests are **deterministic** (`np.random.default_rng(<int>)`), use `np.allclose` + an explicit
  expected value, and where natural one sanity invariant (non-negativity, sums-to-1, symmetry).
- Structure each exercise's test as `check_<id>(fn)` so it can be run against the student's
  function *or* the `ref_` function. **Validate before handing off:** run every check against the
  references and confirm they pass (a throwaway build-and-validate script is fine; delete it after).

## Curriculum is milestone-driven
`INDEX.md` organizes days into **milestones** — concrete things the owner can implement and
recognize in papers (M1: cosine similarity & RAG retrieval; M2: scaled dot-product attention; then
a full attention block, calculus/backprop, probability, generative models). Each day introduces
exactly the math its milestone needs, in dependency order. Chase **forward-pass** understanding
first (it stacks: dot product → cosine similarity → attention); calculus arrives later as its own
milestone. Prefer adding/clarifying milestones over scattering unrelated topics.

## Process
- Pick the next day from `INDEX.md` (milestones + review ledger live there). One new concept/day.
- After writing a day: update `INDEX.md` (record the day's new concept + introduced-on day, mark
  the day done) and the `README.md` day table.

## Boundary with sibling folders
`ml-coding` *implements* vectorized ops + gradients (interview-grade, hard). `paper-math` *teaches
the math* a paper assumes you already know, from zero. If an item is "code this layer's backward,"
it belongs in `ml-coding`; if it's "what does this symbol/identity even mean," it's here.
