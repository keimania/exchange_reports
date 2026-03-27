# Master Plan — Exchange Comparison Research Project

> Created: 2026-03-27 (Session 0)
> Project: compare_exchange_01

---

## Research Tree Decomposition

```
compare_exchange_01/
├── Session 0: Infrastructure Setup (THIS SESSION)
│   ├── reference_inventory.md    ← audit all sources
│   ├── glossary.md               ← 65 bilingual terms
│   ├── report_template.md        ← 10-section mandatory structure
│   ├── plan.md                   ← this file
│   ├── checkpoint.md             ← progress tracking
│   ├── research_gaps.md          ← gap tracker
│   └── source_bibliography.md    ← all sources consolidated
│
├── Session 1 (Batch 1): KRX, NYSE, NASDAQ
│   ├── KRX_report.md             ← 15 sources, EXTURE+, ±30% limits
│   ├── NYSE_report.md            ← 12 sources, Pillar/DMM hybrid
│   └── NASDAQ_report.md          ← 14 sources, OUCH/ITCH pure electronic
│
├── Session 2 (Batch 2): TSE, LSE, HKEX
│   ├── TSE_report.md             ← 10 sources, arrowhead 4.0, Itayose/Zaraba
│   ├── LSE_report.md             ← 7 sources (needs supplement), SETS/SETSqx/SEAQ
│   └── HKEX_report.md            ← 10 sources, Orion/VCM/CAS
│
├── Session 3 (Batch 3): Eurex, ASX, SGX
│   ├── Eurex_report.md           ← 9 sources, T7 system, derivatives focus
│   ├── ASX_report.md             ← 6 sources (needs supplement), Centre Point dark
│   └── SGX_report.md             ← 14 sources, Titan system, Asia derivatives hub
│
├── Session 4: Synthesis & Cross-Comparison
│   ├── comparison_matrix.md      ← 9-exchange side-by-side on all 10 sections
│   ├── theme_analysis.md         ← cross-cutting themes & insights
│   └── executive_summary.md      ← key findings, recommendations
│
└── Session 5: Build (Final Deliverables)
    ├── deliverables/md/          ← finalized markdown reports
    ├── deliverables/html/        ← styled HTML versions
    └── deliverables/docx/        ← Word document versions
```

---

## Session Schedule & Objectives

### Session 0 — Infrastructure Setup ✅ (Current)
- [x] Task 1: Reference audit → reference_inventory.md
- [x] Task 2: Glossary seed → glossary.md (65 terms)
- [x] Task 3: Report template → report_template.md (10 sections)
- [x] Task 4: Master plan → plan.md (this file)
- [x] Task 5: Shared files → checkpoint, research_gaps, source_bibliography, deliverables/

---

### Session 1 — Batch 1: KRX, NYSE, NASDAQ

**Rationale**: Start with the most familiar (KRX) and most documented (NYSE, NASDAQ) exchanges. These three also represent distinct market philosophies: KRX (pure order-driven, Asian), NYSE (hybrid with DMM), NASDAQ (pure electronic order-driven).

#### KRX Checklist (15 sources available)
- [ ] §1 Exchange Overview — trading hours, KOSPI/KOSDAQ/KONEX structure
- [ ] §2 Institutional Philosophy — pure order-driven, no DMM, EXTURE+ system
- [ ] §3 Order Types Basic — 시장가, 지정가, 조건부지정가 from regulations
- [ ] §4 Order Types Advanced — review 업무규정 시행세칙 for iceberg/conditional
- [ ] §5 Order Types Exchange-Specific — 최유리지정가, 최우선지정가, 장전시간외, 장후시간외
- [ ] §6 Matching Engine — EXTURE+ (specs non-public; use secondary sources + KOSCOM overview)
- [ ] §7 Safeguards — circuit breakers (8%/15%/20%), VI (±10%), daily limits (±30%)
- [ ] §8 Special Sessions — 장전 동시호가, 장후 동시호가, 시간외 단일가, 시간외 대량매매
- [ ] §9 LP/MM Obligations — KRX LP program (유동성공급자 제도)
- [ ] §10 Bibliography — consolidate all 15 sources + any new ones found
- [ ] **Gap check**: EXTURE+ technical details (member-only), LP obligation specifics

#### NYSE Checklist (12 sources available)
- [ ] §1 Exchange Overview — NYSE/NYSE Arca/NYSE American structure, Pillar migration
- [ ] §2 Institutional Philosophy — hybrid model, floor + electronic, DMM role
- [ ] §3 Order Types Basic — market, limit, stop from Trading Information page
- [ ] §4 Order Types Advanced — from Pillar Order Type Differences PDF
- [ ] §5 Order Types Exchange-Specific — D-Order, DMM interest types, Retail Liquidity Program
- [ ] §6 Matching Engine — Pillar platform, FIX + Binary protocols, Risk Controls
- [ ] §7 Safeguards — LULD (SEC Rule 201), market-wide circuit breakers (7%/13%/20%)
- [ ] §8 Special Sessions — pre-open (06:30), opening auction (DMM), closing auction, after-hours (→20:00)
- [ ] §9 LP/MM Obligations — DMM obligations (Rule 104), SLP program
- [ ] §10 Bibliography — consolidate all 12 sources
- [ ] **Gap check**: SLP specifics, Retail Liquidity Program details

#### NASDAQ Checklist (14 sources available)
- [ ] §1 Exchange Overview — NASDAQ/BX/PSX structure, fully electronic
- [ ] §2 Institutional Philosophy — pure electronic order-driven, no floor, speed-first design
- [ ] §3 Order Types Basic — from Order Types & Routing Strategies PDF
- [ ] §4 Order Types Advanced — from OUCH 5.0 spec (order types supported)
- [ ] §5 Order Types Exchange-Specific — Midpoint Extended Life Order (MELO), Post-Only
- [ ] §6 Matching Engine — OUCH (order entry), ITCH (market data), INET architecture
- [ ] §7 Safeguards — LULD (shared with NYSE), clearly erroneous execution rules
- [ ] §8 Special Sessions — Opening Cross (09:25-09:30), Closing Cross (15:50-16:00), extended hours
- [ ] §9 LP/MM Obligations — NASDAQ Market Maker program, competitive MM obligations
- [ ] §10 Bibliography — consolidate all 14 sources
- [ ] **Gap check**: MELO specifics, extended hours order type restrictions

---

### Session 2 — Batch 2: TSE, LSE, HKEX

**Rationale**: Three major exchanges from different time zones (Asia, Europe, Asia) with distinct trading system architectures. TSE recently upgraded (arrowhead 4.0), LSE has a unique three-tier system, HKEX has notable VCM/CAS mechanisms.

#### TSE/JPX Checklist (10 sources available)
- [ ] §1 Exchange Overview — JPX group (TSE + OSE merger), arrowhead 4.0 launch (2024.11)
- [ ] §2 Institutional Philosophy — pure order-driven, Itayose + Zaraba dual mechanism
- [ ] §3 Order Types Basic — from Equity Trading Guide 2024 PDF
- [ ] §4 Order Types Advanced — from trading rules pages
- [ ] §5 Order Types Exchange-Specific — Funari (引成), Conditional Limit at Close
- [ ] §6 Matching Engine — arrowhead 4.0 specifications, latency improvements
- [ ] §7 Safeguards — daily price limits (tiered by price level), special quote system
- [ ] §8 Special Sessions — Closing Auction Session (new in 4.0), ToSTNeT (off-auction)
- [ ] §9 LP/MM Obligations — TSE Market Maker program (ETF-focused)
- [ ] §10 Bibliography — consolidate all 10 sources
- [ ] **Gap check**: arrowhead 4.0 detailed specs, CAS implementation details

#### LSE Checklist (7 sources available — NEEDS SUPPLEMENT)
- [ ] §1 Exchange Overview — LSE Group structure, LSEG technology stack
- [ ] §2 Institutional Philosophy — three-tier system (SETS/SETSqx/SEAQ), segment-based
- [ ] §3 Order Types Basic — from MIT201 guide
- [ ] §4 Order Types Advanced — iceberg, hidden, stop from MIT201
- [ ] §5 Order Types Exchange-Specific — Named Order (SETSqx), At Best order
- [ ] §6 Matching Engine — Millennium Exchange, latency specs
- [ ] §7 Safeguards — dynamic circuit breakers, static/dynamic price monitoring
- [ ] §8 Special Sessions — opening/closing auction (SETS), 4x daily auction (SETSqx), Turquoise
- [ ] §9 LP/MM Obligations — SEAQ Market Makers, SETSqx Market Makers
- [ ] §10 Bibliography — consolidate + supplement
- [ ] **Gap check**: Turquoise MTF details, MiFID II impact, Millennium Exchange specs
- [ ] **ACTION**: Research additional sources for LSE (target: 12+ total sources)

#### HKEX Checklist (10 sources available)
- [ ] §1 Exchange Overview — HKEX group, securities + derivatives + LME
- [ ] §2 Institutional Philosophy — order-driven with VCM safeguards, CAS closing mechanism
- [ ] §3 Order Types Basic — from Trading Mechanism Overview
- [ ] §4 Order Types Advanced — from OTP-C interface specs
- [ ] §5 Order Types Exchange-Specific — Special Limit, Enhanced Limit, At-Auction, At-Auction Limit
- [ ] §6 Matching Engine — Orion Trading Platform (OTP-C securities, OTP-D derivatives)
- [ ] §7 Safeguards — VCM (±10%/±5%, 5-min cooling), dynamic price limit
- [ ] §8 Special Sessions — Pre-Opening Session, CAS (16:00-16:10), block trades
- [ ] §9 LP/MM Obligations — HKEX LP program, Stock Connect considerations
- [ ] §10 Bibliography — consolidate all 10 sources
- [ ] **Gap check**: Stock Connect mechanism details, OTP-C order type full list

---

### Session 3 — Batch 3: Eurex, ASX, SGX

**Rationale**: Eurex (European derivatives), ASX (Oceania, dark pool focus), SGX (Southeast Asia, derivatives hub). These complete the 9-exchange coverage with diverse market types.

#### Eurex Checklist (9 sources available)
- [ ] §1 Exchange Overview — Deutsche Börse Group, derivatives focus, T7 platform
- [ ] §2 Institutional Philosophy — hybrid auction + continuous, shared T7 with Xetra
- [ ] §3 Order Types Basic — Limit, Market, Stop from order types page
- [ ] §4 Order Types Advanced — OCO, Iceberg from order types page, ETI manual
- [ ] §5 Order Types Exchange-Specific — Strategy orders, volume discovery orders
- [ ] §6 Matching Engine — T7 Release 13, ETI interface, Application Gateway
- [ ] §7 Safeguards — pre-trade risk controls (max order size/value), volatility interruptions
- [ ] §8 Special Sessions — opening/closing auction, block trade facility, EFP/EFS
- [ ] §9 LP/MM Obligations — Eurex designated MMs, permanent/temporary MMs
- [ ] §10 Bibliography — consolidate all 9 sources
- [ ] **Gap check**: Xetra cash market specifics, volatility interruption thresholds

#### ASX Checklist (6 sources available — NEEDS SUPPLEMENT)
- [ ] §1 Exchange Overview — ASX Limited, securities + derivatives + clearing
- [ ] §2 Institutional Philosophy — order-driven with integrated dark pool (Centre Point)
- [ ] §3 Order Types Basic — from ASX Trade order types PDF
- [ ] §4 Order Types Advanced — from operating rules procedures
- [ ] §5 Order Types Exchange-Specific — Centre Point orders, off-tick matching
- [ ] §6 Matching Engine — ASX Trade platform, CHESS clearing system
- [ ] §7 Safeguards — order controls, anomalous order thresholds
- [ ] §8 Special Sessions — Centre Point dark, pre-open (07:00), closing auction (16:00-16:10)
- [ ] §9 LP/MM Obligations — ASX Market Maker program
- [ ] §10 Bibliography — consolidate + supplement
- [ ] **Gap check**: ASX Trade matching engine details, CHESS settlement specifics
- [ ] **ACTION**: Research additional sources for ASX (target: 12+ total sources)

#### SGX Checklist (14 sources available)
- [ ] §1 Exchange Overview — SGX Group, securities + derivatives, Asia gateway
- [ ] §2 Institutional Philosophy — order-driven, Titan system for derivatives
- [ ] §3 Order Types Basic — MKT, Limit, STP from rules
- [ ] §4 Order Types Advanced — STP Limit, from SGX-ST Rules Chapter 13
- [ ] §5 Order Types Exchange-Specific — Negotiated Large Trade (NLT), QUEST orders
- [ ] §6 Matching Engine — Titan (ITCH/GLIMPSE), QUEST electronic platform
- [ ] §7 Safeguards — trading controls from practice notes, unusual activity monitoring
- [ ] §8 Special Sessions — pre-open (08:30-09:00), NLT facility, OTC (Titan OTC)
- [ ] §9 LP/MM Obligations — SGX Designated Market Maker scheme
- [ ] §10 Bibliography — consolidate all 14 sources
- [ ] **Gap check**: Securities matching engine (separate from Titan derivatives)

---

### Session 4 — Synthesis & Cross-Comparison

**Objective**: Produce analytical deliverables that compare all 9 exchanges across every report section.

#### Deliverables
- [ ] **comparison_matrix.md** — side-by-side table for each of the 10 report sections
  - Market model comparison (order-driven vs. hybrid vs. quote-driven)
  - Order type availability matrix (65+ order types × 9 exchanges)
  - Trading hours overlap visualization (UTC timeline)
  - Safeguard mechanism comparison table
  - Protocol/technology stack comparison
- [ ] **theme_analysis.md** — cross-cutting insights
  - Theme 1: Convergence toward electronic order-driven models
  - Theme 2: Diverse approaches to volatility control
  - Theme 3: Dark pool integration vs. segregation
  - Theme 4: Opening/closing price discovery mechanism design
  - Theme 5: LP/MM program design spectrum (mandatory DMM ↔ voluntary LP)
  - Theme 6: Protocol standardization (FIX) vs. proprietary (OUCH, ETI)
- [ ] **executive_summary.md** — key findings for each exchange + top insights
- [ ] Update research_gaps.md with final gap assessment
- [ ] Update checkpoint.md to reflect completion status

#### Cross-Comparison Dimensions
| Dimension | Compared Across |
|---|---|
| Market philosophy | Order-driven (KRX, NASDAQ, TSE, ASX, SGX) vs. Hybrid (NYSE, LSE SETSqx, Eurex) vs. Quote-driven (LSE SEAQ) |
| Opening mechanism | Call auction (KRX, TSE, LSE, HKEX, Eurex, ASX, SGX) vs. Cross (NASDAQ) vs. DMM auction (NYSE) |
| Closing mechanism | Call auction vs. CAS (HKEX, TSE 4.0) vs. Cross (NASDAQ) vs. DMM (NYSE) |
| Volatility controls | Circuit breakers (KRX, US) vs. VCM (HKEX) vs. Price limits (KRX, TSE) vs. VI (Eurex) |
| Dark trading | Integrated (ASX Centre Point) vs. External (US ATS, EU MTF) vs. Minimal (KRX, TSE) |
| Technology | Proprietary (EXTURE+, arrowhead, Orion) vs. Shared (T7) vs. Protocol-standard (FIX/OUCH/ITCH) |

---

### Session 5 — Build (Final Deliverables)

**Objective**: Convert all markdown reports into polished HTML and DOCX formats.

- [ ] Finalize all 9 exchange reports in deliverables/md/
- [ ] Generate styled HTML versions in deliverables/html/
  - Consistent styling, navigation, cross-links
  - Comparison tables with sortable columns
  - Trading hours UTC timeline visualization
- [ ] Generate DOCX versions in deliverables/docx/
  - Professional formatting, table of contents
  - Consistent heading styles and numbering
- [ ] Final quality check: all [REF:#N] and [WEB:url] citations resolve
- [ ] Korean translation pass (as per LANGUAGE POLICY, final step)

---

## Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| EXTURE+ specs non-public | KRX matching engine section thin | Use KOSCOM overview + secondary academic sources |
| LSE only 7 sources | Report may lack depth | Supplement in Session 2 with web research |
| ASX only 6 sources | Report may lack depth | Supplement in Session 3 with web research |
| Exchange rule changes between sessions | Stale information | Check amendment dates before writing; note "as of" dates |
| Glossary term inconsistency | Korean terms vary by source | Cross-reference KRX official terms as baseline |

---

*Plan version: 1.0 | Created: 2026-03-27 | Last updated: 2026-03-27*
