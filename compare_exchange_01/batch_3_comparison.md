# Batch 3 Cross-Comparison: Eurex vs ASX vs SGX

---

## 1. Market Model Philosophy

| Dimension | Eurex | ASX | SGX |
|---|---|---|---|
| **Primary Focus** | Derivatives (Europe) | Equities + integrated dark pool | Derivatives hub (Asia) |
| **Model** | Electronic order-driven + MM infrastructure | Order-driven + Centre Point dark | Order-driven (cash) + Titan (derivatives) |
| **Unique Feature** | Shared T7 with Xetra (cash+derivatives) | Integrated exchange dark pool | Dual-platform (QUEST + Titan) |
| **MM Role** | Central (RMM/PMM/AMM tiers) | ETF/ETO only; no equity MM | ETF DMM + derivatives MM |

**Key Insight**: Eurex and SGX are both derivatives-first exchanges with securities as secondary. ASX is the opposite — equities-first with its unique integrated dark pool (Centre Point) as the differentiator. All three lack mandatory general equity market makers.

---

## 2. Order Types Comparison

| Order Type | Eurex | ASX | SGX |
|---|---|---|---|
| Market | ✅ | ✅ (Market-to-Limit default) | ✅ (FAK — remainder cancelled) |
| Limit | ✅ | ✅ | ✅ |
| Stop / Stop-Limit | ✅ | ❌ | ✅ (FAK-style) |
| OCO | ✅ (single-ID, unique) | ❌ | ❌ |
| Book-or-Cancel / Post-Only | ✅ BOC | ❌ | ❌ |
| Iceberg | ✅ | ✅ | ❌ |
| GTC | ✅ (up to 1 year) | ✅ | ✅ |
| IOC/FOK | ✅ IOC | ✅ FOK/FAK | ✅ IOC/FOK |
| Opening/Closing Auction orders | ✅ (3 variants) | ✅ (auction phases) | ✅ (pre-open/close) |
| Centre Point / Dark orders | ❌ | ✅ (unique) | ❌ |
| ASX Sweep (dark→lit) | ❌ | ✅ (unique) | ❌ |
| NLT / Block | ✅ (EnLight, EFP/EFS) | ✅ (TRF) | ✅ NLT |
| Strategy / Multi-leg | ✅ (limit only) | ❌ | ❌ |

**Key Insight**: Eurex has the richest order type set (OCO, BOC, 3 auction variants, strategy orders) — reflecting derivatives complexity. ASX uniquely integrates dark pool orders (Centre Point, Sweep). SGX's market order as FAK is distinctive — cancels remainder instead of resting.

---

## 3. Safeguard Mechanisms

| Mechanism | Eurex | ASX | SGX |
|---|---|---|---|
| **Market-wide CB** | No | No | No |
| **Individual VI** | Volatility Interruption → auction | AOT ±10% rejection; ETR 2-min pause | ±10% cooling-off (trading continues) |
| **Response** | Volatility auction (no matching) | Order rejection + brief pause | Band-restricted trading |
| **Daily price limits** | No | No | No |
| **Pre-trade controls** | Max qty/value, delta-equiv, throttle | AOT reference price (VWAP 2-min) | Circuit breaker + regulatory monitoring |
| **Dark pool regulation** | N/A | ASIC "meaningful price improvement" | N/A |

**Key Insight**: All three avoid market-wide circuit breakers and daily price limits. SGX's approach (HKEX-style band-restricted trading) differs from ASX (order rejection + brief pause) and Eurex (full volatility auction). ASX uniquely regulates dark pool execution quality via ASIC rules.

---

## 4. Technology

| Dimension | Eurex | ASX | SGX |
|---|---|---|---|
| **System** | T7 (shared with Xetra) | ASX Trade | QUEST (cash) + Titan (derivatives) |
| **Latency** | ~2,787 ns min reaction time | Not publicly disclosed | Not publicly disclosed |
| **Protocols** | ETI (TCP/IP) + FIX | OMNet + FIX + OUCH | OMAPI + ITCH + GLIMPSE + FIX |
| **Market Data** | EOBI (fastest: ~1.5μs advantage) | Proprietary | ITCH (Titan), proprietary (QUEST) |
| **Unique tech** | Colo 2.0, nanosecond timestamps | CHESS (settlement infra) | Titan ITCH/GLIMPSE |

**Key Insight**: Eurex T7 has the most transparent and fastest disclosed latency (~2.8μs). SGX uses ITCH protocol (like NASDAQ) for derivatives data. ASX uses OUCH (like NASDAQ) for order entry. Technology convergence: OUCH/ITCH protocols spreading beyond NASDAQ.

---

## 5. Full 9-Exchange Comparison Matrix

| Exchange | Model | Latency | MM Model | Closing Mechanism | Unique Feature |
|---|---|---|---|---|---|
| **KRX** | Pure order-driven | 30-50μs | LP + MM | Call auction +30s random | 최유리/최우선/조건부지정가; ±30% limits + VI |
| **NYSE** | Hybrid (floor + DMM) | Sub-ms | Exclusive DMM + SLP | DMM auction + Auction Collars | D-Order; physical floor; parity allocation |
| **NASDAQ** | Pure electronic | <25μs (OUCH) | Competitive MMs | Closing Cross | M-ELO (AI/ML hold); OUCH/ITCH; 23-hr proposal |
| **TSE** | Itayose + Zaraba | μs-level | ETF MM only | CAS (new 2024) | Funari; Special Quote (Tokubetsu Kehai) |
| **LSE** | Three-tier (SETS/SETSqx/SEAQ) | 126μs | Tiered by liquidity | Uncrossing at 16:35 | Named Order; Random Peak Iceberg; three models |
| **HKEX** | Order-driven + VCM | Not disclosed | Derivatives/ETP only | CAS ±5% + random close | Enhanced/Special Limit (10-level); Stock Connect |
| **Eurex** | Derivatives-first | ~2.8μs | RMM/PMM/AMM tiers | Product-specific | OCO single-ID; BOC; T7 shared with Xetra |
| **ASX** | Order-driven + dark pool | Not disclosed | ETO/ETP only | Single-price 16:10-16:12 | Centre Point (integrated dark); ASX Sweep |
| **SGX** | Derivatives hub | Not disclosed | ETF DMM + derivatives | TAC session 10 min | MKT=FAK; TAC; Asia derivatives franchise |

---

*Batch 3 Comparison v1.0 | Created: 2026-03-27*
