# Reference Inventory

> Generated: 2026-03-27 (Session 0)
> Scanned: `references/[exchange]/README_LINKS.md` for all 9 exchanges + Common

---

## Summary Table

| Exchange | README_LINKS.md | URLs | PDFs | Local Docs | Total Sources | Key System |
|----------|:-:|:-:|:-:|:-:|:-:|---|
| KRX | Yes | 10 | 3 | 2 | **15** | EXTURE+ |
| NYSE | Yes | 4 | 8 | 0 | **12** | Pillar |
| NASDAQ | Yes | 7 | 7 | 0 | **14** | OUCH/ITCH |
| TSE/JPX | Yes | 8 | 2 | 0 | **10** | arrowhead 4.0 |
| LSE | Yes | 4 | 3 | 0 | **7** | SETS/SETSqx/SEAQ |
| HKEX | Yes | 2 | 8 | 0 | **10** | Orion (OTP-C/D) |
| Eurex | Yes | 4 | 5 | 0 | **9** | T7 (Release 13) |
| ASX | Yes | 3 | 3 | 0 | **6** | ASX Trade |
| SGX | Yes | 11 | 3 | 0 | **14** | Titan |
| Common | Yes | 5 | 4 | 1 | **10** | (cross-exchange) |
| **Total** | **10/10** | **58** | **46** | **3** | **107** | |

---

## Per-Exchange Detail

### KRX (Korea Exchange)
- **URLs (10)**: KRX Legal Portal, Law Search Service, Regulation Amendments, Global KRX Main, KOSPI Trading Rules, KONEX Trading Rules, Derivatives Trading Hours, KOSCOM EXTURE+ Overview, KRX Data Marketplace, KIND Disclosure
- **PDFs (3)**: Introduction to Trading at KRX (KOFIA), KRX Listing Guide, KOSDAQ Disclosure/Listing Guide 2024
- **Local Docs (2)**: 유가증권시장 업무규정 시행세칙 (2026.02.09), 유가증권시장 업무규정 (2026.01.29)
- **Coverage**: Regulations, trading hours, price limits (±30%), circuit breakers (8%/15%/20%), EXTURE+ system (specs non-public)

### NYSE (New York Stock Exchange)
- **URLs (4)**: NYSE Market Model, Trading Information, FINRA Regulations, SEC EDGAR Rule Filings
- **PDFs (8)**: Rule 104 DMM Interpretation, Pillar FIX Protocol, Pillar Binary Protocol, Pillar Options Binary Protocol, Pillar Risk Controls, Pillar Order Type Differences, Functional Differences NYSE Pillar, Options Common Client Spec
- **Coverage**: DMM role, Pillar platform (FIX + Binary), order type differences across NYSE group, opening/closing auctions

### NASDAQ
- **URLs (7)**: Rule Book, OUCH Overview, TotalView Data, TotalView Solutions, TotalView-ITCH Help Center, INET Nordic Specs, Opening/Closing Crosses
- **PDFs (7)**: Order Types & Routing Strategies, OUCH 5.0 Spec, OUCH 5.0 FAQ, OUCH 4.2 Spec, Nordic Equity TotalView-ITCH 3.04.X, Opening/Closing FAQ
- **Coverage**: OUCH (order entry) and ITCH (market data) protocols, Opening/Closing Cross mechanisms

### TSE / JPX (Tokyo Stock Exchange)
- **URLs (8)**: Domestic Stock Trading Rules, Transaction Methods (Itayose & Zaraba), Daily Price Limits, Derivatives Trading Methods, Other Derivatives Rules, Arrowhead System Overview, Equities Trading Services, JPX Learning
- **PDFs (2)**: Equity Trading Guide 2024, Derivatives Trading Methods Detail
- **Coverage**: Itayose (call auction), Zaraba (continuous), arrowhead 4.0 (2024.11), Closing Auction Session

### LSE (London Stock Exchange)
- **URLs (4)**: LSE Shares Trading Overview, Documentation Portal, SETS Explained, SEAQ/SETS/SETSqx Explained
- **PDFs (3)**: MIT201 Guide Draft 15.7, MIT201 Guide v14.9, SETSqx Auction Improvements
- **Coverage**: Three-tier trading system (SETS, SETSqx, SEAQ), order types, Named Orders, Market Maker obligations
- **Note**: Lowest source count among exchanges — may need supplementary research

### HKEX (Hong Kong Exchanges and Clearing)
- **URLs (2)**: Trading Mechanism Overview, OTP Infrastructure Overview
- **PDFs (8)**: CAS Mechanism, VCM Trading (Derivatives), VCM Info Paper (Securities), OCG Binary Trading Interface, OCG FIX Drop Copy, OMD-C Binary Interface, OMD-D Developers Guide, OMD-D DLite Interface
- **Coverage**: VCM (±10% securities / ±5% derivatives), CAS, Orion platform (OTP-C, OTP-D), OMD market data

### Eurex
- **URLs (4)**: Order Types, Exchange Rules 2024, Exchange Rules 2025, T7 Release 13 Overview
- **PDFs (5)**: ETI Manual, Eurex Trader/Admin GUI Manual, T7 R13.1 Participant Maintenance, T7 R11.1 Simulation Guide, T7 R10.0 Simulation Guide
- **Coverage**: T7 system (shared with Xetra), ETI interface, order types (Limit, Market, Stop, OCO, Iceberg), pre-trade controls

### ASX (Australian Securities Exchange)
- **URLs (3)**: ASX Equities Trading, Order Controls, Centre Point
- **PDFs (3)**: ASX Trade New Order Types, Operating Rules Procedures (Draft), Operating Rules Procedures (2010)
- **Coverage**: Lit Markets, Centre Point (dark pool), order types (FOK, GFD, GTC, Iceberg), trading hours
- **Note**: Second-lowest source count — may need supplementary research

### SGX (Singapore Exchange)
- **URLs (11)**: Rulebook Portal, SGX-ST Rules, SGX-ST Rules Clean, Chapter 13, SGX Rulebooks, Practice Notes, Practice Note 7B, Practice Note 13.8.1, Titan DT/DC Portal, Titan OTC Portal, Derivatives Platforms, Market Access
- **PDFs (3)**: SGX-ST Rules Clean Version PDF, Titan ITCH/GLIMPSE Protocol Specs, Titan OTC FIX API Specs
- **Coverage**: Rulebook, practice notes, Titan system (ITCH, GLIMPSE, FIX), derivatives platforms

### Common (Cross-Exchange Studies)
- **URLs (5)**: IOSCO Public Reports, WFE Research, WFE Statistics, Microstructure Exchange Seminars, 6 Must-Read Papers 2024
- **PDFs (4)**: IOSCO 2025 Work Program, BIS WP No. 1290 (HFT Speed Premium), HFT/Asset Pricing/Microstructure (SSRN), Market Macrostructure (NBER)
- **Docs (1)**: Larry Harris WFE Chapter on Market Microstructure (.doc)
- **Coverage**: Cross-exchange comparison frameworks, price discovery, order types taxonomy, volatility controls, data protocols

---

## Coverage Assessment

### Well-Covered Areas
- Order types and trading rules (all exchanges)
- Trading system specifications (NYSE Pillar, NASDAQ OUCH/ITCH, HKEX Orion, Eurex T7, SGX Titan)
- Volatility/safeguard mechanisms (KRX circuit breakers, HKEX VCM, TSE price limits)

### Gaps Identified
- **LSE**: Only 7 sources — needs more on SETS order types, Turquoise (pan-European MTF), MiFID II implications
- **ASX**: Only 6 sources — needs more on ASX Trade matching engine internals, CHESS settlement
- **KRX**: EXTURE+ specs are member-only (non-public) — may need secondary sources
- **All exchanges**: LP/Market Maker obligation details are thin across the board
- **Common**: No FIA or ISDA cross-exchange studies included yet
