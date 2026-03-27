# SGX (Singapore Exchange) — Exchange Report

---

## 1. Exchange Overview

**Full Legal Name**: Singapore Exchange Limited (SGX Group)
**Country**: Singapore
**Founding Year**: 1999 (merger of Stock Exchange of Singapore and SIMEX) [WEB:wikipedia]
**Parent Group**: SGX Group (self-listed: SGX: S68) [WEB:wikipedia]

**Market Model**: Order-driven (securities via SGX-ST); derivatives hub via Titan system [REF:#1] [REF:#2]

**Asset Classes Traded**: [WEB:wikipedia] [WEB:sgx.com]
- Securities (SGX-ST: equities, REITs, ETFs, fixed income)
- Derivatives (SGX-DT: equity index, FX, interest rate, commodity futures/options)
- OTC derivatives (via Titan OTC)

**Regular Trading Hours (SGT, UTC+8)**: [WEB:sgx-overview] [REF:#1]
- Pre-open: 08:30–09:00 (securities)
- Continuous trading: 09:00–17:00 (securities)
- Pre-close: 17:00–17:04/05
- Closing routine (TAC): 17:06–17:16
- Derivatives: extended hours (varies by product, including overnight sessions)

**Key Statistics**: [WEB:wikipedia] [WEB:ceicdata.com]
- Listed companies: ~700+ (SGX-ST)
- Market capitalization: ~US$824 billion (Dec 2025)
- Revenue split: Securities 75%, Derivatives 25% [WEB:wikipedia]
- Key position: Asia's derivatives hub; gateway for China/India/ASEAN risk management

**Recent Major Changes**: [WEB:sgx.com]
- 2025.12: Streamlined ETF Designated Market-Maker obligations [WEB:allenandgledhill.com]
- Circuit breaker scope expanded to broader securities

---

## 2. Institutional Philosophy

**Primary Market Model**: Electronic order-driven (securities) + derivatives-focused hub [REF:#1]
- Securities traded via QUEST electronic platform [WEB:sgx-overview]
- Derivatives on Titan system (ITCH/GLIMPSE for market data) [REF:#11] [REF:#12]
- Strong Asia-centric derivatives franchise (Nikkei 225, MSCI Asia indices, iron ore)

**Design Rationale**: [WEB:wikipedia]
- Small domestic equity market → strategic pivot to Asia's multi-asset derivatives hub
- Connect Asia's risk management needs with global capital
- Competitive positioning: 24-hour derivatives access via extended trading hours
- Dual-platform approach: QUEST (cash) + Titan (derivatives)

**Role of Intermediaries**: [REF:#2] [WEB:sgx.com/dmm]
- **Designated Market Makers (DMMs)**: For ETFs and selected securities
- **Derivatives Market Makers**: For futures/options products
- **No general equity MM program** — relies on natural order flow for common stocks

**Evolution**: SES + SIMEX → SGX (1999) → demutualized → SGX AsiaClear (OTC clearing) → Titan system → SGX Group restructuring [WEB:wikipedia]

---

## 3. Order Types — Basic

### 3.1 Limit Order [REF:#2] [REF:#4]
- Specifies price and quantity
- Rests on order book if not immediately matched
- Available in all sessions

### 3.2 Market Order (Fill and Kill / MKT) [REF:#4]
- No price specified
- Fills at best available price(s); **unfilled portion cancelled** (FAK-style)
- SGX market orders are effectively IOC — do NOT rest on book

### 3.3 Stop Order (STP — Fill and Kill) [REF:#4]
- Triggered at stop price → becomes market order (FAK-style)
- Unfilled remainder cancelled after trigger

### 3.4 Stop-Limit Order (STP Limit) [REF:#4]
- Triggered at stop price → becomes limit order

---

## 4. Order Types — Advanced

### 4.1 Time-in-Force Options [REF:#2]
- **Day (GFD)**: Default — expires at session end
- **GTC**: Good till cancelled
- **IOC**: Immediate or cancel
- **FOK**: Fill or kill

### 4.2 Pre-Open / Closing Orders [WEB:sgx-overview]
- Orders entered during pre-open: participate in opening auction
- Pre-close / TAC orders: participate in closing routine
- Opening: single-price algorithm at 09:00
- Closing: Trading-at-Close (TAC) session 17:06–17:16

### 4.3 Negotiated Large Trade (NLT) [WEB:sgx.com/nlt]
- Off-book facility for large trades
- Minimum volume thresholds per contract type [WEB:sgx.com/nlt]
- Notification and registration procedures required
- Price within daily price limits

---

## 5. Order Types — Exchange-Specific

### 5.1 Market Order as FAK [REF:#4]
- **SGX-unique implementation**: Market orders are Fill-and-Kill (unfilled cancelled)
- Most exchanges' market orders sweep full book then rest as limit; SGX cancels remainder
- Provides implicit protection against adverse execution

### 5.2 Trading-at-Close (TAC) Session [WEB:sgx-overview]
- **SGX-unique**: Extended closing session (17:06–17:16)
- Orders matched at closing price determined by closing routine
- Allows post-close execution at official closing price
- Longer than most exchanges' closing mechanisms

### 5.3 NLT (Negotiated Large Trade) [WEB:sgx.com/nlt]
- SGX's block trade facility for derivatives
- Pre-negotiated between parties; reported to exchange
- Minimum volume thresholds vary by product
- Similar to: KRX 대량매매, Eurex block trades

### 5.4 QUEST Order Types [WEB:sgx-overview]
- SGX's securities electronic trading platform
- Members access via OMS integration
- Support for standard limit, market (FAK), stop types

---

## 6. Matching Engine & Price Discovery

### Trading Systems [REF:#11] [REF:#12] [REF:#13]
- **QUEST**: Securities market electronic platform [WEB:sgx-overview]
- **Titan DT/DC**: Derivatives trading and clearing [REF:#11]
- **Titan OTC**: OTC derivatives [REF:#12]
- **Protocols**:
  - ITCH: Outbound market data feed (Titan) [REF:#11]
  - GLIMPSE: Point-to-point order book snapshot (Titan) [REF:#11]
  - FIX: Standard order entry (Titan OTC) [REF:#12]
  - OMAPI: Order entry (QUEST) [WEB:sgx-overview]

### Matching Algorithms [WEB:sgx-overview]
- **Price/Time Priority**: Default for most products
- **Price Point Maker (PPM)**: Alternative algorithm
- **Market Maker (MM)**: For designated MM products
- **Pro-Rata**: For selected products (e.g., certain interest rate futures)

### Opening Price [WEB:sgx-overview]
- Pre-open: 08:30–09:00 (order accumulation)
- Non-cancellation: 08:59–09:00
- Single-price algorithm at 09:00 sets opening price

### Closing Routine [WEB:sgx-overview]
- Pre-close: 17:00–17:04/05 (order accumulation)
- Closing auction: Determines closing price
- TAC session: 17:06–17:16 (trading at closing price)

### Tick Size [WEB:sgx-overview]
- Securities: Varies by price level (similar tiered structure)
- Derivatives: Per contract specification

### Lot Size [WEB:sgx-overview]
- Securities: Varies by security (commonly 100 shares per lot)
- Board lots defined per security

---

## 7. Safeguard Mechanisms

### 7.1 Circuit Breaker [WEB:sgx.com/cb] [WEB:sgx-practice-note]

**Scope**: STI and MSCI Singapore Free Index components, related ETFs, Extended Settlement Contracts; securities with reference price ≥ S$0.50

**Mechanism**: [WEB:sgx.com/cb]
- Reference price: last traded price at least 5 minutes ago
- **Trigger**: Incoming order would trade outside ±10% of reference price
- **Action**: Order rejected; 5-minute cooling-off period
- During cooling-off: trading continues within ±10% band
- **NOT a halt**: Similar to HKEX VCM — trading restricted, not stopped

**Operating hours**: 09:00–17:00 (continuous trading only — not during opening/closing)

### 7.2 Unusual Trading Activity Monitoring [REF:#6]
- Practice Note 7B: SGX monitors for unusual trading activity
- Can query listed companies, trading participants
- May impose trading halts for investigation

### 7.3 Market Manipulation Rules [REF:#7]
- Practice Note 13.8.1: Market manipulation and false market provisions
- SGX RegCo enforcement

### 7.4 Error Trade Policy [WEB:sgx.com]
- Revised error trade policy alongside circuit breaker introduction
- Provides framework for handling clearly erroneous executions

---

## 8. Special Sessions

### 8.1 Pre-Open (08:30–09:00) [WEB:sgx-overview]
- Order accumulation; no matching
- Non-cancellation period: 08:59–09:00
- Opening price determined by single-price algorithm at 09:00

### 8.2 Continuous Trading (09:00–17:00) [REF:#2]
- Price-time priority matching (securities)
- All order types available
- Circuit breakers active

### 8.3 Pre-Close / Closing Routine (17:00–17:06) [WEB:sgx-overview]
- Pre-close: 17:00–17:04/05 (order accumulation)
- Closing price determination

### 8.4 Trading-at-Close (TAC) (17:06–17:16) [WEB:sgx-overview]
- Post-close session trading at official closing price
- 10-minute window for closing price execution
- Longer than most exchanges' closing mechanisms

### 8.5 Derivatives Extended Hours [REF:#13] [WEB:sgx.com/platforms]
- Multiple sessions including overnight (varies by product)
- Key products: Nikkei 225 (T+1 session), MSCI indices, iron ore
- Extended hours critical for Asia-Pacific time zone coverage

### 8.6 NLT Facility [WEB:sgx.com/nlt]
- Off-book negotiated large trades
- Derivatives and selected securities
- Minimum volume thresholds; registration required

---

## 9. LP / Market Maker Obligations

### 9.1 Designated Market Makers — Securities [REF:#2] [WEB:sgx.com/dmm]

**ETF DMMs**: [WEB:sgx.com/dmm] [WEB:allenandgledhill.com]
- Must publish competitive bid/offer quotations on continuous basis
- Recent (Dec 2025): Streamlined obligations — removed administrative notification requirements for cease/resume
- Quoting obligations: minimum spread, minimum size, time-in-market

**General Equities**: No mandatory MM program

### 9.2 Derivatives Market Makers [WEB:sgx.com/trading]
- Designated for specific futures/options products
- Continuous quoting and quote request obligations
- Fee rebate incentives
- Critical for SGX's Asia derivatives franchise

### 9.3 Comparison
- **vs. HKEX**: Both have securities DMMs for ETFs only; both are Asia derivatives hubs
- **vs. ASX**: Both lack general equity MMs; ASX has Centre Point dark pool (SGX does not)
- **vs. Eurex**: Both derivatives-focused with tiered MM programs; Eurex more granular (RMM/PMM/AMM)

---

## 10. Source Bibliography

### Reference Sources (Priority 1 — README_LINKS.md)

[REF:#1] SGX, "SGX Rulebook Portal", https://rulebook.sgx.com/
[REF:#2] SGX, "SGX-ST Rules", https://rulebook.sgx.com/rulebook/sgx-st-rules-0
[REF:#3] SGX, "SGX-ST Rules Clean Version (PDF)", https://rulebook.sgx.com/sites/default/files/net_file_store/SGX_ST_June_3_2019_Clean_Version.pdf
[REF:#4] SGX, "Chapter 13 — Trading Practices and Conduct", https://rulebook.sgx.com/rulebook/chapter-13-trading-practices-and-conduct-0
[REF:#5] SGX, "SGX Rulebooks Overview", https://rulebook.sgx.com/rulebook/sgx-rulebooks
[REF:#6] SGX, "Practice Note 7B — Unusual Trading Activity", https://rulebook.sgx.com/rulebook/practice-note-7b-monitoring-and-querying-unusual-trading-activity
[REF:#7] SGX, "Practice Note 13.8.1 — Market Manipulation", https://rulebook.sgx.com/rulebook/practice-note-1381-market-manipulation-and-false-market
[REF:#8–10] SGX, "Practice Notes", Titan DT/DC Portal, Titan OTC Portal
[REF:#11] SGX, "Titan ITCH & GLIMPSE Protocol Specs (PDF)", https://api2.sgx.com/sites/default/files/2018-09/Titan%20ITCH%20&%20GLIMPSE%20Protocol%20Specifications.pdf
[REF:#12] SGX, "Titan OTC FIX API Specs (PDF)", https://api2.sgx.com/sites/default/files/2019-12/SGX%20-%20FIX%20Specification%20-%20v1%205%205.pdf
[REF:#13] SGX, "Derivatives Platforms", https://www.sgx.com/derivatives/platforms
[REF:#14] SGX, "Market Access", https://www.sgx.com/data-connectivity/market-access

### Web Sources (Priority 3 — Gap Fill)

[WEB:wikipedia] Singapore Exchange — Wikipedia, https://en.wikipedia.org/wiki/Singapore_Exchange, Accessed 2026-03-27
[WEB:sgx-overview] "SGX Overview", Trading Technologies, https://library.tradingtechnologies.com/user-setup/sgx-overview.html, Accessed 2026-03-27
[WEB:sgx.com/nlt] "Negotiated Large Trade", https://www.sgx.com/derivatives/negotiated-large-trade-nlt, Accessed 2026-03-27
[WEB:sgx.com/dmm] "Directive No. 3 — DMM Obligations", https://rulebook.sgx.com/rulebook/directive-no-3-obligations-designated-market-maker, Accessed 2026-03-27
[WEB:sgx.com/cb] "Circuit Breaker", https://rulebook.sgx.com/rulebook/practice-note-810a-circuit-breaker, Accessed 2026-03-27
[WEB:sgx-practice-note] "Regulatory Notice 8.14.1 — Circuit Breaker", https://rulebook.sgx.com/rulebook/regulatory-notice-8141-circuit-breaker, Accessed 2026-03-27
[WEB:allenandgledhill.com] "SGX streamlines ETF DMM obligations", https://www.allenandgledhill.com/sg/publication/articles/32174/, Accessed 2026-03-27
[WEB:ceicdata.com] "Singapore Market Capitalization", https://www.ceicdata.com/en/indicator/singapore/market-capitalization, Accessed 2026-03-27

---

*Report version: 1.0 | Batch: 3 | Created: 2026-03-27 | Language: English*
