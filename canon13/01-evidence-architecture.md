# 01 — Evidence Architecture

The seven-element chain. Every factual or quantitative statement in the Canon is an instance of all seven elements (some may be empty *only* where the status allows).

## 1. Source (`SRC-####`, `ledger/sources.tsv`)

Where the knowledge physically comes from. Classes:

| Class | Meaning | Examples in this corpus |
|---|---|---|
| **L0** | The Canon itself, public edition (corpus pages) | framework.html; ch-64; ch-66; research/ pages |
| **L1** | Legislation & directives | NRB Act 1993; SEBON Act 2017; Companies Act 1964; NRB directives; SEBON regulations |
| **L2** | Regulator statistics & reviews | NRB monetary/credit reviews (source of Ch. 64 ROE anchors); SEBON market statistics |
| **L3** | Exchange & depository data | NEPSE index/trade data; CDSC statistics |
| **L4** | Listed-company filings | Annual reports, SIFs, SEBON/CDSC disclosures |
| **L5** | Academic / framework provenance | MSCI quality-factor methodology (cited by name in Ch. 66); any named literature |
| **L6** | Author-derived | Computations, estimates (must link a CALC row) |
| **L7** | Narrative / illustrative | Fictional or hypothetical teaching examples (must be labeled in print) |
| **L8** | Internal audit / red-team | The forensic audit; Canon 13.0's own documents. **Never** a source for market facts. |

Fields: `id, class, issuer, title, doc_no, date, url, snapshot_sha256, accessed, notes`.
Web sources require `url` + `snapshot_sha256` (hash of the captured text) + `accessed` (R6).

## 2. Vintage (`VTG-####`, `ledger/vintages.tsv`)

Every external quantity is a tuple, never a bare value:

```
(value, unit, as_of, effective_from, superseded_by?, source_id)
```

- `as_of`: the date the value was true/observed. Required.
- `effective_from`: when the underlying rule/data started (for regulations: the directive's effective date, not the publication date).
- `superseded_by`: link to the VTG row that replaced it (append-only, R5).
One `VTG` row per (quantity, as_of) observation. A quantity's history is the list of its VTG rows. Protocol: `05-vintage-protocol.md`.

## 3. Claim (`CLM-####`, `ledger/claims.tsv`)

An atomic, checkable proposition. **Atomicity rule:** one subject + one quantity + one period + one relation. "NEPSE fell 12% in 2020 and credit contracted" is two claims.

Fields: `id, status, qkey, statement, value, unit, as_of, superseded_by, source_id, calc_id, rule_refs, xrefs, first_seen, audit_ref, notes`.

**Two-row pattern (critical):** when the book *states* something that is also a *claim about the world*, use two rows:
- the **stated fact** — "Ch. 66 states 45–59 commits no fresh capital" — status `FACT—VERIFIED` against the corpus (L0 source); and
- the **world claim** — "committing no fresh capital at 45–59 is the right action" — status `AUTHOR'S HYPOTHESIS` / `NOT YET VALIDATED` until tested.
Conflating these two is how F2 (epistemic overreach) is written into prose.

## 4. Calculation (`CALC-####`, `ledger/calculations.tsv`)

Derivation: `id, output_claim, formula, notes`.
- `DERIVED—CALCULATED` claims must link a CALC row.
- A formula that evaluates to a number must equal the output claim's value (the tool checks this; a mismatch is an automatic **class A** finding).
- Hemispheric identity checks live here: `40+60 = 100` (verified 2026-08-29); `20+15+10+15+15+15+10 = 100`.

## 5. Rule (`RUL-####`, `ledger/rules.tsv`)

A prescriptive decision instruction: `id, statement, domain, tier, conflicts_with, resolution, status, xrefs, notes`.
- `tier`: T1–T6 per `09-constitution.md`. A rule without a tier may not print as a decision rule.
- `status`: `active` | `open` (in unresolved conflict) | `superseded`.
- Every rule the corpus prints must carry `[RUL-####, T#]` in print.

## 6. Cross-reference (`xrefs`)

Every claim and rule lists **all** its corpus occurrences: `file:line;file:line;…`.
- Occurrences may paraphrase; the **canonical value is the ledger's** (qkey governs identity, `06`).
- Completeness is a gate: an occurrence not in `xrefs` is invisible to the engine and counts as an F1 defect when found in QC.

## 7. Validation status

One of the nine print statuses (+ `UNREVIEWED` in-pipeline). Transitions happen only through documented review events; the `notes` field records each transition with a date. Spec: `02-status-taxonomy.md`.

## Worked example (real data)

**"Hemisphere 2 of the Canon Score is worth 60 points."**

1. **Source:** SRC-0003 (framework.html, L0) + SRC-0002 (ch-64, L0); accessed 2026-08-29.
2. **Vintage:** not vintage-sensitive (a defined constant of Canon v1.0, versioned instead — VTG-0002 pattern).
3. **Claim:** CLM-0001, qkey `canon_hemisphere2_max_points`, value `60`, status `FACT—VERIFIED`.
4. **Calculation:** CALC-0001 `40+60 → 100` (hemispheric identity); CALC-0002 `20+15+10+15+15+15+10 → 100` (dimension identity).
5. **Rule:** none directly; feeds RUL rows on bands (T4).
6. **Cross-reference:** framework rubric block; ch-64 Lesson 64.1 table; research index ("100-point rubric across seven dimensions").
7. **Status:** FACT—VERIFIED (three concordant corpus pages; no as-of needed because it is a versioned constant, not an observed fact).

The audit's "15/40" finding is then simply: some occurrence of a Hemisphere-2 sub-score asserts a denominator of 40 → VALUE collision against CLM-0001 → CON-0001 (class A) → fix the occurrence, ledger unchanged.
