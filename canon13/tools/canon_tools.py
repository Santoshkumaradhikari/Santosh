#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
canon_tools - Canon 13.0 evidence-governance toolkit.

Subcommands
  extract         Scan a corpus of text files for quantitative candidate claims (Phase 1).
  validate        Schema, referential-integrity, status, and arithmetic checks on the ledger.
  contradictions  Detect VALUE / RULE / TEMPORAL collisions (Phase 3 gate).
  report          Markdown summary of ledger state (Phase 10 gate input).

Standard library only. Python >= 3.8.
Ledger layout: <dir>/{schema.json, claims.tsv, vintages.tsv, rules.tsv,
sources.tsv, calculations.tsv, conlog.tsv, tests.tsv, characters.tsv,
corpus-map.tsv}
"""
from __future__ import annotations

import argparse
import ast
import csv
import json
import operator
import re
import sys
from datetime import date, datetime
from pathlib import Path

EMD = "\u2014"
ST = {
    "unreviewed": "UNREVIEWED",
    "verified": "FACT%sVERIFIED" % EMD,
    "vintage": "FACT%sVINTAGE-SENSITIVE" % EMD,
    "derived": "DERIVED%sCALCULATED" % EMD,
    "assumption": "ASSUMPTION",
    "illustrative": "ILLUSTRATIVE",
    "hypothesis": "AUTHOR'S HYPOTHESIS",
    "validated": "EMPIRICALLY VALIDATED",
    "notvalidated": "NOT YET VALIDATED",
    "superseded": "SUPERSEDED",
}
TABLES = ["claims", "vintages", "rules", "sources", "calculations", "conlog", "tests", "characters", "corpusmap"]


def skey(s: str) -> str:
    """Normalization key for cross-file comparison (dashes, quotes, case, spacing)."""
    s = (s or "")
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2019", "'").replace("\u2018", "'")
    return re.sub(r"\s+", " ", s).strip().lower()


def read_table(path: Path):
    if not path.exists():
        return []
    rows = []
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            clean = {}
            for k, v in row.items():
                if k is None:
                    continue
                clean[k.strip()] = (v or "").strip()
            rows.append(clean)
    return rows


def load_ledger(d: Path):
    schema = None
    sp = d / "schema.json"
    if sp.exists():
        schema = json.loads(sp.read_text(encoding="utf-8"))
    tables = {n: read_table(d / (n + ".tsv")) for n in
              ["claims", "vintages", "rules", "sources", "calculations", "conlog", "tests", "characters"]}
    tables["corpusmap"] = read_table(d / "corpus-map.tsv")
    return schema, tables


def split_refs(s):
    return [t.strip() for t in (s or "").split(";") if t.strip()]


def parse_date(s):
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%d %B %Y", "%B %Y", "%d %b %Y", "%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?$", s)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2) or 1), int(m.group(3) or 1))
        except ValueError:
            return None
    return None


_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}


def _eval_node(n):
    if isinstance(n, ast.Expression):
        return _eval_node(n.body)
    if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
        return n.value
    if isinstance(n, ast.BinOp) and type(n.op) in _BINOPS:
        return _BINOPS[type(n.op)](_eval_node(n.left), _eval_node(n.right))
    if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
        return -_eval_node(n.operand)
    if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.UAdd):
        return +_eval_node(n.operand)
    raise ValueError("disallowed expression node")


def safe_eval(expr):
    try:
        tree = ast.parse((expr or "").strip(), mode="eval")
        return _eval_node(tree)
    except Exception:
        return None


# ---------------------------------------------------------------- detection

def detect(T, edition_date=None):
    """Collision detection over the ledger. Returns dict with value/rule/temporal lists."""
    value, rule = [], []
    groups = {}
    for r in T["claims"]:
        q = skey(r.get("qkey", ""))
        if q:
            groups.setdefault(q, []).append(r)
    for q, rows in sorted(groups.items()):
        vals = {skey(r.get("value", "")) for r in rows if r.get("value")}
        if len(vals) > 1:
            value.append({
                "qkey": q,
                "items": [{"id": r.get("id"), "value": r.get("value"), "status": r.get("status")} for r in rows],
            })
    # claim vs its VTG row at the same as_of
    for r in T["claims"]:
        q = skey(r.get("qkey", ""))
        if not q:
            continue
        for v in T["vintages"]:
            if skey(v.get("qkey", "")) != q:
                continue
            if r.get("as_of") and skey(r["as_of"]) == skey(v.get("as_of", "")) \
                    and skey(r.get("value", "")) != skey(v.get("value", "")):
                value.append({
                    "qkey": q + " (vs " + v.get("id") + ")",
                    "items": [
                        {"id": r.get("id"), "value": r.get("value"), "status": r.get("status")},
                        {"id": v.get("id"), "value": v.get("value"), "status": "VTG row"},
                    ],
                })
    seen_pairs = set()
    for r in T["rules"]:
        for tok in split_refs(r.get("conflicts_with", "")):
            other = next((x for x in T["rules"] if x.get("id") == tok), None)
            if other is None:
                continue
            pair = tuple(sorted([r.get("id", "?"), tok]))
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)
            if (r.get("status") or "").strip().lower() == "superseded" \
                    or (other.get("status") or "").strip().lower() == "superseded":
                continue  # superseded rules keep their audit trail but are not open conflicts
            if not (r.get("resolution") and other.get("resolution")):
                rule.append({"ids": list(pair), "domain": r.get("domain", "")})
    temporal = []
    if edition_date:
        ed = parse_date(edition_date)
        if ed:
            for r in T["claims"]:
                if r.get("status") in (ST["verified"], ST["vintage"]):
                    d = parse_date(r.get("as_of", ""))
                    if d and d < ed:
                        temporal.append({"id": r.get("id"), "as_of": r.get("as_of")})
    return {"value": value, "rule": rule, "temporal": temporal}


# ---------------------------------------------------------------- validate

def cmd_validate(args):
    d = Path(args.dir)
    schema, T = load_ledger(d)
    errors = []
    ids = {n: {r.get("id", "") for r in rows} for n, rows in T.items()}
    all_ids = set()
    for s in ids.values():
        all_ids |= s
    specs = (schema or {}).get("tables", {})

    for name in TABLES:
        rows = T[name]
        spec = specs.get(name, {})
        fields = spec.get("fields", [])
        idpat = spec.get("id_pattern")
        for r in rows:
            rid = r.get("id", "?")
            if idpat and rid and rid != "?" and not re.fullmatch(idpat, rid):
                errors.append(f"{name}: id {rid!r} does not match pattern {idpat}")
            for f in fields:
                val = r.get(f["name"], "")
                req = bool(f.get("required"))
                ri = f.get("required_if")
                if ri:
                    req = skey(r.get(ri.get("field", "status"), "")) in {skey(x) for x in ri.get("in", [])}
                if req and not val:
                    why = f" (required when {ri.get('field')} in {ri.get('in')})" if ri else ""
                    errors.append(f"{name}/{rid}: missing required field {f['name']!r}{why}")
        seen = {}
        for r in rows:
            seen[r.get("id", "?")] = seen.get(r.get("id", "?"), 0) + 1
        for k, c in seen.items():
            if c > 1 and k:
                errors.append(f"{name}: duplicate id {k} ({c}x)")

    def refs(rows, field, universe, label):
        for r in rows:
            for tok in split_refs(r.get(field, "")):
                if tok not in universe:
                    errors.append(f"{label}/{r.get('id', '?')}: {field} -> {tok!r} not found")

    refs(T["claims"], "source_id", ids["sources"], "claims")
    refs(T["claims"], "superseded_by", ids["claims"], "claims")
    refs(T["claims"], "calc_id", ids["calculations"], "claims")
    refs(T["claims"], "rule_refs", ids["rules"], "claims")
    refs(T["vintages"], "superseded_by", ids["vintages"], "vintages")
    refs(T["vintages"], "source_id", ids["sources"], "vintages")
    refs(T["rules"], "conflicts_with", ids["rules"], "rules")
    refs(T["calculations"], "output_claim", ids["claims"], "calculations")
    refs(T["conlog"], "item_refs", all_ids, "conlog")
    refs(T["tests"], "hypothesis_ref", ids["claims"], "tests")

    for r in T["claims"]:
        st = r.get("status", "")
        if st in (ST["verified"], ST["vintage"]) and not r.get("as_of"):
            errors.append(f"claims/{r.get('id', '?')}: status {st} requires as_of")
        if st == ST["verified"] and not r.get("xrefs"):
            errors.append(f"claims/{r.get('id', '?')}: FACT-VERIFIED requires xrefs (every verified claim is cross-referenced)")
        if st == ST["superseded"] and not r.get("superseded_by"):
            errors.append(f"claims/{r.get('id', '?')}: SUPERSEDED requires superseded_by")
        if st == ST["validated"]:
            ok = any(t.get("hypothesis_ref") == r.get("id") and t.get("verdict", "").upper() == "PASS"
                     for t in T["tests"])
            if not ok:
                errors.append(f"claims/{r.get('id', '?')}: EMPIRICALLY VALIDATED without a PASS test row in tests.tsv")

    # arithmetic (class A, automatic)
    for c in T["calculations"]:
        fv = safe_eval(c.get("formula", ""))
        if not isinstance(fv, (int, float)):
            continue
        tgt = next((r for r in T["claims"] if r.get("id") == c.get("output_claim")), None)
        if tgt is None:
            continue
        try:
            tv = float(skey(tgt.get("value", "")).replace(",", ""))
        except ValueError:
            continue
        if abs(tv - fv) > 1e-9:
            errors.append(
                f"calculations/{c.get('id', '?')}: ARITHMETIC COLLISION (class A) - "
                f"formula {c.get('formula')!r} = {fv:g} but {c.get('output_claim')} value is {tgt.get('value')!r}"
            )

    # weight-vector sum guard
    for r in T["claims"]:
        v = r.get("value", "")
        if re.fullmatch(r"\d+(?:/\d+)+", v) and "100" in r.get("unit", ""):
            parts = [int(x) for x in v.split("/")]
            if sum(parts) != 100:
                errors.append(f"claims/{r.get('id', '?')}: weight vector {v!r} sums to {sum(parts)}, expected 100")

    if errors:
        print(f"VALIDATE: FAIL - {len(errors)} error(s)")
        for e in errors:
            print("  ERROR  " + e)
        sys.exit(1)
    print("VALIDATE: PASS - no schema, referential, status, or arithmetic errors.")
    sys.exit(0)


# ---------------------------------------------------------------- contradictions

def cmd_contradictions(args):
    d = Path(args.dir)
    _, T = load_ledger(d)
    det = detect(T, args.edition_date)
    print("# Contradiction engine")
    print(f"VALUE collisions: {len(det['value'])}")
    for c in det["value"]:
        print(f"  [VALUE] qkey={c['qkey']}")
        for it in c["items"]:
            print(f"          {it['id']}: value={it['value']!r} status={it['status']}")
    print(f"RULE collisions (open): {len(det['rule'])}")
    for c in det["rule"]:
        print(f"  [RULE] {' <-> '.join(c['ids'])} (domain={c['domain']})")
    print(f"TEMPORAL (as-of older than {args.edition_date or 'n/a'}): {len(det['temporal'])}")
    for t in det["temporal"]:
        print(f"  [TEMPORAL] {t['id']} as_of={t['as_of']}")
    bad = len(det["value"]) + len(det["rule"])
    print(f"\nRESULT: {'FAIL - open collisions present' if bad else 'PASS'} ({bad} open VALUE/RULE)")
    sys.exit(1 if bad else 0)


# ---------------------------------------------------------------- extract

_MONTHS = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
           r"Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)")
MARKERS = [
    ("percent", re.compile(r"\d+(?:[.,]\d+)?\s?(?:%|percent|per cent)", re.I)),
    ("fraction", re.compile(r"\b\d+\s*/\s*\d+\b")),
    ("amount", re.compile(r"(?:(?:NPR|(?<![A-Za-z])Rs\.?|\u0930\u0941)\s?\d[\d,]*(?:\.\d+)*|\d[\d,]*(?:\.\d+)*\s?(?:NPR|(?<![A-Za-z])Rs\.))")),
    ("iso_date", re.compile(r"\b\d{4}-\d{2}-\d{2}\b")),
    ("word_date", re.compile(rf"(?:\b{_MONTHS}\.?\s+\d{{4}}\b|\b\d{{1,2}}(?:st|nd|rd|th)?\s+{_MONTHS}\.?\b)", re.I)),
    ("weight_vector", re.compile(r"\b\d+\s*(?:/\s*\d+){3,}\b")),
    ("score_band", re.compile(r"\b\d{1,3}\s*(?:\u2013|\u2014|-)\s*\d{1,3}\b")),
    ("nepse", re.compile(r"\bNEPSE\b")),
]
HARD = {"percent", "fraction", "amount", "iso_date", "word_date", "weight_vector", "score_band"}


def cmd_extract(args):
    corpus = Path(args.corpus)
    if not corpus.is_dir():
        print(f"EXTRACT: corpus directory not found: {corpus}", file=sys.stderr)
        sys.exit(2)
    exts = {e.lower() for e in args.ext}
    files = [p for p in sorted(corpus.rglob("*")) if p.is_file() and p.suffix.lower() in exts]
    rows = []
    for p in files:
        rel = p.relative_to(corpus).as_posix()
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"  WARN cannot read {p}: {e}", file=sys.stderr)
            continue
        for i, line in enumerate(text.splitlines(), 1):
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            for sent in re.split(r"(?<=[.!?])\s+", s):
                sent = sent.strip()
                if not sent:
                    continue
                marks = []
                first = None
                for name, rx in MARKERS:
                    m = rx.search(sent)
                    if m:
                        marks.append(name)
                        if name in HARD and first is None:
                            first = m.group(0)
                hard_ok = any(n in HARD for n in marks)
                nepse_ok = "nepse" in marks and bool(re.search(r"\d", sent))
                if not (hard_ok or nepse_ok):
                    continue
                rows.append({
                    "candidate_id": "CAND-%04d" % (len(rows) + 1),
                    "status": ST["unreviewed"],
                    "file": rel,
                    "line": str(i),
                    "qkey": "",
                    "statement": sent[:400],
                    "value": first or "",
                    "unit": "",
                    "markers": "|".join(marks),
                    "notes": "auto-extracted; assign qkey + status in triage (03)",
                })
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    cols = ["candidate_id", "status", "file", "line", "qkey", "statement", "value", "unit", "markers", "notes"]
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    per_file = {}
    for r in rows:
        per_file[r["file"]] = per_file.get(r["file"], 0) + 1
    print(f"EXTRACT: {len(rows)} candidate claim(s) from {len(files)} file(s) -> {out}")
    for k in sorted(per_file):
        print(f"  {per_file[k]:4d}  {k}")
    sys.exit(0)


# ---------------------------------------------------------------- report

def cmd_report(args):
    d = Path(args.dir)
    _, T = load_ledger(d)
    det = detect(T, args.edition_date)
    L = []
    L.append("# Canon 13.0 ledger report")
    L.append(f"Generated: {date.today().isoformat()}")
    L.append("")
    L.append("## Ledger size")
    L.append("| table | rows |")
    L.append("|---|---|")
    for n in TABLES:
        L.append(f"| {n} | {len(T[n])} |")
    L.append("")
    L.append("## Claim status")
    counts = {}
    for r in T["claims"]:
        k = r.get("status") or "(none)"
        counts[k] = counts.get(k, 0) + 1
    L.append("| status | count |")
    L.append("|---|---|")
    for k in sorted(counts):
        L.append(f"| {k} | {counts[k]} |")
    L.append("")
    L.append("## Engine detections")
    L.append(f"- VALUE collisions: {len(det['value'])}")
    for c in det["value"]:
        ids = ", ".join(i["id"] for i in c["items"])
        L.append(f"  - {c['qkey']} ({ids})")
    L.append(f"- RULE collisions (open): {len(det['rule'])}")
    for c in det["rule"]:
        L.append(f"  - {' <-> '.join(c['ids'])}")
    L.append(f"- TEMPORAL due (as-of before {args.edition_date or 'n/a'}): {len(det['temporal'])}")
    for t in det["temporal"]:
        L.append(f"  - {t['id']} (as_of {t['as_of']})")
    L.append("")
    L.append("## Contradiction log (conlog)")
    L.append("| id | type | status | description |")
    L.append("|---|---|---|---|")
    for r in T["conlog"]:
        L.append(f"| {r.get('id')} | {r.get('type')} | {r.get('status')} | {r.get('description', '')[:90]} |")
    L.append("")
    L.append("## Duplicate-quantity hotspots (top 10 by occurrences)")
    occ = {}
    for r in T["claims"]:
        q = skey(r.get("qkey", ""))
        if q:
            occ[q] = occ.get(q, 0) + 1 + len(split_refs(r.get("xrefs", "")))
    for r in T["vintages"]:
        q = skey(r.get("qkey", ""))
        if q:
            occ[q] = occ.get(q, 0) + 1
    L.append("| qkey | occurrences |")
    L.append("|---|---|")
    for q, c in sorted(occ.items(), key=lambda kv: -kv[1])[:10]:
        L.append(f"| {q} | {c} |")
    L.append("")
    L.append("## Corpus crawl state")
    cm = T["corpusmap"]
    fetched = sum(1 for r in cm if r.get("status", "").startswith("fetched"))
    L.append(f"- pages fetched: {fetched} / {len(cm)}")
    prio = [r.get("chapter") for r in cm if "PRIORITY 1" in r.get("notes", "")]
    if prio:
        L.append(f"- PRIORITY 1 pending: {', '.join(p for p in prio if p and p != '-')}")
    L.append("")
    L.append("## Unreviewed candidates")
    unrev = sum(1 for r in T["claims"] if r.get("status") == ST["unreviewed"])
    L.append(f"- {unrev} claim row(s) still UNREVIEWED (triage pending, 03)")
    text = "\n".join(L)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"REPORT written to {args.out}")
    else:
        print(text)
    sys.exit(0)


def main():
    ap = argparse.ArgumentParser(prog="canon_tools", description="Canon 13.0 evidence-governance toolkit")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("extract", help="scan a corpus for quantitative candidate claims")
    p.add_argument("--corpus", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--ext", nargs="+", default=[".md", ".txt", ".rst", ".tex"])
    p.set_defaults(fn=cmd_extract)

    p = sub.add_parser("validate", help="schema/referential/status/arithmetic checks")
    p.add_argument("--dir", required=True)
    p.set_defaults(fn=cmd_validate)

    p = sub.add_parser("contradictions", help="VALUE/RULE/TEMPORAL collision detection")
    p.add_argument("--dir", required=True)
    p.add_argument("--edition-date", default=None)
    p.set_defaults(fn=cmd_contradictions)

    p = sub.add_parser("report", help="markdown summary of ledger state")
    p.add_argument("--dir", required=True)
    p.add_argument("--edition-date", default=None)
    p.add_argument("--out", default=None)
    p.set_defaults(fn=cmd_report)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
