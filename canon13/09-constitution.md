# 09 — Decision-Rule Constitution (Phase 6)

Purpose: the corpus must be a **single decision function**. Given (state of world, reader's position, rule set), the instructed action is unique. No reader may be able to assemble, from two chapters, two opposite instructions.

## 1. Precedence tiers

| Tier | Domain | Authority | Power |
|---|---|---|---|
| **T1** | Capital preservation (hard limits: max loss per position, portfolio drawdown triggers per Ch. 97, liquidity floor) | constitutional | may **forbid**; may never *require* a specific purchase |
| **T2** | Regulatory/legal compliance (L1 sources: SEBON rules, NRB directives, tax law) | law | forbids or requires as the law does |
| **T3** | Regime classification (Ch. 0.3 four-phase liquidity-regime framework; ADV/liquidity context per Ch. 54–56) | constitutional | defines the **allowed action space** for each regime (e.g., distribution phase: no fresh equity capital; accumulation: eligible) |
| **T4** | Canon Score bands (ch-66 thresholds: <45 / 45–59 / 60–64 / ≥65; band table owned by ch-64/framework) | constitutional | maps quality **within** the allowed space; may narrow, never widen |
| **T5** | SIP / systematic defaults (Ch. 62) | rule | the standing instruction when T1–T4 are silent about a specific action; **cannot authorize what T1–T4 forbid** |
| **T6** | Discretionary overlays (playbooks Chs. 67–78; entry-timing judgement) | rule | narrowest authority; must cite the T1–T5 consistency check in print |

**Precedence law:** the higher tier wins. A lower tier may restrict; it may never widen. Two rules in the same tier with overlapping trigger and different action are a **RULE collision** (06) and may not print unresolved.

## 2. Alignment with the corpus's own constitution parts

Chs. 94–100 (Part XVII, "The Investment Constitution & Personal Operating System") define the *reader's* personal constitution; Ch. 96 ("Rules for Overriding the Model") already addresses overrides, Ch. 98 the review protocol. Canon 13.0's constitution governs the **book's** internal rules and *supersedes* any in-book wording to the extent of conflict — and that conflict must itself be resolved and printed (R4), not papered over. The reader's personal constitution (Ch. 95) is downstream of this one: the book cannot instruct the reader to build a personal constitution that violates the book's own T1/T2.

## 3. Printing requirements

- Every decision rule in the corpus carries `[RUL-####, T#]` in print (e.g., "45–59: watch list only, no fresh capital [RUL-0001, T4]").
- Every rule that narrows a higher tier cites the rule it narrows.
- Every resolved collision prints its **resolution sentence** at the place where the tension is most visible to the reader.

## 4. The 56–59 collision, resolved by construction (CON-0002)

The verified prohibitive side: ch-66 — 45–59 "commit no fresh capital" [RUL-0001, T4]. The permissive side (location pending crawl; candidates ch-62 T5, ch-67 T6, case studies T6) may stand only as:
- **T5-scoped:** "SIP continues per the standing plan; at 45–59 the plan is in *suspended-fresh-capital* mode, so SIP deferrals apply until the score rebounds above 60" — i.e., T5 yields to T4, and the deferral is the printed resolution; or
- **T3-scoped:** the permissive instruction is regime-conditional ("eligible under regime R only"), and the regime criteria (Ch. 0.3) make the condition checkable.
Either way the reader can never hold both "buy" and "no fresh capital" as simultaneously live instructions: one of them is visibly, printably subordinate. Which scoping is correct is decided when the permissive occurrence is located (Phase 3) — the constitution supplies the *shape* of the resolution in advance, so the fix cannot drift into a numbers game.

## 5. Rule audit (gate G6, Phase 10)

`rules.tsv` must contain every decision rule the corpus prints (xrefs complete), each with a tier; `contradictions` must show zero open RULE collisions; a spot-check in the corpus confirms the `[RUL, T]` tags print correctly.
