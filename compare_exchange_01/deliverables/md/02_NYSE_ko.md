# NYSE (뉴욕증권거래소) — 거래소 보고서

---

## 1. 거래소 개요

**정식 법인명**: New York Stock Exchange LLC (뉴욕증권거래소)
**국가**: 미국
**설립연도**: 1792년 (Buttonwood Agreement); 1817년 공식 조직화 [WEB:wikipedia]
**모기관**: Intercontinental Exchange (ICE), 2013년 인수 [WEB:wikipedia]

**시장 모델**: 혼합형 시장 — 전자 주문주도형 + 지정 시장조성자(DMM) + 물리적 거래 플로어 [REF:#1]

**거래 자산 유형**: [REF:#1]
- 주식 (NYSE, NYSE Arca, NYSE American, NYSE National, NYSE Texas)
- 옵션 (NYSE Arca Options, NYSE American Options)
- 채권 (NYSE Bonds)
- ETF, ETN, 폐쇄형 펀드, SPAC

**정규 매매시간 (ET, UTC−5/−4)**: [REF:#2]
- 사전 개장 (주문 대기): 06:30
- 조기 매매 (Arca): 04:00부터; (American/National/Texas): 07:00부터
- 핵심 매매시간: 09:30–16:00
- 장후 매매 (Arca, American): 16:00–20:00

**주요 통계**: [WEB:bestbrokers] [WEB:statista]
- 상장기업 수: 약 2,400개 이상 (NYSE 기본)
- 시가총액: 약 $30조 이상 (전 세계 최대 거래소)
- 일평균 거래량: 약 15.4억주 / 약 $806억 (2025년 11월)

---

## 2. 제도적 철학

**기본 시장 모델**: 혼합형 — 전자 매칭과 인적 가격 발견의 결합 [REF:#1]

**설계 근거**: [REF:#1] [WEB:nyse.com/market-model]
- NYSE는 **물리적 거래 플로어**를 유지하는 유일한 주요 거래소
- 혼합형 모델: 전자적 속도/효율성 + 복잡한 상황(대규모 불균형, 변동성 이벤트, IPO)에 대한 인적 판단
- DMM이 종목별 전담 전문가로서 지속적 양방향 유동성 제공 및 개장/폐장 경매 관리 [REF:#1]
- 플로어 브로커: 기관 고객 대리, D-Order 등 플로어 전용 주문유형 접근 [WEB:nyse.com/d-orders]

**배분 모델 — 가격/동등/우선**: [REF:#1]
- "가격 설정자에게 보상하고 동일 가격의 복수 참가자에게 배분"
- KRX/NASDAQ의 순수 가격·시간 우선원칙과 차별화

**발전 과정**: 물리적 플로어(1792) → 전문가 시스템 → 혼합형(2006 Archipelago 합병) → Pillar 플랫폼 전환(2016–현재) [WEB:wikipedia]

---

## 3. 주문유형 — 기본

### 3.1 시장가 주문 (Market Order) [REF:#2]
- 가격 미지정; 최적 가용 가격으로 체결
- 개장/폐장 경매 시: 경매 가격으로 참여

### 3.2 지정가 주문 (Limit Order) [REF:#2]
- 최대 매수가 / 최소 매도가 지정
- 유효기간: Day(기본), GTC, IOC, FOK

### 3.3 스톱 주문 (Stop Order) [REF:#2]
- 스톱 가격 도달 시 시장가 주문으로 전환

### 3.4 스톱 지정가 주문 (Stop-Limit Order) [REF:#2]
- 스톱 가격 도달 시 지정가 주문으로 전환
- 스톱가(트리거)와 지정가(체결) 두 가격 지정

### 3.5 시초가 시장가 주문 (MOO) [REF:#2] [REF:#6]
- 개장 경매 전용 시장가 주문
- 시가 결정 참여 보장

### 3.6 시초가 지정가 주문 (LOO) [REF:#2] [REF:#6]
- 개장 경매 전용 지정가 주문

### 3.7 종가 시장가 주문 (MOC) [REF:#2] [WEB:nyse.com/closing-auction]
- 폐장 경매 전용; 입력 마감: 15:50 ET
- 종가 체결 보장

### 3.8 종가 지정가 주문 (LOC) [REF:#2] [WEB:nyse.com/closing-auction]
- 폐장 경매 전용; 입력 마감: 15:50 ET
- 지정가 이내 시 종가 체결

---

## 4. 주문유형 — 고급

### 4.1 빙산 주문 (Reserve/Iceberg Order) [REF:#6]
- 일부 수량만 표시(MaxFloor); 숨겨진 잔량 자동 보충

### 4.2 페그 주문 (Pegged Orders) [REF:#6]
- **Primary Peg**: 같은 쪽 전국 최우선 매수·매도호가(NBBO)에 연동
- **Market Peg**: 상대쪽 NBBO에 연동
- **Midpoint Peg**: NBBO 중간가에 연동

### 4.3 중간가 수동 유동성 주문 (MPL Order) [REF:#6]
- 비표시 주문, NBBO 중간가 체결
- 핵심 매매시간에만 사용 가능

### 4.4 유동성 추가 전용 주문 (ALO Order) [REF:#6]
- 주문장에만 게시; 즉시 체결 시 취소/재가격
- 메이커 리베이트 추구 참가자 대상

### 4.5 시장간 일괄체결 주문 (ISO) [REF:#6]
- NYSE에서 복수 가격 단계 관통 가능
- 발주자가 타 시장 최우선가 동시 라우팅 책임 (Reg NMS 준수)

### 4.6 불균형 상계 주문 (IO Orders) [WEB:nyse.com/closing-auction]
- **Closing Offset (CO)**: 폐장 경매 불균형 상계; 15:50 이후 접수
- **Opening IO**: 개장 경매 불균형 상계

### 4.7 추적 주문 (Tracking Orders) [REF:#6]
- NYSE 플로어 전용 비표시 지정가 주문
- DMM 또는 플로어 브로커 재량으로 체결

---

## 5. 주문유형 — 거래소 고유

### 5.1 D-Order [WEB:nyse.com/d-orders]
- **NYSE 고유**: 플로어 브로커만 사용 가능
- Closing D-Order: 비표시 가격 범위의 재량적 폐장 경매 참여
- Opening D-Order: DMM 개장 경매 참여
- 입력 마감: 15:59:50; 2025.08부터 자동 OMS 사용 [WEB:nyse.com]

### 5.2 DMM 이해관계 주문 [REF:#3]
- DMM 자기계정 매매로 질서 있는 시장 유지
- 경매 불균형 흡수 가능 [WEB:nyse.com/closing-auction]
- 규정 104조 제한 적용 [WEB:sec.gov/rule104]

### 5.3 소매 유동성 프로그램 주문 [REF:#1]
- **Retail Taker Orders**: 자연인 대리 주문
- **Retail Price Improvement (RPI) Orders**: PBBO보다 유리한 비표시 호가
- **Retail Attested Orders**: 개인 투자자 우대 경제

### 5.4 SLP 호가 [REF:#1]
- SLP-Prop 및 SLMM 범주
- 배정 종목 매매일 10% 이상 NBBO 유지 의무 [WEB:liquidity-provider.com]

---

## 6. 매칭엔진 및 가격 발견

### 매매시스템: Pillar [REF:#4] [REF:#5]
- **출범**: 2016년부터 단계적 전환
- **아키텍처**: NYSE 그룹 전 거래소 통합 플랫폼 [REF:#5]
- **프로토콜**: FIX + Binary [REF:#4] [REF:#5]
- **지연시간**: 밀리초 미만 (구체 수치 비공개)

### 매칭 알고리즘: 가격/동등/우선 (Price/Parity/Priority) [REF:#1]
1. **가격 우선**: 최우선 가격 주문 먼저
2. **동등 배분**: 동일 가격에서 복수 참가자에게 배분
3. **가격 설정자 우선**: 새 최우선가 설정자에게 우선권

### 시가 결정 (Opening Auction) [REF:#1]
- 06:30 ET부터 주문 축적 → 09:30에 DMM 주도 단일가 결정
- ~09:28부터 불균형 정보 공개

### 종가 결정 (Closing Auction) [WEB:nyse.com/closing-auction]
- 15:50: MOC/LOC 마감; 불균형 정보 매초 공개
- 16:00: 경매 칼라(Auction Collar) 내 단일가 결정
  - ≤$25: ±5% | $25–$50: ±2% | >$50: ±1% (최소 $0.15)

### 호가단위 (Tick Size)
- 표준: $0.01 (가격 >$1.00)
- 서브페니: $0.001 (가격 <$1.00)

### 매매수량단위 (Lot Size)
- 표준: 100주 (정규거래단위)

---

## 7. 안전장치 메커니즘

### 7.1 시장 전체 서킷브레이커 (MWCB) [REF:#2] [WEB:investor.gov]

| 단계 | 발동 조건 (S&P 500 전일 종가 대비 하락) | 지속 시간 | 시간 제한 |
|---|---|---|---|
| 1단계 | ≥ 7% | 15분 정지 | 15:25 ET 이전만 |
| 2단계 | ≥ 13% | 15분 정지 | 15:25 ET 이전만 |
| 3단계 | ≥ 20% | 잔여 매매일 종결 | 항시 |

- 2025.04.07: 관세 발표로 1단계 발동 [WEB:cnbc.com]

### 7.2 상·하한가 제한 (LULD) [WEB:luldplan.com]

| 등급 | 대상 | 정규시간 (9:45–15:35) | 개장/폐장 |
|---|---|---|---|
| Tier 1 | S&P 500, Russell 1000, 주요 ETP | ±5% | ±10% |
| Tier 2 | 기타 NMS 주식 (>$3.00) | ±10% | ±20% |
| Tier 2 | NMS 주식 (≤$3.00) | ±20% | ±40% |

- 기준가: 5분간 적격 거래 산술평균; 30초마다 갱신 [WEB:luldplan.com]

### 7.3 매매거래정지 [REF:#2]
- 규제 정지: 뉴스 대기(T1/T2), SEC 정지
- LULD 정지: 가격대 위반 시
- DMM 주도 재개장 경매로 재개

### 7.4 사전거래위험관리 (Pillar) [REF:#7]
- 최대 주문 규모/금액 제한, 가격 합리성 검사
- 킬 스위치: 전체 미체결 주문 취소 및 신규 차단 [REF:#7]
- Cancel on Disconnect: 접속 두절 시 자동 취소 [REF:#7]

---

## 8. 특별 세션

### 8.1 사전 개장 세션 [REF:#2]
- 06:30 ET: 주문 대기 시작
- NYSE Arca: 04:00부터 조기 매매; NYSE American: 07:00부터

### 8.2 개장 경매 [REF:#1]
- 09:30 ET: DMM 주도 단일가 경매
- MOO, LOO, IO 주문 참여; ~09:28부터 불균형 정보 공개

### 8.3 핵심 매매시간 [REF:#2]
- 09:30–16:00 ET: 전자 연속 매칭(Pillar) + 플로어 상호작용

### 8.4 폐장 경매 [WEB:nyse.com/closing-auction]
- 15:50–16:00 ET: 불균형 기간; DMM 주도 단일가 경매
- 일 거래량의 ~10% 종가에서 체결

### 8.5 장후 매매 [REF:#2]
- NYSE Arca: 16:00–20:00 ET; NYSE American: 16:00–20:00 ET
- 지정가 주문만 가능

---

## 9. 유동성공급자 / 시장조성자 의무

### 9.1 지정 시장조성자 (DMM) [REF:#1] [REF:#3]
- 종목당 1개 DMM 사 배정; 현재 3사 (Citadel, Virtu, GTS) [REF:#1]
- NBBO 호가 유지: CADV ≥100만주 종목 5%, <100만주 10%, ETP 25% [WEB:sec.gov/rule104]
- 개장/폐장 경매 주도, 불균형 흡수 [REF:#1]

### 9.2 보충적 유동성공급자 (SLP) [REF:#1] [WEB:liquidity-provider.com]
- SLP-Prop / SLMM 두 범주; 전자 참가자 (플로어 불필요)
- 배정 종목 매매일 10% 이상 NBBO 호가 유지
- 월간 ADV 1,000만주 이상
- 리베이트: 체결 주당 ~$0.0020 [WEB:sec.gov/slp]

### 9.3 소매 유동성 프로그램 [REF:#1]
- RPI 주문으로 소매 주문에 가격 개선 ≥$0.001 제공
- NYSE가 소매 유동성 지표(Retail Liquidity Indicator) 게시

---

## 10. 출처 목록

[REF:#1] NYSE, "NYSE Market Model", https://www.nyse.com/market-model
[REF:#2] NYSE, "NYSE Trading Information", https://www.nyse.com/markets/nyse/trading-info
[REF:#3] NYSE, "Rule 104 (DMM) Interpretation", https://www.nyse.com/publicdocs/nyse/markets/nyse/rule-interpretations/2014/14-2.pdf
[REF:#4] NYSE, "Pillar FIX Protocol Spec", https://www.nyse.com/publicdocs/nyse/NYSE_Pillar_Gateway_FIX_Protocol_Specification.pdf
[REF:#5] NYSE, "Pillar Binary Protocol Spec", https://www.nyse.com/publicdocs/nyse/NYSE_Pillar_Gateway_Binary_Protocol_Specification.pdf
[REF:#6] NYSE, "Pillar Order Type Differences", https://www.nyse.com/publicdocs/nyse/markets/nyse/Pillar_Differences.pdf
[REF:#7] NYSE, "Pillar Risk Controls", https://www.nyse.com/publicdocs/nyse/NYSE_Pillar_Risk_Controls.pdf
[REF:#8] NYSE, "Functional Differences NYSE Pillar", https://www.nyse.com/publicdocs/nyse/markets/nyse/Functional_Differences_NYSE_Pillar.pdf

[WEB:nyse.com/market-model] https://www.nyse.com/market-model, 접속일 2026-03-27
[WEB:nyse.com/closing-auction] https://www.nyse.com/article/nyse-closing-auction-insiders-guide, 접속일 2026-03-27
[WEB:nyse.com/d-orders] https://www.nyse.com/data-insights/getting-to-know-d-orders-a-unique-execution-tool-for-nyse-floor-brokers, 접속일 2026-03-27
[WEB:wikipedia] https://en.wikipedia.org/wiki/New_York_Stock_Exchange, 접속일 2026-03-27
[WEB:investor.gov] https://www.investor.gov/introduction-investing/investing-basics/glossary/stock-market-circuit-breakers, 접속일 2026-03-27
[WEB:luldplan.com] https://www.luldplan.com/, 접속일 2026-03-27
[WEB:liquidity-provider.com] https://liquidity-provider.com/articles/what-is-a-supplemental-liquidity-provider-slp-on-the-nyse/, 접속일 2026-03-27
[WEB:sec.gov/rule104] https://www.sec.gov/files/rules/sro/nyse/2019/34-87056.pdf, 접속일 2026-03-27
[WEB:bestbrokers] https://www.bestbrokers.com/stock-trading/stock-trading-market-statistics/, 접속일 2026-03-27
[WEB:statista] https://www.statista.com/statistics/1277195/nyse-nasdaq-comparison-market-capitalization-listed-companies/, 접속일 2026-03-27
[WEB:cnbc.com] https://www.cnbc.com/2025/04/06/sp-500-circuit-breaker-on-tariff-worries-what-that-means.html, 접속일 2026-03-27

---

*보고서 버전: 1.0 | 배치: 1 | 작성일: 2026-03-27 | 언어: 한국어*
