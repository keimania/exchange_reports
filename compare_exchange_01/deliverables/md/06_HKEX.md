# HKEX (Hong Kong Exchanges and Clearing) — Exchange Report

---

## 1. Exchange Overview

**Full Legal Name**: Hong Kong Exchanges and Clearing Limited (HKEX)
**Country**: Hong Kong SAR, China
**Founding Year**: 1891 (original Association of Stockbrokers); HKEX incorporated 2000 [WEB:wikipedia]
**Parent Group**: Self-listed public company (HKEX: 0388.HK) [WEB:wikipedia]

**Market Model**: Order-driven with VCM safeguards and CAS closing mechanism [REF:#1]

**Asset Classes Traded**: [WEB:wikipedia]
- Securities (Main Board, GEM)
- Derivatives (futures, options — via HKFE)
- Commodities (via LME — London Metal Exchange, acquired 2012)
- Fixed Income, ETFs, REITs, Warrants, CBBCs

**Regular Trading Hours (HKT, UTC+8)**: [REF:#1]
- Pre-Opening Session (POS): 09:00–09:30
- Morning session: 09:30–12:00
- Lunch break: 12:00–13:00
- Afternoon session: 13:00–16:00
- Closing Auction Session (CAS): 16:00–16:08/16:10 (random close)

**Key Statistics**: [WEB:wikipedia] [WEB:grokipedia]
- Listed companies: ~2,673 (Feb 2026)
- Market capitalization: ~HK$48.5 trillion / ~US$6.2 trillion (6th globally)
- 2025: Record revenues (+33% YoY), #1 global IPO venue [WEB:scmp]
- Stock Connect: Key gateway between Hong Kong and Mainland China markets

**Recent Major Changes**: [WEB:hkex.com.hk]
- 2025 mid: Minimum spread reduction Phase 1 (50-60% narrower ticks)
- 2025.08: Orion Derivatives Platform (ODP) preview — next-gen derivatives system
- 2025.12: Board lot framework consultation — proposing standard lot sizes
- Stock Connect expansion ongoing (ETF Connect, Bond Connect, Swap Connect)

---

## 2. Institutional Philosophy

**Primary Market Model**: Order-driven with structured safeguards [REF:#1]
- Electronic order book with price-time priority during continuous trading
- Pre-Opening Session and CAS use call auction mechanism
- VCM provides cooling-off protection against extreme volatility
- No designated market makers for general equities (MM programs for derivatives and ETPs) [WEB:hkex.com.hk/mm]

**Design Rationale**: [WEB:wikipedia]
- Gateway between international capital and Mainland China (Stock Connect)
- Order-driven core with strong investor protection mechanisms (VCM, CAS price limits)
- Pragmatic hybrid: pure order book + regulatory safeguards + structured auction sessions
- Emphasis on closing price integrity (CAS with ±5% price band)

**Role of Intermediaries**: [WEB:hkex.com.hk/mm]
- **Derivatives Market Makers**: Primary (PMM) and General (GMM) for options/futures
- **ETP Designated Specialists**: Market making for ETFs/ETPs
- **Securities**: No general equity market maker program — competitive order flow

**Evolution**: Multiple local exchanges → unified SEHK (1986) → demutualized HKEX (2000) → LME acquisition (2012) → Stock Connect (2014) → VCM/CAS introduction (2016) → ODP development (2025+) [WEB:wikipedia]

---

## 3. Order Types — Basic

### 3.1 Limit Order [REF:#1]
- Specifies price and quantity
- Executes only at specified price (no price improvement in continuous trading)
- Bid orders cannot exceed best ask; sell orders cannot fall below best bid
- Available during continuous trading session

### 3.2 Enhanced Limit Order (增強限價盤) [REF:#1]
- Matches across **up to 10 price queues** at specified price or better
- Cannot be entered more than 10 spreads away from current best bid/ask
- Unmatched portion rests on order book at input price
- More aggressive than standard limit — similar to marketable limit

### 3.3 Special Limit Order (特別限價盤) [REF:#1]
- Matches across **up to 10 price queues** with no input price restriction (beyond deviation limits)
- **Unmatched portions cancelled** (unlike Enhanced Limit which rests on book)
- No price distance restriction from best quote
- Function similar to IOC with multi-level sweep

---

## 4. Order Types — Advanced

### 4.1 At-Auction Order (競價盤) [REF:#1]
- No specified price — executes at Indicative Equilibrium Price (IEP)
- **Highest matching priority** among auction order types
- Available during: Pre-Opening Session and CAS
- Guaranteed execution if matching is possible at IEP

### 4.2 At-Auction Limit Order (競價限價盤) [REF:#1]
- Specified price — executes at IEP if competitive enough
- Lower priority than At-Auction Orders
- If unmatched in POS: carries forward to continuous trading as limit order
- CAS: must be within ±5% of Reference Price [WEB:hkex.com.hk/cas]

### 4.3 Time-in-Force [REF:#1]
- **Day**: Default — expires at session end
- Orders do not carry over between days (no GTC for general securities)
- At-Auction Limit Orders from POS carry to continuous session within same day

### 4.4 Odd Lot Trading [REF:#1]
- Quantities less than one board lot
- Traded separately from board lot trades (marked "D")
- Special lot trades: non-integral multiples of board lot

---

## 5. Order Types — Exchange-Specific

### 5.1 Enhanced Limit Order (增強限價盤) [REF:#1]
- **HKEX-unique**: Multi-level matching (up to 10 queues) with resting remainder
- No direct equivalent on other exchanges — combines market order aggression with limit order persistence
- Rationale: Allows investors to access deeper liquidity while maintaining price discipline

### 5.2 Special Limit Order (特別限價盤) [REF:#1]
- **HKEX-unique**: Multi-level sweep with auto-cancel of remainder
- Fills up to 10 price levels; cancels unfilled portion
- Rationale: For investors wanting immediate maximum fill without resting orders

### 5.3 At-Auction Order (競價盤) [REF:#1]
- **HKEX-unique naming and priority**: Carries highest execution priority in auctions
- Unpriced — accepted only during POS and CAS
- Distinct from MOO/MOC on US exchanges: specifically designed for HKEX's IEP mechanism

### 5.4 At-Auction Limit Order (競價限價盤) [REF:#1]
- **HKEX-unique**: Priced order for auction sessions with carry-forward feature
- POS unfilled orders convert to limit orders in continuous session
- CAS orders subject to ±5% Reference Price band
- No equivalent on KRX/NYSE/NASDAQ/TSE/LSE

### 5.5 9-Times Price Deviation Rule [REF:#1]
- All order prices must not deviate ≥9× from nominal price during continuous trading
- Opening quotes within 24 spreads or ±5% (±3.5% for ETPs) of prior close
- HKEX-specific safeguard integrated into order validation

---

## 6. Matching Engine & Price Discovery

### Trading System: Orion Trading Platform (OTP) [REF:#5] [REF:#6]
- **OTP-C**: Securities market (cash equities) [REF:#5]
- **OTP-D**: Derivatives market [REF:#5]
- **OTP-CSC**: Stock Connect channel [WEB:hkex.com.hk/otp-csc]
- **Access**: Orion Central Gateway (OCG) — Binary and FIX protocols [REF:#6]
- **Market Data**: OMD-C (securities), OMD-D (derivatives) [REF:#8] [REF:#9]
- **Latency**: Not publicly disclosed (competitive with regional peers)

### Matching Algorithm [REF:#1]
- **Continuous Trading**: Price-time priority (strict)
- **Auctions (POS/CAS)**: Order type priority (at-auction > at-auction limit) → price → time
- Maximum order size: 3,000 board lots (automatch)
- Maximum price queue capacity: 40,000 orders

### Pre-Opening Session (POS) [REF:#1]
- **09:00–09:15**: Order input period
- **09:15–09:20**: No cancellation period
- **09:20–09:30**: Random matching period → matching at IEP
- At-Auction and At-Auction Limit orders accepted
- Unmatched At-Auction Limit orders carry to continuous session

### Closing Auction Session (CAS) [REF:#2] [WEB:hkex.com.hk/cas]
- **16:00–16:01**: Reference Price fixing (median of 5 prices in last minute)
- **16:01–16:06**: Order input period (at-auction / at-auction limit within ±5% of Reference Price)
- **16:06–16:08**: No cancellation period
- **16:08–16:10**: Random closing period (market closes randomly within 2 min)
- Matching at final IEP; At-Auction orders have priority
- If no IEP determined: Reference Price becomes closing price

### Closing Price (Non-CAS Securities) [REF:#1]
- Median of 5 nominal prices at 15-second intervals in last minute (15:59:00–16:00:00)

### Tick Size (Minimum Spread) [WEB:hkex.com.hk/spread] [WEB:charltonslaw.com]
- Tiered by price level, examples:

| Price Range (HK$) | Tick Size (HK$) |
|---|---|
| 0.01–0.25 | 0.001 |
| 0.25–0.50 | 0.005 |
| 0.50–10.00 | 0.010 |
| 10.00–20.00 | 0.010 (reduced from 0.020 in mid-2025) |
| 20.00–50.00 | 0.020 (reduced from 0.050 in mid-2025) |
| 50.00–100.00 | 0.050 |
| 100.00–200.00 | 0.100 |
| 200.00–500.00 | 0.200 |
| 500.00–1,000 | 0.500 |
| 1,000–2,000 | 1.000 |
| ≥ 2,000 | 2.000 |

- Phase 2 reduction planned for mid-2026 [WEB:hkex.com.hk/spread]

### Board Lot (Trading Unit) [WEB:hkex.com.hk/board-lot]
- Varies by security: from 10 shares to 100,000 shares per lot
- Currently 44 different board lot units in use
- Proposal (Dec 2025): Standardize to max 10,000 shares [WEB:scmp]

---

## 7. Safeguard Mechanisms

### 7.1 Volatility Control Mechanism (VCM) [REF:#3] [REF:#4] [WEB:hkex.com.hk/vcm]

**Securities Market**: [REF:#4]
- **Applicable**: Hang Seng Composite Index constituents, SPACs, eligible ETFs
- **Trigger**: Order price deviates ≥ ±10% from reference price (last trade 5 min ago)
- **Action**: 5-minute cooling-off period — trading continues but only within ±10% band
- **NOT a halt**: Trading continues within restricted price band
- **Multiple triggers**: Unlimited VCM triggers per session per security
- No limitation on number of cooling-off periods

**Derivatives Market**: [REF:#3]
- **Trigger**: ±5% deviation
- **Action**: 5-minute cooling-off period within ±5% band

### 7.2 CAS Price Limits [REF:#2]
- ±5% from Reference Price during CAS
- Orders outside ±5% band rejected
- Reference Price: median of 5 prices in last minute of continuous trading

### 7.3 9-Times Rule [REF:#1]
- Order prices cannot deviate ≥9× from nominal price
- Prevents extreme mis-pricing / fat finger errors

### 7.4 Opening Quote Limits [REF:#1]
- First bid/ask: within 24 spreads or ±5% (±3.5% for ETPs) of prior close

### 7.5 No Market-Wide Circuit Breaker
- HKEX does not have US-style market-wide halts
- VCM applies per-security with cooling-off (not full halt)
- Individual security halts for material news

---

## 8. Special Sessions

### 8.1 Pre-Opening Session (POS) (09:00–09:30) [REF:#1]
- Call auction mechanism with IEP determination
- At-Auction and At-Auction Limit orders only
- 4 sub-periods: input → matching → random matching → opening

### 8.2 Morning Continuous Trading (09:30–12:00) [REF:#1]
- Price-time priority matching
- All order types: Limit, Enhanced Limit, Special Limit

### 8.3 Lunch Break (12:00–13:00) [REF:#1]
- No trading — unique among major exchanges (similar to TSE but longer)

### 8.4 Afternoon Continuous Trading (13:00–16:00) [REF:#1]
- Same as morning session

### 8.5 Closing Auction Session (CAS) (16:00–16:08/16:10) [REF:#2]
- 4 periods: Reference Price fixing → order input → no cancellation → random close
- At-Auction / At-Auction Limit orders within ±5% of Reference Price
- Random close within 16:08–16:10
- Applied to all equities and funds since October 2019 [WEB:hkex.com.hk/cas]

### 8.6 Stock Connect [WEB:hkex.com.hk/stock-connect]
- **Northbound**: HK investors → Shanghai/Shenzhen A-shares
- **Southbound**: Mainland investors → HK-listed securities
- Daily quota: RMB 52 billion (Northbound), RMB 42 billion (Southbound) as of 2025
- ETF Connect, Bond Connect, Swap Connect also operational
- #1 channel for foreign access to China A-shares

### 8.7 Block Trading / Manual Trades [REF:#1]
- Manual trades: Non-direct "M", Direct "X" — reported to exchange
- Special lot / odd lot trades handled separately
- No formal separate block facility (unlike KRX's 대량매매)

---

## 9. LP / Market Maker Obligations

### 9.1 Derivatives Market Makers [WEB:hkex.com.hk/mm]

**Primary Market Makers (PMM)**: [WEB:hkex.com.hk/mm]
- Must provide continuous quotes (CQ) and respond to quote requests (QR)
- Assigned to specific products/series
- Quoting obligations: minimum size, maximum spread, time-in-market percentage

**General Market Makers (GMM)**: [WEB:hkex.com.hk/mm]
- Lighter obligations than PMM
- Respond to quote requests; optional continuous quotes
- Lower incentives than PMM

### 9.2 ETP Designated Specialists [WEB:hkex.com.hk/ds]
- Market making for ETFs and exchange-traded products
- Quoting obligations similar to derivatives MMs
- Fee rebates and incentives for maintaining liquidity

### 9.3 Securities Market — No General MM Program [REF:#1]
- No mandatory market maker for general equities
- Liquidity from natural order flow and institutional activity
- Stock Connect provides significant liquidity channel
- Similar to TSE's approach (MM only for specific product types)

### 9.4 Comparison with Batch 1/2 Exchanges
- **vs. KRX**: KRX has LP + MM for equities; HKEX has none for equities
- **vs. NYSE**: NYSE has exclusive DMM; HKEX has no equivalent
- **vs. NASDAQ**: NASDAQ has competitive MMs; HKEX has MM only for derivatives/ETPs
- **vs. TSE**: Similar — both lack general equity MMs; both have ETF MM programs
- **vs. LSE**: LSE has tiered MM by liquidity; HKEX has MM only for derivatives/ETPs

---

## 10. Source Bibliography

### Reference Sources (Priority 1 — README_LINKS.md)

[REF:#1] HKEX, "Trading Mechanism Overview", https://www.hkex.com.hk/Services/Trading/Securities/Overview/Trading-Mechanism?sc_lang=en

[REF:#2] HKEX, "Closing Auction Session (CAS) Mechanism (PDF)", https://www.hkex.com.hk/eng/market/sec_tradinfra/vcm_cas/Documents/Trading%20Mechanism%20of%20the%20CAS%20in%20the%20Securities%20Market.pdf

[REF:#3] HKEX, "VCM Trading Mechanism — Derivatives (PDF)", https://www.hkex.com.hk/-/media/HKEX-Market/Services/Trading/Derivatives/Trading-Mechanism/Volatility-Control-Mechanism-(VCM)/Trading-Mechanism-for-VCM-Eng.pdf

[REF:#4] HKEX, "VCM Information Paper — Securities (PDF)", https://www.hkex.com.hk/-/media/HKEX-Market/Services/Trading/Securities/Overview/Trading-Mechanism/Trading-Mechanism-for-VCM_E.pdf?la=en

[REF:#5] HKEX, "OTP Infrastructure Overview", https://www.hkex.com.hk/Services/Trading/Securities/Infrastructure/Overview?sc_lang=en

[REF:#6] HKEX, "OCG Binary Trading Interface Specifications (PDF)", https://www.hkex.com.hk/-/media/HKEX-Market/Services/Trading/Securities/Infrastructure/Orion-Trading-Platform-Securities-Market-OTP-C/OTPC/HKEX_OCG_Binary_Trading_Interface_Specifications_v2_1.pdf

[REF:#7] HKEX, "OCG FIX Drop Copy Interface (PDF)", https://www.hkex.com.hk/-/media/HKEX-Market/Services/Trading/Securities/Infrastructure/Orion-Trading-Platform-Securities-Market-OTP-C/OTPC/HKEX_OCG_FIX_Drop_Copy_Interface_Specifications_v2_1(With_Track_Changes).pdf

[REF:#8] HKEX, "OMD-C Binary Interface Specifications (PDF)", https://www.hkex.com.hk/eng/prod/dataprod/Documents/HKEX_OMD-C_Binary_Interface_Specifications_v1.39b.pdf

[REF:#9] HKEX, "OMD-D Developers Guide (PDF)", https://www.hkex.com.hk/-/media/HKEX-Market/Services/Market-Data-Services/Infrastructure/HKEX-Orion-Market-Data-Platform-Derivatives-Market-OMD-D/HKEX-OMDD-Developers-Guide-v1,-d-,26.pdf

[REF:#10] HKEX, "OMD-D DLite Interface (PDF)", https://www.hkex.com.hk/-/media/HKEX-Market/Services/Market-Data-Services/Infrastructure/HKEX-Orion-Market-Data-Platform-Derivatives-Market-OMD-D/Introduction-of-DLite/OMDD-Interface-Specifications-(DLite)-v1,-d-,4d-(for-G4).pdf

### Web Sources (Priority 3 — Gap Fill)

[WEB:wikipedia] Hong Kong Exchanges and Clearing — Wikipedia, https://en.wikipedia.org/wiki/Hong_Kong_Exchanges_and_Clearing, Accessed 2026-03-27

[WEB:hkex.com.hk/vcm] "VCM FAQ", https://www.hkex.com.hk/Global/Exchange/FAQ/Securities-Market/Trading/VCM?sc_lang=en, Accessed 2026-03-27

[WEB:hkex.com.hk/cas] "CAS FAQ", https://www.hkex.com.hk/Global/Exchange/FAQ/Securities-Market/Trading/CAS?sc_lang=en, Accessed 2026-03-27

[WEB:hkex.com.hk/mm] "Market Maker Program", https://www.hkex.com.hk/Products/Listed-Derivatives/Market-Maker-Program?sc_lang=en, Accessed 2026-03-27

[WEB:hkex.com.hk/spread] "Proposed Reduction of Minimum Spreads", https://www.hkex.com.hk/-/media/HKEX-Market/News/Market-Consultations/2016-Present/June-2024-Review-of-Minimum-Spreads/Consultation-Paper/cp202406.pdf, Accessed 2026-03-27

[WEB:hkex.com.hk/board-lot] "Board Lot Framework Enhancements", https://www.hkex.com.hk/-/media/HKEX-Market/News/Market-Consultations/2016-Present/December-2025-Board-Lot-Framework-Enhancements/Consultation-Paper/cp202512.pdf, Accessed 2026-03-27

[WEB:hkex.com.hk/stock-connect] "Stock Connect FAQ 2025", https://www.hkexgroup.com/Media-Centre/Insight/Insight/2025/HKEX-Insight/Top10-questions-HKEX-Stock-Connect-2025-FAQ?sc_lang=en, Accessed 2026-03-27

[WEB:grokipedia] Hong Kong Exchanges and Clearing — Grokipedia, https://grokipedia.com/page/Hong_Kong_Exchanges_and_Clearing, Accessed 2026-03-27

[WEB:scmp] "HKEX proposes slashing board lot variations", SCMP, https://www.scmp.com/business/banking-finance/article/3336940, Accessed 2026-03-27

[WEB:charltonslaw.com] "HKEX Consults on Reducing Minimum Spreads", https://www.charltonslaw.com/hkex-consults-on-reducing-minimum-spreads-for-hong-kong-securities/, Accessed 2026-03-27

[WEB:ifec.org.hk] "Closing Auction Session", https://www.ifec.org.hk/web/en/investment/investment-products/stock/stock-trading/closing-auction-session.page, Accessed 2026-03-27

---

*Report version: 1.0 | Batch: 2 | Created: 2026-03-27 | Language: English*
