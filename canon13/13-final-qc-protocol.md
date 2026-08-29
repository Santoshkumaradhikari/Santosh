# 13 — Final Forensic QC (Phase 10)

The revision passes only when **all** gates pass. Gates run against the full corpus re-scan, after revision — the audit's requirement that we verify the fixes did not create new contradictions.

## Gates

| Gate | Check | Tool / method | Pass criterion |
|---|---|---|---|
| **G0** | Corpus measured | extract + word count | actual page/word counts recorded; audit's "2,475 pp / 700k words" confirmed or corrected (vintage-sensitive: measured per edition) |
| **G1** | Coverage | `extract` over full corpus | every quantitative sentence maps to a ledger row or is registered ILLUSTRATIVE/ASSUMPTION; zero unowned candidates |
| **G2** | Ledger health | `validate` | zero schema/referential/status/arithmetic errors |
| **G3** | Contradictions | `contradictions` | zero open VALUE/RULE collisions; TEMPORAL findings all re-verified or superseded; every closure has winner + printed_resolution |
| **G4** | Vintage pass | 05 §3 re-verification | every FACT—VINTAGE-SENSITIVE claim re-checked against a current snapshot; supersessions recorded (append-only) |
| **G5** | Status print audit | manual + spot automation | no hypothesis prints unlabeled; no claim above its language ceiling (02); all verified figures carry as-of; all rules carry [RUL, T] |
| **G6** | Constitution audit | `rules.tsv` + corpus spot-check | every printed decision rule has id+tier; zero open RULE collisions; resolutions printed |
| **G7** | Narrative | 12 §4 | all five exit criteria |
| **G8** | Regression | ledger(13.x) diff vs. ledger(12.x) | every value change has a supersession or correction event; no unexplained quantity regressions; no qkey lost |

## Report

`tools/canon_tools.py report --dir ledger/ --edition-date <date> --out reports/qc-13.0.md` produces the machine-readable summary (ledger sizes, status counts, engine detections, hotspots, open conlog). The QC report embeds it plus:

- **Open items register** — anything not closed, with owner and due date (nothing may be silently dropped; open items are either fixed or constitutionally-scoped with printed resolutions).
- **Supersession log** — every VTG/CLM supersession this edition, in order.
- **Sign-off** — author name + date + the statement: "The 13.x corpus was re-scanned in full; gates G0–G8 are green; open items are listed with resolutions."

## Re-run rule

Any post-sign-off change to a quantity, rule, or status re-opens G2–G5 for the affected qkeys and G3 globally. The ledger is the source of truth; the prose is its rendering.
