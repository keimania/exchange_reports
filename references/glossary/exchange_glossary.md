# 거래소 주요 용어 사전 (Exchange Glossary)

> 글로벌 주요 거래소에서 사용되는 핵심 용어를 정리한 문서입니다.
> 약어는 풀어서 표기하고, 거래소별 기준이 다른 경우 이를 병기합니다.
> 최종 업데이트: 2026-03-27

---

## 목차

1. [매매 메커니즘 (Trading Mechanisms)](#1-매매-메커니즘-trading-mechanisms)
2. [주문유형 (Order Types)](#2-주문유형-order-types)
3. [시장 구조 및 참여자 (Market Structure & Participants)](#3-시장-구조-및-참여자-market-structure--participants)
4. [가격 및 호가 (Price & Quotation)](#4-가격-및-호가-price--quotation)
5. [변동성 통제 및 안전장치 (Volatility Controls & Safeguards)](#5-변동성-통제-및-안전장치-volatility-controls--safeguards)
6. [청산 및 결제 (Clearing & Settlement)](#6-청산-및-결제-clearing--settlement)
7. [시장 데이터 및 프로토콜 (Market Data & Protocols)](#7-시장-데이터-및-프로토콜-market-data--protocols)
8. [매매시스템 (Trading Systems)](#8-매매시스템-trading-systems)
9. [규제 및 감독 (Regulation & Supervision)](#9-규제-및-감독-regulation--supervision)
10. [지수 및 상품 (Indices & Products)](#10-지수-및-상품-indices--products)
11. [기술 및 인프라 (Technology & Infrastructure)](#11-기술-및-인프라-technology--infrastructure)
12. [기타 (Others)](#12-기타-others)

---

## 1. 매매 메커니즘 (Trading Mechanisms)

### 1-1. Continuous Trading (연속매매)
정규 거래시간 중 매수·매도 주문이 실시간으로 대조되어 체결되는 매매방식. 가격우선·시간우선 원칙에 따라 즉시 체결 가능한 주문이 순차적으로 매칭된다.
- **KRX**: 접속매매 (09:00~15:20)
- **TSE/JPX**: 자라바(ザラバ, Zaraba) — 일본어로 "잡다한 장"이라는 뜻. 장중 최저 매도호가와 최고 매수호가가 일치할 때 체결
- **NYSE**: 정규시장 (09:30~16:00 ET), DMM이 유동성을 보충
- **LSE**: SETS에서의 연속 주문장 매매 (08:00~16:30 London time)
- **HKEX**: 연속매매세션 (09:30~12:00, 13:00~16:00 HKT)

### 1-2. Call Auction (단일가매매, 동시호가)
일정 시간 동안 주문을 접수한 뒤, 하나의 가격으로 일괄 체결하는 매매방식. 시가·종가 결정 등에 사용된다.
- **KRX**: 동시호가 — 장전(08:30~09:00), 장후(15:20~15:30) 동시호가로 시가/종가 결정
- **TSE/JPX**: 이타요세(板寄せ, Itayose) — 일본어로 "호가판을 모은다"는 뜻. 거래량 최대화·미체결 잔량 최소화 원칙으로 단일가 결정
- **NYSE**: Opening/Closing Auction — DMM(Designated Market Maker)이 관리
- **NASDAQ**: Opening Cross / Closing Cross
- **LSE**: Opening/Closing Auction (SETS), 하루 4회 정기경매 (SETSqx)
- **HKEX**: 개장전 세션(Pre-opening Session) 및 종가매매세션(CAS, Closing Auction Session)
- **Eurex**: Opening/Closing Auction (T7 시스템)
- **ASX**: Opening/Closing Auction
- **SGX**: Pre-Open Routine

### 1-3. Opening Auction (시초가 경매)
장 시작 전 주문을 모아 시가(opening price)를 결정하는 단일가매매.
- **KRX**: 장전 동시호가 (08:30~09:00)
- **NYSE**: Opening Auction — DMM이 시가 결정 관리
- **NASDAQ**: Opening Cross (09:28~09:30 ET에 주문 불균형 정보 배포)
- **TSE/JPX**: 전장 이타요세 (08:00~09:00 JST)

### 1-4. Closing Auction (종가 경매)
장 마감 시 주문을 모아 종가(closing price)를 결정하는 단일가매매.
- **KRX**: 장후 동시호가 (15:20~15:30)
- **NYSE**: Closing Auction — DMM이 종가 결정 관리
- **NASDAQ**: Closing Cross (15:50~16:00 ET에 주문 불균형 정보 배포)
- **TSE/JPX**: 후장 이타요세; arrowhead 4.0(2024.11)부터 종가매매세션(Closing Auction Session) 도입
- **HKEX**: CAS (Closing Auction Session, 16:00~16:10 HKT)
- **ASX**: Closing Auction (16:00~16:10 AEST)

### 1-5. Auction Uncrossing (경매 체결)
단일가매매 기간 종료 시 축적된 주문을 단일 가격으로 일괄 체결하는 행위.
- **LSE/SETSqx**: 하루 4회 정기 경매 체결 시점

### 1-6. Pre-Open (장전 세션)
정규 매매 시작 전 주문을 접수하되, 체결은 이루어지지 않는 시간대.
- **KRX**: 08:00~08:30 (주문 접수만), 08:30~09:00 (동시호가)
- **NYSE**: Pre-Opening (06:30~09:30 ET, 주문 접수)
- **ASX**: 07:00~10:00 AEST
- **SGX**: 08:30~09:00 SGT

### 1-7. Post-Close (장후 세션)
정규 매매 종료 후의 추가 매매 시간대.
- **KRX**: 장후 시간외매매 (15:40~16:00, 종가 단일가)
- **NYSE**: After-Hours Trading (16:00~20:00 ET, ECN 경유)

### 1-8. Dark Pool (다크풀)
공개 주문장(order book)에 주문이 표시되지 않는 비공개 매매 장소.
- **ASX**: Centre Point — 호주 최대 다크풀. 익명 주문, 당일 주문 전용, 4자리 소수점 off-tick 체결 허용
- **미국**: ATS(Alternative Trading System) 형태로 다수 운영

### 1-9. Crossing (크로싱)
동일 브로커 내 또는 지정된 시점에 매수·매도 주문을 맞대어 체결하는 방식.
- **ASX Centre Point Crossing**: 크로스 개시 후 최대 30초간 활성, CXXT 코드로 보고
- **NASDAQ Opening/Closing Cross**: 특정 시간대에 주문을 모아 단일가로 체결

### 1-10. Block Trade (대량매매)
일정 수량 이상의 대규모 거래를 일반 주문장 외에서 별도로 체결하는 매매.
- **KRX**: 대량매매 (시간외 대량매매)
- **Eurex**: Block Trade Facility
- **SGX**: Negotiated Large Trade (NLT)

---

## 2. 주문유형 (Order Types)

### 2-1. Market Order (시장가 주문)
가격을 지정하지 않고 현재 최우선 호가로 즉시 체결을 요청하는 주문.
- **KRX**: 시장가 주문 — 최우선 호가에 즉시 체결, 미체결분은 최우선 호가로 자동 전환
- **NYSE/NASDAQ**: Market Order
- **Eurex**: Market Order
- **SGX**: MKT (Fill and Kill) — 미체결분 즉시 취소

### 2-2. Limit Order (지정가 주문)
체결 희망 가격을 명시하여 제출하는 주문. 지정 가격 이상(매도) 또는 이하(매수)에서만 체결.
- 전 거래소 공통으로 사용

### 2-3. Stop Order / Stop-Loss Order (조건부 주문 / 손절매 주문)
지정한 트리거 가격에 도달하면 시장가 주문으로 전환되는 주문.
- **NYSE**: Stop Order
- **Eurex**: Stop Order (Stop-Loss) — 트리거 가격 도달 시 시장가로 전환
- **SGX**: STP (Fill and Kill) — Stop 트리거 후 시장가, 미체결분 취소

### 2-4. Stop-Limit Order (조건부 지정가 주문)
트리거 가격 도달 시 지정가 주문으로 전환되는 주문.
- **SGX**: STP Limit — Stop 트리거 후 지정가
- **NYSE**: Stop-Limit Order

### 2-5. Iceberg Order (빙산 주문)
대량 주문의 전체 수량 중 일부만 주문장에 공개하고, 공개분이 체결되면 다음 수량을 자동으로 노출하는 주문.
- **KRX**: 미지원 (유사하게 분할 주문으로 대응)
- **NYSE**: Reserve Order (Pillar 시스템)
- **LSE/SETS**: Iceberg Order
- **Eurex**: Iceberg Order — 일부 수량만 공개, 체결 시 다음 수량 노출
- **ASX**: Iceberg Order — 대량 주문을 소량 자식 주문으로 분할 노출, 가격/시간 우선 적용

### 2-6. Fill-or-Kill (FOK, 전량즉시체결 주문)
주문 전체 수량이 즉시 체결 가능하지 않으면 전량 취소하는 주문.
- **ASX**: Fill-or-Kill (FOK)
- **Eurex**: Fill-or-Kill

### 2-7. Immediate-or-Cancel (IOC, 즉시체결잔량취소 주문)
체결 가능한 수량만 즉시 체결하고, 미체결 잔량은 즉시 취소하는 주문.
- **KRX**: IOC (즉시체결·잔량취소 조건)
- **NYSE**: IOC Order
- **NASDAQ**: IOC

### 2-8. Fill-and-Kill (FAK)
IOC와 동일한 개념. 체결 가능한 만큼 체결 후 잔량 취소.
- **SGX**: MKT (Fill and Kill), STP (Fill and Kill)

### 2-9. Good-for-Day (GFD, 당일유효 주문)
해당 거래일에만 유효하고, 장 마감 시 자동 취소되는 주문.
- **ASX**: Good for Day (GFD)
- 대부분의 거래소에서 기본(default) 유효기간

### 2-10. Good-Till-Cancel (GTC, 취소시까지유효 주문)
투자자가 직접 취소하거나 체결될 때까지 유효한 주문.
- **ASX**: Good-Till-Cancel (GTC)
- **KRX**: 미지원 (당일 유효가 기본)

### 2-11. Good-Till-Date (GTD, 지정일까지유효 주문)
지정한 날짜까지 유효한 주문.
- **Eurex**: Good-Till-Date
- **LSE**: Good-Till-Date

### 2-12. At Best Order (최우선지정가 주문)
현재 최우선 호가를 가격으로 자동 지정하는 주문.
- **KRX**: 최우선지정가 주문
- **LSE**: At Best Order

### 2-13. OCO — One-Cancels-the-Other (양자택일 주문)
지정가 주문과 Stop 주문을 하나의 Order ID로 묶어, 하나가 체결되면 다른 하나가 자동 취소되는 주문.
- **Eurex**: OCO — 지정가 + Stop 결합, 하나의 Order ID로 관리

### 2-14. Pegged Order (추종 주문)
최우선 매수/매도 호가 또는 중간가에 자동으로 가격이 조정되는 주문.
- **NYSE**: Pegged Order (Primary Peg, Midpoint Peg 등)
- **NASDAQ**: Pegged Order

### 2-15. MOO — Market-on-Open (시초가 시장가 주문)
Opening Auction에서만 체결되는 시장가 주문.
- **NYSE**: MOO
- **NASDAQ**: MOO

### 2-16. MOC — Market-on-Close (종가 시장가 주문)
Closing Auction에서만 체결되는 시장가 주문.
- **NYSE**: MOC
- **NASDAQ**: MOC

### 2-17. LOO — Limit-on-Open (시초가 지정가 주문)
Opening Auction에서만 체결되는 지정가 주문.
- **NYSE**: LOO
- **NASDAQ**: LOO

### 2-18. LOC — Limit-on-Close (종가 지정가 주문)
Closing Auction에서만 체결되는 지정가 주문.
- **NYSE**: LOC
- **NASDAQ**: LOC

### 2-19. Named Order (기명 주문)
주문 제출 시 참가자 이름이 공개되는 주문.
- **LSE/SETSqx**: Named Order — 비익명(non-anonymous) 지정가 주문

### 2-20. Hidden Order (숨김 주문)
주문장에 전혀 표시되지 않는 주문.
- **NASDAQ**: Non-Displayed Order

### 2-21. Midpoint Order (중간가 주문)
최우선 매수호가와 최우선 매도호가의 중간가격으로 체결을 요청하는 주문.
- **NYSE**: Midpoint Liquidity Order
- **ASX Centre Point**: 중간가 체결

### 2-22. Trailing Stop Order (추적 손절매 주문)
가격이 유리하게 움직이면 Stop 가격도 자동으로 조정되는 주문.
- **NYSE**: Trailing Stop

### 2-23. Day Order (당일 주문)
해당 거래일에만 유효한 주문. GFD와 동일.
- **ASX Centre Point**: Day order 전용

---

## 3. 시장 구조 및 참여자 (Market Structure & Participants)

### 3-1. DMM — Designated Market Maker (지정 시장조성자)
특정 종목에 대해 지속적으로 매수·매도 호가를 제시하며 유동성을 공급할 의무가 있는 시장 참여자. NYSE 고유의 제도.
- **NYSE**: DMM — 시가/종가 결정(Opening/Closing Auction) 관리, 유동성 공급 의무

### 3-2. Market Maker (시장조성자)
매수·매도 양방향 호가를 지속적으로 제시하여 시장에 유동성을 제공하는 참여자.
- **KRX**: 유동성공급자(LP, Liquidity Provider) — ETF, ELW 등에서 활동
- **LSE**: Market Maker — SEAQ에서 호가 기반 거래, SETSqx에서 유동성 보충
- **Eurex**: Market Maker — T7 시스템에서 의무 호가 제시

### 3-3. LP — Liquidity Provider (유동성공급자)
시장조성자와 유사한 역할. 거래소와 계약하여 특정 종목의 유동성을 공급하는 참여자.
- **KRX**: LP — ETF, ETN 등의 유동성 공급
- **Eurex**: Liquidity Provider

### 3-4. SLP — Supplemental Liquidity Provider (보충적 유동성공급자)
- **NYSE**: SLP — DMM 외에 추가 유동성을 공급하는 전자 시장참여자

### 3-5. AP — Authorized Participant (지정참가회사)
ETF의 설정(creation) 및 환매(redemption) 권한을 가진 금융기관.
- **KRX**: 지정참가회사 (AP)
- 글로벌 공통 개념

### 3-6. Broker-Dealer (브로커-딜러)
고객 주문을 대리 체결(broker)하거나 자기 계정으로 매매(dealer)하는 금융회사.

### 3-7. Clearing Member (청산회원)
거래소 또는 청산기관에서 청산·결제 자격을 보유한 회원사.
- **KRX**: 청산적격회원
- **Eurex**: Clearing Member (General/Direct)
- **HKEX**: CCASS Participant

### 3-8. Exchange Participant (거래참가자)
거래소에 직접 접속하여 매매할 수 있는 자격을 보유한 참여자.
- **HKEX**: Exchange Participant (EP)
- **SGX**: Trading Member

### 3-9. Order Book (주문장, 호가창)
매수·매도 주문이 가격-시간 우선순위로 정렬되어 표시되는 전자 장부.
- **KRX**: 호가창
- **LSE/SETS**: Central Order Book

### 3-10. CLOB — Central Limit Order Book (중앙지정가주문장)
모든 지정가 주문이 가격-시간 우선순위로 중앙에서 관리되는 주문장.
- 대부분의 전자거래소에서 사용하는 핵심 구조

### 3-11. Quote-Driven Market (호가 기반 시장)
시장조성자의 매수·매도 호가에 의해서만 거래가 이루어지는 시장.
- **LSE/SEAQ**: 호가 기반 시스템 — 시장조성자 호가에 의해서만 거래

### 3-12. Order-Driven Market (주문 기반 시장)
투자자의 주문이 직접 대조되어 체결되는 시장.
- **KRX**, **TSE/JPX**, **NASDAQ**: 주문 기반 시장

### 3-13. Hybrid Market (혼합형 시장)
주문 기반과 호가 기반이 결합된 시장.
- **NYSE**: Hybrid Market — CLOB + DMM
- **LSE/SETSqx**: SETS + Quote 혼합 시스템

---

## 4. 가격 및 호가 (Price & Quotation)

### 4-1. Bid (매수호가)
매수자가 제시하는 매수 희망 가격.

### 4-2. Ask / Offer (매도호가)
매도자가 제시하는 매도 희망 가격.

### 4-3. Spread (스프레드, 호가 차이)
최우선 매수호가(best bid)와 최우선 매도호가(best ask) 간의 가격 차이.

### 4-4. Tick Size (호가 단위)
주문 가격의 최소 변동 단위.
- **KRX**: 주가 구간별 차등 호가단위 (예: 1,000원 미만 → 1원, 5만원 이상 → 50원 등)
- **TSE/JPX**: 주가 구간별 차등 (TOPIX100 종목은 별도 호가단위)
- **NYSE/NASDAQ**: 주로 $0.01 (1센트)
- **HKEX**: 주가 구간별 차등 호가단위

### 4-5. Lot Size (매매 단위)
주문 가능한 최소 주식 수량 단위.
- **KRX**: 1주
- **TSE/JPX**: 100주 (2018년 통일)
- **HKEX**: 종목별 상이 (1 Board Lot = 종목마다 다름)

### 4-6. NBBO — National Best Bid and Offer (전국 최우선 호가)
미국 시장에서 모든 거래소와 ATS를 통합하여 산출한 최우선 매수/매도 호가.
- **NYSE/NASDAQ**: Reg NMS에 의해 NBBO 보호 의무

### 4-7. BBO — Best Bid and Offer (최우선 호가)
특정 거래소 내에서의 최우선 매수/매도 호가.

### 4-8. Reference Price (기준가격)
각종 제도(가격제한폭, 서킷브레이커 등)의 기준이 되는 가격. 통상 전일 종가.
- **KRX**: 기준가격 — 전일 종가 기준
- **HKEX VCM**: 5분 모니터링 기간의 기준가

### 4-9. Theoretical Opening Price (이론적 시초가)
단일가매매 기간 중 실시간으로 산출되는 예상 체결가격.
- **KRX**: 예상체결가

### 4-10. VWAP — Volume-Weighted Average Price (거래량가중평균가격)
일정 기간의 체결 가격을 거래량으로 가중평균한 가격. 기관투자자의 주요 벤치마크.

### 4-11. TWAP — Time-Weighted Average Price (시간가중평균가격)
일정 기간의 체결 가격을 시간 균등으로 평균한 가격.

### 4-12. Last Sale Price (최종 체결가)
가장 최근에 체결된 거래의 가격.

### 4-13. Off-Tick (호가단위 외 체결)
정규 호가단위(tick size)가 아닌 가격으로 체결되는 것.
- **ASX Centre Point**: 4자리 소수점 off-tick 체결 허용

---

## 5. 변동성 통제 및 안전장치 (Volatility Controls & Safeguards)

### 5-1. Circuit Breaker (서킷브레이커)
시장 전체의 급격한 가격 변동 시 매매를 일시 중단하는 안전장치.
- **KRX**: KOSPI 지수가 전일 대비 8%(1단계)/15%(2단계)/20%(3단계) 이상 하락 시 발동. 각 단계별 20분간 매매 정지
- **미국(NYSE/NASDAQ)**: S&P 500 기준 Level 1(7%)/Level 2(13%)/Level 3(20%) 하락 시 발동

### 5-2. LULD — Limit Up-Limit Down (상한가-하한가 제도)
개별 종목의 급격한 가격 변동을 방지하기 위해 일정 범위를 벗어나는 거래를 제한하는 미국의 제도.
- **미국(NYSE/NASDAQ)**: 직전 5분 평균가 기준 ±5%(Tier 1, S&P500/Russell1000) 또는 ±10%(Tier 2, 기타) 가격 밴드. 밴드 도달 시 15초 거래 일시정지(Trading Pause)
- **KRX**: 별도의 LULD 제도는 없으나, 가격제한폭(±30%)과 VI(변동성완화장치)가 유사 기능 수행

### 5-3. Price Limit (가격제한폭)
하루 동안 주가가 움직일 수 있는 최대 범위.
- **KRX**: KOSPI/KOSDAQ 주식 ±30% (기준가 대비)
- **TSE/JPX**: 주가 구간별 차등 가격제한폭 (예: 100엔 미만 → ±30엔, 1000엔 이상 → ±300엔 등)
- **NYSE/NASDAQ**: 개별 종목 가격제한폭 없음 (LULD로 대체)
- **HKEX**: 개별 종목 가격제한폭 없음 (VCM으로 대체)

### 5-4. VI — Volatility Interruption (변동성완화장치)
개별 종목의 급격한 가격 변동 시 2분간 단일가매매로 전환하는 KRX의 안전장치.
- **KRX**: 정적VI — 전일 종가 대비 ±10% 이탈 시 발동 / 동적VI — 직전 체결가 대비 ±3%~6% 이탈 시 발동. 2분간 단일가매매 후 정규매매 복귀

### 5-5. VCM — Volatility Control Mechanism (변동성 통제 메커니즘)
HKEX의 변동성 안전장치. 기준가 대비 일정 비율 이탈 시 5분간 냉각기간을 부여.
- **HKEX**: 5분 모니터링 기간 중 기준가 대비 ±10%(증권)/±5%(파생) 이탈 시 5분 냉각기간(cooling-off period) 발동. 냉각기간 중에는 밴드 내에서만 거래 가능

### 5-6. Dynamic Price Band (동적 가격밴드)
직전 체결가 또는 일정 기간 평균가 기준으로 설정되는 실시간 가격 밴드.
- **Eurex T7**: 사전거래 가격 밴드(Pre-trade Price Band)
- **KRX**: 동적VI의 가격밴드 (직전 체결가 기준)

### 5-7. Trading Halt (매매 거래정지)
특정 종목 또는 시장 전체의 매매를 일시적으로 정지하는 조치. 공시, 감독기관 명령 등에 의해 발동.
- 전 거래소 공통

### 5-8. Cooling-Off Period (냉각기간)
변동성 안전장치 발동 후 매매가 제한되는 시간.
- **HKEX VCM**: 5분 냉각기간

### 5-9. Pre-trade Risk Controls (사전거래통제)
주문 제출 전에 가격, 수량, 금액 등을 검증하여 비정상 주문을 차단하는 시스템.
- **Eurex T7**: 최대 주문가치(Max Order Value), 최대 주문수량(Max Order Quantity) 제한
- **KRX**: 주문 한도 관리 (가격/수량 오류 방지)

---

## 6. 청산 및 결제 (Clearing & Settlement)

### 6-1. CCP — Central Counterparty (중앙청산소)
모든 거래의 상대방이 되어 결제 이행을 보증하는 기관.
- **KRX**: 한국거래소 청산부문 (KRX가 CCP 역할 수행)
- **HKEX**: HKSCC (Hong Kong Securities Clearing Company)
- **Eurex**: Eurex Clearing
- **ASX**: ASX Clear

### 6-2. Settlement Cycle (결제주기)
매매 체결일(T)로부터 실제 결제(대금 수수 및 증권 인도)까지의 기간.
- **KRX**: T+2 (주식)
- **NYSE/NASDAQ**: T+1 (2024년 5월부터 T+2 → T+1 단축)
- **TSE/JPX**: T+2
- **HKEX**: T+2
- **LSE**: T+1 (2027년 전환 예정)

### 6-3. DVP — Delivery Versus Payment (증권인도 대 대금결제)
증권 인도와 대금 결제가 동시에 이루어지는 결제 방식. 결제 위험 최소화.

### 6-4. Netting (차감결제)
매수·매도 거래를 상계하여 순(net) 차액만 결제하는 방식.
- **KRX**: 차감결제 (한국예탁결제원 경유)

### 6-5. Novation (채무인수)
CCP가 매매 양 당사자 사이에 개입하여 각각의 거래상대방이 되는 것.

### 6-6. Margin (증거금)
파생상품 거래 시 이행을 보증하기 위해 예치하는 금액.
- **KRX**: 위탁증거금, 유지증거금
- **Eurex**: Initial Margin, Variation Margin
- **HKEX**: Margin (SPAN 방식)

### 6-7. SPAN — Standard Portfolio Analysis of Risk
CME가 개발한 포트폴리오 기반 위험 증거금 산출 모델.
- **KRX**, **SGX**, **HKEX**: SPAN 방식 증거금 산출

---

## 7. 시장 데이터 및 프로토콜 (Market Data & Protocols)

### 7-1. FIX — Financial Information eXchange (금융정보교환 프로토콜)
증권 거래 관련 전자 통신을 위한 국제 표준 메시징 프로토콜.
- **NYSE Pillar**: FIX 프로토콜 지원
- **HKEX OCG**: FIX Drop Copy 인터페이스
- **SGX Titan OTC**: FIX API (v1.5.5)

### 7-2. ITCH (시장 데이터 피드 프로토콜)
NASDAQ이 개발한 아웃바운드 전용 시장 데이터 피드 프로토콜. 주문진입은 미지원.
- **NASDAQ**: TotalView-ITCH — 전 호가 깊이(full depth) 시장 데이터
- **SGX Titan**: ITCH — 아웃바운드 시장데이터 피드

### 7-3. OUCH (주문진입 프로토콜)
NASDAQ이 개발한 저수준 고성능 주문진입 전용 프로토콜. ITCH(아웃바운드 전용)와 상호보완.
- **NASDAQ**: OUCH 5.0 (최신), OUCH 4.2 (레거시)

### 7-4. GLIMPSE (주문장 스냅샷 프로토콜)
주문장의 현재 상태를 point-to-point 방식으로 제공하는 프로토콜.
- **SGX Titan**: GLIMPSE — 주문장 현재 상태 스냅샷

### 7-5. Binary Protocol (바이너리 프로토콜)
텍스트 기반이 아닌 이진(binary) 형식으로 데이터를 전송하는 프로토콜. 낮은 지연시간 달성에 유리.
- **NYSE Pillar**: Binary 프로토콜
- **HKEX OCG**: Binary Trading Interface
- **HKEX OMD**: Binary Interface (시장 데이터)
- **Eurex T7 ETI**: Binary 기반

### 7-6. ETI — Enhanced Trading Interface (향상된 매매 인터페이스)
Eurex T7 시스템의 고성능 매매 접속 인터페이스. 세션 기반 TCP/IP 접속.
- **Eurex**: ETI — Cash(현물) 및 Derivatives(파생) 지원

### 7-7. Market Data Feed (시장 데이터 피드)
실시간 시세, 호가, 체결 정보를 배포하는 데이터 스트림.
- **NASDAQ TotalView**: 전 호가 깊이 데이터
- **HKEX OMD-C**: 증권시장 데이터 / **OMD-D**: 파생상품 시장 데이터
- **KRX**: 시세 정보 (KOSCOM 경유 배포)

### 7-8. Level 1 Data (1단계 시세)
최우선 매수/매도 호가(BBO) 및 최종 체결가 정보.

### 7-9. Level 2 Data (2단계 시세, 호가 깊이)
복수 호가 단계의 매수/매도 주문 수량 정보 (Market Depth).

### 7-10. Drop Copy (체결 사본)
체결·주문 상태 정보의 실시간 사본을 별도 채널로 수신하는 기능. 위험관리 및 컴플라이언스 용도.
- **HKEX OCG**: FIX Drop Copy Interface

### 7-11. Multicast (멀티캐스트)
하나의 송신자가 다수의 수신자에게 동시에 데이터를 전송하는 네트워크 방식. 시장 데이터 배포에 주로 사용.

### 7-12. Co-location (코로케이션)
거래소 매칭엔진과 물리적으로 가까운 곳에 서버를 설치하여 지연시간을 최소화하는 서비스.
- **KRX**: 코로케이션 서비스 (KOSCOM 데이터센터)
- **NYSE**: Mahwah 데이터센터 코로케이션
- **TSE/JPX**: 코로케이션 서비스

---

## 8. 매매시스템 (Trading Systems)

### 8-1. EXTURE+ (엑스처 플러스)
KRX의 차세대 매매시스템. KOSCOM이 운영.
- **KRX**: 2014년 가동. 기술 사양서는 회원사 대상 비공개

### 8-2. Pillar (필라)
NYSE 그룹의 차세대 통합 매매 플랫폼.
- **NYSE**: FIX 및 Binary 프로토콜 지원. NYSE, NYSE Arca, NYSE American 등 통합

### 8-3. arrowhead (애로우헤드)
TSE/JPX의 현물 주식 매매시스템.
- **TSE/JPX**: 2010년 초대 가동. arrowhead 4.0 (2024.11) — 4세대 시스템, 매매시간 연장, 종가매매세션 도입, 글로벌 최고 수준 저지연·고신뢰

### 8-4. T7
Deutsche Börse 그룹의 매매 플랫폼. Eurex와 Xetra가 공용.
- **Eurex**: T7 — ETI(세션 기반 TCP/IP), Application Gateway 경유 접속
- **Xetra**: T7 (현물 매매)

### 8-5. SETS — Stock Exchange Electronic Trading Service (전자주문장 매매 서비스)
LSE의 주요 전자 주문장 매매시스템. 1997년 도입.
- **LSE**: SETS — FTSE 100, FTSE 250 등 주요 유동성 종목 거래. 주문유형: At Best, Limit, Stop, Iceberg 등

### 8-6. SETSqx
LSE의 중간 유동성 종목용 혼합형 매매시스템. SETS + Quote 결합.
- **LSE**: SETSqx — 2007년 도입. 시장조성자 상시 유동성 제공 + 하루 4회 정기 경매 체결. Named Order(비익명 지정가) 지원

### 8-7. SEAQ — Stock Exchange Automated Quotation (전자호가 시스템)
LSE의 저유동성 종목용 호가 기반(quote-driven) 매매시스템.
- **LSE**: SEAQ — 시장조성자 호가에 의해서만 거래

### 8-8. OTP — Orion Trading Platform (오리온 매매 플랫폼)
HKEX의 매매 플랫폼.
- **HKEX**: OTP-C (증권시장, Securities Market) / OTP-D (파생상품시장, Derivatives Market)

### 8-9. OCG — Orion Central Gateway (오리온 중앙 게이트웨이)
HKEX OTP의 거래 접속 게이트웨이.
- **HKEX**: OCG — Binary Trading Interface 및 FIX Drop Copy Interface 지원

### 8-10. OMD — Orion Market Data (오리온 시장 데이터 플랫폼)
HKEX의 시장 데이터 배포 플랫폼.
- **HKEX**: OMD-C (증권시장 데이터) / OMD-D (파생상품 데이터)

### 8-11. Titan (타이탄)
SGX의 파생상품 전용 매매/청산 플랫폼.
- **SGX**: Titan — ITCH(시장데이터), GLIMPSE(스냅샷), QUEST(전자매매) 지원

### 8-12. QUEST
SGX의 전자 매매 플랫폼. 회원사 OMS를 통해 접속.
- **SGX**: QUEST

### 8-13. ASX Trade
ASX의 현물 매매 플랫폼. Lit Markets, Centre Point, Auctions 통합.
- **ASX**: ASX Trade

### 8-14. INET
NASDAQ의 매매 엔진 기술. Nordic(북유럽) 거래소에도 적용.
- **NASDAQ Nordic**: INET — Nordic 프로토콜 사양 모음

---

## 9. 규제 및 감독 (Regulation & Supervision)

### 9-1. SEC — Securities and Exchange Commission (미국 증권거래위원회)
미국 연방 증권시장 감독기관.

### 9-2. FINRA — Financial Industry Regulatory Authority (금융산업규제기관)
미국 브로커-딜러에 대한 자율규제기관. NYSE의 자율규제 기능이 이관됨.

### 9-3. Reg NMS — Regulation National Market System (전국시장시스템 규정)
미국 주식시장의 공정하고 효율적인 가격 형성을 위한 SEC 규정.
- 핵심: Order Protection Rule(최우선 호가 보호), Access Rule(시장 접근), Sub-Penny Rule

### 9-4. MiFID II — Markets in Financial Instruments Directive II (금융상품시장지침 II)
EU의 금융상품 거래 관련 포괄적 규제 프레임워크.
- 투명성 요구, 거래 보고 의무, 다크풀 거래량 제한 등

### 9-5. SFC — Securities and Futures Commission (증권선물위원회)
홍콩의 증권·선물시장 감독기관.
- **HKEX**: SFC 감독 하에 운영

### 9-6. FSA/JFSA — Financial Services Agency (금융청)
일본의 금융 감독기관.
- **TSE/JPX**: JFSA 감독 하에 운영

### 9-7. FCA — Financial Conduct Authority (금융행위감독청)
영국의 금융시장 행위 감독기관.
- **LSE**: FCA 감독 하에 운영

### 9-8. ASIC — Australian Securities and Investments Commission (호주증권투자위원회)
호주의 증권·투자시장 감독기관.
- **ASX**: ASIC 감독 하에 운영

### 9-9. MAS — Monetary Authority of Singapore (싱가포르 통화감독청)
싱가포르의 중앙은행 겸 금융 감독기관.
- **SGX**: MAS 감독 하에 운영

### 9-10. BaFin — Bundesanstalt für Finanzdienstleistungsaufsicht (독일 연방금융감독청)
독일의 금융 감독기관.
- **Eurex**: BaFin 감독 하에 운영

### 9-11. FSC/FSS — Financial Services Commission / Financial Supervisory Service (금융위원회/금융감독원)
한국의 금융시장 정책 수립(FSC) 및 감독·검사(FSS) 기관.
- **KRX**: FSC/FSS 감독 하에 운영

### 9-12. IOSCO — International Organization of Securities Commissions (국제증권감독기구)
세계 각국 증권감독기관의 국제 협의체. 증권규제 표준 제정.

### 9-13. SRO — Self-Regulatory Organization (자율규제기관)
거래소나 업계 단체가 자체적으로 회원의 행위를 규제하는 기관.
- **KRX**: 자율규제 기능 수행
- **FINRA**: 미국 최대 SRO

### 9-14. Market Surveillance (시장감시)
불공정거래(시세조종, 내부자거래 등)를 탐지·감시하는 활동.
- **KRX**: 시장감시위원회
- **SGX**: Practice Note 7B (이상거래 모니터링), Practice Note 13.8.1 (시장조작)

### 9-15. Disclosure (공시)
기업이 투자자에게 경영 정보를 공개하는 행위.
- **KRX**: KIND (KRX 전자공시시스템)
- **미국**: SEC EDGAR

---

## 10. 지수 및 상품 (Indices & Products)

### 10-1. KOSPI — Korea Composite Stock Price Index (한국종합주가지수)
KRX 유가증권시장(KOSPI시장) 전체 상장종목의 시가총액 기준 지수.

### 10-2. KOSDAQ — Korea Securities Dealers Automated Quotations
KRX 코스닥시장의 기술주/성장주 중심 시장 및 지수.

### 10-3. KONEX — Korea New Exchange
KRX 코넥스시장. 중소·벤처기업 전용 시장.

### 10-4. ETF — Exchange-Traded Fund (상장지수펀드)
특정 지수를 추종하며 거래소에서 주식처럼 매매되는 펀드.

### 10-5. ETN — Exchange-Traded Note (상장지수증권)
발행사의 신용에 기반하여 특정 지수 수익률을 보장하는 파생결합증권.

### 10-6. ELW — Equity-Linked Warrant (주식연계증권)
특정 기초자산의 가격 변동에 연계된 수익을 제공하는 파생증권.
- **KRX**: ELW 시장 운영

### 10-7. SPAC — Special Purpose Acquisition Company (기업인수목적회사)
상장을 통해 자금을 조달한 후 비상장기업을 인수·합병하는 것을 목적으로 하는 페이퍼 컴퍼니.

### 10-8. REIT — Real Estate Investment Trust (부동산투자신탁)
부동산에 투자하여 수익을 투자자에게 배분하는 회사형 또는 신탁형 상품.

### 10-9. Futures (선물)
미래 특정 시점에 미리 정한 가격으로 기초자산을 매매할 의무가 있는 파생상품.

### 10-10. Options (옵션)
미래 특정 시점에 미리 정한 가격으로 기초자산을 매매할 권리(의무 아님)를 부여하는 파생상품.

---

## 11. 기술 및 인프라 (Technology & Infrastructure)

### 11-1. Matching Engine (매칭엔진)
매수·매도 주문을 대조하여 체결시키는 거래소의 핵심 시스템.

### 11-2. Latency (지연시간)
주문 전송부터 체결 확인까지의 소요 시간. 마이크로초(μs) 단위로 측정.

### 11-3. Throughput (처리량)
단위 시간당 처리할 수 있는 주문/체결 건수.

### 11-4. HFT — High-Frequency Trading (고빈도거래)
극도로 짧은 시간 내에 대량의 주문을 제출·취소·체결하는 알고리즘 매매 전략.

### 11-5. Algo Trading — Algorithmic Trading (알고리즘 매매)
사전에 정의된 규칙과 알고리즘에 의해 자동으로 주문을 생성·관리하는 매매 방식.

### 11-6. DMA — Direct Market Access (직접시장접속)
기관투자자가 브로커의 인프라를 통해 거래소에 직접 주문을 제출하는 방식.

### 11-7. OMS — Order Management System (주문관리시스템)
주문의 생성, 라우팅, 체결, 관리를 통합 처리하는 시스템.
- **SGX**: 회원사 OMS를 통해 QUEST 접속

### 11-8. EMS — Execution Management System (체결관리시스템)
최적의 체결(best execution)을 위해 주문 라우팅과 실행을 최적화하는 시스템.

### 11-9. Smart Order Router (스마트주문라우터)
복수의 거래소/ATS 중 최적의 체결 장소로 주문을 자동 분배하는 시스템.
- 미국 시장에서 Reg NMS 준수를 위해 필수

### 11-10. Gateway (게이트웨이)
거래소 매매시스템에 접속하기 위한 네트워크 진입점.
- **NYSE Pillar**: Pillar Gateway
- **HKEX**: OCG (Orion Central Gateway)
- **Eurex T7**: Application Gateway

### 11-11. API — Application Programming Interface (응용 프로그래밍 인터페이스)
매매시스템이나 데이터 서비스에 프로그래밍 방식으로 접속하기 위한 인터페이스.

### 11-12. STP — Straight-Through Processing (직통처리)
주문 입력부터 체결, 청산, 결제까지 사람의 개입 없이 자동으로 처리되는 것.

### 11-13. Failover (장애극복)
주 시스템 장애 시 백업 시스템으로 자동 전환하는 기능.

### 11-14. Business Continuity (업무연속성)
재해, 시스템 장애 등 비상 상황에서도 핵심 업무를 지속할 수 있는 능력 및 계획.

---

## 12. 기타 (Others)

### 12-1. IPO — Initial Public Offering (기업공개, 상장)
기업이 처음으로 주식을 일반 투자자에게 공개 판매하여 증권거래소에 상장하는 것.

### 12-2. Listing (상장)
증권거래소에서 매매 대상으로 등록되는 것.

### 12-3. Delisting (상장폐지)
증권거래소에서 매매 대상 등록이 해제되는 것.

### 12-4. Market Capitalization (시가총액)
상장된 주식의 총 발행주식수에 현재 주가를 곱한 값.

### 12-5. Free Float (유통주식수)
전체 발행주식 중 실제로 시장에서 자유롭게 거래 가능한 주식 수.

### 12-6. Turnover (거래대금)
일정 기간 동안의 총 체결 금액.

### 12-7. Volume (거래량)
일정 기간 동안의 총 체결 주식 수.

### 12-8. Liquidity (유동성)
시장에서 자산을 가격에 큰 영향 없이 신속하게 매매할 수 있는 정도.

### 12-9. Volatility (변동성)
가격 변동의 크기 또는 빈도. 통상 수익률의 표준편차로 측정.

### 12-10. Short Selling (공매도)
보유하지 않은 주식을 빌려서 매도한 후, 나중에 되사서 갚는 거래.
- **KRX**: 공매도 — 개인투자자 공매도 제한 등 별도 규제 적용

### 12-11. Naked Short Selling (무차입 공매도)
주식을 빌리지 않은 상태에서 매도하는 것. 대부분의 시장에서 불법.

### 12-12. Margin Trading (신용거래)
증거금을 담보로 증권사로부터 자금이나 주식을 빌려 매매하는 거래.

### 12-13. ATS — Alternative Trading System (대체거래시스템)
정규 거래소가 아닌 대안적 매매 장소. 다크풀이 대표적.
- **미국**: SEC 등록 ATS (Reg ATS)
- **한국**: 2025년 도입 예정

### 12-14. MTF — Multilateral Trading Facility (다자간 매매체결 시스템)
EU의 대체거래시스템. MiFID에 의해 규제.

### 12-15. Best Execution (최선 집행)
고객 주문을 가격, 비용, 속도, 체결 가능성 등을 종합적으로 고려하여 최선의 조건으로 집행하는 의무.

### 12-16. Price Discovery (가격발견)
매수·매도 주문의 상호작용을 통해 자산의 공정 가격이 형성되는 과정.

### 12-17. Market Depth (시장 깊이)
각 호가 수준에 존재하는 주문 수량. 깊이가 깊을수록 유동성이 풍부.

### 12-18. Order Imbalance (주문 불균형)
매수 주문 총량과 매도 주문 총량의 차이.
- **NASDAQ**: Opening/Closing Cross 전 주문 불균형 정보 배포

### 12-19. Market Impact (시장충격)
대량 주문이 시장 가격에 미치는 영향.

### 12-20. Slippage (슬리피지)
주문 시 예상한 가격과 실제 체결 가격의 차이.

### 12-21. Front Running (선행매매)
고객 주문 정보를 이용하여 고객보다 먼저 매매하는 불공정 행위. 대부분의 시장에서 불법.

### 12-22. Spoofing (스푸핑)
체결 의사 없이 대량 주문을 제출하여 시장을 기만하는 행위. 불법.

### 12-23. Wash Trading (가장매매)
동일인이 매수와 매도를 동시에 수행하여 허위 거래량을 만드는 행위. 불법.

### 12-24. Insider Trading (내부자거래)
미공개 중요 정보를 이용하여 매매하는 불법 행위.

### 12-25. Market Microstructure (시장 미시구조)
시장의 매매 메커니즘, 가격 형성 과정, 정보의 역할 등을 연구하는 금융경제학 분야.

### 12-26. Tick-to-Trade (주문전송-체결 시간)
주문이 매칭엔진에 도달하여 체결될 때까지의 소요 시간. 시스템 성능의 핵심 지표.

### 12-27. Order-to-Trade Ratio (주문-체결 비율)
제출된 총 주문 건수 대비 실제 체결 건수의 비율. HFT 감시 지표로 활용.

### 12-28. Maker-Taker Fee (메이커-테이커 수수료)
유동성을 공급(maker)하는 주문에 리베이트를 주고, 유동성을 소비(taker)하는 주문에 수수료를 부과하는 체계.
- **NASDAQ/NYSE**: Maker-Taker 모델 적용

### 12-29. Reg SHO — Regulation SHO (공매도 규정)
미국의 공매도 관련 규정. 차입 확인(locate) 의무, 미결제(FTD) 규제 등.

### 12-30. SSR — Short Sale Restriction (공매도 제한)
주가가 전일 대비 10% 이상 하락한 종목에 대해 uptick rule을 적용하는 미국의 규제.
- **미국**: Alternative Uptick Rule (Rule 201)

---

## 부록: 약어 총정리

| 약어 | 정식 명칭 | 한국어 |
|------|-----------|--------|
| AP | Authorized Participant | 지정참가회사 |
| ASIC | Australian Securities and Investments Commission | 호주증권투자위원회 |
| ATS | Alternative Trading System | 대체거래시스템 |
| BaFin | Bundesanstalt für Finanzdienstleistungsaufsicht | 독일 연방금융감독청 |
| BBO | Best Bid and Offer | 최우선 호가 |
| BIS | Bank for International Settlements | 국제결제은행 |
| CAS | Closing Auction Session | 종가매매세션 |
| CCP | Central Counterparty | 중앙청산소 |
| CLOB | Central Limit Order Book | 중앙지정가주문장 |
| DMA | Direct Market Access | 직접시장접속 |
| DMM | Designated Market Maker | 지정 시장조성자 |
| DVP | Delivery Versus Payment | 증권인도 대 대금결제 |
| ELW | Equity-Linked Warrant | 주식연계증권 |
| EMS | Execution Management System | 체결관리시스템 |
| ETF | Exchange-Traded Fund | 상장지수펀드 |
| ETI | Enhanced Trading Interface | 향상된 매매 인터페이스 |
| ETN | Exchange-Traded Note | 상장지수증권 |
| FAK | Fill and Kill | 즉시체결잔량취소 |
| FCA | Financial Conduct Authority | 금융행위감독청 |
| FINRA | Financial Industry Regulatory Authority | 금융산업규제기관 |
| FIX | Financial Information eXchange | 금융정보교환 프로토콜 |
| FOK | Fill or Kill | 전량즉시체결 |
| FSC | Financial Services Commission | 금융위원회 |
| FSS | Financial Supervisory Service | 금융감독원 |
| GFD | Good for Day | 당일유효 |
| GTC | Good Till Cancel | 취소시까지유효 |
| GTD | Good Till Date | 지정일까지유효 |
| HFT | High-Frequency Trading | 고빈도거래 |
| IOSCO | International Organization of Securities Commissions | 국제증권감독기구 |
| IOC | Immediate or Cancel | 즉시체결잔량취소 |
| IPO | Initial Public Offering | 기업공개 |
| JFSA | Japan Financial Services Agency | 일본 금융청 |
| KONEX | Korea New Exchange | 코넥스 |
| KOSDAQ | Korea Securities Dealers Automated Quotations | 코스닥 |
| KOSPI | Korea Composite Stock Price Index | 한국종합주가지수 |
| LOC | Limit on Close | 종가 지정가 주문 |
| LOO | Limit on Open | 시초가 지정가 주문 |
| LP | Liquidity Provider | 유동성공급자 |
| LULD | Limit Up-Limit Down | 상한가-하한가 제도 |
| MAS | Monetary Authority of Singapore | 싱가포르 통화감독청 |
| MiFID | Markets in Financial Instruments Directive | 금융상품시장지침 |
| MOC | Market on Close | 종가 시장가 주문 |
| MOO | Market on Open | 시초가 시장가 주문 |
| MTF | Multilateral Trading Facility | 다자간 매매체결 시스템 |
| NBBO | National Best Bid and Offer | 전국 최우선 호가 |
| NLT | Negotiated Large Trade | 협의대량매매 |
| OCG | Orion Central Gateway | 오리온 중앙 게이트웨이 |
| OCO | One Cancels the Other | 양자택일 주문 |
| OMD | Orion Market Data | 오리온 시장 데이터 |
| OMS | Order Management System | 주문관리시스템 |
| OTP | Orion Trading Platform | 오리온 매매 플랫폼 |
| REIT | Real Estate Investment Trust | 부동산투자신탁 |
| SEC | Securities and Exchange Commission | 미국 증권거래위원회 |
| SETS | Stock Exchange Electronic Trading Service | 전자주문장 매매 서비스 |
| SFC | Securities and Futures Commission | 증권선물위원회 |
| SLP | Supplemental Liquidity Provider | 보충적 유동성공급자 |
| SPAN | Standard Portfolio Analysis of Risk | 포트폴리오 위험분석 모델 |
| SPAC | Special Purpose Acquisition Company | 기업인수목적회사 |
| SRO | Self-Regulatory Organization | 자율규제기관 |
| SSR | Short Sale Restriction | 공매도 제한 |
| STP | Straight-Through Processing | 직통처리 |
| TWAP | Time-Weighted Average Price | 시간가중평균가격 |
| VCM | Volatility Control Mechanism | 변동성 통제 메커니즘 |
| VI | Volatility Interruption | 변동성완화장치 |
| VWAP | Volume-Weighted Average Price | 거래량가중평균가격 |
| WFE | World Federation of Exchanges | 세계거래소연합 |
