# Eurex Exchange — Exchange Report

---

## 1. Exchange Overview

**Full Legal Name**: Eurex Frankfurt AG / Eurex Zürich AG
**Country**: Germany / Switzerland
**Founding Year**: 1998 (merger of DTB and SOFFEX) [WEB:wikipedia]
**Parent Group**: Deutsche Börse AG [WEB:wikipedia]

**Market Model**: Hybrid auction + continuous trading; primarily derivatives-focused with shared T7 platform (also powers Xetra cash) [REF:#4]

**Asset Classes Traded**: [WEB:eurex.com/markets]
- Equity index derivatives (EURO STOXX 50, DAX, etc.)
- Single stock options & futures
- Interest rate derivatives (Bund, Bobl, Schatz futures)
- Dividend, volatility, ETF/ETC, FX, credit, commodity, cryptocurrency derivatives
- Eurex Repo (fixed income repo market)

**Regular Trading Hours (CET)**: [WEB:eurex.com/trading-hours]
- System available: 01:00 CET
- Regular trading: 08:00–22:00 CET (varies by product)
- Pre-trading, opening auction, continuous, closing auction, post-trading phases per product

**Key Statistics**: [WEB:wikipedia] [WEB:eurex.com]
- One of the world's largest derivatives exchanges
- Products: 2,000+ listed derivative contracts
- ~1.9 billion contracts traded annually (peak years)

**Recent Major Changes**: [WEB:eurex.com]
- 2025.03: T7 Release 13.1 — latency improvements, Colo 2.0 hardware upgrade
- 2025.05–07: New EURO STOXX 50 options liquidity framework
- 2025.11: T7 Release 14.0 planned for Xetra/Börse Frankfurt

---

## 2. Institutional Philosophy

**Primary Market Model**: Electronic order-driven with strong market maker infrastructure [REF:#1] [WEB:eurex.com]
- Derivatives-first exchange — designed around options/futures microstructure
- Shared T7 platform with Xetra (cash equities) — unique dual-use architecture [REF:#4]
- Heavy emphasis on pre-trade risk controls and market integrity [REF:#7]

**Design Rationale**: [WEB:wikipedia]
- Born electronic (1998) — never had physical trading floor
- Consolidated European derivatives liquidity (replaced floor-based DTB/SOFFEX)
- Market maker programs critical for options markets (quotes required across strikes/maturities)
- T7 designed for ultra-low latency and high throughput

**Role of Intermediaries**: [WEB:eurex.com/mm]
- **Regular Market Makers (RMM)**: Standard quoting obligations
- **Permanent Market Makers (PMM)**: Continuous quoting, stricter obligations, higher incentives
- **Advanced Market Makers (AMM)**: Most demanding obligations, best incentives
- **Designated Market Makers**: Product-specific incentive schemes with fee rebates [WEB:eurex.com/mm]
- Market makers essential for options liquidity (unlike equities where natural flow dominates)

**Evolution**: DTB electronic (1990) + SOFFEX → Eurex (1998) → T7 migration (2012) → T7 Release 13 (2024) → R14 planned (2025) [WEB:wikipedia]

---

## 3. Order Types — Basic

### 3.1 Limit Order [REF:#1]
- Specified price limit; execution at limit or better
- Time-in-force: GFD (day), GTC (up to 1 year), GTD (specified date), IOC
- Available in all sessions

### 3.2 Market Order [REF:#1]
- No price specified; matches at best available contra-side price
- Not visible in order book
- Not available for strategy/calendar spread instruments
- Converts to limit at last execution price if partially filled

### 3.3 Market-to-Limit Order [REF:#1]
- Executes as market order; remainder converts to limit at last execution price
- Prevents adverse multi-level sweep

---

## 4. Order Types — Advanced

### 4.1 Stop Order (Stop-Loss Market) [REF:#1]
- Inactive until stop price triggered → becomes market order
- No execution guarantee at stop price

### 4.2 Stop-Limit Order [REF:#1]
- Inactive until stop price triggered → becomes limit order at specified limit
- Two prices: stop (trigger) and limit (execution)

### 4.3 One-Cancels-the-Other (OCO) [REF:#1]
- Combines limit order + stop market order under single order ID
- Limit side active immediately; stop side inactive until triggered
- Execution of either cancels the other
- Unique implementation with single-ID management

### 4.4 Iceberg Order [REF:#1]
- Partial display; hidden reserve replenishes on execution
- Peak quantity visible; total quantity hidden

### 4.5 Book-or-Cancel (BOC) [REF:#1]
- **Rejected if immediately executable** — accepted only if would rest on book
- Opposite of IOC — ensures order adds liquidity, never removes
- Similar to NYSE ALO / NASDAQ Post-Only

### 4.6 Closing Auction Order [REF:#1]
- Limit or market variant
- Active only during Closing Auction and Closing Auction Freeze states

### 4.7 Opening Auction Order [REF:#1]
- Limit or market variant
- Active only during Opening Auction and Opening Auction Freeze states

### 4.8 Auction-Only Order [REF:#1]
- Active across all auction states (opening, intraday, closing)
- Not active during continuous trading

### 4.9 Time-in-Force Options [REF:#1]
- **GFD**: Good for day (default)
- **GTC**: Good till cancelled (up to 1 year auto-cancel)
- **GTD**: Good till specified date (up to 1 year)
- **IOC**: Immediate or cancel

---

## 5. Order Types — Exchange-Specific

### 5.1 OCO (One-Cancels-the-Other) [REF:#1]
- Eurex implementation is distinctive: single order ID manages both limit and stop legs
- Most exchanges implement OCO as two separate linked orders
- Rationale: Simplifies order management for derivatives traders hedging directional risk

### 5.2 Book-or-Cancel (BOC) [REF:#1]
- Post-only variant specific to Eurex T7
- Ensures passive execution only — important for market maker strategies seeking spread capture

### 5.3 Strategy Orders [WEB:eurex.com]
- Multi-leg orders for options strategies (spreads, straddles, strangles, etc.)
- Only limit orders supported for strategy instruments
- T7 handles leg allocation and execution atomically

### 5.4 Volume Discovery Orders [WEB:eurex.com]
- Mechanism for block-size price discovery in derivatives
- Allows large orders to find counterparty interest without market impact
- Part of Eurex's off-book trading capabilities

### 5.5 Auction-Specific Order Variants [REF:#1]
- Opening/Closing/Auction-Only — three distinct session-targeted types
- More granular than most exchanges (which typically offer only MOO/MOC)
- Rationale: Derivatives products have complex auction mechanics with volatility interruptions

---

## 6. Matching Engine & Price Discovery

### Trading System: T7 [REF:#4] [REF:#5] [WEB:eurex.com/t7]
- **Platform**: Shared with Xetra (cash), EEX (energy), Nodal Exchange [WEB:databento.com]
- **Current version**: Release 13.1 (March 2025); R14.0 planned Nov 2025
- **Latency**: Minimum reaction time ~2,787 ns (nanosecond level); top 10 participants <2,830 ns [WEB:eurex.com/insights]
- **EOBI market data**: Median 1.5 μs faster than ETI response [WEB:eurex.com/insights]
- **Throughput**: ~8,000 kHz at core; ~500 kHz at participant level [WEB:eurex.com/insights]
- **Interface**: ETI (Enhanced Trading Interface) — session-based TCP/IP [REF:#5]
- **Infrastructure**: Colo 2.0 — upgraded in 2025 [WEB:eurex.com/insights]
- **Timestamping**: Nanosecond-precision for regulatory and analysis purposes [WEB:databento.com]

### Matching Algorithm: Price-Time Priority [REF:#1]
1. Best price first
2. Same price: earliest order first
3. Market orders: highest priority (treated as accepting any price)
4. Pro-rata matching available for some products (e.g., certain options)

### Auction Phases [WEB:eurex.com/trading-phases]
- **Pre-Trading**: System open, order entry allowed, no matching
- **Opening Auction**: Order accumulation → freeze → uncrossing at equilibrium price
- **Continuous Trading**: Price-time priority matching
- **Closing Auction**: Order accumulation → freeze → uncrossing
- **Post-Trading**: Trade confirmation, no new orders

### Volatility Interruptions [WEB:eurex.com/vi]
- Triggered when next execution price deviates beyond short/long time-window bands
- Execution prevented → market switches to **volatility auction** (intraday auction)
- Participants can submit/cancel orders; no matching during auction
- No minimum duration for dynamic volatility interruptions [WEB:eurex.com/vi]
- Separate from opening/closing auctions — specific to intraday continuous trading

### Tick Size
- Product-specific; set per contract specification [REF:#2]
- Eurex/Xetra: Configurable by instrument, typically aligned with MiFID II RTS 11 for cash equities

### Lot Size
- Standard: 1 contract (derivatives)
- Scaled instruments: Users can create intraday instruments with scaled lot sizes [WEB:eurex.com]

---

## 7. Safeguard Mechanisms

### 7.1 Volatility Interruptions [WEB:eurex.com/vi] [WEB:eurex.com/safeguards]
- **Dynamic**: Short-window price deviation triggers intraday volatility auction
- **Extended**: Long-window deviation triggers extended auction
- Product-specific parameters (adjustable by Eurex per market conditions)
- Recent: Parameters adjusted for products with Asian/US trading hours [WEB:eurex.com/vi-circular]

### 7.2 Pre-Trade Risk Controls [REF:#5] [REF:#7] [WEB:eurex.com/safeguards]
- **Maximum order quantity**: Per-product limits
- **Maximum order value**: Monetary limits per order
- **Price reasonability checks**: Orders outside bands rejected
- **Delta-equivalent controls**: For options — position limits in delta-equivalent futures units
- **Throttling**: Message rate limits per session
- **Kill Switch**: Bulk cancellation capability

### 7.3 No Market-Wide Circuit Breaker (Eurex-specific)
- Eurex uses per-product volatility interruptions rather than market-wide halts
- Different from US-style S&P 500-based MWCB
- Consistent with European regulatory framework

### 7.4 Stressed Market Conditions
- Eurex Market Supervision can adjust volatility interruption parameters
- Emergency procedures for system-wide issues

---

## 8. Special Sessions

### 8.1 Pre-Trading (01:00 CET) [WEB:eurex.com/trading-hours]
- System opens; order entry/modification allowed
- No matching

### 8.2 Opening Auction [WEB:eurex.com/trading-phases]
- Product-specific start times (typically ~08:00–08:50 CET)
- Accumulation → Freeze → Uncrossing
- Opening/Auction-Only orders active

### 8.3 Continuous Trading [REF:#1]
- Core trading session; price-time priority matching
- All order types available (except auction-only)
- Volatility interruptions may pause matching

### 8.4 Closing Auction [WEB:eurex.com/trading-phases]
- Product-specific times (varies widely)
- Accumulation → Freeze → Uncrossing
- Closing Auction orders active

### 8.5 Post-Trading [WEB:eurex.com/trading-hours]
- Trade confirmation and reporting
- No new order entry

### 8.6 Off-Book Trading (T7 Entry Service) [WEB:eurex.com]
- **Block Trades**: Pre-negotiated, reported to exchange
- **EFP/EFS/EFR**: Exchange for Physical/Swap/Related position
- **Volume Discovery**: Mechanism for large order price discovery
- **Eurex EnLight**: Request-for-quote platform for off-book negotiation

### 8.7 Extended Trading Hours [WEB:eurex.com/thx]
- Select products: Trading until 22:00 CET
- Asian hours access for Nikkei, KOSPI products
- US hours overlap for interest rate products

---

## 9. LP / Market Maker Obligations

### 9.1 Market Making Models [WEB:eurex.com/mm]

**Regular Market Making (RMM)**:
- Standard quoting obligations (response to quote requests)
- Basic fee rebates

**Permanent Market Making (PMM)**: [WEB:eurex.com/mm]
- Continuous quoting required (not just quote response)
- Stricter spread/size obligations
- Higher fee rebates
- Must quote all maturities and wide delta range (for options) [WEB:eurex.com/oesx-lp]

**Advanced Market Making (AMM)**:
- Most demanding obligations
- Best incentive structure
- Reserved for highest-commitment participants

**Designated Market Making**: [WEB:eurex.com/dmm]
- Product-specific schemes
- 50% transaction fee reimbursement upon fulfillment [WEB:eurex.com/dmm]
- Time-limited programs for specific products

### 9.2 Quoting Requirements [WEB:eurex.com/mm]
- Minimum quote sizes set per product
- Spread requirements calibrated to market conditions
- 90% coverage requirement for EURO STOXX 50 options (new 2025) [WEB:eurex.com/oesx-lp]
- Monthly average fulfillment assessment
- MiFID II regulatory market-making compliance

### 9.3 Comparison
- **vs. NYSE DMM**: Eurex has multiple MM tiers (RMM/PMM/AMM) vs. NYSE's single exclusive DMM
- **vs. NASDAQ**: Both competitive models; Eurex more structured with explicit tiers
- **vs. KRX/TSE/HKEX**: Those exchanges have limited/no equity MMs; Eurex's MM programs are central to derivatives liquidity

---

## 10. Source Bibliography

### Reference Sources (Priority 1 — README_LINKS.md)

[REF:#1] Eurex, "Order Types", https://www.eurex.com/ex-en/trade/order-book-trading/order-types
[REF:#2] Eurex, "Exchange Rules Circular (2024)", https://www.eurex.com/ex-en/find/circulars/circular-3763988
[REF:#3] Eurex, "Exchange Rules Circular (2025)", https://www.eurex.com/ex-en/find/circulars/circular-4176840
[REF:#4] Eurex, "T7 Release 13 Overview", https://www.eurex.com/ex-en/support/initiatives/t7-release13
[REF:#5] Eurex, "ETI Manual (PDF)", https://www.eurexchange.com/resource/blob/297838/54cd4e591b23d7e3d60ef8e707c21a56/data/eurex_eti_manual_V31.pdf
[REF:#6] Eurex, "Eurex Trader & Admin GUI Manual (PDF)", https://www.eurexchange.com/resource/blob/279888/c6872432b05d4085a6642319104cc320/data/Eurex-Trader-and-Admin-GUI-User-Manual.pdf
[REF:#7] Eurex, "T7 R13.1 Participant Maintenance Manual (PDF)", https://www.eurex.com/resource/blob/4332334/61e2e29f08a63ff88d20ee30c4dc2049/data/T7_R.13.1_Derivatives_Market_-_Participant_and_User_Maintenance_Manual_Version_1.pdf

### Web Sources (Priority 3 — Gap Fill)

[WEB:wikipedia] Eurex — Wikipedia, https://en.wikipedia.org/wiki/Eurex, Accessed 2026-03-27
[WEB:eurex.com] Eurex main, https://www.eurex.com/ex-en/, Accessed 2026-03-27
[WEB:eurex.com/mm] "Market-Making and Liquidity Provisioning", https://www.eurex.com/ex-en/trade/market-making-and-liquidity-provisioning, Accessed 2026-03-27
[WEB:eurex.com/trading-hours] "Trading Hours", https://www.eurex.com/ex-en/trade/trading-hours, Accessed 2026-03-27
[WEB:eurex.com/trading-phases] "Trading Phases", https://www.eurex.com/ex-en/trade/trading-hours/trading-phases, Accessed 2026-03-27
[WEB:eurex.com/vi] "Volatility Interruption Functionality", https://www.eurex.com/ex-en/support/emergencies-and-safeguards/volatility-interruption-functionality, Accessed 2026-03-27
[WEB:eurex.com/safeguards] "Trading Safeguards (Oct 2025 PDF)", https://www.eurex.com/resource/blob/2448162/28033c3a73ea19078860573d526f8f33/data/presentation-trading-safeguards.pdf, Accessed 2026-03-27
[WEB:eurex.com/insights] "Insights into Trading System Dynamics (Mar 2025 PDF)", https://www.eurex.com/resource/blob/48918/4f724c9415d2731cfb27295db6269c9c/data/presentation-insights-into-trading-system-dynamics.pdf, Accessed 2026-03-27
[WEB:eurex.com/oesx-lp] "New EURO STOXX 50 Options Liquidity Framework", https://www.eurex.com/ex-en/find/news-center/news/oesx-new-lp-scheme-4321212, Accessed 2026-03-27
[WEB:databento.com] "What is the T7 trading platform?", https://databento.com/microstructure/t7, Accessed 2026-03-27

---

*Report version: 1.0 | Batch: 3 | Created: 2026-03-27 | Language: English*
