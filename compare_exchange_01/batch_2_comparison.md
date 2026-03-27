# Batch 2 Cross-Comparison: TSE vs LSE vs HKEX

---

## 1. Market Model Philosophy

| Dimension | TSE | LSE | HKEX |
|---|---|---|---|
| **Model** | Pure order-driven (Itayose + Zaraba) | Three-tier (SETS/SETSqx/SEAQ) | Order-driven with VCM safeguards |
| **Floor** | None (fully electronic) | None (fully electronic) | None (fully electronic) |
| **Primary Intermediary** | ETF MM only (incentive scheme) | Varies by tier: none / MM / quote-driven | Derivatives/ETP MM only |
| **Allocation** | Price-time priority (Zaraba); quantity in Itayose | Price-time priority | Price-time priority; order-type priority in auctions |
| **Lunch Break** | Yes (11:30–12:30) | No | Yes (12:00–13:00) |

**Key Insight**: All three are primarily order-driven, but LSE uniquely segments by liquidity into three completely different trading models. TSE and HKEX share the Asian exchange pattern of lunch breaks and no general equity MMs. LSE's SEAQ remains one of the last purely quote-driven segments on a major exchange.

---

## 2. Order Types Comparison

| Order Type | TSE | LSE | HKEX |
|---|---|---|---|
| Market | ✅ 成行 | ✅ | ❌ (no pure market order) |
| Limit | ✅ 指値 | ✅ | ✅ |
| Enhanced Limit | ❌ | ❌ | ✅ (10-level sweep + rest) |
| Special Limit | ❌ | ❌ | ✅ (10-level sweep + cancel) |
| At Best | ❌ | ✅ (unique) | ❌ |
| Funari | ✅ (unique) | ❌ | ❌ |
| Named Order | ❌ | ✅ SETSqx (unique) | ❌ |
| At-Auction | ❌ | ❌ | ✅ (unique priority) |
| At-Auction Limit | ❌ | ❌ | ✅ (unique, carry-forward) |
| MOO/MOC | ✅ | ❌ | ❌ |
| LOO/LOC | ✅ | ❌ | ❌ |
| Iceberg | ❌ | ✅ (random peak) | ❌ |
| Hidden | ❌ | ✅ (LIS required) | ❌ |
| Mid-Price Pegged | ❌ | ✅ | ❌ |
| Stop / Stop-Limit | ❌ | ✅ | ❌ |
| IOC | ✅ | ✅ | ❌ (Special Limit serves similar) |
| FOK | ✅ | ✅ | ❌ |
| GTC | ❌ | ✅ | ❌ |

**Key Insight**: HKEX's Enhanced/Special Limit orders (10-level sweep) are unique globally — no other exchange offers this specific multi-level matching with rest/cancel variants. LSE has the richest advanced order set (iceberg, hidden, pegged, stop). TSE's Funari is the Asian parallel to KRX's Conditional Limit. HKEX notably lacks pure market orders, iceberg, and hidden orders — more restrictive than peers.

---

## 3. Trading Hours (UTC)

| Session | TSE (UTC+9) | LSE (UTC+0) | HKEX (UTC+8) |
|---|---|---|---|
| Pre-market | 23:00–00:00 prev | 05:05–07:50 | 01:00–01:30 |
| Opening auction | 00:00 (Itayose) | 07:50–08:00 | 01:00–01:30 (POS) |
| Morning session | 00:00–02:30 | 08:00–16:30 | 01:30–04:00 |
| Lunch break | 02:30–03:30 | None | 04:00–05:00 |
| Afternoon session | 03:30–06:25 | (continuous) | 05:00–08:00 |
| Closing auction | 06:25–06:30 (CAS) | 16:30–16:35 | 08:00–08:10 (CAS) |

**Key Insight**: TSE and HKEX both have lunch breaks; LSE trades continuously. LSE's trading day (08:00–16:30 London) overlaps with HKEX afternoon (13:00–16:00 HKT = 05:00–08:00 UTC). TSE's new CAS (arrowhead 4.0) aligns it with HKEX's established CAS model.

---

## 4. Closing Mechanisms

| Dimension | TSE | LSE | HKEX |
|---|---|---|---|
| **Type** | CAS — Itayose (NEW 2024) | Closing auction uncrossing | CAS — IEP-based auction |
| **Duration** | 5 min (15:25–15:30) | 5 min (16:30–16:35) | 8-10 min (16:00–16:10) |
| **Price band** | None (daily limits apply) | No specific CAS band | ±5% from Reference Price |
| **Random close** | No | No | Yes (2-min random window) |
| **Funari/conditional** | ✅ Funari → market at CAS | ❌ | ❌ |
| **Order types** | On-close + funari + regular | Regular limit/market | At-Auction + At-Auction Limit |
| **Carry-forward** | No | No | At-Auction Limit → continuous (POS) |

**Key Insight**: HKEX has the most structured CAS: 4 distinct sub-periods, ±5% price band, random close. TSE's newly introduced CAS is simpler (single Itayose at 15:30) but benefits from Funari order conversion. LSE's closing auction is straightforward with no special price bands.

---

## 5. Safeguard Mechanisms

| Mechanism | TSE | LSE | HKEX |
|---|---|---|---|
| **Market-wide CB** | No (equities); derivatives ~8% | No | No |
| **Individual stock VI** | Special Quote (Tokubetsu Kehai) | Dynamic 3% / Static 8% (FTSE100) | VCM ±10% (securities) |
| **VI response** | Slow-motion indicative quote | 5-min call auction | 5-min cooling-off (trading continues) |
| **Daily price limits** | Yes (absolute ¥ by price level) | No | No (9× rule only) |
| **Halt mechanism** | Special Quote (not a halt) | Call auction (brief halt) | Cooling-off (not a halt) |
| **Price band** | N/A | Per-instrument calibrated | ±5% CAS; ±10% VCM |
| **Short-sell restriction** | Uptick rule | Short Selling Regulation (EU/UK) | Designated securities list only |

**Key Insight**: All three avoid US-style market-wide circuit breakers. TSE's Special Quote is unique — a "slow-motion" indicative process rather than a halt. HKEX's VCM is distinctive: trading continues within bands (not suspended). LSE uses hard 5-minute call auctions. TSE is the only one with daily price limits (absolute ¥ amounts, not percentages).

---

## 6. Technology

| Dimension | TSE | LSE | HKEX |
|---|---|---|---|
| **System** | arrowhead 4.0 | Millennium Exchange | Orion Trading Platform (OTP) |
| **Launch/Version** | Nov 2024 (4th gen) | 2011 | Progressive updates |
| **Latency** | Microsecond-level (undisclosed exact) | 126 μs (native) / 196 μs (FIX) | Not disclosed |
| **Infrastructure** | 462 Fujitsu PRIMERGY servers | MillenniumIT (Sri Lanka) | OTP-C/OTP-D/OTP-CSC |
| **Protocols** | Proprietary + FIX | Native API + FIX 5.0 | OCG Binary + FIX |
| **Market Data** | Proprietary | GTP (multicast UDP) | OMD-C / OMD-D |
| **Special feature** | Memory triplication, CAS | Random peak iceberg | Stock Connect gateway |

**Key Insight**: LSE's Millennium Exchange has the most publicly benchmarked latency (126μs). TSE's arrowhead 4.0 is the newest platform. HKEX's OTP uniquely integrates Stock Connect cross-border infrastructure. All three support both proprietary binary and FIX protocols.

---

## 7. LP/MM Programs

| Dimension | TSE | LSE | HKEX |
|---|---|---|---|
| **General equity MM** | No | SETS: No; SETSqx/SEAQ: Yes | No |
| **ETF/ETP MM** | Yes (incentive scheme) | Optional | Yes (Designated Specialists) |
| **Derivatives MM** | N/A (OSE handles) | N/A (separate venues) | Yes (PMM/GMM) |
| **Model** | Incentive-based | Liquidity-tier dependent | Product-type dependent |
| **Unique aspect** | Only ETF MM scheme | Three-tier MM structure | Stock Connect as liquidity channel |

---

## 8. Cross-Batch Comparison (Batch 1 vs Batch 2)

| Dimension | Batch 1 (KRX/NYSE/NASDAQ) | Batch 2 (TSE/LSE/HKEX) |
|---|---|---|
| **Latency leaders** | NASDAQ <25μs, KRX 30-50μs | LSE 126μs (disclosed) |
| **MM models** | KRX LP/MM, NYSE DMM, NASDAQ competitive | TSE/HKEX: ETF only; LSE: tiered |
| **Closing mechanisms** | KRX call auction, NYSE DMM auction, NASDAQ Cross | TSE CAS (new), LSE uncrossing, HKEX CAS (±5%) |
| **Safeguards** | KRX dual-layer, US LULD/MWCB | TSE Special Quote, LSE 3%/8%, HKEX VCM ±10% |
| **GTC support** | KRX/TSE: No; NYSE/NASDAQ: Yes | TSE/HKEX: No; LSE: Yes |
| **Unique features** | KRX 최유리/최우선, NYSE D-Order, NASDAQ M-ELO | TSE Funari, LSE Named Order, HKEX Enhanced/Special Limit |

---

*Batch 2 Comparison v1.0 | Created: 2026-03-27*
