# Research Gaps — Batch 2

> Gaps identified during Batch 2 (TSE, LSE, HKEX) research.

---

## TSE

| Gap | Severity | Status | Notes |
|---|---|---|---|
| arrowhead 4.0 exact latency figure | Medium | Accepted | Fujitsu says "microsecond-level"; prior gen ~0.5ms; JPX blocks web fetch |
| Complete tick size table (all tiers) | Low | Accepted | TOPIX 500 table documented; full table on jpx.co.jp (403 blocked) |
| Complete daily price limit table | Low | Accepted | Framework documented; example ¥1,000→±¥300; full table on jpx.co.jp |
| CAS detailed order interaction rules | Low | Accepted | Key mechanics documented from web search; JPX PDF inaccessible |
| ToSTNeT detailed specifications | Low | Deferred | Basic framework documented; detailed specs member-only |

## LSE

| Gap | Severity | Status | Notes |
|---|---|---|---|
| MIT201 full PDF content | Medium | Accepted | PDF exists but not parseable via web; key order types extracted via search |
| Turquoise Plato detailed mechanism | Low | Open | Basic structure documented; detailed matching rules not found |
| MiFID II specific tick size table values | Low | Accepted | RTS 11 framework documented; exact per-security values computed algorithmically |
| SETSqx auction schedule exact times | Low | Accepted | ~08:00, 11:00, 14:30, 16:35 from web sources |
| Millennium Exchange exact throughput | Low | Open | Latency documented (126μs); throughput not publicly available |
| AIM-specific trading rules | Low | Deferred | AIM uses SETS/SETSqx depending on liquidity; specific AIM rules deferred |

## HKEX

| Gap | Severity | Status | Notes |
|---|---|---|---|
| OTP-C exact latency specifications | Medium | Accepted | Not publicly disclosed by HKEX |
| Complete spread table (all codes) | Low | Accepted | Code 01 (main) documented; codes 03/04/05 for special securities |
| Stock Connect detailed daily quota mechanics | Low | Open | RMB 52B/42B daily noted; detailed mechanics deferred to Session 4 |
| VCM trigger count statistics | Low | Open | Unlimited triggers documented; actual frequency data not found |
| Board lot standardization timeline | Low | Monitoring | Dec 2025 consultation; implementation pending |

---

## Cross-Exchange Gaps

| Gap | Severity | Notes |
|---|---|---|
| Lunch break impact on liquidity | Low | TSE and HKEX both have lunch; LSE continuous — comparative analysis deferred |
| CAS adoption comparison | Low | TSE CAS (2024) vs HKEX CAS (2016) — maturity difference noted |
| Dark pool volumes comparison (Asia vs EU) | Medium | Japan PTS data available; HKEX minimal dark; LSE has Turquoise — deferred to Session 4 |
| Settlement cycle comparison | Low | Japan T+2, HK T+2, UK T+1 (2027 planned) — deferred |

---

*Batch 2 Gaps | Created: 2026-03-27*
