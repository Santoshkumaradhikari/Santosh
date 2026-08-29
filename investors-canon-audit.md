# Deep Audit — The Investor's Canon
`https://santoshkumaradhikari.com.np/investors-canon/`
Audited 2026-08-29 · 128 HTML pages analyzed (hub + framework + glossary + study guide + whole-book page + 121 chapter pages + root site files)

---

## Scorecard

| Area | Grade | Summary |
|---|---|---|
| Link integrity | A+ | 0 broken internal links across all 128 pages; prev/next chain on all 121 chapters is perfect |
| Content accuracy | A | CGT chapter matches the actual FY 2083/84 budget (7.5% / 10%) — verified against current sources |
| On-page SEO basics | A− | Unique titles, unique meta descriptions, canonicals, JSON-LD on every page |
| Social / rich SEO | D | No `og:image`, no dates in schema, weak schema types |
| Accessibility | C+ | Good skip-links and ARIA labels, but real gaps in tables, dark mode, and the audio player |
| Trust & compliance | D | No investment disclaimer, no "last updated" dates, no cited sources |
| Performance | B− | Lean pages, but heavy font payload and a 4.9 MB "Whole Book" page linked in the global nav |
| Consistency | B | Three different footers, two of them contradicting the "Complete" claim |

---

## 🔴 High-impact mistakes

### 1. A confirmed dark-mode bug: table headers are nearly invisible
`table.figures th` uses `color: var(--bg)` on `background: var(--navy)`. In light mode that's fine (contrast 14.4:1). But in dark mode `--bg` becomes `#171310` (near-black) and `--navy` becomes `#1c2a45` (dark navy) — **contrast ratio 1.29:1**. Every table header in all 118 chapters is essentially unreadable for dark-mode users. This is the single clearest bug on the site.
**Fix:** in the dark `:root` block add `table.figures th { color: var(--ink); }` or define a dedicated `--table-th-text` variable.

### 2. No investment disclaimer anywhere
This is a 700,000-word book telling Nepali readers how to invest in NEPSE — including specific playbooks, position-sizing rules, and tax planning — and there is **no "this is not investment advice / educational purposes only" disclaimer** on the hub, the chapters, or the footer. The word "disclaimer" only appears incidentally inside 4 chapters' body text. For financial content this is a legal-exposure and credibility gap, and SEBON-adjacent content especially warrants it.
**Fix:** add a one-line disclaimer to the shared footer and a short disclaimer block on the hub page.

### 3. No dates anywhere — fatal for a book that promises to stay current
The site's core promise is "revised as Nepal's rules and data change," yet:
- No chapter shows a "Last updated" date.
- The JSON-LD `Article` schema has **no `datePublished` / `dateModified`** (Google increasingly requires these for article rich results).
- Every one of the 129 sitemap `<lastmod>` entries is the identical date (build-stamped), which search engines learn to ignore.

A reader on the Capital Gains Tax chapter has no way to know whether the FY 2083/84 rates shown are current or stale. **Fix:** stamp a per-chapter "Last verified: <date>" line and mirror it into `dateModified` in the schema; make the sitemap `lastmod` reflect real file changes (git commit dates).

### 4. Stale/contradictory footers — the site disagrees with itself about being finished
Three different footer texts are live simultaneously:
- Hub: *"The Canon is complete and is revised as…"* ✅
- All 121 chapters: *"The Investor's Canon is written and updated over time."* (vague)
- **Framework, Glossary, Study Guide: "New chapters are added as they're drafted."** ❌ — directly contradicts the hub's "✓ Complete — all 118 chapters drafted and published" banner.

**Fix:** unify to one footer (the hub's version).

### 5. No favicon, no `og:image` — broken presentation everywhere the site is shared
- Zero pages define a favicon / `apple-touch-icon` / `theme-color` / web manifest — browser tabs and phone home-screen saves show a blank default icon.
- Zero pages define `og:image` or `twitter:image` — every share on Facebook, WhatsApp, LinkedIn, X (major channels in Nepal) renders as a bare grey text card. For a project whose growth depends on sharing, this throws away free click-through.

**Fix:** one branded 1200×630 cover image + favicon set added to the shared `<head>`.

---

## 🟠 Medium-impact mistakes

### 6. The 4.9 MB "Whole Book" page is one tap away in the global nav
`book.html` is 4.9 MB of HTML (721,548 words, 126 `<h1>` tags). It's linked as "Whole Book" in the header of every page with no size warning. On a mobile data plan in Nepal that's an expensive accidental tap, and the page will freeze low-end phones while parsing.
**Fix:** add a size warning ("~5 MB — best on Wi-Fi/desktop"), and/or offer a pre-built PDF download instead. Also demote the compiled chapter `<h1>`s to `<h2>` (a document should have one `<h1>`).

### 7. No search or filter over 121 chapters
The hub is a single wall of 121 links. There's no search box, no filter, no collapsible parts. Finding "circuit breaker" means Ctrl+F or guessing which chapter covers it. For a reference work this size, client-side search (even a simple title filter input, ~20 lines of JS) is table stakes.

### 8. No in-chapter navigation for 6,000-word pages
Median chapter length is ~5,960 words with up to 9 `<h2>` sections — but **headings have no `id` attributes**, so there's no table of contents, no deep-linking to a section, and no way to cite "Chapter 8, section on SEBON" with a URL. **Fix:** auto-generate `id`s on `h2`/`h3` and render a small sticky TOC.

### 9. Zero sources or references in a data-heavy book
Chapters that quote NRB rates, tax tables, and historical NEPSE data (e.g. Ch. 35 tax tables, Ch. 106 "Data Handbook — Historical Almanac") contain **no external citation links at all** — the only external links on chapter pages are Google Fonts. For an "institution-grade" claim, uncited data is the biggest credibility gap. **Fix:** a short "Sources" block per chapter linking NRB, SEBON, NEPSE, IRD.

### 10. Accessibility gaps
- **All 118 chapters have data tables with no `scope` attributes and no `<caption>`** — screen readers can't associate header cells with data cells.
- The audio player has no `aria-live` region and no `aria-pressed` state — screen-reader users get no feedback that playback started, and "Paragraph X of Y" progress is silent.
- On no-JS browsers the header shows a dead audio button until JS hides it (the *hiding* itself requires JS to run).
- 121 pages use inline `onclick="window.print()"` — blocks any future strict CSP and mixes behavior into markup.

### 11. Mobile header will wrap into a 3-row stack
`.header-links` has 5 text links + 2 icon buttons and no mobile treatment (no hamburger, no priority collapse) — on a 360 px screen it wraps into a cluttered multi-row band on every one of 128 pages. The 640 px media queries only handle the hero, grids, and audio bar.

### 12. Wide tables have no horizontal-scroll fallback
`table.figures` is `width:100%` with no `overflow-x: auto` wrapper. The 5-column CGT table (Ch. 35) and the almanac tables will squeeze or overflow the 360 px viewport. **Fix:** wrap tables in `<div class="table-scroll" style="overflow-x:auto">`.

---

## 🟡 Low-impact / polish

13. **Schema types are weaker than they could be.** The hub is `WebPage` — it should be `Book` with `hasPart` chapters (or at least an `ItemList`); chapters could add `BreadcrumbList` and `position`/`isPartOf` with chapter numbers. This is the difference between plain and rich results.
14. **Font payload is heavy:** 3 families / 11 weight variants from Google Fonts (Fraunces + Source Serif 4 + Inter) on every page. Two families would look identical; self-hosting with `font-display: swap` subset to Latin would cut ~150–300 KB and a third-party connection.
15. **"118 chapters" arithmetic is fuzzy.** There are actually 121 chapter pages (0.1, 0.2, 0.3 + chapters 1–118). The hero says "Part 0 plus 18 parts and 118 chapters" and the badge says "all 118 chapters" — consistently phrased, but readers who count will notice. Say "121 chapters (Part 0's 3 frameworks + 118 chapters)" once, clearly.
16. **Hero copy is jargon-dense before the reader is oriented:** "A no-gap, execution-safe, 10-year investing operating system" uses three unexplained coinages in the first sentence of a book whose stated rule is "no term used before it's defined."
17. **`og:locale` is `en_US`** — should be `en_GB` (the prose uses "behaviour", "modelling") or ideally paired with `ne_NP` alternate; trivial but off-brand for a "Nepal Edition."
18. **`book.html` is absent from the sitemap** — actually *consistent* with its `noindex`, so fine, but worth confirming it's intentional.
19. **No analytics at all** — no way to know which chapters people read, where they drop off, or whether the audio feature is used. Even privacy-friendly analytics (GoatCounter/Plausible) would inform revisions.
20. **Every status pill says the same thing.** All 121 rows show "Read now →" — the pill column now carries zero information. Could be repurposed as reading time (e.g., "~25 min"), which the site currently doesn't show anywhere despite 6,000-word chapters.
21. **Glossary has 53 terms for a 700k-word book** — for comparison, the book defines far more terms in-line ("no term used before it's defined"). The glossary undersells the content; it also uses `<h3>`/`div` markup instead of semantic `<dl>/<dt>/<dd>`.

---

## ✅ What is genuinely well done (worth keeping)

- **Zero broken links** across all 128 pages — rare for a hand-built site of this size.
- **Perfect prev/next chapter chain** across all 121 chapters, verified programmatically against the hub's ordering.
- **Unique `<title>` and unique meta description on every single page** — no duplicates found.
- **Content is factually current:** the Capital Gains Tax chapter's 7.5% / 10% rates match the actual FY 2083/84 budget changes.
- Canonical URLs, `robots.txt` + sitemap, `noindex` on the compiled book page, skip-links, print styles, reduced-motion-safe design, dark mode, and a graceful no-JS fallback plan for the audio reader — all present and mostly correct.

---

## Top 5 fixes, in order

1. Fix the dark-mode table-header contrast bug (one CSS line).
2. Add a disclaimer + unified footer (removes the contradiction and the legal gap).
3. Add favicon + `og:image` (biggest sharing/branding win for the least work).
4. Add per-chapter "Last verified" dates + `dateModified` schema (protects the site's core promise).
5. Add heading `id`s + a chapter TOC, and a title-filter search on the hub (biggest usability win).
