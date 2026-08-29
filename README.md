# Santosh

Author repository for **The Investor's Canon** and its **Canon 13.0 Forensic Reconstruction**.

The forensic audit of edition 12.x concluded the book has an *evidence-governance* problem, not a writing problem. This repository holds the control system that tells the manuscript what is allowed to be true — built first, per the reconstruction charter, before any prose revision.

## Layout

```
canon13/
  00-charter.md            Red-team spec: diagnosis, architecture, standing rules, phase plan, live findings
  01-evidence-architecture.md   Source → Vintage → Claim → Calculation → Rule → Cross-reference → Status
  02-status-taxonomy.md    Nine controlled statuses + UNREVIEWED; language ceilings; transitions
  03-triage-protocol.md    Defect classes A (error) / B (contradiction) / C (unsupported) / D (stale)
  04-ledger-schema.md      Ledger field specification
  05-vintage-protocol.md   DATA VINTAGE formalized (tuple rule, re-verification pass, supersession)
  06-contradiction-engine.md  qkeys, collision types, resolution order
  07-canon-score-governance.md  Canon v1.0 as hypothesis: charter, disclosures, threshold governance
  08-validation-protocol.md     Calibration vs validation; pre-registration; survivorship/look-ahead
  09-constitution.md       T1–T6 decision-rule precedence; the 56–59 resolution shape
  10-source-apparatus.md   Source classes L0–L8; snapshot rule; provenance honesty
  11-empirical-exhibits-spec.md EXH-001 credit-growth/NEPSE lead; EXH-002/003 placeholders
  12-narrative-integrity.md Character register; cross-reference map; count convention
  13-final-qc-protocol.md  Gates G0–G8
  ledger/                  The live evidence ledger (TSV) + schema.json + corpus-map.tsv (127 pages)
  corpus/evidence/         Exact quotes backing the seeded ledger rows (fetched 2026-08-29)
  tools/canon_tools.py     extract / validate / contradictions / report (stdlib only)
  fixtures/                Deliberately broken corpus + ledger demonstrating the failure gates
  reports/                 Generated QC reports (baseline-2026-08-29.md)
```

## Quickstart

```bash
python3 canon13/tools/canon_tools.py validate --dir canon13/ledger
python3 canon13/tools/canon_tools.py contradictions --dir canon13/ledger
python3 canon13/tools/canon_tools.py report --dir canon13/ledger --edition-date 2026-08-29
python3 canon13/tools/canon_tools.py extract --corpus canon13/corpus/evidence --out /tmp/candidates.tsv
# failure-mode demo (intentionally broken fixture):
python3 canon13/tools/canon_tools.py validate --dir canon13/fixtures/ledger
```

## Baseline state (2026-08-29)

- `validate`: **PASS** (schema, referential integrity, status rules, arithmetic identities 40+60=100 and 20+15+10+15+15+15+10=100).
- `contradictions`: **FAIL by design** — 2 open real collisions: the 56–59 band (VALUE + RULE; the prohibitive side verified verbatim in Ch. 66) and its rule pair RUL-0001↔RUL-0002.
- `conlog`: 6 open items (CON-0001…0006), including two findings *beyond* the audit's 12 items (band-vocabulary duplication; the 118-vs-121 chapter count) and one live class-D supersession (Chilime 62/100 vs. the 26 Aug 2026 flood, "not yet been rescored").
- Corpus crawl: 6 of 127 pages fetched (direct network is blocked in this environment; pages are fetched one at a time through the review proxy). PRIORITY 1 targets are marked in `ledger/corpus-map.tsv`.

## Status

Phase 0 (control system) **complete**. Phases 1–3 (ledger population, vintage control, contradiction resolution) are proceeding against the public web edition and are blocked on fuller corpus access — see `canon13/00-charter.md` §8.
