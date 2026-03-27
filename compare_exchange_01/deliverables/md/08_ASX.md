# ASX (Australian Securities Exchange) — Exchange Report

---

## 1. Exchange Overview

**Full Legal Name**: ASX Limited (Australian Securities Exchange)
**Country**: Australia
**Founding Year**: 1987 (merger of six state exchanges); demutualized 1998 [WEB:wikipedia]
**Parent Group**: ASX Limited (self-listed: ASX.AX) [WEB:wikipedia]

**Market Model**: Order-driven with integrated dark pool (Centre Point) [REF:#1]

**Asset Classes Traded**: [WEB:wikipedia]
- Equities (ASX main board)
- ETFs, ETPs, managed funds
- Derivatives (equity options, index futures, interest rate)
- Fixed income (government bonds, corporate bonds)
- Warrants

**Regular Trading Hours (AEST/AEDT, UTC+10/+11)**: [REF:#1] [WEB:asx.com.au/trading-hours]
- Pre-opening: 07:00–10:00 (staggered open from ~09:59)
- Normal trading: 10:00–16:00
- Pre-closing: 16:00–16:10
- Closing auction: 16:10–16:12
- Post-trading: after 16:12

**Key Statistics**: [WEB:wikipedia] [WEB:asx.com.au/blog]
- Listed companies: ~2,200+
- Market capitalization: ~A$2.8 trillion / ~US$1.8 trillion
- Average daily turnover: ~A$4.685 billion
- 2025: 92 new listings (+37% vs 2024), adding A$38.8 billion market cap [WEB:asx.com.au/blog]

---

## 2. Institutional Philosophy

**Primary Market Model**: Order-driven with integrated dark pool [REF:#1]
- Lit market (order book) + Centre Point (dark midpoint) on single platform
- Unique integration: dark and lit operate together, not as separate venues
- Price-time priority on lit; midpoint matching on dark [REF:#1]

**Design Rationale**: [WEB:wikipedia]
- Single-exchange market for Australian equities (no competing exchanges until Cboe Australia 2011)
- Centre Point provides institutional-grade dark liquidity without fragmenting the market
- "Meaningful price improvement" rule: dark trades must execute at NBBO midpoint or better (ASIC regulation) [WEB:marketsmedia.com]
- Emphasis on market integrity — ASIC Market Integrity Rules govern all venues

**Role of Intermediaries**: [WEB:asx.com.au/mm]
- **ETO Market Makers**: Contractual for equity options (quoting obligations)
- **ETP Market Makers**: For ETFs/ETPs
- **No mandatory equity market makers** — lit market relies on natural order flow
- Market-to-limit default for "market orders" provides implicit price protection [WEB:commsec.com.au]

**Evolution**: Six state exchanges → ASX (1987) → demutualized (1998) → ASX Trade platform → Centre Point dark pool → CHESS replacement project (ongoing) [WEB:wikipedia]

---

## 3. Order Types — Basic

### 3.1 Limit Order [REF:#4] [WEB:asx.com.au]
- Specifies maximum buy / minimum sell price
- Available in lit market, auctions, and Centre Point
- Time-in-force: Day (GFD), GTC

### 3.2 Market-to-Limit Order [WEB:asx-game] [WEB:commsec.com.au]
- ASX's default "market order" implementation
- Fills at best available price; remainder converts to limit at last execution price
- Prevents adverse multi-level sweep — built-in price protection

### 3.3 Fill-or-Kill (FOK) [REF:#4]
- Must fill entirely or cancel completely
- Immediate execution required

### 3.4 Fill-and-Kill (FAK / IOC) [REF:#4]
- Fills available quantity immediately; cancels remainder

---

## 4. Order Types — Advanced

### 4.1 Iceberg Order [REF:#4]
- Large order split into smaller child orders
- Only current child visible in order book
- Price-time priority applies to each displayed child
- Reserve replenishes automatically

### 4.2 Good-Till-Cancel (GTC) [REF:#4]
- Persistent order — remains active across trading days until filled or cancelled
- Available on ASX (unlike KRX, TSE, HKEX which are day-only)

### 4.3 Centre Point Orders [REF:#3] [WEB:asx.com.au/centre-point]
- **Centre Point Limit**: Dark order at midpoint or better
- **Centre Point Block**: Minimum quantity required; midpoint only; single fill
- **Any Price Block**: Block order with minimum acceptable quantity (MAQ)
- **ASX Sweep**: Sweeps Centre Point first, then lit market — integrated dark-lit routing

### 4.4 Unintentional Crossing Prevention (UCP) [REF:#1]
- Optional service preventing self-trades
- Available via OMNet, FIX, or OUCH protocols

---

## 5. Order Types — Exchange-Specific

### 5.1 Centre Point Order [REF:#3] [WEB:asx.com.au/centre-point]
- **ASX-unique**: Integrated exchange-operated dark pool orders
- Anonymous midpoint matching — all dark trades execute at NBBO midpoint
- Off-tick execution permitted (4 decimal places) [REF:#3]
- 30-second activity window after cross initiation [REF:#3]
- CXXT trade code for Centre Point crosses [WEB:commsec.com.au]
- Rationale: Provides institutional price improvement without market fragmentation

### 5.2 ASX Sweep Order [WEB:asx.com.au/centre-point]
- **ASX-unique**: Integrated dark-then-lit routing
- First attempts Centre Point midpoint fill; remainder routes to lit order book
- Single order achieves best execution across both venues
- No equivalent on exchanges that don't operate integrated dark pools

### 5.3 Market-to-Limit Default [WEB:commsec.com.au]
- ASX's "market order" is actually market-to-limit by default
- Unique implicit price protection — prevents full sweep of order book
- Different from pure market orders on KRX, NYSE, NASDAQ, TSE

### 5.4 Centre Point Block with MAQ [REF:#3]
- Minimum Acceptable Quantity (MAQ) prevents partial fills on large orders
- Anti-gaming: protects against "pinging" (small orders probing dark liquidity)

---

## 6. Matching Engine & Price Discovery

### Trading System: ASX Trade [REF:#1]
- Integrated platform for lit markets, Centre Point, and auctions
- Protocols: OMNet, FIX, **OUCH** (low-latency, similar to NASDAQ) [WEB:asx-ouch]
- CHESS: Clearing House Electronic Sub-register System (settlement infrastructure)
- CHESS replacement project ongoing (distributed ledger technology exploration)

### Matching Algorithm [REF:#1]
- **Lit market**: Price-time priority
- **Centre Point**: Midpoint price matching; priority by time of entry
- **Auctions**: Single-price equilibrium (maximize volume)

### Opening Auction [WEB:asx.com.au/trading-hours]
- **07:00–~10:00**: Pre-opening order accumulation (no matching)
- **~09:59 + random 15 sec**: Staggered opening — securities open alphabetically over ~10 minutes
- Single-price auction per security at opening

### Closing Auction [WEB:asx.com.au/trading-hours]
- **16:00–16:10**: Pre-closing (order accumulation)
- **16:10–16:12**: Closing single-price auction
- Sets official closing price for index calculation

### Tick Size (Price Steps) [REF:#1]

| Price Range (A$) | Tick Size |
|---|---|
| Up to $0.10 | $0.001 |
| $0.10–$2.00 | $0.005 |
| ≥ $2.00 | $0.01 |

### Lot Size
- Standard: 1 share (no minimum lot for most securities)
- Odd lots: Supported

---

## 7. Safeguard Mechanisms

### 7.1 Anomalous Order Thresholds (AOT) [WEB:asx.com.au/order-controls]
- ASIC Market Integrity Rule — applied to all Australian markets
- Reference price: VWAP of previous 2 minutes, updated every minute
- Orders > **±10% from reference price** rejected as anomalous
- Prevents fat-finger errors and extreme mis-pricing

### 7.2 Extreme Trade Range (ETR) [WEB:asx.com.au/order-controls]
- If trade would execute outside extreme range: **2-minute trading pause**
- Individual security level (not market-wide)
- Brief cooling-off for price discovery correction

### 7.3 No Market-Wide Circuit Breaker
- Australia does NOT have US-style market-wide circuit breakers
- Individual security controls via AOT and ETR
- ASIC can suspend trading in individual securities or market-wide as regulator

### 7.4 "Meaningful Price Improvement" Rule (ASIC) [WEB:marketsmedia.com]
- Dark pool trades below A$200,000: Must execute at NBBO midpoint or with ≥1 tick improvement
- Ensures dark trading provides genuine price improvement
- Unique Australian regulatory approach to dark pool governance

---

## 8. Special Sessions

### 8.1 Pre-Opening (07:00–~10:00) [WEB:asx.com.au/trading-hours]
- Order entry from 07:00; no matching
- Staggered opening: securities open alphabetically from ~09:59 + random 15 sec

### 8.2 Normal Trading (10:00–16:00) [REF:#1]
- Continuous matching: lit market + Centre Point
- All order types available

### 8.3 Pre-Closing / Closing Auction (16:00–16:12) [WEB:asx.com.au/trading-hours]
- 16:00–16:10: Pre-closing order accumulation
- 16:10–16:12: Single-price closing auction

### 8.4 Centre Point (Dark) [REF:#3]
- Operates during normal trading hours
- Midpoint matching at NBBO mid
- Centre Point Block, Centre Point Limit, ASX Sweep order types
- Australia's largest dark pool [REF:#3]

### 8.5 Trade Reporting Facility (TRF) [REF:#1]
- Off-market and administrative trades
- Block trades, portfolio trades, late/out-of-hours trades
- Reported post-trade

---

## 9. LP / Market Maker Obligations

### 9.1 ETO (Exchange Traded Options) Market Makers [WEB:asx.com.au/mm]
- Contractual arrangements with ASX
- Quoting obligations: minimum 50% on each benchmark, combined 70% average
- Continuous quotes + response to quote requests
- Minimum time-in-market and liquidity requirements
- Maximum bid-ask spread limits
- Nov 2025: Updated quoting obligations and special size levels [WEB:asxonline.com]

### 9.2 ETP Market Makers [WEB:asx.com.au/mm-etp]
- Similar structure to ETO MMs
- Quoting obligations for ETFs and exchange-traded products
- Ensures liquidity in index tracking products

### 9.3 Equity Market — No MM Program
- No mandatory market maker for general equities
- Lit market liquidity from natural order flow
- Centre Point provides additional anonymous dark liquidity
- Similar to TSE, HKEX approach

---

## 10. Source Bibliography

### Reference Sources (Priority 1 — README_LINKS.md)

[REF:#1] ASX, "ASX Equities Trading", https://www.asx.com.au/markets/trade-our-cash-market/asx-equities-trading.html
[REF:#2] ASX, "Order Controls", https://www.asx.com.au/markets/trade-our-cash-market/asx-equities-trading/order-controls
[REF:#3] ASX, "ASX Centre Point", https://www.asx.com.au/markets/trade-our-cash-market/asx-equities-trading/asx-centre-point.html
[REF:#4] ASX, "ASX Trade New Order Types (PDF)", https://www.asx.com.au/documents/resources/asx_trade_new_order_types.pdf
[REF:#5] ASX, "Operating Rules Procedures — Draft (PDF)", https://www.asx.com.au/documents/rules/Draft_ASX_Operating_Rules_procedures.pdf
[REF:#6] ASX, "Operating Rules Procedures — 2010 (PDF)", https://www.asx.com.au/documents/rules/asx_or_procedures.pdf

### Web Sources (Priority 3 — Gap Fill)

[WEB:wikipedia] Australian Securities Exchange — Wikipedia, https://en.wikipedia.org/wiki/Australian_Securities_Exchange, Accessed 2026-03-27
[WEB:asx.com.au/trading-hours] "Cash Market Trading Hours", https://www.asx.com.au/markets/market-resources/trading-hours-calendar/cash-market-trading-hours, Accessed 2026-03-27
[WEB:asx.com.au/centre-point] "ASX Centre Point", https://www.asx.com.au/markets/trade-our-cash-market/asx-equities-trading/asx-centre-point, Accessed 2026-03-27
[WEB:asx.com.au/mm] "Market Maker Arrangements", https://www.asx.com.au/markets/market-resources/market-maker-arrangements, Accessed 2026-03-27
[WEB:asx.com.au/blog] "ASX Capital Markets: 2025 Year in Review", https://www.asx.com.au/blog/listed-at-asx/asx-capital-markets-2025-year-in-review-and-2026-outlook, Accessed 2026-03-27
[WEB:marketsmedia.com] "A Deep Dive into Public Dark Pool Trading in Australia", https://www.marketsmedia.com/a-deep-dive-into-public-dark-pool-trading-in-australia/, Accessed 2026-03-27
[WEB:commsec.com.au] "What do CX, CXXT mean?", https://www.commsec.com.au/support/help-centre/About-the-sharemarket/what-do-cx-cxxt-and-nxxt-mean.html, Accessed 2026-03-27
[WEB:asx-ouch] "ASX Trade OUCH Message Specification (Apr 2025)", https://www.asxonline.com/content/dam/asxonline/public/documents/asx-trade-refresh-manuals/asx-trade-ouch-message-specification.pdf, Accessed 2026-03-27

---

*Report version: 1.0 | Batch: 3 | Created: 2026-03-27 | Language: English*
