# 10 — Source Apparatus (Phase 7)

## 1. The register

`ledger/sources.tsv` is the single source register, printed as the **Source Register** appendix in 13.x. Every SRC cited in the corpus resolves to one register row. No orphan citations; no citation without a register row.

## 2. Citation form

In print: `[SRC-####]`. Register row: `issuer, title, doc_no, date, url, snapshot_sha256, accessed, class`.

## 3. Snapshot rule (R6)

Regulatory and market pages mutate. Any web-sourced L0–L4 figure is captured as:
- `url` + `accessed` date, and
- `snapshot_sha256` — SHA-256 of the captured text (this session's captures are recorded against the fetched markdown text).
An edition's figures are pinned to the edition's snapshot set. "Verify against current filings" (the research pages' own disclaimer) is a *reader* instruction; the *book's* figures are still accountable to a named, dated snapshot.

## 4. Classes (restated with corpus instances)

| Class | Instance (verified this session) | Instance (pending) |
|---|---|---|
| L0 corpus | framework.html; ch-64; ch-66; research/ index; investors-canon index | remaining 118 chapter pages |
| L1 legislation/directive | — (Ch. 8 regulatory architecture names the architecture) | SEBON Act 2017; NRB Act 1993; specific directives cited in Chs. 1–3, 10, 110 |
| L2 regulator statistics | — | NRB reviews behind Ch. 64 ROE anchors (SRC-0006) |
| L3 exchange/depository | — | NEPSE index series for EXH-001; CDSC statistics |
| L4 company filings | — | Nabil/Chilime annual reports & SIFs behind the research pages |
| L5 academic/framework | MSCI quality-factor index construction (named in ch-66 Lesson 66.1) — **must be cited or marked "informed by"** | any named literature in Chs. 45–49, 79–82 |
| L6 author-derived | CALC-0001/0002 (structural identities) | EXH-001 outputs |
| L7 narrative/illustrative | Kavita/Suman report-card frame (ch-64 opening) — labeled by context; register check | all teaching examples |
| L8 internal audit | the forensic audit (SRC-0001); Canon 13.0 documents | — |

## 5. Provenance honesty

- A framework "used but not cited" prints as **informed by** (L5, no citation) — never as a citation. (The MSCI mention in ch-66 is the standing example to fix: either cite the MSCI quality-factor documentation or rephrase as "as quality-factor index providers do".)
- L8 never backs a market fact. The audit tells us what to check; it is not itself evidence that the market did X.
- L7 is excluded from validation entirely, but must be *registered* (narrative integrity, 12) so an illustrative number can never be read as a fact in later editions.
