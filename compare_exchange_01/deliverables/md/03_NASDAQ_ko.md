# NASDAQ (나스닥) — 거래소 보고서

---

## 1. 거래소 개요

**정식 법인명**: The Nasdaq Stock Market LLC (나스닥 주식시장)
**국가**: 미국
**설립연도**: 1971년 (최초 전자 주식시장); 2006년 공식 거래소 등록 [WEB:wikipedia]
**모기관**: Nasdaq, Inc. [WEB:nasdaq.com]

**시장 모델**: 순수 전자 주문주도형 시장 + 경쟁적 시장조성자 [REF:#1]

**거래 자산 유형**: [WEB:nasdaq.com]
- 주식 (Nasdaq, Nasdaq BX, Nasdaq PSX)
- 옵션 (Nasdaq Options Market, ISE, GEMX, MRX, PHLX)
- ETF, ETN

**정규 매매시간 (ET, UTC−5/−4)**: [REF:#7] [WEB:tradinghours.com]
- 장전 매매: 04:00–09:30
- 핵심 매매시간: 09:30–16:00
- 장후 매매: 16:00–20:00
- **제안 중**: 23시간 매매 (21:00–20:00 ET) 2025.12 신청 [WEB:federalregister.gov]

**주요 통계**: [WEB:marketcap.company] [WEB:bestbrokers]
- 상장기업 수: 약 4,000–4,278개
- 시가총액: 약 $28조 이상
- 일평균 거래량: 약 40억주 이상

---

## 2. 제도적 철학

**기본 시장 모델**: 순수 전자, 주문주도형, 물리적 거래 플로어 없음 [REF:#1] [REF:#2]

**설계 근거**: [WEB:wikipedia]
- 1971년 세계 최초 전자 주식시장으로 설립 — 처음부터 속도와 기술 중심 설계
- 플로어 없음, 전문가(specialist) 없음, 체결 과정 인적 중개 없음 — 전량 알고리즘 매칭
- 저지연 접속, 투명한 가격 발견, 프로토콜 효율성(OUCH/ITCH) 강조
- 독점 DMM이 아닌 경쟁적 시장조성자 모델 [REF:#1]

**중개 기관의 역할**: [REF:#1]
- **등록 시장조성자**: 종목당 복수 MM (경쟁 모델, 비독점)
- 지정 비율 이내에서 지속적 양방향 호가 유지 의무 [WEB:federalregister.gov/rule4613]
- 확정호가 규칙: 게시 호가에서 반드시 체결 [WEB:finra.org]

**발전 과정**: 전자 호가 시스템(1971) → ECN 통합 → INET 매칭엔진(2006 Instinet 인수) → 글로벌 기술 제공자(Nasdaq OMX) → 핀테크 플랫폼(2025+) [WEB:wikipedia]

---

## 3. 주문유형 — 기본

### 3.1 시장가 주문 (Market Order) [REF:#1]
- 최적 가용 가격으로 즉시 체결

### 3.2 지정가 주문 (Limit Order) [REF:#1]
- 최대 매수가 / 최소 매도가 지정; 미체결 시 주문장에 등록
- 유효기간: Day, GTC, IOC, FOK, Extended Hours, System Hours

### 3.3 시초가 시장가 주문 (MOO) [REF:#7]
- Opening Cross 전용 시장가 주문

### 3.4 시초가 지정가 주문 (LOO) [REF:#7]
- Opening Cross 전용 지정가 주문

### 3.5 종가 시장가 주문 (MOC) [REF:#7]
- Closing Cross 전용 시장가 주문

### 3.6 종가 지정가 주문 (LOC) [REF:#7]
- Closing Cross 전용 지정가 주문

---

## 4. 주문유형 — 고급

### 4.1 빙산 주문 (Reserve/Iceberg Order) [REF:#1]
- 일부만 표시; 숨겨진 잔량이 자동 보충

### 4.2 페그 주문 (Pegged Orders) [REF:#1]
- **Primary Peg**: 같은 쪽 내부호가에 연동
- **Market Peg**: 상대쪽 내부호가에 연동
- **Midpoint Peg**: NBBO 중간가에 연동

### 4.3 게시 전용 주문 (Post-Only Order) [REF:#1]
- 주문장에만 등록; 즉시 체결 시 취소/재가격
- 메이커 리베이트 추구 참가자 대상

### 4.4 시장간 일괄체결 주문 (ISO) [REF:#1]
- 나스닥에서 복수 가격 단계 관통; 발주자가 타 시장 보호 책임

### 4.5 불균형 전용 주문 (IO Orders) [REF:#7]
- IO Open / IO Close: 경매 불균형 상계 전용 지정가 주문

### 4.6 비표시 주문 (Non-Displayed Order) [REF:#1]
- 주문장에 미표시; 중간가 이상에서 체결
- 동일 가격 표시 주문보다 낮은 우선순위

### 4.7 주문 유효기간 옵션 [REF:#1]
- Day, GTC, IOC, FOK, Extended Hours(04:00–20:00), System Hours(전 세션), Market Hours(09:30–16:00)

---

## 5. 주문유형 — 거래소 고유

### 5.1 중간가 연장수명 주문 (M-ELO) [WEB:nasdaq.com/melo]
- **나스닥 고유**: 비표시 중간가 주문 + 의무 보유기간 (최소 0.5초)
- 다른 M-ELO 또는 M-ELO+CB와만 체결 가능
- 설계 근거: 정보 누출 감소, 역선택 방지

### 5.2 동적 M-ELO (Dynamic M-ELO) [WEB:nasdaq.com/dynamic-melo]
- AI/ML로 30초마다 보유기간 재계산
- 안정 시장 = 짧은 보유, 변동 시장 = 긴 보유
- 2023.09 SEC 승인 [WEB:federalregister.gov/melo]

### 5.3 M-ELO+CB [WEB:nasdaq.com/melo]
- M-ELO + 연속장 상호작용 결합
- M-ELO뿐 아니라 비표시 중간가/MPPO 주문과도 체결 가능

### 5.4 중간가 페그 게시 전용 주문 (MPPO) [WEB:nasdaqtrader.com/mppo]
- 비표시, NBBO 중간가 설정; 경제적 유리 시에만 입력 시 체결
- 보유기간 없음 (M-ELO와 구별)

### 5.5 시장조성자 페그 주문 (MM Peg Order) [WEB:nasdaqtrader.com/mmpeg]
- 등록 시장조성자 전용; 호가 의무 준수를 위해 자동 재가격
- 수동 호가 관리 부담 감소

### 5.6 Opening/Closing Cross [REF:#7] [REF:#8]
- **Opening Cross**: 09:25–09:30 NOII 배포 → 09:30 단일가 체결
- **Closing Cross**: 15:50–16:00 NOII 배포 → 16:00 단일가 체결
- 전체 NMS 증권 대상 [REF:#7]

---

## 6. 매칭엔진 및 가격 발견

### 매매시스템: INET [REF:#2] [REF:#3] [WEB:nasdaq.com/matching]
- **유래**: Instinet 인수(2006), Island ECN 기술 기반 [WEB:wikipedia]
- **아키텍처**: 수평 확장 가능 매칭엔진, 범용 하드웨어 [WEB:nasdaq.com/matching]
- **지연시간**: 40마이크로초 미만; 코로케이션 OUCH: <25μs, FIX: <80μs [WEB:nasdaqtrader.com/latency]
- **네트워크**: 40 Gbps 인프라 [WEB:tradersmagazine.com]
- **강화**: FPGA 기술로 결정론적 피크 시간 동작 [REF:#2]

### 프로토콜 [REF:#2] [REF:#3]
- **OUCH 5.0**: 저지연 주문 진입 프로토콜 (인바운드) [REF:#3]
- **ITCH 5.0**: 시장 데이터 피드 프로토콜 (아웃바운드) [REF:#5]
- **FIX**: 업계 표준 주문 진입 (OUCH 대비 높은 지연시간)

### 매칭 알고리즘: 가격·시간 우선원칙 [REF:#2]
1. **가격 우선**: 최우선 가격 먼저
2. **시간 우선**: 동일가 중 먼저 접수된 주문 우선
3. **표시 우선**: 동일가에서 표시 주문이 비표시 주문에 우선

### 시가 결정 — Opening Cross [REF:#7]
- 04:00: 주문 접수 시작 → 09:25: NOII 배포 시작 → 09:30: 단일가 체결

### 종가 결정 — Closing Cross [REF:#7]
- 15:50: NOII 배포 시작 → 16:00: 단일가 체결
- 일부 종목 일 거래량의 ~15% 종가에서 체결

### 호가단위 (Tick Size)
- 표준: $0.01 (가격 >$1.00); 서브페니: $0.0001 (가격 <$1.00)
- 중간가 체결: 하프페니($0.005) 단위 허용

### 매매수량단위 (Lot Size)
- 표준: 100주 (정규거래단위); 단주(<100주) 완전 지원

---

## 7. 안전장치 메커니즘

### 7.1 시장 전체 서킷브레이커 (MWCB)
- NYSE와 동일 국가 규정 (S&P 500 기준 7%/13%/20%)

### 7.2 상·하한가 제한 (LULD) [WEB:luldplan.com]
- NYSE와 동일 국가 플랜 (Tier 1: ±5%, Tier 2: ±10%/±20%)
- 나스닥 고유: LULD 밴드 도달 후 15초 → 5분 매매 일시정지
- 재개: Nasdaq Halt Cross 메커니즘

### 7.3 명백히 착오적인 체결 (CEE) [REF:#1]
- 30분 이내 검토 요청; 기준가 비율 기반 임계값

### 7.4 규제 매매정지 [REF:#1]
- T1/T2 (뉴스 대기/배포), T12 (IPO), LUDP (LULD 일시정지)
- 재개: Halt Cross로 재개장

### 7.5 사전거래위험관리 [REF:#2]
- 주문 가격 합리성 검사, 최대 주문 규모 제한
- 킬 스위치, Drop Copy 실시간 위험 모니터링

---

## 8. 특별 세션

### 8.1 장전 매매 [WEB:tradinghours.com]
- 04:00–09:30 ET; 연속 전자 매칭; 지정가만 (Extended Hours TIF)

### 8.2 Opening Cross [REF:#7]
- 09:25–09:30 NOII 배포; 09:30 단일가 체결
- MOO, LOO, IO Open, 일반 지정가/시장가

### 8.3 핵심 매매시간 [REF:#1]
- 09:30–16:00 ET; INET 연속 가격·시간 우선 매칭
- M-ELO, MPPO, 페그 등 전 주문유형 사용 가능

### 8.4 Closing Cross [REF:#7]
- 15:50–16:00 NOII 배포; 16:00 단일가 체결
- MOC, LOC, IO Close

### 8.5 장후 매매 [WEB:tradinghours.com]
- 16:00–20:00 ET; 연속 전자 매칭; 지정가만

### 8.6 Halt Cross / IPO Cross [REF:#1] [WEB:nasdaq.com]
- 규제 정지 후 재개장 및 신규 상장 첫 거래에 사용
- NOII 배포 후 단일가 체결 — 전량 전자, DMM 없음

---

## 9. 유동성공급자 / 시장조성자 의무

### 9.1 나스닥 시장조성자 (경쟁 모델) [REF:#1]

**구조**: [REF:#1]
- 종목당 **복수 시장조성자** (경쟁적, 비독점)
- 모든 등록 브로커-딜러가 하나 이상의 종목에서 MM 등록 가능

**호가 의무 (Rule 4613)**: [WEB:federalregister.gov/rule4613]
- 매매시간 중 지속적 양방향 호가 유지
- 지정 비율(Designated Percentage) 이내 호가 가격 유지
- 정규거래단위(100주) 이상 게시 호가에서 체결 의무

**확정호가 규칙**: [WEB:finra.org]
- 게시 호가·수량에서 반드시 체결 — 다른 FINRA 회원과의 거래

**도구**: [WEB:nasdaqtrader.com/mmpeg]
- 시장조성자 페그 주문: 의무 준수를 위한 자동 재가격

### 9.2 수수료 구조 / 인센티브 [WEB:nasdaq.com]
- **메이커-테이커 모델**: 표시 유동성 추가 시 리베이트, 제거 시 수수료
- 일반 리베이트: 체결 주당 ~$0.002–0.003
- 거래량 임계값 기반 단계별 가격 책정

### 9.3 NYSE DMM과 비교 [REF:#1]
- **NYSE**: 종목당 독점 DMM 1사, 의무 + 특권
- **나스닥**: 종목당 다수 MM, 경쟁적 호가, 독점권 없음
- **결과**: NYSE = 보장된 깊은 유동성; 나스닥 = 폭넓은 경쟁적 압력

---

## 10. 출처 목록

[REF:#1] Nasdaq, "NASDAQ Rule Book", https://listingcenter.nasdaq.com/rulebook/nasdaq/rules
[REF:#2] Nasdaq, "OUCH Overview", https://www.nasdaqtrader.com/Trader.aspx?id=OUCH
[REF:#3] Nasdaq, "OUCH 5.0 Specification", https://nasdaqtrader.com/content/technicalsupport/specifications/TradingProducts/Ouch5.0.pdf
[REF:#4] Nasdaq, "OUCH 5.0 FAQ", https://nasdaqtrader.com/content/productsservices/trading/OUCH_5.0_FAQ.pdf
[REF:#5] Nasdaq, "Nordic Equity TotalView-ITCH 3.04.X", https://www.nasdaq.com/docs/2025/11/13/Nordic-Equity-TotalView-ITCH-3.04.X.pdf
[REF:#6] Nasdaq, "NASDAQ TotalView", https://data.nasdaq.com/databases/NTV
[REF:#7] Nasdaq, "Opening and Closing Crosses", https://nasdaqtrader.com/Trader.aspx?id=OpenClose
[REF:#8] Nasdaq, "Opening/Closing Cross FAQ", https://nasdaqtrader.com/content/productsservices/trading/crosses/openclose_faqs.pdf
[REF:#9] Nasdaq, "Order Types & Routing Strategies", https://www.nasdaqtrader.com/content/marketregulation/regnms/rash_strategy.pdf
[REF:#10–13] 추가 참조 출처 (TotalView Solutions, Help Center, OUCH 4.2, INET Nordic)

[WEB 출처] 전체 목록은 영문 보고서 §10 참조

---

*보고서 버전: 1.0 | 배치: 1 | 작성일: 2026-03-27 | 언어: 한국어*
