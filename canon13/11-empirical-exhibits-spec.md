# 11 — Empirical Exhibits Spec (Phase 8)

Exhibits are the book's public proofs. Each has a spec, a pre-registered test (08), a verdict, and an **honesty clause**: a negative result is published in the book, and the corresponding claim downgrades to mechanism-plus-evidence-requirement.

## EXH-001 — Credit growth → NEPSE lead (the audit's central missing evidence)

**Hypothesis under test:** CLM-0010 — "credit growth allows reading NEPSE 6–18 months ahead" (as asserted in Part 0: ch-0.1 Credit Cycle, ch-0.2 NRB Transmission, ch-0.3 Liquidity Regimes; exact phrasings pending crawl).

### Data (to collect — SRC L2/L3)
| Series | Source | Frequency | Window |
|---|---|---|---|
| Broad credit growth (total credit to private sector; separate narrow credit if the book uses it) | NRB monetary/credit reviews, monthly | monthly | maximum available; start date stated in the exhibit |
| NEPSE daily index → month-end close | NEPSE | daily → monthly | same window |
| Regime markers (for subsampling) | derived from Ch. 0.3 criteria once transcribed | monthly | same window |

### Method
1. **Descriptive:** level series + growth series; simple stationarity note (no pretending at cointegration).
2. **Lead-lag:** cross-correlation of Δcredit-growth vs. Δindex at lags 0–18 months. Report **all** lags (multiple-testing rule, 08 §3).
3. **Naive leading-indicator protocol:** define a binary signal (credit growth above/below its trailing 12-month mean); measure its hit rate for index direction at 6, 12, 18 months ahead; compare against base rates (all-chance and persistence). Report hit rates with confidence intervals.
4. **Out-of-sample split:** develop on the first ⅔, verify on the last ⅓, split date fixed in the test registration (chronological, no shuffling).
5. **Regime subsample:** repeat the hit-rate in bull vs. bear windows (per Ch. 0.3 criteria) — the honest version of the book's own claim, which is really a regime claim.

### Output
One figure (series + signal), one hit-rate table with base rates + CIs, and a plain-language verdict: PASS / FAIL / INCONCLUSIVE per 08 §4.

### Honesty clause
If FAIL/INCONCLUSIVE: every corpus occurrence of the lead claim rephrases to: "the Canon hypothesises this mechanism; the evidence required to establish it is EXH-001; current status: \<verdict\> and its limits." The mechanism chapters (Part 0) keep the *mechanism* (NRB policy → credit → liquidity → prices is plausible and documented as a chain) and lose the *timing precision*.

### Status
NOT STARTED. Blocked on: data collection (B3), and the exact claim phrasings (crawl of ch-0.1/0.2/0.3).

## EXH-002 — Regime-framework validation (placeholder)

Hypothesis: the Ch. 0.3 four-phase liquidity-regime classification predicts the action space correctly (i.e., acting per the phase would have outperformed acting per the opposite phase). Spec drafted once the four phases and their criteria are transcribed verbatim (crawl of ch-0.3). Registered in Phase 5.

## EXH-003 — Canon Score out-of-sample ranking (placeholder, Phase 5)

Hypothesis: CLM-0009 — companies scoring high on the v1.0 rubric (at time t, from point-in-time filings) outperform low-scoring companies over t→t+36 months, out-of-sample, survivorship-controlled. This is what "validated" would have to mean for a static rubric; criteria to be registered in Phase 5. This is the most expensive exhibit; it may legitimately be declared out of scope for 13.0, in which case CLM-0009 stays NOT YET VALIDATED and the print says so.
