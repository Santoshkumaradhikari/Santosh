# 05 — Vintage Control (DATA VINTAGE protocol)

The book already has DATA VINTAGE as a concept (Ch. 107 "Keeping the Canon Current", Ch. 110 "Regulatory Change Tracker"). This protocol formalizes it as governance.

## 1. The tuple rule

No external number appears in the corpus without the tuple `(value, unit, as_of, effective_from, source)`. A number without an as-of is a ledger defect (it will be caught by G4 in Phase 10).

## 2. Printed form

- **Chapter DATA VINTAGE box:** every chapter that quotes external data prints a box listing each input's as-of (e.g., "NRB base rate — as of 31 Mar 2025; NEPSE close — 28 Aug 2025; Ch. 64 ROE anchors — 9 months to Q3 FY2024/25"). The box is the chapter's supersession surface: it shows at a glance what is dated and how old.
- **Inline form:** "X as of \<date\>" for single figures.

## 3. Re-verification pass (each edition)

1. Scan all claims with status `FACT—VINTAGE-SENSITIVE` (and `FACT—VERIFIED` whose as-of predates the edition date — class D candidates).
2. For each, fetch the current source snapshot (R6) and compare.
3. Same value → advance the as-of, keep the row (verification event noted).
4. Different value → create the new VTG row; the old row becomes SUPERSEDED (R5, append-only); the print updates; the edition changelog lists the supersession.
5. **Silent in-place edits of a value without a ledger event are prohibited (R7).**

## 4. Supersession is a state, not an edit

`VTG.superseded_by` + `CLM.superseded_by` encode replacement. The corpus never "forgets" a value: a superseded figure remains citable as historical ("the rate stood at 6.25% as of 31 Mar 2025; it is now …"). This is what makes the book auditable across editions — and what the audit's version-control finding (F1) says was missing.

## 5. Live exemplars in the current corpus

| Item | as-of | Status |
|---|---|---|
| Chilime 62/100 (research page) | analysis complete 25 Aug 2026 (flood 26 Aug 2026) | **D — supersession pending** (CON-0004); corpus admits "has not yet been rescored" |
| Ch. 64 ROE anchors (13% → <8%; 7.73% system-wide) | 9 months to Q3 FY2024/25 (book-stated) | re-verification against NRB pending (SRC-0006) |
| Ch. 66 SEBON filing deadlines | stated non-specifically ("a set number of days") | must be pinned to the regulation's actual number + source, or stay non-specific with a pointer |

## 6. Regulations specifically

For L1 sources (directives, regulations): `effective_from` is the directive's effective date, `as_of` is the snapshot date. When a directive is amended, the old VTG row is superseded by the amendment's row, and any chapter that depends on the old figure is flagged by qkey for re-read. This is the mechanism that prevents the "chapter 2 quotes the 2019 rule, chapter 110 quotes the 2026 rule" class of F1 defect.
