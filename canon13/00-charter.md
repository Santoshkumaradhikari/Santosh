# Canon 13.0 — Forensic Reconstruction Charter

**Status:** RED-TEAM SPEC v0.1 · 2026-08-29
**Scope:** The Investor's Canon — 4 volumes, Part 0 (0.1–0.3) + Parts I–XVIII (chapters 1–118) = 121 chapter pages, plus the framework page and published research (Nabil Bank, Chilime Hydropower). Public web edition at santoshkumaradhikari.com.np is the verification baseline until a private manuscript export supersedes it.
**Baseline:** the forensic audit of edition 12.x (≈700k words / 2,475 pages per audit; page count to be re-measured in Phase 10).

## 0. Accepted diagnosis

The book's problem is not writing. It is **evidence governance**. Three failure classes:

- **F1 — Version control failure.** Regulatory and market inputs are duplicated across chapters instead of centrally governed. *Confirmed live this session:* the Canon Score band vocabulary exists in at least two ungoverned systems (Chapter 66 screening tiers vs. the research pages' "Strong/Adequate" labels) over the same 0–100 score.
- **F2 — Epistemic validation failure.** The Canon Score, the regime framework (Ch. 0.3 four-phase model) and the ADV Rule (Ch. 56) are presented more confidently than their empirical validation permits.
- **F3 — Decision-rule collision.** Different parts instruct a disciplined reader to opposite actions. *Confirmed live this session:* Chapter 66 states 45–59 "commit no fresh capital"; the audit reports another part presenting 56–59 as investable (occurrence pending crawl).

**Positive finding (accepted):** the book already contains the repair methodology — Claim → Evidence → Verification, DATA VINTAGE (Ch. 107 "Keeping the Canon Current", Ch. 110 "Regulatory Change Tracker"), point-in-time case studies, a whole Calibration & Backtesting part (Chs. 79–82), and disclosed failed calls (Ch. 89 bank failure). Canon 13.0 makes that methodology the *governing system* and runs the corpus through it.

## 1. Prime directive

> **Do not start rewriting the corpus. Build the control system that tells the manuscript what is allowed to be true.**

A prose revision without the control system regenerates the same contradictions. Revision happens *as the application* of this system, phase by phase.

## 2. Evidence architecture — the seven-element chain

Every factual or quantitative statement in the corpus is an instance of:

```
Source → Vintage → Claim → Calculation → Rule → Cross-reference → Validation status
```

- A claim without a source is either ASSUMPTION, ILLUSTRATIVE, or AUTHOR'S HYPOTHESIS — it may not print as a fact.
- A claim with a source but no effective date is at most FACT—VINTAGE-SENSITIVE and must carry an as-of date.
- A rule without a precedence tier (09) may not print as a decision rule.
- A quantitative claim without a quantity key (qkey) is invisible to the contradiction engine — by definition, ungoverned.

Full field specification: `01-evidence-architecture.md`.

## 3. Controlled status set (nine print statuses + one pipeline status)

`FACT—VERIFIED` · `FACT—VINTAGE-SENSITIVE` · `DERIVED—CALCULATED` · `ASSUMPTION` · `ILLUSTRATIVE` · `AUTHOR'S HYPOTHESIS` · `EMPIRICALLY VALIDATED` · `NOT YET VALIDATED` · `SUPERSEDED` — plus `UNREVIEWED`, which exists only in the ledger pipeline and may never print.

Each status has required fields, permitted transitions, and a **language ceiling** (the maximum confidence the corpus may use for it). Spec: `02-status-taxonomy.md`.

## 4. Triage — three (now four) defect classes, never conflated

| Class | Meaning | Remedy |
|---|---|---|
| **A — Error** | Arithmetic or factual mistake. Ex.: Hemisphere 2 printed "15/40" against a denominator of 60. | Correct the value; all xrefs inherit. |
| **B — Contradiction** | Two parts prescribe different actions/values. Ex.: 56–59 investable vs. barred. | Governance: assign precedence tiers, pick the winner, **print the resolution**. |
| **C — Unsupported proposition** | More confidence than evidence. Ex.: credit growth reads NEPSE 6–18 months ahead. | Add the evidence (a registered test) or reduce confidence language to the ceiling. |
| **D — Stale / supersession-pending** *(introduced by this system)* | A dated fact is known to be out of date; supersession not yet executed. Ex.: Chilime 62/100 predates the 26 Aug 2026 flood; "has not yet been rescored." | Execute supersession (new VTG row, old SUPERSEDED) or explicitly re-affirm with a new as-of. |

Never remediate a B with an A-fix. Never remediate a C with an A-fix. Spec + decision tree: `03-triage-protocol.md`.

## 5. Phase plan (entry/exit criteria)

| # | Phase | Entry | Exit | Primary artifacts |
|---|---|---|---|---|
| 0 | Control system | audit accepted | charter + schema + toolkit working | `canon13/00–13`, `ledger/`, `tools/` |
| 1 | Evidence ledger | corpus pages crawlable | every quantitative sentence → candidate; every material claim → CLM row with status | `ledger/claims.tsv` populated |
| 2 | Vintage control | P1 | every external number has a VTG row (as_of, source, supersession) | `ledger/vintages.tsv`; DATA VINTAGE box spec |
| 3 | Contradiction engine | P1+P2 | all VALUE/RULE collisions resolved or constitutionally scoped; A/B items closed | `contradictions` gate green |
| 4 | Canon Score reconstruction | P3 | v1.0 chartered as hypothesis; thresholds + governance overrides fixed | `07` completed; band RUL rows |
| 5 | Validation protocol | P4 | pre-registered test defined for every hypothesis | `tests.tsv` registered rows |
| 6 | Constitution | P3 | every decision rule has tier + ID; every resolution printed | `09` + rule audit pass |
| 7 | Source apparatus | P1 | every SRC cited with snapshot + access date; Source Register appendix | `sources.tsv` + appendix template |
| 8 | Empirical exhibits | P5 | EXH-001 run with verdict; claim promoted or downgraded | `exhibits/` + test verdicts |
| 9 | Narrative integrity | P3 | register, xrefs, names, self-references all close | `characters.tsv` + checklist |
| 10 | Final forensic QC | P1–P9 | gates G1–G8 pass; regression diff vs. 12.x ledger clean | `reports/qc-13.0.md` |

## 6. Standing rules (non-negotiable)

- **R1.** No quantitative statement prints without a ledger ID (exception: labeled ILLUSTRATIVE/ASSUMPTION, which must be registered).
- **R2.** The Canon Score v1.0 weighting is a **hypothesis, not an empirically established optimum** (07). It is disclosed as such in print.
- **R3.** The credit-cycle lead claim is NOT YET VALIDATED until EXH-001 (11) runs (08).
- **R4.** Rule collisions are resolved by the constitution (09) and the resolution is printed in the corpus.
- **R5.** Supersession is append-only. SUPERSEDED rows are never deleted; they carry `superseded_by`.
- **R6.** Web-sourced regulatory/market figures require a dated snapshot with SHA-256 (source apparatus, 10).
- **R7.** Any change to a quantity's value updates the ledger (value, vintage, supersession) in the same change.
- **R8.** Post-revision, the full corpus is re-scanned (13). A revision passes only with zero open VALUE/RULE collisions and zero unexplained value regressions.

## 7. Findings log — live (this session, 2026-08-29)

Verified against the public edition on the day of this charter:

1. **F1 live instance:** two band vocabularies for one score (CON-0005).
2. **F3 live instance (BOTH SIDES VERIFIED, 2026-08-29 full-corpus sweep):** Ch. 66 Lesson 66.1 — "45 to 59: Watch list only … you commit no fresh capital" vs. **Ch. 64 band table (ch-64:136-140) — "55 – 69: Adequate — investable, but size the position carefully and watch the weak dimensions"**. Overlap 55–59 is where the book contradicts itself (CON-0002; RUL-0001 ↔ RUL-0003). Case studies ch-87/88 and both research pages follow ch-64's bands.
3. **F2 live instance (candidate):** Ch. 64 ROE anchors ("13% Q3 FY2022/23 → under 8% Q3 FY2024/25"; "7.73% system-wide, 15.8% to under 1%") — book-stated, externally unverified; triage path to FACT—VINTAGE-SENSITIVE via NRB.
4. **D live instance:** Chilime 62/100 (analysis complete 25 Aug 2026) vs. flood damage 26 Aug 2026; "not yet been rescored" (CON-0004, open).
5. **Vagueness instance:** Ch. 66 REGULATORY DETAIL states SEBON filing deadlines as "a set number of days" — a verifiable specific exists in the regulation; the corpus must state the number + source or stay non-specific.
6. **Provenance instance:** Ch. 66 cites MSCI quality-factor index construction by name — L5 academic/framework provenance; must be cited or marked "informed by".
7. **Count instance (VERIFIED, 2026-08-29):** "118 chapters" self-references found at ch-117:105, ch-118:75/85/87, framework:37-38, home:11; TOC has 121 chapter pages (Part 0 + 1–118). Convention coherent but undeclared (CON-0006).
8. **Class-A instance (audit's "15/40" LOCATED, 2026-08-29):** Hemisphere 2 denominator printed as 40 in **three** case studies: ch-91:70 ("15 out of 40"), ch-92:82 ("20 out of 40"), ch-93:82 ("29 out of 40") vs. canonical 60 (CON-0001; CLM-0014/0015/0016; the audit quoted the ch-91 line). Sums themselves are arithmetically correct (CALC-0004…0006).
9. **C-class instance (WORDING PINNED, 2026-08-29):** credit lead claim at ch-0-1:23 ("reading the equity market six to eighteen months in advance"), :44 ("causal, not merely correlated"), :47 ("consistently predictive of NEPSE direction 3–12 months forward"), lag table :87-91, 2021 example :119 (CON-0003; CLM-0010; EXH-001 target defined).

The audit's remaining items (CON-0007…CON-0012) are seeded once the full 12-item audit text is supplied.

## 8. Blockers

- **B1. RESOLVED (2026-08-29):** Full corpus captured via the user's site-source repo (`santoshkumaradhikari.github.io`, cloned to `canon-corpus-src/` outside the repo): **126 pages, 721,294 words**, sha-256-pinned text snapshot at `corpus/snapshot-2026-08-29/` with manifest; `ledger/corpus-map.tsv` fully populated (CM-0001…0126). The private 12.x manuscript (2,475 pp.) is still unknown — if it diverges from the public edition, a second snapshot supersedes this one.
- **B2.** Full 12-item audit text not yet in the repo (3 exemplar findings + summary received in session).
- **B3.** NRB/SEBON/NEPSE/CDSC primary data for EXH-001 and ROE verification not yet collected.
