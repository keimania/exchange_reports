# Research Gaps — Batch 1

> Gaps identified during Batch 1 (KRX, NYSE, NASDAQ) research.
> Logged per CLAUDE.md §Step 3 gap-fill protocol.

---

## KRX

| Gap | Severity | Status | Notes |
|---|---|---|---|
| EXTURE+ internal architecture details | Low | Accepted | Member-only specs. Mitigated via KOSCOM + Global KRX public pages (100K TPS, 30-50μs) |
| LP contract-level spread requirements | Low | Accepted | Exact spread percentages set per-contract, not published. Framework documented from regulations |
| Listed companies exact count 2025-2026 | Low | Accepted | Approximate ~2,600+ from secondary sources; exact requires KRX Data Marketplace subscription |
| Average daily trading volume | Medium | Open | Not found in current sources; KRX Data Marketplace likely has this |
| KOSDAQ/KONEX specific trading rule differences | Low | Deferred | Report focused on KOSPI/유가증권시장 regulations; KOSDAQ has parallel but similar rules |

## NYSE

| Gap | Severity | Status | Notes |
|---|---|---|---|
| Pillar binary protocol internals | Low | Accepted | PDF not parseable via web fetch; specs referenced but not deep-dived |
| Risk controls specific parameter values | Low | Accepted | Configurable per-firm; documented framework from web search |
| SLP exact current rebate schedule 2026 | Low | Open | Rebate ~$0.0020/share from 2012 filing; current may differ |
| Pillar exact latency figures | Medium | Accepted | NYSE does not publicly disclose; "sub-millisecond" is best available |
| Extended hours 24/5 plans | Low | Monitoring | NYSE Arca extended hours expanding; watch for SEC filings |

## NASDAQ

| Gap | Severity | Status | Notes |
|---|---|---|---|
| OUCH 5.0 full message format details | Low | Accepted | PDF specs referenced but not deep-dived; protocol overview documented |
| M-ELO exact execution statistics | Low | Open | Adoption/fill rates not publicly available |
| NASDAQ exact current maker rebate schedule | Low | Open | Approximate ~$0.002-0.003; exact tiers require Nasdaq fee schedule |
| 23-hour trading implementation details | Low | Monitoring | Filed Dec 2025; pending SEC approval; target Q3 2026 |
| Nasdaq BX and PSX specific differences | Low | Deferred | Report focused on primary Nasdaq market; BX/PSX have inverted pricing |

---

## Cross-Exchange Gaps

| Gap | Severity | Notes |
|---|---|---|
| Dark pool / ATS volume comparison | Medium | US ATS data available via FINRA; KRX has minimal dark trading |
| Settlement cycle comparison (T+1 vs T+2) | Medium | US moved to T+1 (May 2024); KRX settlement details not covered |
| Regulatory framework comparison (SEC vs FSC) | Low | Deferred to Session 4 synthesis |

---

*Batch 1 Gaps | Created: 2026-03-27*
