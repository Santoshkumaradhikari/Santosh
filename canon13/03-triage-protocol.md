# 03 — Triage Protocol

Every audit finding (and every engine detection) is triaged into exactly one primary class before any remediation. The class determines the remedy. Mixing remedies is how fixes regenerate defects.

## 1. Classes

| Class | Definition | Test | Remedy | Proof of remediation |
|---|---|---|---|---|
| **A — Error** | A value is wrong (arithmetic or factual). | Re-derivation or source comparison shows a different correct value. | Correct the value in the canonical occurrence; all xrefs inherit via qkey. | CALC re-evaluation passes; engine shows no residual VALUE collision on that qkey. |
| **B — Contradiction** | Two live assertions/rules conflict. | Same qkey, different values; or two active rules with overlapping trigger and different action. | Governance: assign tiers (09), determine winner, **print the resolution**. The loser is superseded or re-scoped — never deleted silently. | Both RUL/CLM rows updated; `conlog` closed with `winner`, `loser`, `printed_resolution`. |
| **C — Unsupported proposition** | Confidence exceeds evidence. | The proposition is asserted as fact but no test exists (or the test failed). | (i) run the registered test (08/11) and let the verdict set the status; or (ii) downgrade language to the ceiling of `NOT YET VALIDATED`. | Status changed with dated note; print phrasing audited against the ceiling. |
| **D — Stale / supersession-pending** | A dated fact is known to be out of date; supersession not executed. | A newer observation (event, re-issue, rescore) exists after the claim's as-of. | Execute supersession: new VTG row, old row SUPERSEDED (R5), print updated or explicitly re-affirmed with new as-of. | VTG pair complete; `conlog` closed. |

## 2. Decision tree

```
finding
├─ Is a single value demonstrably wrong?                    → A
├─ Do two live parts disagree (value or prescription)?      → B
├─ Is a dated value known out-of-date, supersession pending?→ D
└─ Is a claim asserted more strongly than any test supports?→ C
```

Order of triage when ambiguous: **A first** (mechanical, cheap), then **B**, then **D**, then **C** (evidence work). One item may carry secondary classes (e.g., a C item that also collides — that is a C+B ticket; both tickets must close). The primary class is recorded in `conlog.type`; secondaries in `notes`.

## 3. Worked exemplars (from the baseline audit, verified where possible)

### A — Hemisphere 2 "15/40"
- Finding: Hemisphere 2 sub-score printed as a fraction over 40; the Hemisphere-2 denominator is 60.
- Canonical controls (verified 2026-08-29): framework.html — "Hemisphere 2 — Quantitative Forensics … 60 points"; ch-64 dimension table sums 20+15+15+10 = 60.
- Remedy: correct the printed occurrence; qkey `canon_hemisphere2_max_points` (CLM-0001, value 60) is unchanged; CALC-0001/0002 guard the identity going forward.
- Proof: engine shows no `/40` VALUE collision on the hemisphere qkeys after the fix.
- Tracking: CON-0001 (open; exact occurrence pending corpus crawl).

### B — Canon Score 56–59
- Finding: investable in one chapter; barred from fresh capital in another.
- Verified side (2026-08-29): ch-66 Lesson 66.1 — "45 to 59: Watch list only. You track the company, you read its quarterly disclosures, **but you commit no fresh capital**." → RUL-0001 (T4, active).
- Unverified side: "56–59 investable" — candidate locations: ch-62 (SIP), ch-67 (long-term value), case studies 83–93. → RUL-0002 (T4 candidate, open).
- Remedy (per 09): the two prescriptions occupy the same tier and trigger, so a constitutional scoping is required — e.g., the permissive rule is regime-conditional ("eligible under regime R only") while the prohibitive rule stands, and the resolution sentence is printed where both bands are discussed. Closing this by editing one number would be an A-fix for a B — prohibited.
- Tracking: CON-0002 (open).

### C — Credit growth reads NEPSE 6–18 months ahead
- Finding: asserted as established market behaviour; no historical series test exists.
- Status decision (this charter): `NOT YET VALIDATED` (CLM-0010). The mechanism chapters are Part 0 (0.1 Credit Cycle, 0.2 NRB Transmission, 0.3 Liquidity Regimes).
- Remedy options: (i) EXH-001 (11) — collect NRB credit series + NEPSE index, run lead-lag + naive hit-rate with base rates, pre-registered per 08; (ii) if not run before 13.0 sign-off, rephrase every occurrence to: "the Canon hypothesises this mechanism; the evidence required to establish it is §EXH-001; current status: not yet collected."
- Prohibited: any present-tense predictive phrasing ("credit growth lets you read NEPSE ahead of the market") until a PASS verdict exists.
- Tracking: CON-0003 (open).

### D — Chilime rescore (found live this session, beyond the audit's 12)
- Finding: research/ states Chilime 62/100 "Adequate†"; "Chilime was damaged by the Bhotekoshi flood of 26 August 2026, one day after this analysis was completed. … the analysis predates that event and **has not yet been rescored**."
- This is the system working as intended: a D item is detectable from the corpus's own admission.
- Remedy: rescore (new VTG row, old SUPERSEDED) or re-affirm with an explicit "as of 25 Aug 2026, pre-flood" label and a dated rescore commitment. Blocks Phase 10 sign-off for that exhibit until closed.
- Tracking: CON-0004 (open).

## 4. Remediation record

Every closed conlog entry requires: `winner`, `loser` (or "re-scoped to …"), `printed_resolution` (the exact sentence the corpus will carry), and a QC re-run (Phase 10 G3) showing the collision is gone. Closure without these fields fails `validate`.
