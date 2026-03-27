# TSE / JPX (Tokyo Stock Exchange) — Exchange Report

---

## 1. Exchange Overview

**Full Legal Name**: Tokyo Stock Exchange, Inc. (株式会社東京証券取引所)
**Country**: Japan
**Founding Year**: 1878 (original); re-established 1949; merged into JPX 2013 [WEB:wikipedia]
**Parent Group**: Japan Exchange Group, Inc. (JPX) — formed 2013 by merger of TSE and Osaka Securities Exchange (OSE) [WEB:wikipedia]

**Market Model**: Pure order-driven market with Itayose (call auction) + Zaraba (continuous) dual mechanism [REF:#2]

**Asset Classes Traded**: [REF:#1] [WEB:jpx.co.jp]
- Equities (Prime, Standard, Growth, TOKYO PRO Market)
- ETFs, ETNs, REITs, Infrastructure Funds
- Derivatives (via OSE — Nikkei 225 futures/options, TOPIX futures, JGB futures)
- Bonds (via OSE)

**Regular Trading Hours (JST, UTC+9)**: [REF:#1] [WEB:market-clock.com]
- Morning session: 09:00–11:30
- Lunch break: 11:30–12:30
- Afternoon session: 12:30–15:25 (Zaraba)
- **Closing Auction Session (CAS)**: 15:25–15:30 (NEW — arrowhead 4.0)
- Order acceptance: from 08:00 (morning) and 12:05 (afternoon)

**Key Statistics**: [WEB:jpx.co.jp] [WEB:statista]
- Listed companies: ~3,945 (Prime: 1,599, Standard: 1,569, Growth: 614, PRO: 163) as of 2025
- Annual trading value (2025): ¥1,419.6 trillion (record high — Prime domestic common stocks) [WEB:jpx.co.jp/trading-overview]
- Market capitalization: ~¥900+ trillion (third largest globally)

**Recent Major Changes**: [WEB:fujitsu.com] [WEB:jpx.co.jp]
- 2024.11.05: arrowhead 4.0 launched — fourth-generation trading system
- 2024.11.05: Trading hours extended by 30 min (afternoon close: 15:25→15:30 with CAS)
- 2024.11.05: Closing Auction Session (CAS) introduced
- 2022.04: Market restructuring — First/Second/Mothers/JASDAQ → Prime/Standard/Growth

---

## 2. Institutional Philosophy

**Primary Market Model**: Pure order-driven, auction-based with dual mechanism [REF:#2]
- **Itayose (板寄せ, Call Auction)**: Used for opening, closing, and post-halt price determination
- **Zaraba (ザラバ, Continuous Trading)**: Used during regular intraday trading
- No designated market maker for general equities [REF:#1]

**Design Rationale**: [WEB:wikipedia] [REF:#1]
- Japanese exchange tradition emphasizing order-book transparency and fairness
- Dual mechanism combines: batch processing for equilibrium prices (Itayose) + continuous matching for real-time price discovery (Zaraba)
- No floor brokers or human intermediaries — all electronic via arrowhead [REF:#8]
- Market maker programs limited to ETFs (incentive-based, not mandatory for stocks) [WEB:jpx.co.jp/etf-mm]

**Evolution**: Physical floor (1878) → electronic (1999 system upgrade) → arrowhead 1.0 (2010) → 2.0 (2015) → 3.0 (2019) → **4.0 (2024.11)** [WEB:fujitsu.com]

---

## 3. Order Types — Basic

### 3.1 Limit Order (指値注文) [REF:#2] [REF:#3]
- Specifies price, quantity, and side (buy/sell)
- Rests on order book if not immediately matchable
- Time-in-force: Day (default — expires at session end)
- Available in all sessions

### 3.2 Market Order (成行注文) [REF:#2] [REF:#3]
- No price specified; executes at best available price
- In Itayose: treated as willing to trade at any price within daily limits [REF:#2]
- In Zaraba: sweeps order book at available prices [REF:#2]
- Available in all sessions

### 3.3 Market-on-Open (寄付注文) [WEB:ppro8wiki]
- Market order targeting opening Itayose price
- Executes only at opening price determination

### 3.4 Market-on-Close (引け注文) [WEB:ppro8wiki]
- Market order targeting closing Itayose/CAS price
- Executes only at closing price determination

### 3.5 Limit-on-Open (LOO) [WEB:ppro8wiki]
- Limit order for opening auction only

### 3.6 Limit-on-Close (LOC) [WEB:ppro8wiki]
- Limit order for closing auction only

---

## 4. Order Types — Advanced

### 4.1 IOC (Immediate-or-Cancel) [REF:#3] [WEB:ppro8wiki]
- Executes immediately against available liquidity; unfilled portion cancelled
- Available for both limit and market orders
- Used during Zaraba session

### 4.2 FOK (Fill-or-Kill) [REF:#3]
- Must fill entirely or cancel completely
- Available during Zaraba session

### 4.3 Conditional Orders [REF:#1]
- Stop orders converted to market/limit upon trigger price being reached
- Used for risk management and algorithmic strategies

### 4.4 Time-in-Force [REF:#3]
- **Day**: Default — expires at end of trading day
- **IOC**: Immediate or cancel
- **FOK**: Fill or kill
- Note: TSE does not offer GTC for equities — all orders are day orders

---

## 5. Order Types — Exchange-Specific

### 5.1 Funari Order (引成注文) [REF:#2] [WEB:ppro8wiki]
- **TSE-unique**: Limit order during Zaraba that automatically converts to market order for closing Itayose/CAS
- If executed during continuous trading: behaves as standard limit
- If unexecuted at session close: becomes market order for closing auction [REF:#2]
- Closest analog: KRX's 조건부지정가호가 (Conditional Limit Order)
- Rationale: Combines intraday limit discipline with guaranteed closing participation

### 5.2 Conditional Limit at Close [REF:#1]
- Variant of closing participation order with price constraint
- Participates in closing auction only if price is within specified range

### 5.3 Special Quote (特別気配, Tokubetsu Kehai) [WEB:wikipedia] [WEB:nber.org]
- **TSE-unique mechanism**: Not an order type but a system-generated indicative quote
- Issued when order imbalance prevents normal price discovery at open or during trading
- Flags transient order imbalances to attract counterparty orders
- Moves in increments until sufficient counter-orders arrive
- Functions as a "slow-motion auction" — unique alternative to hard trading halts
- Effectively a volatility management tool integrated into price formation

---

## 6. Matching Engine & Price Discovery

### Trading System: arrowhead 4.0 [REF:#8] [REF:#9] [WEB:fujitsu.com]
- **Launch**: November 5, 2024 (fourth generation since 2010) [WEB:fujitsu.com]
- **Developer**: Fujitsu [WEB:fujitsu.com]
- **Infrastructure**: 462 Fujitsu PRIMERGY RX2540 M6 x86 servers [WEB:fujitsu.com]
- **Software**: Fujitsu Software Primesoft Server — ultra-high-speed in-memory data management [WEB:fujitsu.com]
- **Latency**: Microsecond-level order processing (exact figure not disclosed; prior gen: ~0.5 ms) [WEB:fujitsu.com]
- **Reliability**: Triple memory replication of trading data; parallel server operation; sub-second failover with zero data loss [WEB:fujitsu.com]
- **New features (4.0)**: Closing Auction Session, 30-min trading hours extension, per-order market information distribution, bulk order cancellation [WEB:fujitsu.com]

### Matching Algorithm [REF:#2]

**Itayose (板寄せ, Call Auction)**: [REF:#2]
1. All accumulated orders treated as simultaneous (no time priority)
2. Single price determined to: maximize traded volume, minimize untraded volume
3. All sell orders above the price and all buy orders below execute
4. Used for: opening, closing (CAS), post-halt reopening

**Zaraba (ザラバ, Continuous Trading)**: [REF:#2]
1. Price-time priority matching
2. Incoming order matches against resting orders at best available price
3. Execution when lowest ask ≤ highest bid
4. Unmatched portion rests on book

### Opening Price (Itayose at 09:00) [REF:#2]
- Orders accumulate from 08:00
- At 09:00: Itayose determines single opening price
- If insufficient orders: Special Quote (Tokubetsu Kehai) issued

### Closing Price — Closing Auction Session (CAS) [WEB:jpx.co.jp] [WEB:globaltrading.net]
- **15:25**: Zaraba ends; pre-closing order acceptance period begins
- During pre-closing (15:25–15:30): orders accepted but no trades executed
- Funari orders and on-close orders registered in order book [WEB:medium.com/tokyo-fintech]
- **15:30**: Itayose determines closing price
- CAS introduced November 2024 to improve transparency of closing price formation [WEB:jpx.co.jp/closing-auction]

### Tick Size Regime [REF:#4] [WEB:jpx.co.jp/tick-size]
TSE uses tiered tick sizes by price level. For **TOPIX 500 constituents** (narrower ticks):

| Price Range (¥) | Tick Size (¥) |
|---|---|
| < 1,000 | 0.1 |
| 1,000–2,999 | 0.5 |
| 3,000–4,999 | 1 |
| 5,000–9,999 | 5 |
| 10,000–29,999 | 5 |
| 30,000–49,999 | 10 |
| 50,000–99,999 | 50 |
| ≥ 100,000 | 100 |

For **other stocks**: wider tick sizes (e.g., ¥1 for <3,000; ¥5 for 3,000–5,000; ¥10 for 5,000–30,000; ¥100 for 30,000–50,000, etc.) [WEB:jpx.co.jp/tick-size]

### Lot Size (Trading Unit) [REF:#1] [WEB:jpx.co.jp/unit]
- **Standardized at 100 shares** for all domestic stocks (since October 2018)
- Previously varied (1, 10, 50, 100, 500, 1000 shares)

---

## 7. Safeguard Mechanisms

### 7.1 Daily Price Limits (値幅制限) [REF:#4] [WEB:jpx.co.jp/price-limits]
- Absolute yen-denominated limits set by base price level (NOT percentage-based like KRX)
- Base price = previous day's closing price
- Example: Base price ¥1,000–1,499 → daily limit ±¥300 [WEB:futunn.com]
- Limits widen with higher price levels
- Can be broadened for individual issues experiencing sustained limit-hits [WEB:jpx.co.jp/broadened]

### 7.2 Special Quote System (特別気配, Tokubetsu Kehai) [WEB:wikipedia] [WEB:nber.org]
- When opening/intraday order imbalance prevents normal matching:
  - Exchange issues special indicative quote (not a trade)
  - Quote moves in preset increments toward equilibrium
  - Attracts counter-orders gradually
- Functions as a **soft circuit breaker** — slows rather than halts price discovery
- Unique to TSE — other exchanges use hard halts for similar situations

### 7.3 Circuit Breakers (Derivatives) [WEB:jpx.co.jp/cb]
- Nikkei 225 / TOPIX futures: ~8% decline triggers 10-minute halt
- April 2025: Nikkei 225 futures circuit breaker triggered on tariff concerns [WEB:forexfactory.com]
- Note: Equities on TSE do NOT have market-wide circuit breakers — they use daily price limits + special quotes instead

### 7.4 Trading Halts [REF:#1]
- Individual stock halts for material information dissemination
- Resume via Itayose (call auction) mechanism

---

## 8. Special Sessions

### 8.1 Pre-Opening (08:00–09:00) [REF:#1]
- Order acceptance period — no matching
- All order types accepted
- Orders accumulate for opening Itayose at 09:00

### 8.2 Morning Session (09:00–11:30) [REF:#1]
- Opening: Itayose at 09:00
- 09:00–11:30: Zaraba (continuous trading)
- Closing: Itayose at 11:30

### 8.3 Lunch Break (11:30–12:30) [REF:#1]
- No trading
- Order acceptance resumes at 12:05

### 8.4 Afternoon Session (12:30–15:25) [REF:#1]
- Opening: Itayose at 12:30
- 12:30–15:25: Zaraba (continuous trading)

### 8.5 Closing Auction Session (CAS) — NEW [WEB:jpx.co.jp] [WEB:globaltrading.net]
- **15:25–15:30**: Pre-closing order acceptance (no trading)
  - Funari orders convert to market orders
  - On-close orders registered
- **15:30**: Closing Itayose — single price determination
- Introduced November 5, 2024 with arrowhead 4.0
- Rationale: Improve transparency and fairness of closing price discovery

### 8.6 ToSTNeT (Off-Auction Trading) [WEB:clearstream.com] [WEB:finextra.com]
- **Hours**: Up to 08:20–18:00 (outside regular auction hours)
- **ToSTNeT-1**: Single-issue transactions at closing price ± price limit
- **ToSTNeT-2**: Basket trading (portfolio-level)
- **ToSTNeT-3**: Own-share repurchase system [WEB:recruit-holdings.com]
- Used for: block trades, basket rebalancing, share buybacks
- Not anonymous — requires pre-arrangement between parties

### 8.7 Dark Pool Activity [WEB:jpx.co.jp/dark-pools]
- Japan has growing dark pool (PTS: Proprietary Trading System) activity
- JPX publishes monthly dark pool trading value data
- As of 2025: PTS/dark pool share growing but TSE lit market remains dominant

---

## 9. LP / Market Maker Obligations

### 9.1 ETF Market Making Incentive Scheme [WEB:jpx.co.jp/etf-mm]

**Structure**: [WEB:jpx.co.jp/etf-mm]
- TSE designates market makers for ETF issues based on applications
- Incentive-based program (not mandatory for all participants)
- Introduced: July 2, 2018

**Obligations**: [WEB:jpx.co.jp/etf-mm]
- Quote in at least 5 ETF issues
- Maintain quotes for ≥ 80% of continuous auction time
- Version 2.0 (2026): Display continuous quotes of ~¥100 million
- Exempt during trading halts or special quote periods

**Incentives**: [WEB:jpx.co.jp/etf-mm]
- Fee rebates / reduced trading fees
- Quarterly performance evaluation
- Tiered incentive structure based on quoting quality

### 9.2 Equity Market Makers [REF:#1]
- TSE does **not** have a mandatory market maker program for general equities
- No DMM-style exclusive assignment (unlike NYSE)
- No competitive MM quoting obligations (unlike NASDAQ)
- Liquidity in equities relies entirely on natural order flow and institutional participants
- Rationale: Japanese market tradition of order-driven purity; ETF MM scheme added only due to specific ETF liquidity concerns

### 9.3 Comparison with Batch 1 Exchanges
- **vs. KRX**: KRX has both LP program (ETF/ELW) AND MM program (low-liquidity stocks); TSE only has ETF MM
- **vs. NYSE**: NYSE has exclusive DMM + SLP; TSE has no equivalent
- **vs. NASDAQ**: NASDAQ has competitive MMs; TSE has no general equity MMs

---

## 10. Source Bibliography

### Reference Sources (Priority 1 — README_LINKS.md)

[REF:#1] JPX, "Overview of Domestic Stock Trading Rules", https://www.jpx.co.jp/english/equities/trading/domestic/index.html

[REF:#2] JPX, "Transaction Methods (Itayose & Zaraba)", https://www.jpx.co.jp/english/equities/trading/domestic/04.html

[REF:#3] JPX, "Equity Trading Guide 2024 (PDF)", https://www.jpx.co.jp/english/equities/trading/domestic/tvdivq000000tpfi-att/eg.pdf

[REF:#4] JPX, "Daily Price Limits", https://www.jpx.co.jp/english/equities/trading/domestic/06.html

[REF:#5] JPX, "Derivatives Trading Methods", https://www.jpx.co.jp/english/derivatives/rules/trading-methods/index.html

[REF:#6] JPX, "Derivatives Trading Methods Detail (PDF)", https://www.jpx.co.jp/english/derivatives/rules/trading-methods/tvdivq0000004h12-att/tvdivq000000ueul.pdf

[REF:#7] JPX, "Other Derivatives Trading Rules", https://www.jpx.co.jp/english/derivatives/rules/others/01.html

[REF:#8] JPX, "Arrowhead System Overview", https://www.jpx.co.jp/english/systems/equities-trading/01.html

[REF:#9] JPX, "Equities Trading Services", https://www.jpx.co.jp/english/systems/equities-trading/index.html

[REF:#10] JPX, "Learning Resources", https://www.jpx.co.jp/english/corporate/learning/resources/index.html

### Web Sources (Priority 3 — Gap Fill)

[WEB:fujitsu.com] Fujitsu, "arrowhead4.0 press release", https://www.fujitsu.com/global/about/resources/news/press-releases/2024/1105-01.html, Accessed 2026-03-27

[WEB:wikipedia] Tokyo Stock Exchange — Wikipedia, https://en.wikipedia.org/wiki/Tokyo_Stock_Exchange, Accessed 2026-03-27

[WEB:jpx.co.jp] Japan Exchange Group main, https://www.jpx.co.jp/english/, Accessed 2026-03-27

[WEB:jpx.co.jp/trading-overview] "Trading Overview in Year 2025", https://www.jpx.co.jp/english/corporate/news/news-releases/0063/20251230-01.html, Accessed 2026-03-27

[WEB:jpx.co.jp/etf-mm] "ETF Market Making Incentive Scheme", https://www.jpx.co.jp/english/equities/products/etfs/market-making/, Accessed 2026-03-27

[WEB:jpx.co.jp/tick-size] "Tick Size", https://www.jpx.co.jp/english/equities/trading/domestic/07.html, Accessed 2026-03-27

[WEB:jpx.co.jp/unit] "Standardization of Trading Unit", https://www.jpx.co.jp/english/equities/improvements/unit/index.html, Accessed 2026-03-27

[WEB:jpx.co.jp/price-limits] "Daily Price Limits", https://www.jpx.co.jp/english/equities/trading/domestic/06.html, Accessed 2026-03-27

[WEB:jpx.co.jp/closing-auction] "Extension of Trading Hours and CAS", https://www.jpx.co.jp/english/news/1030/20230920-01.html, Accessed 2026-03-27

[WEB:globaltrading.net] "TSE updates trading system as closing auction demand soars", https://www.globaltrading.net/tse-updates-trading-system-as-closing-auction-demand-soars/, Accessed 2026-03-27

[WEB:medium.com/tokyo-fintech] "TSE extends trading hours by 30 minutes", https://medium.com/tokyo-fintech/tse-extends-trading-hours-by-30-minutes-44b84fe12a36, Accessed 2026-03-27

[WEB:ppro8wiki] "Tokyo Stock Exchange — Order Types", https://www.ppro8wiki.com/doku.php?id=tokyo_stock_exchange, Accessed 2026-03-27

[WEB:statista] "Japan: number of listed companies by market division 2025", https://www.statista.com/statistics/1336987/japan-number-listed-companies-tse-by-market-division/, Accessed 2026-03-27

[WEB:market-clock.com] "Tokyo Stock Exchange — Market Clock", https://www.market-clock.com/markets/jpx/tse/equities/, Accessed 2026-03-27

[WEB:nber.org] "Market Structure and Liquidity on the TSE", https://www.nber.org/system/files/chapters/c8108/c8108.pdf, Accessed 2026-03-27

---

*Report version: 1.0 | Batch: 2 | Created: 2026-03-27 | Language: English*
