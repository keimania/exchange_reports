# NASDAQ — Exchange Report

---

## 1. Exchange Overview

**Full Legal Name**: The Nasdaq Stock Market LLC
**Country**: United States of America
**Founding Year**: 1971 (first electronic stock market); became registered exchange 2006 [WEB:wikipedia]
**Parent Group**: Nasdaq, Inc. [WEB:nasdaq.com]

**Market Model**: Pure electronic order-driven market with competitive market makers [REF:#1]

**Asset Classes Traded**: [WEB:nasdaq.com]
- Equities (Nasdaq, Nasdaq BX, Nasdaq PSX)
- Options (Nasdaq Options Market, Nasdaq ISE, Nasdaq GEMX, Nasdaq MRX, Nasdaq PHLX)
- ETFs, ETNs

**Regular Trading Hours (ET, UTC−5/−4)**: [REF:#7] [WEB:tradinghours.com]
- Pre-market: 04:00–09:30
- Core trading: 09:30–16:00
- After-hours: 16:00–20:00
- **Proposed**: 23-hour trading (9:00 PM–8:00 PM ET) filed Dec 2025 [WEB:federalregister.gov]

**Key Statistics**: [WEB:marketcap.company] [WEB:bestbrokers]
- Listed companies: ~4,000–4,278
- Market capitalization: ~$28+ trillion
- Average daily volume: ~4+ billion shares

**Recent Major Changes**: [WEB:nasdaq.com]
- 2023: Dynamic M-ELO with AI/ML-adjusted holding periods [WEB:federalregister.gov/melo]
- 2025.12: Filed for 23-hour weekday trading expansion [WEB:federalregister.gov]
- FPGA technology implementation for deterministic matching behavior [REF:#2]

---

## 2. Institutional Philosophy

**Primary Market Model**: Pure electronic, order-driven, no physical trading floor [REF:#1] [REF:#2]

**Design Rationale**: [WEB:wikipedia]
- Founded as the world's first electronic stock market (1971) — designed from inception for speed and technology
- No floor, no specialists, no human intermediaries in execution — all matching is algorithmic
- Emphasizes low-latency access, transparent price discovery, and protocol efficiency (OUCH/ITCH)
- Competitive market maker model rather than exclusive DMM assignment [REF:#1]

**Role of Intermediaries**: [REF:#1] [WEB:finra.org]
- **Registered Market Makers**: Multiple MMs per security (competitive model, not exclusive)
- Must maintain continuous two-sided quotes at designated percentage [WEB:federalregister.gov/rule4613]
- Execute orders at displayed quotation (firm quote rule) [WEB:finra.org]
- No special information advantages — operate on same electronic platform as all participants

**Evolution**: Electronic quotation system (1971) → ECN integration → INET matching engine (2006 Instinet acquisition) → Global technology provider (Nasdaq OMX) → Fintech platform (2025+) [WEB:wikipedia]

---

## 3. Order Types — Basic

### 3.1 Market Order [REF:#1]
- Executes immediately at best available price
- Available: All sessions
- Time-in-force: Day (immediate execution or cancel)

### 3.2 Limit Order [REF:#1]
- Specifies maximum buy / minimum sell price
- If not immediately filled, rests on limit order book
- Time-in-force: Day, GTC, IOC, FOK, Extended Hours, System Hours

### 3.3 Market-on-Open (MOO) [REF:#7] [REF:#8]
- Market order for Opening Cross only
- Entered starting 04:00 ET; executes at 09:30 opening price

### 3.4 Limit-on-Open (LOO) [REF:#7] [REF:#8]
- Limit order for Opening Cross only
- Participates at opening price if within limit

### 3.5 Market-on-Close (MOC) [REF:#7] [REF:#8]
- Market order for Closing Cross only
- Entered during trading day; executes at 16:00 closing price

### 3.6 Limit-on-Close (LOC) [REF:#7] [REF:#8]
- Limit order for Closing Cross only
- Participates at closing price if within limit

---

## 4. Order Types — Advanced

### 4.1 Reserve (Iceberg) Order [REF:#1]
- Partially displayed; hidden reserve replenishes displayed quantity
- Price-time priority: displayed portion gets time priority; reserve gets new timestamp on replenishment

### 4.2 Pegged Orders [REF:#1] [WEB:nasdaqtrader.com]
- **Primary Peg**: Pegged to same-side inside quote
- **Market Peg**: Pegged to contra-side inside quote
- **Midpoint Peg**: Pegged to NBBO midpoint
- Optional offset from peg reference price

### 4.3 Post-Only Order [REF:#1]
- Posts to book only; will not remove liquidity
- If would lock/cross, cancels or reprices (depending on configuration)
- Used for maker rebate capture

### 4.4 Intermarket Sweep Order (ISO) [REF:#1]
- Sweeps multiple price levels on Nasdaq
- Sender handles Reg NMS away-market protection

### 4.5 Imbalance-Only (IO) Orders [REF:#7]
- **IO Open**: Priced limit order to offset opening imbalance
- **IO Close**: Priced limit order to offset closing imbalance
- Must be limit-priced (no market IO orders) [REF:#7]

### 4.6 Non-Displayed Order [REF:#1]
- Hidden order not visible in displayed book
- Executes at midpoint or better
- Lower priority than displayed orders at same price

### 4.7 Time-in-Force Options [REF:#1] [REF:#3]
- **Day**: Expires at 16:00 (or 20:00 for extended hours)
- **GTC**: Good until cancelled
- **IOC**: Immediate or cancel
- **FOK**: Fill or kill
- **Extended Hours**: Active 04:00–20:00
- **System Hours**: Active for all Nasdaq sessions
- **Market Hours**: Active 09:30–16:00 only

---

## 5. Order Types — Exchange-Specific

### 5.1 Midpoint Extended Life Order (M-ELO) [WEB:nasdaq.com/melo] [WEB:nasdaqtrader.com/melo]
- **Nasdaq-unique**: Non-displayed midpoint order with mandatory holding period
- Minimum holding period: 0.5 seconds from acceptance before eligible for execution [WEB:nasdaqtrader.com/melo]
- Designed to reduce information leakage and protect against adverse selection
- Executes only against other M-ELOs or M-ELO+CB orders
- Rationale: Provides safer midpoint execution for institutional investors by filtering latency-sensitive flow

### 5.2 Dynamic M-ELO [WEB:nasdaq.com/dynamic-melo]
- Enhanced M-ELO with AI/ML-adjusted holding periods
- Holding period recalculated every 30 seconds based on real-time market conditions [WEB:federalregister.gov/melo]
- Shorter hold during stable markets, longer during volatile conditions
- SEC-approved September 2023 [WEB:federalregister.gov/melo]

### 5.3 M-ELO+CB (M-ELO Plus Continuous Book) [WEB:nasdaq.com/melo]
- Combines M-ELO with continuous book interaction
- May execute against M-ELOs AND against non-displayed midpoint/MPPO orders
- Broader execution opportunity while retaining holding period protection

### 5.4 Midpoint Peg Post-Only (MPPO) Order [WEB:nasdaqtrader.com/mppo]
- Non-displayed, priced at NBBO midpoint
- Post-only: executes on entry only when economically beneficial
- No holding period (unlike M-ELO)
- Rationale: Passive midpoint liquidity provision without adverse selection timer

### 5.5 Market Maker Peg Order [WEB:nasdaqtrader.com/mmpeg]
- Exclusive to registered Nasdaq market makers
- Automatically re-prices to maintain compliance with quoting obligations
- Reduces manual monitoring burden for competitive MMs

### 5.6 Opening/Closing Cross [REF:#7] [REF:#8]
- **Opening Cross**: 09:28–09:30 ET with Net Order Imbalance Indicator (NOII) dissemination from 09:25
- **Closing Cross**: 15:50–16:00 ET with NOII from 15:50
- All nationally-listed securities eligible [REF:#7]
- Single-price execution maximizing matched volume

---

## 6. Matching Engine & Price Discovery

### Trading System: INET [REF:#2] [REF:#3] [WEB:nasdaq.com/matching]
- **Origin**: Acquired via Instinet (2006), originally Island ECN technology [WEB:wikipedia]
- **Architecture**: Horizontally scalable matching engine on commodity hardware [WEB:nasdaq.com/matching]
- **Latency**: Sub-40 microseconds; collocated OUCH: <25μs, FIX: <80μs [WEB:nasdaqtrader.com/latency]
- **Enhancement**: FPGA technology for deterministic peak-time behavior [REF:#2]
- **Network**: 40 Gbps infrastructure [WEB:tradersmagazine.com]

### Protocols [REF:#2] [REF:#3] [REF:#4]
- **OUCH 5.0**: Low-latency order entry protocol (inbound) [REF:#3]
  - Supports limit orders, IoC, DAY, GTC, extended hours [REF:#3]
  - Binary protocol for minimal overhead
- **ITCH 5.0**: Market data feed protocol (outbound) [REF:#5] [REF:#6]
  - Full order book depth (TotalView-ITCH)
  - System events, stock directory, trading action messages
- **FIX**: Industry-standard order entry (higher latency alternative to OUCH)

### Matching Algorithm: Price-Time Priority [REF:#2]
1. **Price priority**: Best price first
2. **Time priority**: Among same-price orders, earliest order first
3. **Display priority**: Displayed orders prioritized over non-displayed at same price
4. Pure algorithmic matching — no human discretion or parity allocation

### Opening Cross [REF:#7] [REF:#8]
- **04:00 ET**: Order entry opens
- **09:25 ET**: NOII dissemination begins (imbalance direction, quantity, indicative price)
- **09:30 ET**: Opening Cross executes — single price maximizing matched volume
- Order participation: MOO, LOO, IO Open, regular limit/market orders

### Closing Cross [REF:#7] [REF:#8]
- **15:50 ET**: NOII dissemination begins
- **16:00 ET**: Closing Cross executes — single price maximizing matched volume
- Order participation: MOC, LOC, IO Close, regular limit orders
- ~15% of daily volume in some securities [WEB:nasdaq.com]

### Tick Size
- Standard: $0.01 for stocks priced >$1.00
- Sub-penny: $0.0001 for stocks priced <$1.00
- Midpoint executions at half-penny ($0.005) increments

### Lot Size
- Standard lot: 100 shares (round lot)
- Odd lots (<100 shares) fully supported on Nasdaq's electronic platform

---

## 7. Safeguard Mechanisms

### 7.1 Market-Wide Circuit Breakers (MWCB) [WEB:nasdaqtrader.com/cb]
- Same rules as NYSE (national regulation):

| Level | Trigger (S&P 500 decline) | Duration | Time Restriction |
|---|---|---|---|
| Level 1 | ≥ 7% | 15-min halt | Before 3:25 PM ET |
| Level 2 | ≥ 13% | 15-min halt | Before 3:25 PM ET |
| Level 3 | ≥ 20% | Remainder of day | Anytime |

### 7.2 Limit Up-Limit Down (LULD) [WEB:luldplan.com]
- Same national plan as NYSE (see NYSE §7.2 for full band details)
- Nasdaq-specific implementation:
  - Trading Pause: If stock remains at LULD band for 15 seconds → 5-minute pause
  - Re-opening: Via Nasdaq Halt Cross mechanism

### 7.3 Clearly Erroneous Execution (CEE) [REF:#1]
- Executions at prices significantly away from prevailing market
- Review request within 30 minutes
- Thresholds based on reference price percentage deviation

### 7.4 Regulatory Trading Halts [REF:#1]
- **T1 (Halt News Pending)**: Material news dissemination pending
- **T2 (Halt News Dissemination)**: News being disseminated
- **T12 (Halt IPO Issue)**: IPO not yet released for trading
- **LUDP**: LULD pause
- Resume via Nasdaq Halt Cross (IPO/Halt Cross mechanism)

### 7.5 Pre-Trade Risk Controls [REF:#2]
- **Order price reasonability**: Orders outside bands rejected
- **Maximum order size limits**: Configurable
- **Risk management gateway**: Pre-trade checks before matching engine
- **Kill Switch**: Cancel all open orders functionality
- **Drop Copy**: Real-time execution copies for risk monitoring

---

## 8. Special Sessions

### 8.1 Pre-Market Session [WEB:tradinghours.com]
- **Hours**: 04:00–09:30 ET
- **Mechanism**: Continuous electronic matching
- **Order types**: Limit orders with Extended Hours TIF
- No Opening/Closing Cross orders accepted during pre-market continuous

### 8.2 Opening Cross [REF:#7] [REF:#8]
- **NOII period**: 09:25–09:30 ET
- **Execution**: 09:30 ET
- **Mechanism**: Single-price auction (Cross)
- **Order types**: MOO, LOO, IO Open, limit, market
- New listings: activate on first trading day [REF:#7]

### 8.3 Core Trading Session [REF:#1]
- **Hours**: 09:30–16:00 ET
- **Mechanism**: Continuous price-time priority matching via INET
- All order types available including M-ELO, MPPO, pegged orders

### 8.4 Closing Cross [REF:#7] [REF:#8]
- **NOII period**: 15:50–16:00 ET
- **Execution**: 16:00 ET
- **Mechanism**: Single-price auction (Cross)
- **Order types**: MOC, LOC, IO Close, limit

### 8.5 After-Hours Session [WEB:tradinghours.com]
- **Hours**: 16:00–20:00 ET
- **Mechanism**: Continuous electronic matching
- **Order types**: Limit orders with Extended Hours TIF
- No market orders; reduced liquidity typical

### 8.6 Halt Cross [REF:#1]
- Used to reopen trading after regulatory halts or LULD pauses
- Similar mechanics to Opening Cross
- NOII published during 5-minute quote-only period before cross

### 8.7 IPO Cross [WEB:nasdaq.com]
- Specific mechanism for first-day trading of new listings
- NOII disseminated during price discovery period
- DMM-free: entirely electronic, no floor broker involvement

---

## 9. LP / Market Maker Obligations

### 9.1 Nasdaq Market Makers (Competitive Model) [REF:#1] [WEB:federalregister.gov/rule4613]

**Structure**: [REF:#1]
- **Multiple market makers per security** (competitive, not exclusive)
- Any registered broker-dealer may register as Nasdaq MM in one or more securities
- No exclusive assignment — contrasts with NYSE's DMM model

**Quoting Obligations (Rule 4613)**: [WEB:federalregister.gov/rule4613]
- Maintain continuous two-sided quotes during market hours
- Price bid/offer at Designated Percentage (set by Nasdaq per security tier)
- Execute at displayed quotation for at least one normal unit of trading (100 shares)
- If unable to fill full displayed size: must update to inferior quote [WEB:finra.org]

**Firm Quote Rule**: [WEB:finra.org]
- MM must honor displayed quotes — execute at displayed price and size
- Applies to all interactions with other FINRA members

**Tools**: [WEB:nasdaqtrader.com/mmpeg]
- Market Maker Peg Order: Auto-reprices to maintain compliance
- Reduces operational burden of manual quote maintenance

### 9.2 Fee Structure / Incentives [WEB:nasdaq.com]
- **Maker-taker model**: Rebate for adding displayed liquidity; fee for removing
- Typical rebate: ~$0.002–0.003 per share for adding liquidity
- Tiered pricing based on volume thresholds
- MMs receive incremental benefits for meeting quoting obligations

### 9.3 Comparison with NYSE DMM [REF:#1]
- **NYSE**: Exclusive 1:1 DMM per security, obligations + privileges
- **Nasdaq**: Many MMs per security, competitive quoting, no exclusive rights
- **Result**: NYSE has deeper guaranteed liquidity per stock; Nasdaq has broader competitive pressure

---

## 10. Source Bibliography

### Reference Sources (Priority 1 — README_LINKS.md)

[REF:#1] Nasdaq, "NASDAQ Rule Book", https://listingcenter.nasdaq.com/rulebook/nasdaq/rules

[REF:#2] Nasdaq, "OUCH Overview", https://www.nasdaqtrader.com/Trader.aspx?id=OUCH

[REF:#3] Nasdaq, "OUCH 5.0 Specification (PDF)", https://nasdaqtrader.com/content/technicalsupport/specifications/TradingProducts/Ouch5.0.pdf

[REF:#4] Nasdaq, "OUCH 5.0 FAQ (PDF)", https://nasdaqtrader.com/content/productsservices/trading/OUCH_5.0_FAQ.pdf

[REF:#5] Nasdaq, "Nordic Equity TotalView-ITCH 3.04.X (PDF)", https://www.nasdaq.com/docs/2025/11/13/Nordic-Equity-TotalView-ITCH-3.04.X.pdf

[REF:#6] Nasdaq, "NASDAQ TotalView", https://data.nasdaq.com/databases/NTV

[REF:#7] Nasdaq, "Opening and Closing Crosses", https://nasdaqtrader.com/Trader.aspx?id=OpenClose

[REF:#8] Nasdaq, "Opening/Closing Cross FAQ (PDF)", https://nasdaqtrader.com/content/productsservices/trading/crosses/openclose_faqs.pdf

[REF:#9] Nasdaq, "Order Types & Routing Strategies (PDF)", https://www.nasdaqtrader.com/content/marketregulation/regnms/rash_strategy.pdf

[REF:#10] Nasdaq, "NASDAQ TotalView Solutions", https://www.nasdaq.com/solutions/data/equities/nasdaq-totalview

[REF:#11] Nasdaq, "TotalView-ITCH Help Center", https://help.data.nasdaq.com/category/970-nasdaq-totalview-itch

[REF:#12] Nasdaq, "OUCH 4.2 Specification (PDF)", https://www.nasdaqtrader.com/content/technicalsupport/specifications/tradingproducts/ouch4.2.pdf

[REF:#13] Nasdaq, "INET Nordic Protocol Specifications", https://www.nasdaq.com/solutions/inet-nordic-protocol-specifications

### Web Sources (Priority 3 — Gap Fill)

[WEB:wikipedia] NASDAQ — Wikipedia, https://en.wikipedia.org/wiki/Nasdaq, Accessed 2026-03-27

[WEB:nasdaq.com] Nasdaq main, https://www.nasdaq.com/, Accessed 2026-03-27

[WEB:nasdaq.com/melo] "Midpoint Extended Life Order (M-ELO)", https://www.nasdaq.com/solutions/dynamic-m-elo, Accessed 2026-03-27

[WEB:nasdaq.com/matching] "Exchange Matching Engine", https://www.nasdaq.com/solutions/fintech/nasdaq-eqlipse/trading-technology/exchange-matching, Accessed 2026-03-27

[WEB:nasdaqtrader.com/melo] "M-ELO FAQs (PDF)", https://www.nasdaqtrader.com/Content/ProductsServices/TRADING/M-ELO-FAQs.pdf, Accessed 2026-03-27

[WEB:nasdaqtrader.com/mppo] "Midpoint Peg Post-Only Factsheet", https://www.nasdaqtrader.com/content/productsservices/trading/MPPO_factsheet.pdf, Accessed 2026-03-27

[WEB:nasdaqtrader.com/mmpeg] "Market Maker PEG Order Factsheet", https://www.nasdaqtrader.com/content/productsservices/trading/mmpegorder_factsheet.pdf, Accessed 2026-03-27

[WEB:nasdaqtrader.com/latency] "OUCH Latency Measurements", https://www.nasdaqtrader.com/snippets/inet2.html, Accessed 2026-03-27

[WEB:nasdaqtrader.com/cb] "Circuit Breaker", https://www.nasdaqtrader.com/trader.aspx?id=CircuitBreaker, Accessed 2026-03-27

[WEB:tradinghours.com] "NASDAQ Market Hours 2026", https://www.tradinghours.com/markets/nasdaq, Accessed 2026-03-27

[WEB:federalregister.gov] "NASDAQ 23-Hour Trading Proposal", https://www.federalregister.gov/documents/2026/01/13/2026-00416/, Accessed 2026-03-27

[WEB:federalregister.gov/melo] "Dynamic M-ELO Approval", https://www.federalregister.gov/documents/2023/09/13/2023-19728/, Accessed 2026-03-27

[WEB:federalregister.gov/rule4613] "Rule 4613 Amendment", https://www.federalregister.gov/documents/2020/11/17/2020-25270/, Accessed 2026-03-27

[WEB:finra.org] "Rule 4613A Character of Quotations", https://www.finra.org/rules-guidance/rulebooks/retired-rules/4613a, Accessed 2026-03-27

[WEB:marketcap.company] "NASDAQ Exchange Market Capitalization", https://marketcap.company/stock-exchanges/nasdaq-nasdaq-exchange-market-capitalization/, Accessed 2026-03-27

[WEB:bestbrokers] "Stock Market Trading Statistics 2026", https://www.bestbrokers.com/stock-trading/stock-trading-market-statistics/, Accessed 2026-03-27

[WEB:luldplan.com] "Limit Up Limit Down", https://www.luldplan.com/, Accessed 2026-03-27

---

*Report version: 1.0 | Batch: 1 | Created: 2026-03-27 | Language: English*
