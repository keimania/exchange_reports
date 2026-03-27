# Checkpoint — Batch 3 (Session 3)

> Last updated: 2026-03-27

---

## Session 3 Status: **COMPLETE**

| Exchange | Report (EN) | Report (KO) | Quality Gate | Sources Used |
|---|---|---|---|---|
| Eurex | ✅ 07_Eurex.md | ✅ 07_Eurex_ko.md | ✅ All passed | 7 REF + 10 WEB |
| ASX | ✅ 08_ASX.md | ✅ 08_ASX_ko.md | ✅ All passed | 6 REF + 8 WEB |
| SGX | ✅ 09_SGX.md | ✅ 09_SGX_ko.md | ✅ All passed | 14 REF + 8 WEB |

---

## Batch 3 Deliverables

| File | Status | Location |
|---|---|---|
| Eurex Report (EN) | Complete | deliverables/md/07_Eurex.md |
| Eurex Report (KO) | Complete | deliverables/md/07_Eurex_ko.md |
| ASX Report (EN) | Complete | deliverables/md/08_ASX.md |
| ASX Report (KO) | Complete | deliverables/md/08_ASX_ko.md |
| SGX Report (EN) | Complete | deliverables/md/09_SGX.md |
| SGX Report (KO) | Complete | deliverables/md/09_SGX_ko.md |
| Batch Comparison | Complete | batch_3_comparison.md |
| Glossary (New Terms) | Complete | glossary_batch3.md (25 new terms: #116-140) |
| Research Gaps | Complete | research_gaps_batch3.md |
| Checkpoint | Complete | checkpoint_batch3.md (this file) |

---

## Key Findings (Batch 3)

### Market Model Spectrum
- **Eurex**: Derivatives-first with T7 shared platform (Xetra cash); most sophisticated MM tiers
- **ASX**: Equities-first with unique integrated dark pool (Centre Point)
- **SGX**: Derivatives hub for Asia; QUEST (cash) + Titan (derivatives) dual-platform

### Notable Discoveries
1. **Eurex T7 nanosecond latency**: ~2,787 ns minimum reaction time — fastest disclosed among all 9 exchanges
2. **Eurex tiered MM model**: RMM/PMM/AMM — most granular market maker structure across all 9
3. **ASX Centre Point**: Only exchange with a fully integrated exchange-operated dark pool
4. **ASX "meaningful price improvement" rule**: ASIC mandates dark trades at midpoint or ≥1 tick better — unique regulatory approach
5. **ASX market-to-limit default**: "Market orders" are actually market-to-limit — built-in price protection
6. **SGX market order as FAK**: Remainder cancelled (not rested) — unique implementation
7. **SGX TAC session**: 10-minute post-close trading at closing price — longest closing mechanism
8. **SGX + HKEX parallel**: Both Asian derivatives hubs with similar VCM-style circuit breakers (trading continues within bands)

### Volatility Control Spectrum (All 9 Exchanges)
| Approach | Exchanges |
|---|---|
| Market-wide CB + LULD | NYSE, NASDAQ |
| Daily price limits + VI | KRX |
| Daily price limits + Special Quote | TSE |
| Per-stock dynamic/static CB → auction | LSE |
| Per-stock VCM → band-restricted trading | HKEX, SGX |
| Per-product volatility interruption → auction | Eurex |
| AOT rejection + ETR pause | ASX |

---

## Cumulative Progress (Sessions 0-3)

| Session | Exchanges | Status |
|---|---|---|
| Session 0 | Infrastructure | ✅ Complete |
| Session 1 (Batch 1) | KRX, NYSE, NASDAQ | ✅ Complete |
| Session 2 (Batch 2) | TSE, LSE, HKEX | ✅ Complete |
| **Session 3 (Batch 3)** | **Eurex, ASX, SGX** | **✅ Complete** |
| Session 4 | Synthesis & Cross-Comparison | **NEXT** |
| Session 5 | Build (HTML/DOCX) | Pending |

### All 9 Exchange Reports: COMPLETE ✅
| # | Exchange | EN | KO | Batch |
|---|---|---|---|---|
| 01 | KRX | ✅ | ✅ | 1 |
| 02 | NYSE | ✅ | ✅ | 1 |
| 03 | NASDAQ | ✅ | ✅ | 1 |
| 04 | TSE | ✅ | ✅ | 2 |
| 05 | LSE | ✅ | ✅ | 2 |
| 06 | HKEX | ✅ | ✅ | 2 |
| 07 | Eurex | ✅ | ✅ | 3 |
| 08 | ASX | ✅ | ✅ | 3 |
| 09 | SGX | ✅ | ✅ | 3 |

### Glossary Progress
- Main glossary: 65 terms
- Batch 1: 25 terms (#66-90)
- Batch 2: 25 terms (#91-115)
- Batch 3: 25 terms (#116-140)
- **Total after merge: 140 terms**

### Total Deliverables: 18 reports (9 EN + 9 KO) + 3 batch comparisons + 3 glossary batches + 3 gap files + 3 checkpoints = **30 files**

---

## Next Session (Session 4): Synthesis & Cross-Comparison
- comparison_matrix.md — 9-exchange side-by-side on all 10 report sections
- theme_analysis.md — cross-cutting themes
- executive_summary.md — key findings
- Merge glossary batches into main glossary.md (→140 terms)
- Final research_gaps.md update

---

*Checkpoint Batch 3 v1.0 | Created: 2026-03-27*
