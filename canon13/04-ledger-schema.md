# 04 — Evidence Ledger (schema)

The ledger is the single controlled state of "what is allowed to be true." Files under `canon13/ledger/`:

| File | ID prefix | Holds |
|---|---|---|
| `claims.tsv` | CLM-#### | Atomic factual/quantitative/hypothetical propositions |
| `vintages.tsv` | VTG-#### | (quantity, value, as_of, supersession) history |
| `rules.tsv` | RUL-#### | Prescriptive decision rules with constitution tier |
| `sources.tsv` | SRC-#### | Source register (classes L0–L8, snapshots, access dates) |
| `calculations.tsv` | CALC-#### | Derivations checked mechanically |
| `conlog.tsv` | CON-#### | Triage & remediation log (types A/B/C/D) |
| `tests.tsv` | TEST-#### | Pre-registered validation tests and verdicts |
| `characters.tsv` | CHAR-#### | Narrative register (Phase 9) |
| `corpus-map.tsv` | CM-#### | Corpus inventory: every page, URL, fetch/snapshot state |
| `schema.json` | — | Machine-readable field spec consumed by `tools/canon_tools.py validate` |

## Field notes

### claims.tsv
`id, status, qkey, statement, value, unit, as_of, superseded_by, source_id, calc_id, rule_refs, xrefs, first_seen, audit_ref, notes`
- `qkey`: the quantity's canonical identity (snake_case). **One qkey = one canonical value.** All other occurrences are xrefs. See 06.
- `value`: the canonical value (number, ratio, or controlled vocabulary token such as `no_fresh_capital` / `investable`).
- `xrefs`: `file:line;file:line;…` — every corpus occurrence.
- `first_seen`: where the claim was first extracted/identified.
- `audit_ref`: link to the audit finding (AUD-##) when applicable.

### vintages.tsv
`id, qkey, value, unit, as_of, effective_from, superseded_by, source_id, notes`
- One row per (qkey, as_of) observation. `superseded_by` non-empty ⇔ the row is superseded (append-only, R5).

### rules.tsv
`id, statement, domain, tier, conflicts_with, resolution, status, xrefs, notes`
- `tier`: T1–T6 (09). `status`: `active` | `open` | `superseded`.
- A rule may not print as a decision instruction without `id` + `tier`.

### sources.tsv
`id, class, issuer, title, doc_no, date, url, snapshot_sha256, accessed, notes`
- `class`: L0–L8 (01 §1 / 10). Web sources require `url` + `snapshot_sha256` + `accessed` (R6).

### calculations.tsv
`id, output_claim, formula, notes`
- `formula`: arithmetic expression over constants (tool-safe). If it evaluates to a number and the output claim's value parses as a number, the two must agree (class A check).

### conlog.tsv
`id, type, item_refs, description, winner, loser, printed_resolution, status, notes`
- `type`: A | B | C | D (03). `status`: `open` | `closed`.
- Closure requires `winner` + `printed_resolution` (enforced by `validate`).

### tests.tsv
`id, hypothesis_ref, data_window, method, criteria, registered_at, result_at, verdict, limitations, notes`
- `hypothesis_ref` → a CLM row. `verdict`: PASS | FAIL | INCONCLUSIVE (08).

### corpus-map.tsv
`id, kind, chapter, part, volume, title, url, fetched, status, snapshot_sha256, words`
- `kind`: chapter | framework | research | index | home.
- `status`: `fetched` | `pending`. `snapshot_sha256` set when the page text is captured locally.

## Conventions

- TSV, UTF-8, one header row, no embedded tabs. Semicolon-separated ref lists.
- IDs are unique and never reused. Retired rows are marked SUPERSEDED/superseded, never deleted (R5).
- Status tokens are canonical (em-dash form, 02). The tool compares them case-insensitively with dash normalization, but the files must use the canonical tokens.
