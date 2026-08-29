# 12 — Narrative Integrity (Phase 9)

Fictional and structural continuity is part of evidence governance: a disciplined reader tracks characters, cross-references, and self-references the same way they track a score. Inconsistencies there erode trust in the quantitative claims.

## 1. Character register (`ledger/characters.tsv`)

Known roster as of 2026-08-29 (crawl in progress; expect growth):

| ID | Name | First verified occurrence | Notes |
|---|---|---|---|
| CHAR-0001 | Keshav | corpus:pending (named in audit) | continuity/arc check open — audit finding |
| CHAR-0002 | Bimal | corpus:pending (named in audit) | continuity/arc check open — audit finding |
| CHAR-0003 | Rukmini | corpus:pending (named in audit) | continuity/arc check open — audit finding |
| CHAR-0004 | Kavita | ch-64 opening (report-card frame, Falgun, Biratnagar) | framing device; check reuse consistency |
| CHAR-0005 | Suman | ch-64 opening (Kavita's father, taxi driver, Biratnagar) | as above |

Rules:
- Every character has one canonical row; aliases recorded in `aliases`.
- **Duplicate-name check:** any proper noun colliding with a registered name across chapters must be adjudicated (same person? different person? typo?) and recorded. The audit flagged duplicate character names — the register is the fix mechanism.
- **Continuity table** (built during the crawl): (chapter, character, state/event). Contradictions between chapters → conlog items (class A or B as applicable).
- State transitions (jobs, locations, marriage, wealth level, "died in the story" etc.) are one-directional unless the text explicitly reverses them — a reversal without an explicit text event is a defect.

## 2. Cross-reference map (chapter/Part/section)

- Every in-corpus reference — "Part N", "Chapter N", "Lesson N.M", "see §…" — must resolve to an existing unit. The corpus is 121 chapter pages + Part 0; references to a "chapter 119" or an unnumbered Part are defects.
- **Count consistency:** the site self-describes "118 chapters" while the TOC contains 121 chapter pages (Part 0's 0.1–0.3 plus 1–118) — CON-0006 (open). Decide the counting convention, state it once (framework page), and align every self-reference to it.
- **Self-references:** the book referring to itself (edition, part structure, "this chapter") must match the actual structure of the edition being published. Ch. 117 ("The Canon Audit — Annual Self-Assessment") and Ch. 107 ("Keeping the Canon Current") are the natural homes for the Canon 13.0 governance disclosures and should be rewritten to point at the ledger-based system.

## 3. Volume/Part structure check

Framework page lists: V1 = Parts 0, I–IV (ch. 0.1–23); V2 = V–IX (24–49); V3 = X–XV (50–82); V4 = XVI–XVIII (83–118). Verify each volume page's part list against this map during the crawl; mismatches → conlog.

## 4. Exit criteria (gate G7)

1. Zero unresolved chapter/Part/section references.
2. Zero unadjudicated name collisions.
3. Every audit-flagged continuity item (Keshav/Bimal/Rukmini + full 12-item list when supplied) has a resolution or a deliberate-retrofit note.
4. Count convention decided and consistently printed.
5. Self-reference chapters (107, 117) point at the live governance system.
