# 07 — Canon Score Governance (Phase 4)

## 1. The position (accepted from the audit, endorsed by this charter)

> **The current weighting scheme is a hypothesis, not an empirically established optimum.**

The audit found the weights were selected narratively. Therefore, per the non-inference principle below, a failed calibration proves neither that the operator misapplied the score nor that the weights are wrong — it proves the calibration failed. The intellectually honest print position retains the framework as **Canon v1.0**, discloses its status, and attaches a validation protocol instead of pretending proof.

## 2. Canon v1.0 charter (verified against the public edition, 2026-08-29)

- **Structure:** 7 dimensions, **added, never averaged**; ceiling exactly 100 (framework.html + ch-64 Lesson 64.1 + research index — three concordant pages).
- **Dimensions & weights** (CLM-0003; CALC-0002 guards the sum = 100):

| # | Dimension | Points | Hemisphere |
|---|---|---|---|
| 1 | Financial Strength & Profitability | 20 | H2 |
| 2 | Governance & Promoter Behaviour | 15 | H1 |
| 3 | Liquidity & Tradability | 10 | H1 |
| 4 | Valuation Reasonableness | 15 | H2 |
| 5 | Sector & Business Model Durability | 15 | H1 |
| 6 | Growth Trajectory | 15 | H2 |
| 7 | Dividend & Capital Return Discipline | 10 | H2 |

- **Hemispheres** (CLM-0001/0002; CALC-0001 guards 40+60=100): H1 Qualitative Defence = 40 (Governance 15 + Liquidity 10 + Sector 15); H2 Quantitative Forensics = 60 (FS 20 + Valuation 15 + Growth 15 + Dividend 10).
- **Versioning:** the vector is a *versioned quantity* (VTG-0002). Canon v1.0 → v1.1 only via: a diff table, a registered test (tests.tsv), and a SUPERSEDED row for v1.0's vector. Never a silent edit (R5/R7).
- **Rubric home:** ch-64 (generic), ch-65 (sector adjustments), ch-66 (use in decisions), case studies ch-83/84.

## 3. Status assignments

| Item | Status | Note |
|---|---|---|
| "The book states the vector 20/15/10/15/15/15/10" (CLM-0003) | FACT—VERIFIED | a fact *about the book* (L0) |
| "The vector is an empirically established optimum" (CLM-0009) | **NOT YET VALIDATED** | the audit's core epistemic finding; pre-registered test required (08) before any promotion |
| "Hemispheres H1=40 / H2=60 / max=100" (CLM-0001/0002/0012) | FACT—VERIFIED | structural identities, CALC-guarded |
| Screening thresholds (ch-66: <45 / 45–59 / 60–64 / ≥65) | FACT—VERIFIED (stated) + rule rows RUL | the *wisdom* of the thresholds is a hypothesis, not a fact |

## 4. Required disclosures in 13.x print

1. **Status paragraph** (ch-63 or ch-64): "The v1.0 weighting is the author's calibrated hypothesis, not an empirically established optimum. A validation protocol (Part XV, Chs. 79–82, extended by TEST-####) governs promotion to a validated status."
2. **Uncertainty:** report sensitivity — how the final band shifts under a ±3-point perturbation of any single weight (a DERIVED exhibit, not a new claim).
3. **Overlap disclosure:** which dimensions double-count the same risk (e.g., Liquidity & Tradability vs. Exit Risk chapters; Governance vs. Promoter Behaviour content shared with Part IV) and how the rubric avoids double penalization.
4. **Governance overrides:** hard risk rules (T1/T2 in 09) trump the score unconditionally; the score gates *within* the allowed action space, never against a higher tier.

## 5. Threshold governance

Any change to a band boundary (e.g., 45/60/65) requires: (a) a written, pre-registered justification; (b) a constitution consistency check against RUL rows in 09 (this is where the 56–59 collision gets resolved — CON-0002); (c) a supersession entry. Band vocabulary is **one system, one owner** (06, CON-0005): the canonical band table lives in the framework page/ch-64; the research pages cite it rather than inventing labels.

## 6. Calibration history (to be transcribed, Phase 5)

Chs. 79–82 (Calibration & Backtesting) constitute the corpus's own calibration part. Phase 5 transcribes each calibration into tests.tsv with: window, method, in-sample/out-of-sample split, verdict. Failed calibrations are kept in the record — the book's willingness to expose failed calls (audit's positive finding) is the credibility asset that makes the hypothesis status *stronger*, not weaker.
