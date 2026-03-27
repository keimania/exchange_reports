# Batch 1 Cross-Comparison: KRX vs NYSE vs NASDAQ

---

## 1. Market Model Philosophy

| Dimension | KRX | NYSE | NASDAQ |
|---|---|---|---|
| **Model** | Pure order-driven | Hybrid (electronic + floor + DMM) | Pure electronic order-driven |
| **Floor** | None (fully electronic) | Physical floor (unique) | None (fully electronic) |
| **Primary Intermediary** | LP/MM (voluntary, non-exclusive) | DMM (exclusive, 1 per security) | Competitive MMs (multiple per security) |
| **Allocation** | Price-time priority | Price/parity/priority | Price-time-display priority |

**Key Insight**: NYSE is the outlier — the only exchange retaining a physical floor and exclusive DMM assignment. KRX and NASDAQ share the pure electronic order-driven philosophy but differ in LP structure (KRX: contractual LP + regulator-assigned MM vs. NASDAQ: competitive voluntary MM).

---

## 2. Order Types Comparison

| Order Type | KRX | NYSE | NASDAQ |
|---|---|---|---|
| Market | ✅ 시장가 | ✅ | ✅ |
| Limit | ✅ 지정가 | ✅ | ✅ |
| Stop | ✅ 스톱지정가 (NEW 2025) | ✅ Stop/Stop-Limit | ✅ |
| MOO/LOO | ❌ (uses call auction) | ✅ | ✅ |
| MOC/LOC | ❌ (conditional limit fills role) | ✅ | ✅ |
| Conditional Limit | ✅ 조건부지정가 (unique) | ❌ | ❌ |
| Best Limit | ✅ 최유리지정가 (unique) | ❌ | ❌ |
| Best Quote | ✅ 최우선지정가 (unique) | ❌ | ❌ |
| Midpoint | ✅ 중간가 (NEW 2025) | ✅ MPL | ✅ MPPO, M-ELO |
| D-Order | ❌ | ✅ (unique) | ❌ |
| Reserve/Iceberg | ❌ (not available for equities) | ✅ | ✅ |
| Pegged | ❌ | ✅ (Primary/Market/Mid) | ✅ (Primary/Market/Mid) |
| Post-Only/ALO | ❌ | ✅ ALO | ✅ Post-Only |
| ISO | ❌ (single exchange) | ✅ | ✅ |
| M-ELO | ❌ | ❌ | ✅ (unique) |
| IOC/FOK | ✅ | ✅ | ✅ |
| GTC | ❌ (day orders only) | ✅ | ✅ |

**Key Insight**: KRX has unique auto-pricing orders (최유리/최우선/조건부) that don't exist on US exchanges. US exchanges have far more non-displayed and midpoint variants (M-ELO, MPPO, MPL, ALO). NASDAQ's M-ELO with holding period is unique globally. KRX's 2025 stop-limit and midpoint introductions show convergence toward US order type richness.

---

## 3. Trading Hours (UTC)

| Session | KRX (UTC+9) | NYSE (UTC−5) | NASDAQ (UTC−5) |
|---|---|---|---|
| Pre-market | 23:00–00:00 prev day | 11:30–14:30 | 09:00–14:30 |
| Opening auction | 23:00–00:00 | 14:30 (DMM) | 14:25–14:30 (Cross) |
| Core trading | 00:00–06:30 | 14:30–21:00 | 14:30–21:00 |
| Closing auction | 06:20–06:30 | 20:50–21:00 (DMM) | 20:50–21:00 (Cross) |
| After-hours | 06:40–09:00 | 21:00–01:00 (Arca) | 21:00–01:00 |

**Key Insight**: KRX and US markets have virtually no overlap in core hours — enabling 24-hour coverage strategies. KRX's after-hours extends to 18:00 KST (09:00 UTC), while NASDAQ's proposed 23-hour trading would cover almost all time zones.

---

## 4. Opening/Closing Mechanisms

| Dimension | KRX | NYSE | NASDAQ |
|---|---|---|---|
| **Opening** | Call auction (단일가매매) | DMM-facilitated auction | Opening Cross |
| **Random closing** | +30 sec randomization | No randomization | No randomization |
| **Closing** | Call auction (10 min) | DMM-facilitated + Auction Collars | Closing Cross |
| **Imbalance info** | Not formally published | From 3:50 PM (1-sec intervals) | NOII from 3:50 PM |
| **Human involvement** | None | DMM + Floor brokers | None |
| **Conditional→market** | ✅ (조건부지정가) | ❌ | ❌ |

**Key Insight**: KRX uses anti-gaming randomization (+30 sec) absent on US exchanges. NYSE's DMM-facilitated auction is unique — enables human judgment for large imbalances. NASDAQ's Cross is entirely algorithmic. KRX's conditional limit order (auto-converting to market at close) is a unique mechanism for closing price participation.

---

## 5. Safeguard Mechanisms

| Mechanism | KRX | NYSE | NASDAQ |
|---|---|---|---|
| **Circuit breaker index** | KOSPI | S&P 500 | S&P 500 |
| **CB Level 1** | 8% ↓, 20-min halt | 7% ↓, 15-min halt | 7% ↓, 15-min halt |
| **CB Level 2** | 15% ↓, 20-min halt | 13% ↓, 15-min halt | 13% ↓, 15-min halt |
| **CB Level 3** | 20% ↓, day terminates | 20% ↓, day terminates | 20% ↓, day terminates |
| **Individual stock VI** | Dynamic: 3%/6%; Static: 10% | LULD: 5%/10%/20% by tier | LULD: 5%/10%/20% by tier |
| **VI mechanism** | 2-min call auction | 15-sec pause → 5-min halt | 15-sec pause → 5-min halt |
| **Daily price limits** | ±30% | None (LULD replaces) | None (LULD replaces) |
| **Short-sell restriction** | Uptick rule (always) | Reg SHO (triggered at 10%↓) | Reg SHO (triggered at 10%↓) |

**Key Insight**: KRX uniquely combines both daily price limits (±30%) AND volatility interruptions — double-layer protection. US exchanges rely solely on LULD without hard daily limits. KRX's VI converts to a 2-minute auction (allowing price discovery), while US LULD uses a halt (stopping all trading).

---

## 6. Technology & Protocols

| Dimension | KRX | NYSE | NASDAQ |
|---|---|---|---|
| **System** | EXTURE+ | Pillar | INET |
| **Launch** | 2014 | 2016 (phased) | 2006 (Instinet) |
| **Latency** | 30–50 μs | Sub-ms (undisclosed) | <25 μs (OUCH collocated) |
| **Throughput** | 100,000+ TPS | Not disclosed | Not disclosed |
| **Order Protocol** | FIX/FAST | FIX + Binary | OUCH (proprietary) + FIX |
| **Data Protocol** | Proprietary | Binary | ITCH (proprietary) |
| **Architecture** | Memory-based, x86 Linux | Unified platform | FPGA-enhanced |

**Key Insight**: NASDAQ leads in raw latency (<25μs via OUCH), followed by KRX (30–50μs). All three use proprietary binary protocols for lowest latency alongside FIX for broader access. KRX uniquely publishes throughput specs (100K+ TPS). NASDAQ's FPGA enhancement represents cutting-edge deterministic processing.

---

## 7. LP/MM Programs

| Dimension | KRX | NYSE | NASDAQ |
|---|---|---|---|
| **Model** | LP + MM (separate programs) | DMM + SLP + Retail LP | Competitive MMs |
| **Exclusivity** | Non-exclusive | DMM: exclusive; SLP: non-exclusive | Non-exclusive |
| **Quoting obligation** | Spread + time + amount | DMM: 5-25% NBBO time; SLP: 10% | Continuous two-sided quotes |
| **Assignment** | Contract (LP) / Selection (MM) | Assignment (DMM) / Application (SLP) | Self-registration |
| **Compensation** | Fee rebates | Fee advantages + allocation priority | Maker-taker rebates |
| **Floor presence** | None | DMMs + Floor brokers | None |

---

## 8. Summary of Distinctive Features

| Exchange | Most Distinctive Feature |
|---|---|
| **KRX** | Dual VI system (dynamic+static) + daily ±30% limits; unique auto-pricing orders (최유리/최우선/조건부); 2025 midpoint & stop-limit additions show modernization |
| **NYSE** | Only major exchange with physical floor + exclusive DMM; D-Orders and Auction Collars; parity allocation vs. time priority |
| **NASDAQ** | Pure electronic speed champion; M-ELO with AI/ML holding periods; OUCH/ITCH proprietary protocol ecosystem; proposed 23-hour trading |

---

*Batch 1 Comparison v1.0 | Created: 2026-03-27*
