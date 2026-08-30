---
title: "Part II · Chapter 12 — Market Microstructure Failures in NEPSE"
first_published: "2026-08-21"
last_verified: "2026-08-30"
author: "Santosh Kumar Adhikari"
---

# Part II · Chapter 12: Market Microstructure Failures in NEPSE

**First published 21 Aug 2026 · Last verified 30 Aug 2026**

---

### In this chapter

1. [Lesson 12.1 — What Market Microstructure Means and Why It Matters to a Retail Investor](#lesson-121--what-market-microstructure-means-and-why-it-matters-to-a-retail-investor)
2. [Lesson 12.2 — Queue Priority Mechanics: How the Order Queue Works and Who Benefits](#lesson-122--queue-priority-mechanics-how-the-order-queue-works-and-who-benefits)
3. [Lesson 12.3 — Fake Volume Creation: How Matched Trades Between Connected Parties Simulate Activity](#lesson-123--fake-volume-creation-how-matched-trades-between-connected-parties-simulate-activity)
4. [Lesson 12.4 — Broker-Level Order Routing Incentives: Where Your Order Goes and Execution Quality](#lesson-124--broker-level-order-routing-incentives-where-your-order-goes-and-execution-quality)
5. [Lesson 12.5 — Price Ramping in Illiquid Stocks: The 4-Phase Anatomy of How It Is Done](#lesson-125--price-ramping-in-illiquid-stocks-the-4-phase-anatomy-of-how-it-is-done)
6. [Lesson 12.6 — Information Asymmetry in NEPSE: Who Knows What and How Early](#lesson-126--information-asymmetry-in-nepse-who-knows-what-and-how-early)
7. [Lesson 12.7 — Circuit Limit Exploitation: How Operators Use Circuits to Trap Retail Investors](#lesson-127--circuit-limit-exploitation-how-operators-use-circuits-to-trap-retail-investors)
8. [Lesson 12.8 — Protecting Yourself From Microstructure Predation: Practical Rules](#lesson-128--protecting-yourself-from-microstructure-predation-practical-rules)

---

> *Most books ignore this. Most retail investors are harmed by it.*

When retail investors in Nepal lose money, they almost always blame personal shortcomings: bad timing, wrong stock selection, or emotional impatience. Rarely do they realize that a significant portion of their losses stems directly from **market microstructure failures** — structural design flaws in an illiquid, order-driven market that systematically favor insiders, operators, and connected traders over outsiders.

Market microstructure is the study of how trades actually execute beneath the screen price: *Who gets filled first? Who knows material information before public disclosure? Whose order disappears before execution?* In the Nepal Stock Exchange (NEPSE) — characterized by shallow order books, high promoter lock-in concentration, and developing regulatory surveillance — microstructure predation is a daily reality. Understanding these adversarial mechanisms is the first requirement for long-term capital preservation.

---

## Lesson 12.1 — What Market Microstructure Means and Why It Matters to a Retail Investor

### The Gap Between Quoted Price and True Execution

When you see a stock quoted at Rs. 450 on NEPSE, that figure represents only the **Last Traded Price (LTP)**. It guarantees nothing about whether you can buy at that price, what volume is available, or how much your own order will move the market.

```
                              THE THREE HIDDEN EXECUTION COSTS
   ┌───────────────────────┐   ┌───────────────────────┐   ┌───────────────────────┐
   │    Bid-Ask Spread     │   │     Market Impact     │   │   Adverse Selection   │
   │ The gap between best  │   │ Large orders push the │   │ Informed sellers dump │
   │ bid and ask consumes  │   │ price higher as they  │   │ stock into retail     │
   │ 1–5% immediately.     │   │ sweep thin books.     │   │ buy orders.           │
   └───────────────────────┘   └───────────────────────┘   └───────────────────────┘
```

1. **The Bid-Ask Spread:** The immediate cost paid when crossing the spread in an illiquid counter (often 1–4% in smaller hydropower or microfinance scrips).
2. **Market Impact (Slippage):** Placing a market buy order in a shallow book consumes multiple ask levels, driving your average fill price significantly above the screen price.
3. **Adverse Selection:** When an insider or large operator sells aggressively into your buy order, they frequently possess advance knowledge of deteriorating fundamentals or post-lock-in share supply floods.

---

## Lesson 12.2 — Queue Priority Mechanics: How the Order Queue Works and Who Benefits

### Price-Time Priority in NATS

The **NEPSE Automated Trading System (NATS)** processes orders strictly on **Price-Time Priority**:
- Orders at the best price execute first.
- Among orders placed at the exact same price, the order registered earliest at the exchange matching engine executes first.

### The Broker Terminal Latency Advantage

In practice, "time of arrival" is determined by network latency. A retail investor placing an order through a smartphone app or browser-based TMS experiences multiple network routing hops. In contrast, dedicated institutional workstations and broker dealer desks have lower-latency connections directly to the NOTS gateway, consistently securing queue priority at opening prints and circuit limits.

### Queue Spoofing

Operators frequently place large, visible buy or sell orders with no intention of executing them. A massive sell order at Rs. 460 signals artificial resistance, intimidating retail buyers and allowing the operator to accumulate shares at Rs. 445. Once accumulation completes, the spoofed sell order is cancelled within seconds.

---

## Lesson 12.3 — Fake Volume Creation: How Matched Trades Between Connected Parties Simulate Activity

### The Mechanics of Wash Trading

Wash trading is the practice of simultaneously buying and selling the same security across coordinated nominee accounts (family members, shell entities, or syndicate partners) with **zero change in beneficial ownership**:

```
                              CIRCULAR WASH TRADING SCHEME
   ┌───────────────────────┐       ┌───────────────────────┐       ┌───────────────────────┐
   │ Syndicate Account A   │ ────> │ NATS Matching Engine  │ ────> │ Syndicate Account B   │
   │ Places Sell Order at  │       │ Matches trade on thin │       │ Places Buy Order at   │
   │ targeted price tier.  │       │ book; volume spikes.  │       │ identical price tier. │
   └───────────────────────┘       └───────────────────────┘       └───────────────────────┘
```

### Why Wash Trading Fools Retail Traders

Retail investors routinely screen for **"Volume Breakouts"** as confirmation of institutional accumulation. Operators deliberately manufacture volume in dormant, low-float scrips to trigger automated screeners and social media buzz, creating the artificial liquidity needed to dump their pre-accumulated holdings into retail hands.

---

## Lesson 12.4 — Broker-Level Order Routing Incentives: Where Your Order Goes and Execution Quality

### Agency vs. Proprietary Interests

While brokers act as legal agents for retail clients, informal conflicts of interest can arise:
- **Front-Running Risks:** When a broker desk receives large, price-moving client orders, the incentive exists to accumulate shares ahead of executing the client order.
- **Order Discretion:** Market orders provide maximum discretion over fill prices; **Limit Orders** restrict execution strictly to the investor's pre-determined price floor or ceiling.

---

## Lesson 12.5 — Price Ramping in Illiquid Stocks: The 4-Phase Anatomy of How It Is Done

In low-float NEPSE stocks (particularly small-cap hydropower, finance, and microfinance), price ramping follows a repeatable 4-phase cycle:

```
                            THE 4-PHASE NEPSE PRICE RAMP
   ┌──────────────────────────────────────────────────────────────────────────────────┐
   │ 1. Quiet Accumulation  ──> 2. Volume Ignition ──> 3. Controlled Run ──> 4. Exit  │
   │ Flat price; small lots;    Wash trades + rumors;   Multi-day upper      Dumping  │
   │ zero social buzz.          first upper circuit.    circuits lure retail into FOMO│
   └──────────────────────────────────────────────────────────────────────────────────┘
```

1. **Phase 1: Quiet Accumulation:** Operators quietly absorb floating shares over weeks in small lots without moving the price.
2. **Phase 2: Volume Ignition & Narrative Seeding:** Small wash trades simulate activity. Rumors of bonus shares, rights issues, or acquisitions are planted in Facebook/Telegram groups. The stock hits its first +10% upper circuit.
3. **Phase 3: Controlled Retail Run:** The stock hits consecutive upper circuits. The visual scarcity of sellers lures retail investors into placing aggressive buy orders at the ceiling.
4. **Phase 4: Distribution & Exit:** Operators dump their entire accumulated inventory into the retail buy queue at peak valuation. Once the syndicate exits, buying support collapses, locking retail buyers into a downward cascade.

---

## Lesson 12.6 — Information Asymmetry in NEPSE: Who Knows What and How Early

### The NEPSE Information Hierarchy

```
                             THE NEPSE INFORMATION PYRAMID
                                    ▲
                                   ╱ ╲     Tier 1: Company Promoters & Insiders
                                  ╱   ╲    (Financial results, PPAs, dividends)
                                 ╱─────╲
                                ╱       ╲   Tier 2: Connected Broker Desks & Operators
                               ╱─────────╲
                              ╱           ╲  Tier 3: Institutional Funds & Large HNWIs
                             ╱─────────────╲
                            ╱               ╲ Tier 4: Public Retail Investors
                           ─────────────────── (Read news on social media after the move)
```

By the time a corporate announcement or quarterly report appears on public social media channels, informed participants have already priced in the news. Buying on unverified social media "tips" invariably means providing exit liquidity to earlier tiers.

---

## Lesson 12.7 — Circuit Limit Exploitation: How Operators Use Circuits to Trap Retail Investors

### 1. The Upper Circuit Trap (Manufactured Scarcity)
Operators corner the thin sell side of an illiquid scrip, locking it at **+10% upper circuit**. The growing queue of unexecuted retail buy orders creates intense FOMO (Fear Of Missing Out). When the queue reaches maximum frenzy, operators dump their shares into the pending buy orders, triggering an immediate reversal.

### 2. The Lower Circuit Trap (Manufactured Panic)
Operators aggressively dump a block of shares at market open, triggering a **-10% lower circuit**. Panicking retail holders, unable to sell due to the circuit lock, place desperate sell orders for the following session. The operator steps in at the bottom, absorbing distressed shares at extreme discounts.

---

## Lesson 12.8 — Protecting Yourself From Microstructure Predation: Practical Rules

### The 8 Rules of Defensive NEPSE Investing

1. **Never Use Market Orders in Illiquid Counters:** Always use **Limit Orders** with a strict price ceiling to prevent slippage.
2. **Treat Multi-Day Upper Circuits as Danger Signals:** Never buy a stock that has hit 3+ consecutive upper circuits without extraordinary fundamental justification.
3. **Demand Verifiable News Catalysts for Volume Surges:** If a volume breakout has no corresponding audited financial improvement or official regulatory circular, assume it is wash-traded.
4. **Ignore Social Media Tipping Channels:** Tips shared in public Facebook, YouTube, or Telegram channels represent stale intelligence used for distribution.
5. **Build Positions in Staggered Tranches:** Accumulate illiquid shares across 3–5 separate sessions to minimize market impact and identify potential front-running.
6. **Never Sell in Panic During Engineered Lower Circuits:** If your fundamental thesis remains sound and the business balance sheet is intact, hold through panic cascades.
7. **Treat Brokers Strictly as Execution Intermediaries:** Never rely on broker trade desks for unverified investment advice.
8. **Maintain a Detailed Decision Log:** Document whether your entry was motivated by fundamental valuation or microstructure FOMO (volume spikes, circuit streaks).

---

### Microstructure Checklist for Every Trade

- [ ] Is this order a **Limit Order** placed within acceptable bid-ask spreads?
- [ ] Has this stock hit consecutive upper circuits over the last 3 days? (If yes $\rightarrow$ High distribution risk).
- [ ] Is the current volume surge corroborated by an official corporate disclosure on NEPSE/SEBON?
- [ ] Can my position be liquidated within 10–15 trading days without exceeding 10% of Average Daily Volume?

---

### Primary Data Sources

- **[Nepal Stock Exchange (NEPSE)](https://www.nepalstock.com/):** Live market depth, NOTS floorsheet records, official circulars.
- **[Securities Board of Nepal (SEBON)](https://www.sebon.gov.np/):** Market surveillance directives, insider trading investigation reports.
- **[CDS and Clearing Limited (CDSC)](https://www.cdsc.com.np/):** Free-float registers and beneficial ownership data.

---

*Educational material only. Nothing on this site constitutes investment advice or a solicitation to buy or sell securities. Consult a licensed financial professional before acting.*

**© 2026 Santosh Kumar Adhikari. All rights reserved.**
