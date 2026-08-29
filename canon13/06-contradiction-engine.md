# 06 — Contradiction Engine

Phase 3. Detects and drives resolution of every duplicated quantity and conflicting rule. Two detection layers:

1. **Automated** — `tools/canon_tools.py contradictions` (mechanical, qkey-based).
2. **Manual/structural** — duplicates the engine cannot see without semantics (arithmetic implied by a printed fraction, prose paraphrases across chapters). These enter via triage (03) as A/B items.

## 1. Quantity keys (qkey)

The engine's identity relation. Rules:
- One qkey per distinct quantity, corpus-wide: `canon_score_max`, `canon_hemisphere1_max_points`, `canon_hemisphere2_max_points`, `canon_weight_vector_v1`, `canon_band_45_59_action`, `nrb_bank_roe_q3_fy2425`, `canon_score_chilime`, …
- A claim row owns the **canonical value** for its qkey. Every other occurrence in the corpus is an xref that must agree with the canonical value (or be a documented historical/SUPERSEDED use).
- New qkeys are created by the ledger owner; two qkeys for the same quantity is itself an F1 defect.

## 2. Collision types

| Type | Definition | Detected by |
|---|---|---|
| **VALUE** | Same qkey, different asserted values (across claims, or claim vs. its VTG row at the same as-of). | automatic |
| **RULE** | Two rules with overlapping trigger and different action (`conflicts_with` set, no `resolution`). | automatic (via conlog/rules) |
| **ARITHMETIC** | A CALC formula evaluates to a number that disagrees with the output claim's value. | automatic (validate) |
| **TEMPORAL** | A printed-as-current claim whose as-of predates the edition date without a re-verification event (class D). | automatic with `--edition-date` |
| **VOCAB** | Two ungoverned naming systems for the same quantity (e.g., band labels: "Strong/Adequate" vs. screening tiers). | manual → B item |

## 3. Resolution order

1. **RULE** collisions: constitution tier (09) decides. Higher tier wins; a lower tier may restrict but never widen. The resolution sentence is printed (R4).
2. **VALUE** collisions: for FACTs, the latest *verified* vintage wins; the losing row becomes SUPERSEDED. For stated-facts (L0), the corpus occurrence is corrected (class A).
3. **TEMPORAL**: re-verification pass (05) — either superseded or re-affirmed with a new as-of.
4. **ARITHMETIC**: re-derive; the correct value wins; the wrong occurrence is a class A fix.

## 4. Gate semantics

- `contradictions` exits non-zero while any open VALUE or RULE collision exists. Phase 10 sign-off requires exit zero, or an explicit, documented, constitutionally-scoped residual (recorded in conlog with `printed_resolution`).
- TEMPORAL findings are warnings in the gate but **defects at sign-off**: a stale un-re-verified number in a "current" book is exactly the F1 failure.

## 5. Current open collisions (baseline 2026-08-29)

| qkey / rules | Collision | Tracking |
|---|---|---|
| `canon_band_45_59_action` (CLM-0004 `no_fresh_capital` vs. CLM-0005 `investable`) + RUL-0001 ↔ RUL-0002 | VALUE + RULE | CON-0002 |
| Band vocabulary (tiers vs. Strong/Adequate) | VOCAB → B | CON-0005 |
| Hemisphere-2 denominator (occurrence pending crawl) | ARITHMETIC/VALUE (latent) | CON-0001 |
| Chilime 62/100 vs. post-flood reality | TEMPORAL/D | CON-0004 |
