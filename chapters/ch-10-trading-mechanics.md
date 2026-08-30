---
title: "Part II · Chapter 10 — Trading Mechanics in NEPSE"
first_published: "2026-08-21"
last_verified: "2026-08-30"
author: "Santosh Kumar Adhikari"
---

# Part II · Chapter 10: Trading Mechanics in NEPSE

**First published 21 Aug 2026 · Last verified 30 Aug 2026**

---

### In this chapter

1. [Lesson 10.1 — The NEPSE Trading Engine: NATS, NOTS, and the TMS Portal](#lesson-101--the-nepse-trading-engine-nats-nots-and-the-tms-portal)
2. [Lesson 10.2 — Trading Hours, Pre-Open Session, and Market Timing](#lesson-102--trading-hours-pre-open-session-and-market-timing)
3. [Lesson 10.3 — Order Types Available: Market Orders, Limit Orders — What Exists and What Does Not](#lesson-103--order-types-available-market-orders-limit-orders--what-exists-and-what-does-not)
4. [Lesson 10.4 — The Order Book: Bids, Asks, Spreads, Price Ticks, and Market Depth](#lesson-104--the-order-book-bids-asks-spreads-price-ticks-and-market-depth)
5. [Lesson 10.5 — Price Circuit Limits: Daily Price Bands and Market-Wide Circuit Breakers](#lesson-105--price-circuit-limits-daily-price-bands-and-market-wide-circuit-breakers)
6. [Lesson 10.6 — T+2 Settlement Cycle, Fund Transfers, and the 20% Close-Out Penalty](#lesson-106--t2-settlement-cycle-fund-transfers-and-the-20-close-out-penalty)
7. [Lesson 10.7 — MEROSHARE: Demat System, EDIS Transfer, C-ASBA, and Portfolio Verification](#lesson-107--meroshare-demat-system-edis-transfer-c-asba-and-portfolio-verification)
8. [Lesson 10.8 — Broker-Assisted Trading vs. Self-Directed Trading via TMS](#lesson-108--broker-assisted-trading-vs-self-directed-trading-via-tms)
9. [Lesson 10.9 — Short Selling: Why It Does Not Exist on NEPSE and the Consequences for Price Discovery](#lesson-109--short-selling-why-it-does-not-exist-on-nepse-and-the-consequences-for-price-discovery)
10. [Lesson 10.10 — Dividends, Bonus Shares, and Rights: Timelines, Book Closure, and Ex-Dates](#lesson-1010--dividends-bonus-shares-and-rights-timelines-book-closure-and-ex-dates)

---

> *The way orders are placed, matched, and settled defines the boundary between theoretical analysis and real investment performance.*

The Nepal Stock Exchange (NEPSE) operates under a distinct set of mechanical and structural rules that differ substantially from mature exchanges such as the BSE, NSE, or NYSE. For the disciplined investor, understanding these trading mechanics is foundational. The structure of the matching engine, order book depth, circuit limits, settlement timing, and missing order types dictate what a rational execution strategy must look like in Nepal.

---

## Lesson 10.1 — The NEPSE Trading Engine: NATS, NOTS, and the TMS Portal

### Order-Driven Market Architecture

NEPSE operates as a fully automated, **order-driven electronic double auction**. In a quote-driven market (common among Western market maker systems), designated dealers post continuous bid and ask quotes. In an order-driven market like NEPSE, **there are no designated market makers**. Liquidity exists solely when independent buyers and sellers place overlapping orders in the central order book.

```
                             NEPSE ELECTRONIC TRADING PIPELINE
   ┌───────────────────────┐       ┌───────────────────────┐       ┌───────────────────────┐
   │ 1. Investor Order     │ ────> │ 2. Broker Gateway     │ ────> │ 3. Central Matching   │
   │ Placed via web/mobile │       │ Risk filter, margin   │       │ NATS engine executes  │
   │ Trade Mgmt System(TMS)│       │ check & collateral    │       │ on Price-Time priority│
   └───────────────────────┘       └───────────────────────┘       └───────────────────────┘
```

### The Technology Backbone: NATS & NOTS

1. **NEPSE Automated Trading System (NATS):** The central electronic engine that stores all pending orders, computes the official index in real time, and executes matches.
2. **NEPSE Online Trading System (NOTS):** The automated software framework introduced to eliminate open-outcry trading and integrate broker back-offices with the exchange.
3. **Trade Management System (TMS):** The browser-based interface provided by licensed stockbrokers that allows retail and institutional investors to enter, modify, and monitor orders from their own devices.

### The Matching Algorithm: Price-Time Priority

All orders entered into NATS are matched strictly on **Price-Time Priority**:
- **Price Priority:** The highest buy price (highest bid) and the lowest sell price (lowest ask) always take precedence.
- **Time Priority:** When two orders are placed at identical price points, the order with the earlier system timestamp is executed first.

---

## Lesson 10.2 — Trading Hours, Pre-Open Session, and Market Timing

### The Trading Schedule (Sunday to Thursday)

NEPSE operates five days a week on Nepal Standard Time (**NST: UTC+5:45**), following Nepal's regular working calendar:

```
                            NEPSE DAILY TRADING SESSIONS
   ┌──────────────────────┬──────────────────────┬───────────────────────────────────────┐
   │ Session              │ Time Window (NST)    │ Functional Rules                      │
   ├──────────────────────┼──────────────────────┼───────────────────────────────────────┤
   │ Pre-Open Session     │ 10:30 AM – 10:45 AM  │ Order entry & matching at single IEP  │
   │ Pre-Open Matching    │ 10:45 AM – 11:00 AM  │ System calculates equilibrium price   │
   │ Continuous Trading   │ 11:00 AM – 3:00 PM   │ Real-time continuous order matching   │
   │ Market Close         │ 3:00 PM              │ Trading ends; settlement files gen.   │
   └──────────────────────┴──────────────────────┴───────────────────────────────────────┘
```

### The Pre-Open Session & Indicative Equilibrium Price (IEP)

Between **10:30 AM and 10:45 AM**, market participants can enter, modify, or cancel orders within a **±5% price band** of the previous day's closing price. No continuous executions take place during this window.

Instead, NATS continuously calculates the **Indicative Equilibrium Price (IEP)** — the single price point at which the maximum volume of shares can be matched. At the conclusion of the pre-open session, all eligible buy and sell orders execute simultaneously at the calculated IEP, establishing the official opening price for continuous trading.

---

## Lesson 10.3 — Order Types Available: Market Orders, Limit Orders — What Exists and What Does Not

### Available Order Types

| Order Type | Operational Mechanism | Risk / Advantage |
| :--- | :--- | :--- |
| **Limit Order** | Executes only at the specified price or better (lower for buys, higher for sells). | **High price certainty; zero slippage.** Order may remain unfilled if the market does not reach the limit. |
| **Market Order** | Matches immediately against the best available asks/bids in the order book. | **High execution certainty, but severe slippage risk** in thin NEPSE order books. |

### Missing Order Types on NEPSE

Unlike mature global exchanges, NEPSE does **not** natively support advanced conditional order types:
- **No Native Stop-Loss Orders:** Investors cannot set automated stop-loss triggers in the exchange engine. Downside risk must be monitored manually.
- **No Good-Till-Cancelled (GTC) Orders:** Orders placed on TMS are standard **Day Orders**, automatically expiring at the 3:00 PM close if unfilled.
- **No Native Trailing Stops or Bracket Orders:** Complex algorithmic order routes must be managed externally.

---

## Lesson 10.4 — The Order Book: Bids, Asks, Spreads, Price Ticks, and Market Depth

### Anatomy of the Order Book

The order book displays the pending buying interest (Bids) and selling interest (Asks) ranked by price priority:

```
                              NEPSE LIVE MARKET DEPTH (TOP 5)
                BUY SIDE (BIDS)                          SELL SIDE (ASKS)
        Orders   Quantity    Bid Price           Ask Price   Quantity   Orders
        ───────────────────────────────         ───────────────────────────────
          3       1,200       Rs. 450.00          Rs. 452.50     500        2
          5       2,500       Rs. 448.00          Rs. 454.00    1,800       4
          2         800       Rs. 446.00          Rs. 457.00    3,200       6
          1         300       Rs. 445.00          Rs. 460.00    5,000       8
          4       1,500       Rs. 442.00          Rs. 465.00    2,100       3
```

- **Bid-Ask Spread:** The difference between the Best Bid (Rs. 450.00) and Best Ask (Rs. 452.50) = **Rs. 2.50 (0.55%)**.
- **Minimum Price Tick:** Orders must be entered in minimum price increments of **Rs. 0.10 (10 Paisa)**.
- **Intraday Order Band:** During continuous trading, orders cannot be placed at prices more than **±2%** away from the Last Traded Price (LTP).

---

## Lesson 10.5 — Price Circuit Limits: Daily Price Bands and Market-Wide Circuit Breakers

### Individual Stock Price Circuit Bands

To prevent extreme intraday manipulation, NEPSE restricts price movements for individual listed ordinary shares to a **±10% maximum daily band** relative to the previous day's closing price:
- **Upper Circuit (+10%):** The maximum price at which buy orders can execute for the day.
- **Lower Circuit (-10%):** The minimum price at which sell orders can execute for the day.

### Market-Wide Index Circuit Breakers

To manage systemic panic or extreme market euphoria, NEPSE enforces a standardized **three-tier market-wide circuit breaker system**:

```
                            MARKET-WIDE CIRCUIT BREAKERS
   ┌──────────────────────────────────┬──────────────────────┬───────────────────────────┐
   │ Trigger Threshold                │ Trading Time Window  │ Market Halt Duration      │
   ├──────────────────────────────────┼──────────────────────┼───────────────────────────┤
   │ 4% Index Movement (Up/Down)      │ 1st Hour (to 12:00PM)│ 20 Minutes Suspension     │
   │ 5% Index Movement (Up/Down)      │ 2nd Hour (to 1:00 PM)│ 40 Minutes Suspension     │
   │ 6% Index Movement (Up/Down)      │ At any trading time  │ Closed for Rest of Day    │
   └──────────────────────────────────┴──────────────────────┴───────────────────────────┘
```

---

## Lesson 10.6 — T+2 Settlement Cycle, Fund Transfers, and the 20% Close-Out Penalty

### The T+2 Settlement Sequence

NEPSE trades settle on a **T+2 business day cycle** managed by CDSC:

```
                            T+2 SETTLEMENT CHRONOLOGY
   ┌──────────────────────────┬──────────────────────────────────────────────────────────┐
   │ Day                      │ Operational Settlement Action                            │
   ├──────────────────────────┼──────────────────────────────────────────────────────────┤
   │ T (Trade Day)            │ Order matches on NATS; transaction contract generated.   │
   │ T+1 (Next Business Day)  │ Buyer arranges payment; Seller executes EDIS transfer.   │
   │ T+2 (Settlement Day)     │ CDSC transfers shares to buyer Demat & cash to seller.   │
   └──────────────────────────┴──────────────────────────────────────────────────────────┘
```

### The 20% Close-Out Penalty (क्लोजआउट पेनाल्टी)

One of the most critical operational risks for NEPSE investors is the **Close-Out Penalty**:
- If an investor sells shares on TMS but fails to transfer the shares from their Demat account via **EDIS on MeroShare** before the settlement cut-off time, a settlement shortage occurs.
- CDSC automatically levies a mandatory **20% cash penalty on the total traded value** against the defaulting seller.
- This penalty is credited directly to the buyer as compensation for non-delivery (subject to applicable TDS).

---

## Lesson 10.7 — MEROSHARE: Demat System, EDIS Transfer, C-ASBA, and Portfolio Verification

### Core MeroShare Modules

Operated by CDSC, **MeroShare** serves as the central digital portal for retail investors in Nepal:

```
                                 MEROSHARE DIGITAL SUITE
   ┌───────────────────────┐   ┌───────────────────────┐   ┌───────────────────────┐
   │   Electronic Demat    │   │     EDIS Transfer     │   │   C-ASBA IPO Module   │
   │ Complete record of all│   │ Digital authorization │   │ Apply for IPOs/Rights │
   │ beneficial holdings   │   │ for share debits upon │   │ with bank account     │
   │ across all 16-digit   │   │ trade execution.      │   │ funds blocked via CRN.│
   │ BOID accounts.        │   │ Avoids close-out fees.│   │                       │
   └───────────────────────┘   └───────────────────────┘   └───────────────────────┘
```

1. **Beneficial Owner Identification (BOID):** A unique 16-digit permanent demat number that holds electronic title to all shares, debentures, and mutual funds.
2. **Electronic Delivery Instruction Slip (EDIS):** After executing a sell order on TMS, the investor must log into MeroShare, calculate capital gains under the **WACC (Weighted Average Cost of Capital)** module, and approve the EDIS transfer.
3. **C-ASBA & CRN:** Enables online IPO and Rights applications. Funds remain securely blocked in the investor's bank account using their unique **C-ASBA Registration Number (CRN)** until allotment.

---

## Lesson 10.8 — Broker-Assisted Trading vs. Self-Directed Trading via TMS

| Feature | Broker-Assisted Trading | Self-Directed TMS Trading |
| :--- | :--- | :--- |
| **Order Placement** | Phone call / physical visit to broker terminal. | Direct online web/mobile execution. |
| **Speed & Latency** | High communication latency; queue delays. | Instant order routing to NATS matching engine. |
| **Order Book Visibility** | Relies on broker commentary. | Full live Top-5 Market Depth visibility. |
| **Best Suited For** | High-net-worth clients desiring trade desk support. | Independent analytical investors and active traders. |

---

## Lesson 10.9 — Short Selling: Why It Does Not Exist on NEPSE and the Consequences for Price Discovery

### Structural Absence of Short Selling

NEPSE does not permit short selling. Every sell order entered on NATS must represent pre-existing, settled shares held in the seller's BOID.

```
                           CONSEQUENCES OF NO SHORT SELLING
   ┌───────────────────────┐   ┌───────────────────────┐   ┌───────────────────────┐
   │   Asymmetric Pricing  │   │ Persistent Bubbles    │   │ Higher Average P/E    │
   │ Negative views cannot │   │ Overvalued counters   │   │ Market lacks downward │
   │ be expressed without  │   │ stay detached from    │   │ discipline from short │
   │ holding physical stock│   │ fundamentals longer.  │   │ sellers.              │
   └───────────────────────┘   └───────────────────────┘   └───────────────────────┘
```

- **One-Way Upward Bias:** In markets with short selling, informed investors who identify overvaluation short the stock, bringing prices back to intrinsic value. On NEPSE, informed bears can only choose not to buy or sell existing inventory.
- **Valuation Discipline Requirement:** Because the market lacks short-side corrective pressure, investors must exercise rigorous fundamental valuation to avoid buying into prolonged speculative bubbles.

---

## Lesson 10.10 — Dividends, Bonus Shares, and Rights: Timelines, Book Closure, and Ex-Dates

### Value Distribution Sequence

```
                               CORPORATE ACTION LIFECYCLE
   ┌───────────────────────┐       ┌───────────────────────┐       ┌───────────────────────┐
   │ 1. Board Proposal     │ ────> │ 2. Book Closure Date  │ ────> │ 3. Allotment & Credit │
   │ Board proposes cash / │       │ Shareholder register  │       │ Cash to bank account; │
   │ bonus / rights ratio. │       │ locked; Ex-date set.  │       │ Bonus to Demat BOID.  │
   └───────────────────────┘       └───────────────────────┘       └───────────────────────┘
```

1. **Cash Dividends:** Direct monetary distributions credited to the investor's linked bank account. Subject to a **5% withholding tax (TDS)** for individual investors.
2. **Bonus Shares (Stock Dividends):** Free additional shares capitalized from retained earnings. On the **Book Closure Date**, NEPSE automatically adjusts the market price downward:

$$\text{Adjusted Price} = \frac{\text{Previous Closing Price}}{1 + \text{Bonus Share \%}}$$

3. **Rights Issues:** Offerings of new equity to existing shareholders at a discounted price (typically Rs. 100 face value). Shareholders must exercise their entitlement during the subscription window or face equity dilution.

$$\text{Ex-Rights Price} = \frac{\text{Closing Price} + (\text{Rights Ratio} \times \text{Issue Price})}{1 + \text{Rights Ratio}}$$

---

### Corporate Action Investor Checklist

| Corporate Action | Critical Investor Rule |
| :--- | :--- |
| **Cash Dividend** | Must hold shares in Demat on or before the **Book Closure Date** to receive payout. |
| **Bonus Shares** | Price adjusts automatically on Ex-Date; verify Demat credit on MeroShare post-AGM. |
| **Rights Issues** | Apply via MeroShare C-ASBA before the subscription deadline to prevent ownership dilution. |
| **EDIS Clearance** | Approve EDIS transfer on MeroShare before T+2 settlement cut-off to avoid the **20% Close-Out Penalty**. |

---

### Primary Data Sources

- **[Nepal Stock Exchange (NEPSE)](https://www.nepalstock.com/):** Live market depth, NOTS circulars, corporate announcements.
- **[CDS and Clearing Limited (CDSC)](https://www.cdsc.com.np/):** Settlement regulations, MeroShare portal, EDIS rules.
- **[Securities Board of Nepal (SEBON)](https://www.sebon.gov.np/):** Public issue directives, circuit breaker regulations.
- **[Inland Revenue Department (IRD)](https://ird.gov.np/):** Capital gains and dividend withholding tax rates.

---

*Educational material only. Nothing on this site constitutes investment advice or a solicitation to buy or sell securities. Consult a licensed financial professional before acting.*

**© 2026 Santosh Kumar Adhikari. All rights reserved.**
