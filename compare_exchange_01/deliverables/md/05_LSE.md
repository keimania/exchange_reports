# LSE (London Stock Exchange) — Exchange Report

---

## 1. Exchange Overview

**Full Legal Name**: London Stock Exchange plc
**Country**: United Kingdom
**Founding Year**: 1801 (formally); trading since 1698 at Jonathan's Coffee House [WEB:wikipedia]
**Parent Group**: London Stock Exchange Group (LSEG) [WEB:wikipedia]

**Market Model**: Three-tier system — order-driven (SETS), hybrid (SETSqx), quote-driven (SEAQ) [REF:#3] [REF:#4]

**Asset Classes Traded**: [WEB:wikipedia]
- Equities (Main Market, AIM)
- ETFs, ETPs, Bonds, GDRs
- Derivatives (via LSEG subsidiary venues)
- International Order Book (IOB — depositary receipts)

**Regular Trading Hours (GMT/BST)**: [WEB:tradinghours.com]
- Pre-trading: 05:05–07:50
- Opening auction: 07:50–08:00 (uncrossing at 08:00)
- Continuous trading: 08:00–16:30
- Closing auction: 16:30–16:35
- Post-trading: 16:40–17:15

**Key Statistics**: [WEB:statista] [WEB:wikipedia]
- Listed companies: ~1,900+ from 60+ countries
- Market capitalization: ~£4.5 trillion / ~$5.9 trillion (April 2025)
- FTSE 100 surpassed 10,000 points for first time (early 2026) [WEB:statista]

---

## 2. Institutional Philosophy

**Primary Market Model**: Segmented three-tier system based on security liquidity [REF:#3] [REF:#4]

**SETS (Stock Exchange Electronic Trading Service)**: [REF:#1] [WEB:stockexchangesecrets.com]
- Pure electronic order book for most liquid securities
- FTSE 100, FTSE 250, FTSE SmallCap, most liquid AIM stocks, ETFs
- Continuous order-driven trading + opening/closing auctions
- No mandatory market makers

**SETSqx (SETS quotes and crosses)**: [REF:#3] [WEB:aim-watch.com]
- Hybrid system for less liquid securities
- Combines periodic auctions (4x daily) + continuous market maker quotes
- Market makers provide continuous liquidity between auctions
- Named Orders: non-anonymous limit orders unique to this platform [REF:#3]

**SEAQ (Stock Exchange Automated Quotation)**: [REF:#3] [WEB:aim-watch.com]
- Pure quote-driven system for least liquid securities
- Minimum 2 market makers per security required [WEB:wikipedia-seaq]
- No electronic order book — trading via market maker quotes only
- Similar to original NASDAQ model (pre-electronic order book)

**Evolution**: Coffee house trading (1698) → physical floor → SEAQ electronic quotes (1986 Big Bang) → SETS order book (1997) → SETSqx hybrid (2007) → Millennium Exchange platform (2011) [WEB:wikipedia]

---

## 3. Order Types — Basic

### 3.1 Limit Order [REF:#1] [REF:#2]
- Specifies maximum buy / minimum sell price
- Rests on order book if not immediately matched
- Available on SETS and SETSqx (during auctions)
- Time-in-force: Day (default), GTC, IOC, FOK, GTD

### 3.2 Market Order [REF:#1]
- Executes at best available price
- Available on SETS during continuous trading
- Converts to limit if partially filled (remainder at last execution price)

### 3.3 At Best Order [REF:#1] [WEB:stockexchangesecrets.com]
- Similar to market order but fills at a single price level only
- If not fully filled at best price, remainder cancelled
- Unique LSE variant providing single-price execution guarantee

---

## 4. Order Types — Advanced

### 4.1 Iceberg (Random Peak Size) Order [REF:#1] [REF:#2]
- Displays random portion of total quantity
- Peak size randomized between specified minimum and maximum [WEB:lse-hidden-orders]
- Reserve replenishes automatically
- Available on SETS

### 4.2 Hidden Order [REF:#1] [WEB:lse-hidden-orders]
- Fully non-displayed order
- MiFID II requirement: Must exceed Large-in-Scale (LIS) threshold for MiFID securities [WEB:lse-hidden-orders]
- Lower priority than displayed orders at same price

### 4.3 Mid-Price Pegged Order [REF:#1] [REF:#2]
- Pegged to midpoint of best bid and offer
- Non-displayed
- Optional: user-defined minimum execution size per trade
- Optional: automatic parking when midpoint moves outside specified range
- IOC/FOK variants not subject to LIS validation [WEB:lse-hidden-orders]

### 4.4 Stop Order [REF:#1] [REF:#2]
- Triggered when stop price reached; becomes market order
- Available on SETS

### 4.5 Stop-Limit Order [REF:#1] [REF:#2]
- Triggered when stop price reached; becomes limit order at specified price

### 4.6 Time-in-Force Options [REF:#1]
- **Day**: Expires at session end
- **GTC**: Good until cancelled (persistent across days)
- **IOC**: Immediate or cancel
- **FOK**: Fill or kill
- **GTD**: Good till specified date
- Note: GTC and GTD available — unlike KRX and TSE (day-only)

---

## 5. Order Types — Exchange-Specific

### 5.1 Named Order (SETSqx) [REF:#3] [WEB:aim-watch.com]
- **LSE-unique**: Non-anonymous limit order where counterparty identity is visible
- Available only on SETSqx platform
- Market makers and brokers can see who placed the order
- Rationale: In less liquid markets, knowing counterparty identity helps assess order quality and encourages bilateral negotiation
- Contrasts with all other major exchanges where order books are anonymous

### 5.2 At Best Order [REF:#1]
- LSE-specific variant: Fills at single best price only; cancels unfilled remainder
- Differs from standard market orders that sweep multiple levels
- Provides protection against adverse multi-level execution

### 5.3 Executable Quote (SETSqx / SEAQ) [REF:#3]
- Market maker firm quote — executable on demand
- Two-sided (bid/offer) with specified size
- Provides continuous liquidity on quote-driven segments

### 5.4 Random Peak Size Iceberg [REF:#1]
- LSE enhancement: Peak display size randomized between min/max bounds
- Reduces pattern detection by algorithmic traders
- Standard icebergs on other exchanges use fixed display quantity

---

## 6. Matching Engine & Price Discovery

### Trading System: Millennium Exchange [WEB:wikipedia-millennium] [WEB:lseg.com]
- **Launch**: 2011 (replaced TradElect) [WEB:wikipedia-millennium]
- **Developer**: MillenniumIT (LSEG subsidiary, Sri Lanka) [WEB:wikipedia-millennium]
- **Architecture**: Multi-market, multi-asset platform [WEB:lseg.com]
- **Latency**: Average 126 μs (native API); 196 μs (FIX 5.0) [WEB:wikipedia-millennium]
- **Market Data**: Group Ticker Plant (GTP) — multicast UDP delivery [WEB:lse-gtp]
- **Used by**: LSE, Borsa Italiana, Johannesburg Stock Exchange, and others [WEB:wikipedia-millennium]

### Matching Algorithm (SETS): Price-Time Priority [REF:#1]
1. Price priority: Best price first
2. Time priority: Among same-price orders, earliest first
3. Hidden orders: Lower priority than displayed at same price

### Opening Auction (SETS) [WEB:tradinghours.com]
- **07:50–08:00**: Order accumulation (no matching)
- **08:00**: Uncrossing — single price maximizing volume
- Orders from pre-trading session participate

### Closing Auction (SETS) [WEB:tradinghours.com]
- **16:30**: Continuous trading ends; closing auction begins
- **16:35**: Uncrossing — closing price determined
- Intraday auction (SETS): ~12:00–12:02 (optional midday price discovery)

### SETSqx Auctions [REF:#3] [WEB:aim-watch.com]
- **4 scheduled auctions per day**: ~08:00, 11:00, 14:30, 16:35
- Between auctions: market maker quotes provide liquidity
- At auction: order book crosses with accumulated orders

### Tick Size Regime [WEB:mifid-tick-size]
- MiFID II harmonized tick size table (RTS 11)
- Tick size depends on: price level AND average daily number of transactions (liquidity band)
- Applied uniformly across all EU/UK venues for same security
- Typically: £0.01 for liquid stocks under £10; wider for less liquid

### Lot Size
- Standard: 1 share (no minimum lot requirement for most securities)
- Market makers may set minimum dealing sizes

---

## 7. Safeguard Mechanisms

### 7.1 Dynamic Circuit Breaker [WEB:fca.org.uk] [WEB:lse-orderly-markets]
- **Trigger**: Potential trade price > **3%** from last executed order book price (FTSE 100)
- **Action**: 5-minute call auction (no continuous trading)
- Calibrated per instrument based on liquidity
- Wider thresholds for less liquid securities

### 7.2 Static Circuit Breaker [WEB:fca.org.uk] [WEB:lse-orderly-markets]
- **Trigger**: Potential trade price > **8%** from last auction price (FTSE 100)
- **Action**: 5-minute call auction
- Static threshold resets after each auction completion

### 7.3 ETP Price Monitoring [WEB:lse-etp-monitoring]
- Additional monitoring for ETFs/ETPs
- Separate dynamic/static bands calibrated for ETP characteristics

### 7.4 No Market-Wide Circuit Breaker
- UK does not have a US-style market-wide halt (S&P 500 7%/13%/20%)
- Individual security circuit breakers only
- FCA oversees market integrity; can impose trading suspensions

### 7.5 MiFID II Pre-Trade Controls
- Maximum order size/value limits
- Price collar validation
- Kill switch functionality required for algorithmic traders

---

## 8. Special Sessions

### 8.1 Pre-Trading (05:05–07:50) [WEB:tradinghours.com]
- Order entry period — no matching
- Trade reporting for off-book transactions

### 8.2 Opening Auction (07:50–08:00) [WEB:tradinghours.com]
- Order accumulation → uncrossing at 08:00
- SETS securities only

### 8.3 Continuous Trading (08:00–16:30) [REF:#1]
- SETS: Full electronic order book matching
- SETSqx: Market maker quotes + order book
- SEAQ: Market maker quotes only

### 8.4 Intraday Auction (~12:00–12:02) [WEB:tradinghours.com]
- Brief midday auction on SETS
- Helps price discovery during lunch period

### 8.5 Closing Auction (16:30–16:35) [WEB:tradinghours.com]
- SETS closing uncrossing at 16:35
- SETSqx closing auction at 16:35

### 8.6 Post-Trading (16:40–17:15) [WEB:tradinghours.com]
- Trade reporting only — no new matching

### 8.7 Turquoise (Pan-European MTF) [WEB:lseg.com]
- LSEG-owned Multilateral Trading Facility
- **Turquoise Lit**: Displayed order book with price-time priority
- **Turquoise Plato (Dark)**: Non-displayed midpoint matching
- **Turquoise Plato Block Discovery**: Block-size indications of interest
- MiFID II compliant; competes with national exchanges across EU/UK

---

## 9. LP / Market Maker Obligations

### 9.1 SETS Market Makers (Voluntary) [REF:#1]
- No mandatory market maker program for SETS securities
- Liquidity from natural order flow (similar to TSE)
- Optional registered market makers may participate for fee advantages

### 9.2 SETSqx Market Makers (Obligatory for Service) [REF:#3] [WEB:aim-watch.com]
- Market makers provide continuous two-sided quotes between auctions
- Must deal at displayed price and size when hit [WEB:aim-watch.com]
- Multiple MMs per security (competitive model)
- Named Orders allow identity-visible trading

### 9.3 SEAQ Market Makers (Core to Service) [REF:#3] [WEB:wikipedia-seaq]
- **Minimum 2 market makers per security** [WEB:wikipedia-seaq]
- Continuous two-sided firm quotes (bid/offer with size)
- Must honor displayed quotes
- Pure quote-driven — all liquidity from MMs
- Spread represents MM profit margin

### 9.4 Comparison with Batch 1/2 Exchanges
- LSE's three-tier approach is unique: different MM obligations by liquidity segment
- **vs. NYSE**: NYSE has single hybrid model; LSE segments by liquidity
- **vs. NASDAQ**: NASDAQ competitive MMs everywhere; LSE only on SETSqx/SEAQ
- **vs. TSE**: Both lack general equity MMs on main order book
- **vs. KRX**: KRX has LP/MM programs for all; LSE only for less-liquid segments

---

## 10. Source Bibliography

### Reference Sources (Priority 1 — README_LINKS.md)

[REF:#1] LSE, "MIT201 — Guide to the Trading System (Draft 15.7, PDF)", https://docs.londonstockexchange.com/sites/default/files/documents/draft-mit201-guide-to-the-trading-system-15.7.pdf

[REF:#2] LSE, "MIT201 — Guide to the Trading System (v14.9, PDF)", https://docs.londonstockexchange.com/sites/default/files/documents/draftguidetothetradingsystem2.pdf

[REF:#3] LSE, "Shares Trading — SETSqx and SEAQ", https://www.londonstockexchange.com/equities-trading/asset-classes/shares-trading/setsqx-and-seaq

[REF:#4] LSE, "SETSqx Auction Improvements Factsheet (PDF)", https://docs.londonstockexchange.com/sites/default/files/documents/Further%20improvements%20to%20auctions%20on%20the%20SETSqx%20Trading%20Service.pdf

[REF:#5] LSE, "Official Documentation Portal", https://docs.londonstockexchange.com/

[REF:#6] StockExchangeSecrets, "SETS Explained", https://www.stockexchangesecrets.com/london-stock-exchange-SETS.html

[REF:#7] AIM-Watch, "SEAQ, SETS & SETSqx Explained", https://aim-watch.com/project/seaq-sets-setsqx/

### Web Sources (Priority 3 — Gap Fill / Supplementary)

[WEB:wikipedia] London Stock Exchange — Wikipedia, https://en.wikipedia.org/wiki/London_Stock_Exchange, Accessed 2026-03-27

[WEB:wikipedia-millennium] Millennium Exchange — Wikipedia, https://en.wikipedia.org/wiki/Millennium_Exchange, Accessed 2026-03-27

[WEB:wikipedia-seaq] SEAQ — Wikipedia, https://en.wikipedia.org/wiki/SEAQ, Accessed 2026-03-27

[WEB:lseg.com] LSEG Markets Technology, https://www.lseg.com/en/capital-markets/market-infrastructure-business-development, Accessed 2026-03-27

[WEB:statista] "Market cap of firms on the LSE 2025", https://www.statista.com/statistics/324578/market-value-of-companies-on-the-london-stock-exchange/, Accessed 2026-03-27

[WEB:tradinghours.com] "LSE Market Hours", https://www.tradinghours.com/markets/lse, Accessed 2026-03-27

[WEB:fca.org.uk] FCA, "Analysis of Circuit Breakers in UK Equity Markets", https://www.fca.org.uk/publications/research/analysis-circuit-breakers-uk-equity-markets, Accessed 2026-03-27

[WEB:lse-hidden-orders] LSE, "SETS Hidden Order Enhancements", https://docs.londonstockexchange.com/sites/default/files/documents/LSEG_CM_SETS_HIDDEN_ORDERS_BROCHURE_CMYK_LR.pdf, Accessed 2026-03-27

[WEB:lse-orderly-markets] LSE, "Maintaining Orderly Markets", https://docs.londonstockexchange.com/sites/default/files/documents/maintaining-orderly-markets.pdf, Accessed 2026-03-27

[WEB:lse-etp-monitoring] LSE, "ETP Price Monitoring Mechanisms", https://docs.londonstockexchange.com/sites/default/files/documents/LSE_ETP_Price_Monitoring_Mechanisms_factsheet.pdf, Accessed 2026-03-27

[WEB:aim-watch.com] "SEAQ, SETS & SETSqx Explained", https://aim-watch.com/project/seaq-sets-setsqx/, Accessed 2026-03-27

[WEB:stockexchangesecrets.com] "London Stock Exchange SETS", https://www.stockexchangesecrets.com/london-stock-exchange-SETS.html, Accessed 2026-03-27

[WEB:mifid-tick-size] "MiFID II tick-size regime", https://www.emissions-euets.com/tick-size-regime, Accessed 2026-03-27

---

*Report version: 1.0 | Batch: 2 | Created: 2026-03-27 | Language: English*
