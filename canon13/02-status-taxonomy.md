# 02 — Status Taxonomy

Nine print statuses + one pipeline status. Canonical machine tokens use the em-dash (—):
`FACT—VERIFIED`, `FACT—VINTAGE-SENSITIVE`, `DERIVED—CALCULATED`, `ASSUMPTION`, `ILLUSTRATIVE`, `AUTHOR'S HYPOTHESIS`, `EMPIRICALLY VALIDATED`, `NOT YET VALIDATED`, `SUPERSEDED`, `UNREVIEWED`.

## 1. Definitions, required fields, language ceilings

| Status | Definition | Required fields (beyond id/statement/status) | Language ceiling in print |
|---|---|---|---|
| `FACT—VERIFIED` | Matches a source snapshot. | `source_id`, `xrefs` | Full assertion + source citation. |
| `FACT—VINTAGE-SENSITIVE` | True for a dated window; re-verification scheduled. | `source_id`, `as_of`, `xrefs` | Full assertion + "as of \<date\>" + source. |
| `DERIVED—CALCULATED` | Reproducible from cited inputs via a documented CALC. | `calc_id` | Assertion + "calculated from \<inputs, method\>" or appendix ref. |
| `ASSUMPTION` | Explicit, bounded premise; not a fact about the world. | — (register in appendix) | "Assuming …" — framed as premise, never as fact. |
| `ILLUSTRATIVE` | Teaching example; not a claim about the real world. | — (label in print) | "For example / suppose …" — labeled, excluded from validation. |
| `AUTHOR'S HYPOTHESIS` | The author's testable proposal (Canon v1.0 weights; credit-cycle mechanism; four-phase regime model). | — (must carry a test plan ref in `notes`) | "The Canon proposes / hypothesises …" + testability statement. No predictive assertions. |
| `EMPIRICALLY VALIDATED` | Passed a pre-registered out-of-sample test (08). | tests row with `verdict=PASS` for this claim | Assertion + data window + limitations + test ref. |
| `NOT YET VALIDATED` | Hypothesis with no completed (or a failed) test. | — | Mechanism description + "the evidence required to establish this is …; its current status is: not yet collected/tested." **No predictive assertions.** |
| `SUPERSEDED` | Replaced by a newer claim. Terminal. | `superseded_by` | Must not print as current. Historical printing requires "superseded by \<id\>". |
| `UNREVIEWED` | Pipeline only: candidate extracted, not yet triaged. | — | **May never print.** |

## 2. Transitions

| From | To | Gate |
|---|---|---|
| `UNREVIEWED` | any print status except `SUPERSEDED`/`EMPIRICALLY VALIDATED` | triage per `03` (a documented decision, recorded in `notes`) |
| `FACT—VINTAGE-SENSITIVE` | `FACT—VERIFIED` | re-verified against a current snapshot; the as-of advances, history retained |
| `FACT—VERIFIED` / `FACT—VINTAGE-SENSITIVE` | `FACT—VINTAGE-SENSITIVE` | supersession-pending detected (class D): new observation exists but supersession not executed |
| `AUTHOR'S HYPOTHESIS` | `EMPIRICALLY VALIDATED` | pre-registered out-of-sample PASS (08). No direct jumps from `UNREVIEWED`. |
| `EMPIRICALLY VALIDATED` | `NOT YET VALIDATED` | scope violation found (survivorship/look-ahead) or replication failure — a **regression event**, recorded |
| any | `SUPERSEDED` | successor accepted; `superseded_by` set. Terminal. |

## 3. Print-label selection

A claim has one primary status. Secondary attributes (`vintage_sensitive`, `superseded`) are orthogonal flags in `notes`, not extra statuses. When a claim is both derived and time-bound, the printed label is the most conservative of the two (a `DERIVED—CALCULATED` value whose inputs are `VINTAGE-SENSITIVE` prints with the as-of of its most time-bound input).

## 4. Enforcement

- `tools/canon_tools.py validate` enforces the required-fields column mechanically (e.g., `EMPIRICALLY VALIDATED` without a PASS test row is an error; `FACT—VERIFIED` without `xrefs` is an error).
- The Phase 10 gate G5 audits the *print* against the ceilings (status → allowed phrasing). A ceiling breach is a defect even when the underlying claim is correct: it is exactly the F2 overconfidence pattern.
