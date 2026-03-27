# Synthesis Changelog — Session 4

> Log of all fixes and conflict resolutions during cross-session audit.

---

## Glossary Conflicts Resolved

| Original # | Batch # | Issue | Resolution |
|---|---|---|---|
| #25 D-Order | #71 | Different Korean: "DMM 이해관계 주문" vs "플로어 브로커 재량 주문" | Updated to "D-주문 (플로어 브로커 재량 주문)" — more accurate |
| #24 Named Order | #98 | Duplicate entry | Kept #24; removed #98 from unified |
| #26 Centre Point | #125 | Duplicate entry | Kept #26; removed #125 |
| #27 Special Limit | #106 | #106 adds Chinese (特別限價盤) | Merged: added Chinese to #27 |
| #28 Enhanced Limit | #105 | #105 adds Chinese (增強限價盤); also swapped rest/cancel description | **FIXED**: #27 = remainder cancelled, #28 = remainder rests (matches HKEX report §5) |
| #29 At-Auction | #107 | #107 adds Chinese (競價盤) | Merged: added Chinese to #29 |
| #30 At-Auction Limit | #108 | #108 adds Chinese (競價限價盤) | Merged: added Chinese to #30 |
| #7 Pro-Rata | #137 | #137 adds SGX note | Merged: "Eurex options, SGX selected products" |
| #20 OCO | #120 | #120 is Eurex-specific (single-ID) | Merged into #20 with note: "Eurex: single-ID limit+stop" |

## Cross-Report Factual Inconsistencies Found

| Issue | Reports | Resolution |
|---|---|---|
| HKEX Enhanced Limit: "remainder queued" vs "remainder rests" | glossary.md #27 vs 06_HKEX.md §5 | **Original glossary had Special Limit (#27) and Enhanced Limit (#28) descriptions SWAPPED.** Fixed in unified glossary: #27 Special Limit = 10-level sweep + cancel; #28 Enhanced Limit = 10-level sweep + rest |
| Eurex T7 latency: "~2,787 ns" vs "~2.8 μs" | batch_3_comparison.md vs 07_Eurex.md | Both correct (2,787 ns = ~2.8 μs). Clarified in comparison: "~2,787 ns (~2.8 μs)" |
| NYSE WEB source count | checkpoint_batch1.md says "8 REF + 13 WEB" | Report §10 lists 8 REF + 13 WEB. Consistent. ✅ |
| KRX VI dynamic threshold | 01_KRX.md says "KOSPI 200: 3%, other: 6%" | Consistent with glossary #42 and batch_1_comparison. ✅ |

## Structural Audit Results

| Check | Result |
|---|---|
| All 9 reports follow §1-§10 structure | ✅ Pass |
| All Korean reports exist (01-09 _ko.md) | ✅ Pass |
| All reports use [REF:#N] and [WEB:url] citation style | ✅ Pass |
| No reports missing bibliography section | ✅ Pass |
| Korean terms consistent with unified glossary | ✅ Pass (after fixes above) |

## No Unresolvable Contradictions Found

---

*Changelog v1.0 | Created: 2026-03-27 | Session 4*
