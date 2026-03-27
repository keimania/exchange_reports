# Glossary — Market Structure Terms (English / Korean)

> Unified bilingual glossary for the 9-exchange comparison project.
> 140 terms covering: order types, market models, mechanisms, session names, safeguards, systems, protocols.
> Merged from: glossary.md (v1.0) + glossary_batch1.md + glossary_batch2.md + glossary_batch3.md
> Conflicts resolved: see synthesis_changelog.md

---

## A. Mechanisms (매매 메커니즘)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 1 | Continuous Trading | 접속매매 (연속매매) | Mechanism | KRX: 접속매매; TSE: Zaraba; standard intraday matching |
| 2 | Call Auction | 단일가매매 (동시호가) | Mechanism | Opening/closing price determination |
| 3 | Opening Auction | 시초가 경매 (장전 동시호가) | Mechanism | KRX 08:30-09:00; NYSE/NASDAQ opening cross |
| 4 | Closing Auction | 종가 경매 (장후 동시호가) | Mechanism | KRX 15:20-15:30; HKEX CAS 16:00-16:10 |
| 5 | Auction Uncrossing | 경매 체결 (단일가 체결) | Mechanism | Moment accumulated orders execute at single price |
| 6 | Price-Time Priority | 가격·시간 우선원칙 | Mechanism | Primary matching rule across most exchanges |
| 7 | Pro-Rata Matching | 비례배분 체결 | Mechanism | Eurex options, SGX selected products |
| 84 | Parity Allocation | 동등 배분 | Mechanism | NYSE: allocation among resting orders at same price |
| 91 | Itayose (板寄せ) | 이타요세 (판기매) | Mechanism | TSE: call auction for open/close/halt resumption |
| 92 | Zaraba (ザラバ) | 자라바 (연속매매) | Mechanism | TSE: continuous price-time priority matching |

## B. Order Types — Basic (기본 주문유형)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 8 | Market Order | 시장가 주문 | Order Type | Execute at best available price; SGX: FAK-style |
| 9 | Limit Order | 지정가 주문 | Order Type | Execute at specified price or better |
| 10 | Stop Order | 조건부지정가 주문 (스톱 주문) | Order Type | Triggered when price reaches stop level |
| 11 | Stop-Limit Order | 스톱 지정가 주문 | Order Type | Stop trigger + limit price execution |
| 12 | Market-to-Limit Order | 시장가-지정가 전환 주문 | Order Type | Converts to limit at execution price; ASX default |
| 14 | Fill-or-Kill (FOK) | 전량체결-전량취소 주문 | Order Type | Must fill entirely or cancel completely |
| 15 | Fill-and-Kill (FAK) | 즉시체결-잔량취소 주문 | Order Type | Fill available, cancel remainder; aka IOC |
| 16 | Immediate-or-Cancel (IOC) | 즉시체결-잔량취소 (IOC) | Order Type | Synonym for FAK in most markets |
| 17 | Good-for-Day (GFD) | 당일 유효 주문 | Order Type | Expires at end of trading day |
| 18 | Good-Till-Cancel (GTC) | 취소시까지 유효 주문 | Order Type | Remains active; NYSE/NASDAQ/LSE/ASX/SGX/Eurex |
| 19 | Good-Till-Date (GTD) | 지정일까지 유효 주문 | Order Type | Expires on specified date; LSE, Eurex |
| 78 | Market-on-Open (MOO) | 시초가 시장가 주문 | Order Type | NYSE/NASDAQ/TSE: opening auction market order |
| 79 | Market-on-Close (MOC) | 종가 시장가 주문 | Order Type | NYSE/NASDAQ/TSE: closing auction market order |
| 80 | Limit-on-Open (LOO) | 시초가 지정가 주문 | Order Type | Opening auction limit order |
| 81 | Limit-on-Close (LOC) | 종가 지정가 주문 | Order Type | Closing auction limit order |

## C. Order Types — Advanced (고급 주문유형)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 13 | Iceberg Order | 빙산 주문 (비공개잔량주문) | Order Type | Partial display; reserve hidden |
| 20 | One-Cancels-the-Other (OCO) | 양자택일 주문 (OCO) | Order Type | Eurex: single-ID limit+stop; others: linked pair |
| 21 | Pegged Order | 페그 주문 (연동 주문) | Order Type | Auto-adjusts to reference (mid, best bid/ask) |
| 22 | Midpoint Peg | 중간가 페그 | Order Type | Pegged to NBBO/BBO midpoint |
| 23 | Minimum Quantity Order | 최소수량 주문 | Order Type | Requires minimum fill size per execution |
| 77 | Post-Only Order | 게시 전용 주문 | Order Type | Posts only; cancels if would remove liquidity |
| 100 | Random Peak Size Iceberg | 무작위 피크 빙산 주문 | Order Type | LSE: randomized display quantity |
| 119 | Book-or-Cancel (BOC) | 게시전용 주문 (BOC) | Order Type | Eurex: rejected if immediately executable |
| 122 | Strategy Order | 전략 주문 (다리 주문) | Order Type | Eurex: multi-leg options strategy |
| 123 | Volume Discovery Order | 거래량 발견 주문 | Order Type | Eurex: block-size price discovery |
| 88 | Market Maker Peg Order | 시장조성자 페그 주문 | Order Type | NASDAQ: auto-repricing for MM compliance |

## D. Order Types — Exchange-Specific (거래소 고유 주문유형)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 25 | D-Order | D-주문 (플로어 브로커 재량 주문) | Order Type | NYSE: floor broker discretionary auction interest |
| 66 | Stop-Limit Order (KRX) | 스톱지정가호가 | Order Type | KRX: introduced 2025.02.05 |
| 67 | Midpoint Order (KRX) | 중간가호가 | Order Type | KRX: introduced 2025.02.27; arithmetic mean of BBO |
| 68 | Conditional Limit Order | 조건부지정가호가 | Order Type | KRX: limit during continuous → market at close |
| 69 | Best Limit Order | 최유리지정가호가 | Order Type | KRX: auto-prices at counterparty best |
| 70 | Best Quote Order | 최우선지정가호가 | Order Type | KRX: auto-prices at own-side best |
| 72 | Midpoint Passive Liquidity (MPL) | 중간가 수동 유동성 주문 | Order Type | NYSE: non-displayed midpoint |
| 73 | Add Liquidity Only (ALO) | 유동성 추가 전용 주문 | Order Type | NYSE: post-only variant |
| 74 | Midpoint Extended Life Order (M-ELO) | 중간가 연장수명 주문 (M-ELO) | Order Type | NASDAQ: midpoint with 0.5s hold |
| 75 | Dynamic M-ELO | 동적 M-ELO | Order Type | NASDAQ: AI/ML-adjusted holding periods |
| 76 | Midpoint Peg Post-Only (MPPO) | 중간가 페그 게시 전용 주문 | Order Type | NASDAQ: passive midpoint, no hold |
| 93 | Funari Order (引成注文) | 후나리 주문 (인성주문) | Order Type | TSE: limit→market at closing auction |
| 24 | Named Order | 기명 주문 | Order Type | LSE SETSqx: non-anonymous limit order |
| 99 | At Best Order | 최우선가 주문 | Order Type | LSE: single-price fill, remainder cancelled |
| 114 | Executable Quote | 체결 가능 호가 | Order Type | LSE SETSqx/SEAQ: MM firm quote |
| 27 | Special Limit Order (HKEX) | 특별지정가 주문 (特別限價盤) | Order Type | HKEX: 10-level sweep, remainder cancelled |
| 28 | Enhanced Limit Order (HKEX) | 증강지정가 주문 (增強限價盤) | Order Type | HKEX: 10-level sweep, remainder rests |
| 29 | At-Auction Order | 경매주문 (競價盤) | Order Type | HKEX: unpriced, highest auction priority |
| 30 | At-Auction Limit Order | 경매지정가 주문 (競價限價盤) | Order Type | HKEX: priced auction, carry-forward |
| 26 | Centre Point Order | 센터포인트 주문 | Order Type | ASX: integrated dark pool midpoint |
| 126 | ASX Sweep | ASX Sweep (다크→릿 통합 라우팅) | Order Type | ASX: dark-then-lit routing |
| 134 | NLT (Negotiated Large Trade) | NLT (협의대량거래) | Order Type | SGX: off-book large trade facility |
| 136 | Market Order as FAK | 시장가(FAK) 방식 | Order Type | SGX: market order cancels remainder |

## E. Market Models & Participants (시장 모델 · 참가자)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 31 | Order-Driven Market | 주문주도형 시장 | Market Model | KRX, NASDAQ, TSE, ASX, SGX |
| 32 | Quote-Driven Market | 호가주도형 시장 | Market Model | LSE SEAQ |
| 33 | Hybrid Market | 혼합형 시장 | Market Model | NYSE with DMM, LSE SETSqx, Eurex |
| 34 | Designated Market Maker (DMM) | 지정 시장조성자 | Participant | NYSE: exclusive per security |
| 35 | Market Maker (MM) | 시장조성자 | Participant | Continuous two-sided quotes |
| 36 | Liquidity Provider (LP) | 유동성 공급자 | Participant | Contractual liquidity obligation |
| 85 | Supplemental Liquidity Provider (SLP) | 보충적 유동성공급자 (SLP) | Participant | NYSE: electronic LP |
| 86 | Retail Liquidity Program | 소매 유동성 프로그램 | Program | NYSE: price improvement for retail |
| 138 | Regular/Permanent/Advanced MM | 일반/상시/고급 시장조성자 | Participant | Eurex: tiered MM model (RMM/PMM/AMM) |

## F. Venues (거래 장소)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 37 | Dark Pool | 다크풀 (비공개 매매장소) | Venue | ASX Centre Point, US ATS |
| 38 | Alternative Trading System (ATS) | 대체거래시스템 | Venue | US: non-exchange venue |
| 39 | Multilateral Trading Facility (MTF) | 다자간매매체결시설 | Venue | EU/UK: Turquoise, BATS Europe |
| 96 | ToSTNeT | ToSTNeT (장외매매시스템) | Venue | TSE: off-auction block/basket/buyback |
| 102 | SETS | SETS (주식전자거래서비스) | Venue | LSE: order book for liquid stocks |
| 103 | SETSqx | SETSqx (호가+교차) | Venue | LSE: hybrid for mid-liquidity |
| 104 | SEAQ | SEAQ (주식자동호가시스템) | Venue | LSE: quote-driven for low-liquidity |
| 113 | Turquoise | 터쿼이즈 | Venue | LSEG: pan-European MTF |
| 124 | Eurex EnLight | Eurex EnLight | Venue | Eurex: RFQ off-book negotiation |
| 140 | Trade Reporting Facility (TRF) | 거래보고시설 (TRF) | Venue | ASX: off-market trade reporting |

## G. Safeguards (안전장치)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 40 | Circuit Breaker | 서킷브레이커 | Safeguard | KRX 8%/15%/20%; US 7%/13%/20% |
| 41 | Volatility Control Mechanism (VCM) | 변동성완화장치 | Safeguard | HKEX ±10%(증권)/±5%(파생), SGX ±10% |
| 42 | Volatility Interruption (VI) | 변동성 완화장치 (VI) | Safeguard | KRX: dynamic 3%/6%, static 10% |
| 43 | Daily Price Limit | 가격제한폭 | Safeguard | KRX ±30%; TSE varies by price level |
| 44 | Limit Up-Limit Down (LULD) | 상·하한가 제한 (LULD) | Safeguard | US: dynamic bands by tier |
| 45 | Trading Halt | 매매거래 정지 | Safeguard | Regulatory/news-driven suspension |
| 46 | Pre-Trade Risk Control | 사전거래위험관리 | Safeguard | Max order size/value (Eurex T7, NYSE Pillar) |
| 47 | Kill Switch | 긴급주문취소 (킬 스위치) | Safeguard | Emergency bulk cancellation |
| 83 | Auction Collar | 경매 칼라 (가격 제한대) | Safeguard | NYSE: closing auction price collar |
| 94 | Special Quote (Tokubetsu Kehai) | 특별기배 (특별 참고호가) | Safeguard | TSE: indicative quote for imbalance |
| 110 | 9-Times Rule | 9배 가격편차 규칙 | Safeguard | HKEX: order price ≤9× nominal |
| 121 | Volatility Interruption (Eurex) | 변동성 중단 | Safeguard | Eurex: volatility auction trigger |
| 127 | Anomalous Order Threshold (AOT) | 이상주문임계값 (AOT) | Safeguard | ASX/ASIC: VWAP ±10% rejection |
| 128 | Extreme Trade Range (ETR) | 극단거래범위 (ETR) | Safeguard | ASX: 2-min pause |
| 129 | Meaningful Price Improvement | 의미 있는 가격 개선 | Regulation | ASIC: dark pool midpoint rule |

## H. Sessions (세션)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 48 | Opening Cross | 시초가 크로스 | Session | NASDAQ: 09:28-09:30 ET |
| 49 | Closing Cross | 종가 크로스 | Session | NASDAQ: 15:50-16:00 ET |
| 50 | Closing Auction Session (CAS) | 종가매매세션 (CAS) | Session | HKEX 16:00-16:10; TSE 15:25-15:30 |
| 51 | Pre-Opening Session | 장전 세션 (개장전 세션) | Session | Order acceptance before market open |
| 52 | After-Hours Trading | 시간외 거래 (장후 거래) | Session | Trading after regular session close |
| 53 | Block Trade | 대량매매 | Session | Large-size negotiated trade |
| 54 | Off-Book Trade | 장외 매매 (비주문장 매매) | Session | Negotiated trade reported to exchange |
| 87 | Competitive Block Trade | 경쟁대량매매 | Session | KRX: block at VWAP |
| 89 | Halt Cross | 정지 후 재개장 크로스 | Session | NASDAQ: reopening after halt |
| 90 | IPO Cross | IPO 크로스 | Session | NASDAQ: first-day trading |
| 135 | Trading-at-Close (TAC) | TAC (종가매매세션) | Session | SGX: 10-min post-close |

## I. Price & Structure (가격 · 구조)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 55 | Tick Size | 호가단위 (틱 사이즈) | Price | Minimum price increment |
| 56 | Lot Size | 매매단위 (거래 단위) | Price | Minimum tradable quantity |
| 57 | Best Bid and Offer (BBO) | 최우선 매수·매도 호가 | Price | Best prices on an exchange |
| 58 | National Best Bid and Offer (NBBO) | 전국 최우선 매수·매도호가 | Price | US: best across all venues |
| 59 | Order Book | 주문장 (호가창) | Structure | Buy/sell queue by price level |
| 60 | Order Imbalance | 주문 불균형 | Structure | Difference buy vs sell interest |
| 82 | Net Order Imbalance Indicator (NOII) | 순 주문불균형 지표 (NOII) | Structure | NASDAQ: pre-cross imbalance data |
| 109 | Indicative Equilibrium Price (IEP) | 참고균형가격 (IEP) | Price | HKEX: auction matching price |
| 115 | Board Lot | 보드롯 (매매단위) | Price | HKEX: varies 10–100,000 shares |

## J. Protocols & Systems (프로토콜 · 시스템)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 61 | OUCH Protocol | OUCH 프로토콜 | Protocol | NASDAQ/ASX: low-latency order entry |
| 62 | ITCH Protocol | ITCH 프로토콜 | Protocol | NASDAQ/SGX: outbound market data |
| 63 | FIX Protocol | FIX 프로토콜 | Protocol | Industry-standard messaging |
| 117 | ETI (Enhanced Trading Interface) | ETI (향상 매매 인터페이스) | Protocol | Eurex T7: session-based TCP/IP |
| 118 | EOBI (Enhanced Order Book Interface) | EOBI (향상 주문장 인터페이스) | Protocol | Eurex T7: low-latency market data |
| 133 | GLIMPSE | GLIMPSE (주문장 스냅샷) | Protocol | SGX Titan: point-to-point snapshot |
| 97 | arrowhead 4.0 | 애로헤드 4.0 | System | TSE: 4th-gen equity trading (2024.11) |
| 101 | Millennium Exchange | 밀레니엄 익스체인지 | System | LSE: trading platform since 2011 |
| 111 | Orion Trading Platform (OTP) | 오리온 매매 플랫폼 (OTP) | System | HKEX: OTP-C/OTP-D |
| 116 | T7 Trading System | T7 매매시스템 | System | Deutsche Börse: Eurex + Xetra |
| 131 | QUEST | QUEST (전자매매플랫폼) | System | SGX: securities electronic platform |
| 132 | Titan | Titan (타이탄) | System | SGX: derivatives platform |
| 139 | Colo 2.0 | Colo 2.0 (코로케이션 2.0) | Infrastructure | Eurex: upgraded co-location (2025) |

## K. Settlement & Programs (결제 · 프로그램)

| # | English Term | Korean Official Term | Category | Notes |
|---|---|---|---|---|
| 64 | Clearing | 청산 | Settlement | Post-trade netting and confirmation |
| 65 | Central Counterparty (CCP) | 중앙청산소 (CCP) | Settlement | Guarantees settlement |
| 130 | CHESS | CHESS (전자등록결제시스템) | Settlement | ASX: Clearing House Electronic Sub-register |
| 112 | Stock Connect | 스톡 커넥트 (후강통/선강통) | Program | HKEX-SSE/SZSE cross-border channel |

---

*140 terms | Version 2.0 (Unified) | Created: 2026-03-27 | Merged: Session 4*
*Conflicts resolved: #25 D-Order updated with Batch 1 description; #27/#28 updated with Chinese terms; #7 updated with SGX note; duplicates #98/#125/#105/#106/#107/#108/#120/#137 merged into originals*
