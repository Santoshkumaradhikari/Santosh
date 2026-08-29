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

## State (2026-08-29, after full-corpus capture)

**Corpus: fully captured.** The user's site-source repo was cloned and every page is now a sha-256-pinned text snapshot: **126 pages, 721,294 words** in `canon13/corpus/snapshot-2026-08-29/` (manifest alongside). Blocker B1 is resolved.

- `validate`: **PASS** (19 claims, 3 rules, 13 sources, 6 calculations, 12 characters; arithmetic identities 40+60=100, 20+15+10+15+15+15+10=100, plus Nabil 12+11+10+6+13+10+9=71 and the three H2 sums).
- `contradictions`: **FAIL by design** — 3 open VALUE/RULE clusters + 1 temporal:
  - the 55–59 band: ch-64 "Adequate — investable" (ch-64:139) vs. ch-66 "45–59 no fresh capital" (RUL-0001 ↔ RUL-0003);
  - the Hemisphere-2 denominator: canonical 60 vs. "out of 40" printed in ch-91:70, ch-92:82, ch-93:82 (the audit's "15/40");
  - CLM-0007 as-of 2026-08-25 (pre-flood Chilime 62/100) vs. edition date.
- All six conlog items (CON-0001…0006) are now **located** with exact `file:line` in the snapshot; every ledger claim carries `first_seen`/`xrefs` into the snapshot.
- New findings beyond the audit's 12: band-system duplication (ch-64 bands vs. ch-66 tiers), the 118-vs-121 chapter count, and character-register flags (Keshav↔Rukmini bio parallel; Suman/Suman Gurung and Kavita/Kabita name collisions; Bimala recurring in ch-59/80/85).

## Status

Phase 0 (control system) **complete**. Phase 1 (evidence ledger) **in progress and unblocked** — full corpus is in; remaining blockers are B2 (full 12-item audit text) and B3 (NRB/NEPSE primary data for EXH-001 and ROE verification). Next: populate remaining audit items, then Phase 3 remediation of the class-A denominator errors.
