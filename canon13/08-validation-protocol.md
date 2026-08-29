# 08 — Validation Protocol (Phase 5)

## 1. Two things that are not the same

- **Calibration** — fitting or checking the model on data it was developed against. In-sample. Produces confidence in mechanics, not in predictive power.
- **Validation** — testing a pre-registered hypothesis on data the model was *not* developed against (out-of-sample, chronological).

The corpus's failed calibration (Chs. 79–82 territory) is neither. It is a failed calibration — and per 07 §1 it proves nothing about the weights specifically. Every claim in 13.x about the Canon Score's predictive power must be traceable to a **validation** row, not a calibration.

## 2. Pre-registration

Before touching test data, a TEST-#### row exists with:
- `hypothesis_ref` → the CLM row being tested (e.g., CLM-0010 credit lead; CLM-0009 weights).
- `data_window`: exact series, start, end, frequency, and the out-of-sample split rule.
- `method`: the procedure, step by step.
- `criteria`: what counts as PASS, FAIL, INCONCLUSIVE — stated in advance.
- `registered_at`: the lock date.

No post-hoc changes to a registered test. A changed test is a **new** test with a new ID; the old one stays in the record (append-only, R5).

## 3. Bias controls (explicit, per the audit)

- **Survivorship:** the test universe must include delisted, suspended, and failed issuers as they stood *at the window start* (point-in-time universe). For NEPSE: the book's own Ch. 89 (bank failure/near-failure) case studies show the failure mode exists; the universe must contain those names. Index-level tests (EXH-001) are survivorship-free by construction — say so.
- **Look-ahead:** point-in-time inputs only. Announcements as knowable at the time; regulations by effective date (05 §6); no current-page values applied to historical dates. The corpus's point-in-time case-study method (audit's positive finding) is the template; it is now a requirement.
- **Multiple testing:** when many lags/thresholds are examined (EXH-001 tests lags 0–18 months), report *all* results and flag the best-honest one with its confidence interval; never cherry-pick the single best lag.

## 4. Verdicts

| Verdict | Consequence |
|---|---|
| **PASS** (with stated limitations) | hypothesis claim → `EMPIRICALLY VALIDATED`; print may assert, with window + limitations + test ref. |
| **FAIL** | → `NOT YET VALIDATED`; language drops to the ceiling (02). The failure is published in the book (credibility asset). |
| **INCONCLUSIVE** | → `NOT YET VALIDATED`; state what would make it conclusive. |

A regression path exists: `EMPIRICALLY VALIDATED` → `NOT YET VALIDATED` if a scope violation (survivorship/look-ahead) is later found, or a replication fails. This is recorded as a review event, never erased.

## 5. Current test register (baseline)

- TEST-#### for CLM-0009 (weights) and CLM-0010 (credit lead): **registered at Phase 5** — criteria drafted in 11 (EXH-001) for the credit lead; the weights test must define what "validated" would even mean for a static rubric (e.g., does sorting by v1.0 score separate later outperformers from underperformers over the window, out-of-sample?). Until registered, both claims sit at `NOT YET VALIDATED` and the print obeys the ceiling.
