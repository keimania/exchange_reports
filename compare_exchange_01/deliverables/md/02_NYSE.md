# NYSE (New York Stock Exchange) — Exchange Report

---

## 1. Exchange Overview

**Full Legal Name**: New York Stock Exchange LLC
**Country**: United States of America
**Founding Year**: 1792 (Buttonwood Agreement); formally organized 1817 [WEB:wikipedia]
**Parent Group**: Intercontinental Exchange (ICE), acquired 2013 [WEB:wikipedia]

**Market Model**: Hybrid — electronic order-driven with Designated Market Maker (DMM) and physical trading floor [REF:#1]

**Asset Classes Traded**: [REF:#1]
- Equities (NYSE, NYSE Arca, NYSE American, NYSE National, NYSE Texas)
- Options (NYSE Arca Options, NYSE American Options)
- Bonds (NYSE Bonds)
- ETFs, ETNs, Closed-End Funds, SPACs

**Regular Trading Hours (ET, UTC−5/−4)**: [REF:#2]
- Pre-opening (order queuing): 06:30
- Early trading (Tapes B&C, Arca): from 04:00 (Arca) or 07:00
- Core trading: 09:30–16:00
- Late trading (Arca, American): 16:00–20:00

**Key Statistics**: [WEB:bestbrokers] [WEB:statista]
- Listed companies: ~2,400+ (NYSE primary)
- Market capitalization: ~$30+ trillion (largest exchange globally)
- Average daily volume: ~1.54 billion shares / ~$80.6 billion (Nov 2025)

**Recent Major Changes**: [WEB:nyse.com]
- 2024: Closing D-Order imbalance threshold moved to 3:50 PM for transparency
- 2025.08: Floor brokers migrated to automated OMS for D-Order entry
- Extended trading hours expansion across NYSE group venues

---

## 2. Institutional Philosophy

**Primary Market Model**: Hybrid — combines electronic matching with human-facilitated price discovery [REF:#1]

**Design Rationale**: [REF:#1] [WEB:nyse.com/market-model]
- NYSE uniquely retains a **physical trading floor** where DMMs and floor brokers interact
- The hybrid model aims to capture benefits of both: electronic speed/efficiency + human judgment for complex situations (large imbalances, volatility events, IPO pricing)
- DMMs serve as assigned specialists per security, providing continuous two-sided liquidity and managing opening/closing auctions [REF:#1]
- Floor brokers represent institutional clients, accessing unique order types (D-Orders) available only on the floor [WEB:nyse.com/d-orders]

**Parity/Priority Allocation**: [REF:#1]
- NYSE uses a unique allocation model that "rewards price setters and then allocates incoming orders across multiple participants resting at the same price"
- Differs from pure price-time priority used at KRX/NASDAQ

**Evolution**: Physical floor (1792) → specialist system → hybrid electronic + floor (2006 merger with Archipelago) → Pillar platform migration (2016–present) [WEB:wikipedia]

**Role of Intermediaries**: [REF:#1]
- **DMMs**: Exclusive assignment per security; obligated to maintain fair and orderly markets [REF:#3]
- **Supplemental Liquidity Providers (SLPs)**: Electronic high-volume members adding displayed liquidity [REF:#1]
- **Floor Brokers**: Human representatives executing institutional orders with access to D-Orders [REF:#1]

---

## 3. Order Types — Basic

### 3.1 Market Order [REF:#2]
- No price specified; executes at best available price
- Available in all sessions
- During opening/closing auctions: participates at auction price

### 3.2 Limit Order [REF:#2]
- Specifies maximum buy / minimum sell price
- Available in all sessions
- Time-in-force: Day (default), GTC, IOC, FOK

### 3.3 Stop Order [REF:#2]
- Becomes market order when stop price is reached
- Buy stop: triggered at or above stop price
- Sell stop: triggered at or below stop price

### 3.4 Stop-Limit Order [REF:#2]
- Becomes limit order when stop price is reached
- Two prices specified: stop (trigger) and limit (execution)

### 3.5 Market-on-Open (MOO) [REF:#2] [REF:#6]
- Market order for opening auction only
- Guaranteed participation in opening price determination

### 3.6 Limit-on-Open (LOO) [REF:#2] [REF:#6]
- Limit order for opening auction only
- Participates at specified price or better in opening auction

### 3.7 Market-on-Close (MOC) [REF:#2] [WEB:nyse.com/closing-auction]
- Market order for closing auction
- Entry cutoff: 3:50 PM ET
- Guaranteed fill at closing auction price

### 3.8 Limit-on-Close (LOC) [REF:#2] [WEB:nyse.com/closing-auction]
- Limit order for closing auction
- Entry cutoff: 3:50 PM ET
- Participates at closing auction price if within limit

---

## 4. Order Types — Advanced

### 4.1 Reserve (Iceberg) Order [REF:#6]
- Displays only a portion (MaxFloor) of total quantity
- Hidden reserve replenishes as displayed quantity executes
- Mixed lot MaxFloor allowed [REF:#6]

### 4.2 Pegged Orders [REF:#6]
- **Primary Peg**: Pegged to same-side NBBO (best bid for buy, best offer for sell)
- **Market Peg**: Pegged to contra-side NBBO
- **Midpoint Peg**: Pegged to NBBO midpoint
- Discretionary offset available for all peg types

### 4.3 Midpoint Passive Liquidity (MPL) Order [REF:#6]
- Non-displayed order priced at NBBO midpoint
- Provides passive price improvement
- Available only during core trading

### 4.4 Add Liquidity Only (ALO) Order [REF:#6]
- Posts to book only; does not remove liquidity on arrival
- Cancelled or repriced if it would execute immediately
- Used by participants seeking maker rebates

### 4.5 Intermarket Sweep Order (ISO) [REF:#6]
- Enables sweeping across multiple price levels on NYSE
- Sender responsible for simultaneously routing to away markets at better prices (Reg NMS compliance)

### 4.6 Imbalance Offset (IO) Orders [WEB:nyse.com/closing-auction]
- **Closing Offset (CO)**: Offsets closing auction imbalance; accepted after 3:50 PM
- **Opening IO**: Offsets opening auction imbalance
- Can only offset published imbalance direction

### 4.7 Tracking Orders [REF:#6]
- Non-displayed limit orders on NYSE floor
- Trade at DMM or floor broker discretion within specified price range

---

## 5. Order Types — Exchange-Specific

### 5.1 D-Order (Closing D-Order / Opening D-Order) [WEB:nyse.com/d-orders]
- **NYSE-unique**: Available only through floor brokers
- Closing D-Order: Discretionary interest for closing auction with undisplayed price range
- Opening D-Order: DMM interest for opening auction
- Entry deadline: 3:59:50 PM for Closing D-Orders
- As of Aug 2025: Automated via third-party OMS [WEB:nyse.com]
- Rationale: Combines human judgment with electronic execution for large auction interest

### 5.2 DMM Interest Orders [REF:#3]
- **DMM Proprietary Orders**: DMMs trade for their own account to maintain orderly markets
- DMMs can add capital to offset auction imbalances [WEB:nyse.com/closing-auction]
- Subject to Rule 104 restrictions (e.g., last 10 minutes position rules) [WEB:sec.gov/rule104]

### 5.3 Retail Liquidity Program Orders [REF:#1]
- **Retail Taker Orders**: Agency orders from natural persons
- **Retail Price Improvement (RPI) Orders**: Non-displayed interest priced better than PBBO
- **Retail Attested Orders**: Enhanced economics for individual investors
- NYSE-specific program to attract retail order flow with price improvement

### 5.4 SLP Interest [REF:#1]
- SLP-Prop and SLMM order categories
- Must maintain NBBO at least 10% of trading day per assigned security [WEB:liquidity-provider.com]
- Receive financial rebates for adding displayed liquidity

---

## 6. Matching Engine & Price Discovery

### Trading System: Pillar [REF:#4] [REF:#5]
- **Launch**: Phased migration 2016–present
- **Architecture**: Unified technology platform for all NYSE group exchanges [REF:#5]
- **Protocols**: FIX Protocol + Binary Protocol [REF:#4] [REF:#5]
- **Risk Controls**: Integrated pre-trade controls (see §7) [REF:#7]
- **Latency**: Sub-millisecond (specific figures not publicly disclosed)

### Matching Algorithm: Price/Parity/Priority [REF:#1]
1. **Price priority**: Best-priced orders first
2. **Parity allocation**: At same price level, orders allocated among multiple participants
3. **Priority for price setters**: First order establishing a new best price gets priority
- This differs from pure price-time priority (KRX, NASDAQ) — NYSE's model rewards liquidity provision more broadly

### Opening Auction [REF:#1] [WEB:nyse.com/auction]
- Orders accumulate from 06:30 ET
- At 09:30: DMM facilitates opening price determination
- **Imbalance information**: Published starting ~09:28 for primary-listed securities
- DMM can add capital to offset imbalances
- Single equilibrium price maximizing matched volume

### Closing Auction [WEB:nyse.com/closing-auction]
- **3:50 PM**: MOC/LOC entry cutoff; imbalance publication begins (1-second intervals)
- **3:50–4:00 PM**: Closing Offset orders accepted; D-Orders active
- **3:59:50 PM**: D-Orders frozen
- **4:00 PM**: Auction executes within **Auction Collars**:
  - Price ≤$25: ±5% collar
  - Price $25–$50: ±2% collar
  - Price >$50: ±1% collar
  - Minimum collar: $0.15 or percentage, whichever greater

### Tick Size [WEB:sec.gov]
- Standard: $0.01 for stocks priced >$1.00
- Sub-penny: $0.001 for stocks priced <$1.00
- Midpoint executions at half-penny increments permitted

### Lot Size
- Standard lot: 100 shares (round lot)
- Odd lots: <100 shares (increasingly relevant; now included in some auction calculations)

---

## 7. Safeguard Mechanisms

### 7.1 Market-Wide Circuit Breakers (MWCB) [REF:#2] [WEB:investor.gov]

| Level | Trigger (S&P 500 decline from prior close) | Duration | Time Restriction |
|---|---|---|---|
| Level 1 | ≥ 7% | 15-min halt | Before 3:25 PM ET only |
| Level 2 | ≥ 13% | 15-min halt | Before 3:25 PM ET only |
| Level 3 | ≥ 20% | Trading halted for remainder of day | Anytime |

- Levels reset daily based on prior day's S&P 500 closing price [WEB:investor.gov]
- April 7, 2025: Level 1 circuit breaker triggered on tariff announcement [WEB:cnbc.com]

### 7.2 Limit Up-Limit Down (LULD) [WEB:luldplan.com]

| Tier | Securities | Regular Hours (9:45–3:35) | Open/Close (9:30–9:45, 3:35–4:00) |
|---|---|---|---|
| Tier 1 | S&P 500, Russell 1000, select ETPs | ±5% | ±10% (doubled) |
| Tier 2 | All other NMS stocks >$3.00 | ±10% | ±20% (doubled) |
| Tier 2 | NMS stocks ≤$3.00 | ±20% | ±40% (doubled) |
| Low-priced | Stocks ≤$0.75 | Lesser of $0.15 or 75% | Lesser of $0.30 or 150% |

- Reference price: 5-minute arithmetic mean of eligible reported transactions [WEB:luldplan.com]
- Updated every 30 seconds
- If stock hits LULD band: 15-second trading pause → if still at limit, 5-minute halt

### 7.3 Trading Halts [REF:#2]
- **Regulatory halts**: News-pending (T1/T2), SEC suspension
- **LULD halts**: Triggered by price band violations
- **Operational halts**: Technical issues
- Resume via reopening auction with DMM facilitation

### 7.4 Pre-Trade Risk Controls (Pillar) [REF:#7]
- **Maximum order size/value limits**: Configurable per firm
- **Price reasonability checks**: Orders outside bands rejected
- **Kill Switch**: Firms can cancel all open orders and block new entry [REF:#7]
- **Cancel on Disconnect**: Auto-cancels orders if connectivity lost [REF:#7]
- **Gross Credit Controls**: Position and credit limit monitoring
- Extended hours LULD: Optional double-wide bands (20%/10%/6%) [WEB:nyse.com]

### 7.5 Clearly Erroneous Execution (CEE) [REF:#2]
- Members may request execution review within 30 minutes
- Reference price-based thresholds for bust/adjust decisions

---

## 8. Special Sessions

### 8.1 Pre-Opening Session [REF:#2]
- **Hours**: 06:30 ET (order queuing begins)
- **NYSE Primary (Tape A)**: Orders queued until 09:30 opening auction
- **NYSE Arca**: Early trading from 04:00 ET; Early Open Auction at 04:00
- **NYSE American/National/Texas**: Early trading from 07:00 ET
- **Order types**: Limit orders primarily

### 8.2 Opening Auction [REF:#1] [WEB:nyse.com/auction]
- **Time**: 09:30 ET
- **Mechanism**: DMM-facilitated single-price auction
- **Order types**: MOO, LOO, Limit, Market, IO orders
- **Imbalance info**: Published starting ~09:28 for primary-listed
- Floor broker and DMM participation for price discovery

### 8.3 Core Trading Session [REF:#2]
- **Hours**: 09:30–16:00 ET
- **Mechanism**: Continuous electronic matching (Pillar) + floor interaction
- All order types available
- DMM continuous quoting obligations active

### 8.4 Closing Auction [WEB:nyse.com/closing-auction]
- **Imbalance period**: 3:50–4:00 PM ET
- **Mechanism**: DMM-facilitated single-price auction with Auction Collars
- **Order types**: MOC, LOC, Closing IO, Closing D-Orders
- ~10% of daily volume executes at close [WEB:nyse.com/closing-auction]

### 8.5 After-Hours / Late Trading [REF:#2]
- **NYSE Arca**: 16:00–20:00 ET
- **NYSE American**: 16:00–20:00 ET
- **NYSE Primary**: No formal late session for Tape A securities (traded on Arca after hours)
- **Order types**: Limit orders only; no market orders

### 8.6 Block Trade / Large Orders
- No formal separate block facility — large orders handled via:
  - Floor broker discretion with D-Orders and Tracking Orders
  - Dark pool / ATS alternatives (external)
  - SLP institutional-size interest
  - Auction participation for large closing interest

---

## 9. LP / Market Maker Obligations

### 9.1 Designated Market Makers (DMMs) [REF:#1] [REF:#3]

**Structure**: [REF:#3]
- One DMM firm assigned per NYSE-listed security
- Currently 3 firms: Citadel Securities, Virtu Americas, GTS Securities [REF:#1]
- Operate both electronically and manually on trading floor

**Obligations (Rule 104)**: [REF:#3] [WEB:sec.gov/rule104]
- Maintain continuous two-sided quotes
- Quoting at NBBO for:
  - Securities with CADV ≥ 1M shares: ≥ 5% of trading day
  - Securities with CADV < 1M shares: ≥ 10% of trading day
  - Listed ETPs: ≥ 25% of trading day
- Facilitate opening and closing auctions — set prices, absorb imbalances [REF:#1]
- Maintain fair and orderly markets — engage in stabilizing transactions [REF:#3]
- Subject to restrictions on proprietary trading in last 10 minutes [WEB:sec.gov/rule104]

**Privileges**:
- Exclusive assignment per security
- Access to floor-based information flow
- Fee advantages and participation in allocation model

### 9.2 Supplemental Liquidity Providers (SLPs) [REF:#1] [WEB:liquidity-provider.com]

**Structure (Rule 107B)**: [WEB:sec.gov/slp]
- Two categories: SLP-Prop (proprietary) and SLMM (registered market makers) [REF:#1]
- Electronic participants — no floor presence required

**Obligations**: [WEB:liquidity-provider.com]
- Maintain bid or offer at NBBO for ≥ 10% of trading day per assigned security
- ADV > 10 million shares across all assigned securities per month
- Must add displayed liquidity (no hidden-only participation)

**Privileges**:
- Financial rebates: ~$0.0020 per executed share (meeting all requirements) [WEB:sec.gov/slp]
- Three consecutive months of non-compliance → loss of SLP status

### 9.3 Retail Liquidity Program [REF:#1]
- Incentivizes retail-friendly pricing via RPI orders
- Providers offer price improvement ≥$0.001 better than PBBO
- NYSE publishes Retail Liquidity Indicator when better prices available

---

## 10. Source Bibliography

### Reference Sources (Priority 1 — README_LINKS.md)

[REF:#1] NYSE, "NYSE Market Model", https://www.nyse.com/market-model

[REF:#2] NYSE, "NYSE Trading Information", https://www.nyse.com/markets/nyse/trading-info

[REF:#3] NYSE, "Rule Interpretations — Rule 104 (DMM)", https://www.nyse.com/publicdocs/nyse/markets/nyse/rule-interpretations/2014/14-2.pdf

[REF:#4] NYSE, "NYSE Pillar Gateway FIX Protocol Specification (PDF)", https://www.nyse.com/publicdocs/nyse/NYSE_Pillar_Gateway_FIX_Protocol_Specification.pdf

[REF:#5] NYSE, "NYSE Pillar Gateway Binary Protocol Specification (PDF)", https://www.nyse.com/publicdocs/nyse/NYSE_Pillar_Gateway_Binary_Protocol_Specification.pdf

[REF:#6] NYSE, "Pillar Order Type Differences (PDF)", https://www.nyse.com/publicdocs/nyse/markets/nyse/Pillar_Differences.pdf

[REF:#7] NYSE, "NYSE Pillar Risk Controls (PDF)", https://www.nyse.com/publicdocs/nyse/NYSE_Pillar_Risk_Controls.pdf

[REF:#8] NYSE, "Functional Differences NYSE Pillar (PDF)", https://www.nyse.com/publicdocs/nyse/markets/nyse/Functional_Differences_NYSE_Pillar.pdf

### Web Sources (Priority 3 — Gap Fill)

[WEB:nyse.com/market-model] NYSE Market Model overview, https://www.nyse.com/market-model, Accessed 2026-03-27

[WEB:nyse.com/closing-auction] "An Insider's Guide to the NYSE Closing Auction", https://www.nyse.com/article/nyse-closing-auction-insiders-guide, Accessed 2026-03-27

[WEB:nyse.com/d-orders] "Getting to know D Orders", NYSE Data Insights, https://www.nyse.com/data-insights/getting-to-know-d-orders-a-unique-execution-tool-for-nyse-floor-brokers, Accessed 2026-03-27

[WEB:nyse.com/auction] "NYSE Auction Tool", https://www.nyse.com/data-insights/nyse-introduces-the-enhanced-nyse-auction-tool-with-opening-imbalance-history, Accessed 2026-03-27

[WEB:wikipedia] New York Stock Exchange — Wikipedia, https://en.wikipedia.org/wiki/New_York_Stock_Exchange, Accessed 2026-03-27

[WEB:investor.gov] "Stock Market Circuit Breakers", Investor.gov, https://www.investor.gov/introduction-investing/investing-basics/glossary/stock-market-circuit-breakers, Accessed 2026-03-27

[WEB:luldplan.com] "Limit Up Limit Down", https://www.luldplan.com/, Accessed 2026-03-27

[WEB:liquidity-provider.com] "What is the Role of SLP on NYSE?", https://liquidity-provider.com/articles/what-is-a-supplemental-liquidity-provider-slp-on-the-nyse/, Accessed 2026-03-27

[WEB:sec.gov/rule104] SEC Filing — NYSE Rule 104, https://www.sec.gov/files/rules/sro/nyse/2019/34-87056.pdf, Accessed 2026-03-27

[WEB:sec.gov/slp] SEC Filing — NYSE Rule 107B SLP, https://www.sec.gov/files/rules/sro/nyse/2012/34-66821-ex5.pdf, Accessed 2026-03-27

[WEB:bestbrokers] "Stock Market Trading Statistics 2026", https://www.bestbrokers.com/stock-trading/stock-trading-market-statistics/, Accessed 2026-03-27

[WEB:statista] "NYSE and Nasdaq: market cap comparison 2025", https://www.statista.com/statistics/1277195/nyse-nasdaq-comparison-market-capitalization-listed-companies/, Accessed 2026-03-27

[WEB:cnbc.com] "S&P 500 circuit breaker on tariff worries", CNBC, https://www.cnbc.com/2025/04/06/sp-500-circuit-breaker-on-tariff-worries-what-that-means.html, Accessed 2026-03-27

---

*Report version: 1.0 | Batch: 1 | Created: 2026-03-27 | Language: English*
