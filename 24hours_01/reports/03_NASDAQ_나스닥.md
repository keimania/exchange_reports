# NASDAQ 23/5 글로벌 거래 생태계 분석

## 1. 기관 개요

### 1.1 NASDAQ Inc. 구조 및 글로벌 위상

NASDAQ(National Association of Securities Dealers Automated Quotations)은 1971년 설립된 세계 최초의 전자식 주식 거래소로, 현재 글로벌 자본시장 인프라의 핵심 축을 담당하고 있다. 2025년 기준 NASDAQ에는 약 3,700개 이상의 기업이 상장되어 있으며, 일평균 거래대금은 수천억 달러에 달한다. Apple, Microsoft, Amazon, NVIDIA 등 세계 시가총액 상위 기업 대다수가 NASDAQ에 상장되어 있어, 사실상 글로벌 기술주 거래의 중심지 역할을 수행한다.

NASDAQ Inc.는 단순한 거래소를 넘어 시장 기술(Market Technology) 공급자로서의 정체성을 강화하고 있다. 전 세계 130개 이상의 시장 운영자에게 거래소 기술 솔루션을 제공하며, 한국거래소(KRX)를 포함한 아시아 주요 거래소에도 기술 자문 및 플랫폼을 공급한 바 있다.

### 1.2 Genium INET 매칭엔진 및 Eqlipse 기술 스택

NASDAQ의 거래 처리 핵심은 **Genium INET** 매칭엔진이다. 이 엔진은 마이크로초(microsecond) 단위의 주문 처리 성능을 제공하며, 결정론적(deterministic) 매칭 로직을 통해 동일한 입력에 대해 동일한 결과를 보장한다. 이는 고빈도매매(HFT) 참여자들의 핵심 요구사항이다.

2024년부터 NASDAQ은 차세대 기술 스택인 **Eqlipse**로의 전환을 본격화하고 있다. Eqlipse의 주요 특징은 다음과 같다:

| 구분 | 사양 |
|------|------|
| 아키텍처 | 클라우드 네이티브 (AWS 파트너십) |
| 하드웨어 가속 | FPGA 기반 게이트웨이 |
| 네트워크 | 커널 바이패스(Kernel Bypass) 네트워킹 (Solarflare/Xilinx 기반) |
| 업데이트 방식 | Rolling Restart / Evergreen Update |
| 확장성 | 마이크로서비스 아키텍처, 동적 인스턴스 확장 |

Eqlipse는 24시간 운영 환경에서 가장 중요한 요건인 **무중단 패치(Zero-Downtime Patching)**를 지원한다. 개별 컴포넌트(게이트웨이, 시장데이터 퍼블리셔 등)를 매칭엔진 가동 중에 독립적으로 업데이트할 수 있으며, 이는 23/5 운영 모델의 기술적 전제 조건이다.

---

## 2. 현행 거래시간 제도

NASDAQ의 현행 거래시간은 하루 총 16시간(04:00~20:00 ET)으로, 세 개의 세션으로 구분된다.

### 2.1 Pre-Market (04:00~09:30 ET)

- **운영시간**: 5시간 30분
- **허용 주문유형**: 지정가(Limit) 주문만 허용
- **특징**: 공식 시가(Opening Price)가 형성되기 전 구간으로, 유동성이 제한적이며 스프레드가 넓다
- **참여자**: 주로 기관투자자 및 전문 트레이더가 활용하며, 유럽 시장 개장 전후 뉴스 반영 거래가 활발

### 2.2 Regular Market (09:30~16:00 ET)

- **운영시간**: 6시간 30분
- **핵심 메커니즘**:
  - **Opening Cross (09:30 ET)**: Pre-Market 기간 축적된 주문을 집합하여 공식 시가를 결정하는 단일가 매매 메커니즘. 수요-공급 균형점에서 최대 체결량을 산출
  - **Closing Cross (16:00 ET)**: MOC(Market-on-Close), LOC(Limit-on-Close) 주문을 집합하여 공식 종가를 결정. 인덱스 펀드 리밸런싱 등 대규모 주문이 집중되어, 일일 거래량의 약 10~15%가 이 시점에 체결
- **규제**: Regulation NMS Rule 611(Order Protection Rule)이 완전 적용되어, 타 거래소의 최우선호가보다 불리한 가격으로 체결되는 것(Trade-Through)을 금지
- **시장보호**: LULD(Limit Up-Limit Down) 메커니즘이 작동하여 급격한 가격 변동 시 거래를 일시 정지

### 2.3 Post-Market (16:00~20:00 ET)

- **운영시간**: 4시간
- **허용 주문유형**: 지정가 주문 위주
- **특징**: 실적 발표 등 장 마감 후 뉴스에 대한 반응 거래가 주로 발생. 유동성은 정규시간 대비 현저히 낮으며, Reg NMS 보호가 완화된 환경
- **종료 시점**: 20:00 ET에 모든 미체결 주문이 자동 취소(Order Flush)되며, 이는 현행 거래일의 종료를 의미

---

## 3. 23/5 확장 제안 (SR-NASDAQ-2025-106)

NASDAQ은 2025년 SEC에 규칙변경안 SR-NASDAQ-2025-106을 제출하여, 기존 16시간 거래를 **23시간/주 5일** 모델로 확장하는 방안을 제안하였다. 이는 단순한 시간 연장이 아닌, 거래일 수명주기(Session Lifecycle)의 **근본적 재설계**를 의미한다.

### 3.1 이중 세션 모델 (Bifurcated Session Model)

NASDAQ은 거래일을 법적, 기술적, 운영적으로 구분되는 두 개의 세션으로 분할한다.

| 세션 | 시간 (ET) | 운영시간 | 성격 |
|------|-----------|----------|------|
| **Day Session** | 04:00~20:00 | 16시간 | 기존 운영 구조 유지 (Pre-Market + Regular + Post-Market) |
| **Maintenance Pause** | 20:00~21:00 | 1시간 | 거래 중단, 시스템 정비, 거래일 전환 |
| **Night Session** | 21:00~04:00 | 7시간 | 신규 도입, 제한적 주문유형, 격리된 유동성 풀 |

- **거래주 시작**: 일요일 21:00 ET (Night Session 개시)
- **거래주 종료**: 금요일 20:00 ET (Day Session 종료)
- **Night Session 운영일**: 일요일~목요일 (주 5회)

### 3.2 "Double Flush" 메커니즘 (20:00 ET + 04:00 ET)

23/5 모델의 핵심 리스크 관리 장치는 **이중 플러시(Double Flush)** 메커니즘이다.

**제1차 플러시 (20:00 ET)**:
- Day Session 종료 시점에 NASDAQ 주문대장(Order Book)의 **모든 미체결 주문을 일괄 취소**
- Day, GTC, Extended Hours 등 모든 유형의 주문이 대상
- 이를 통해 Day Session과 Night Session 사이에 **깨끗한 상태(Clean Slate)**를 확보
- 20:00 ET 이전 정보를 기반으로 설정된 주문이 야간 시장 환경에서 부적절하게 체결되는 것을 방지

**제2차 플러시 (04:00 ET)**:
- Night Session 종료 시점에 야간 주문대장의 **모든 미체결 주문을 일괄 취소**
- 참여자는 04:00 ET Pre-Market 개시를 위해 주문을 **완전히 재입력**해야 함
- 유럽/아시아 거시경제 뉴스로 인해 공정가치가 근본적으로 변동했을 수 있으므로, 야간 주문의 자동 이월을 차단

이 메커니즘의 핵심 목적은 **진부화된 주문(Stale Orders)**의 체결을 방지하고, 참여자가 각 세션의 시장 상황에 맞게 능동적으로 주문을 관리하도록 강제하는 것이다.

### 3.3 Trade Date 로직 (20:00 ET 기준)

미국 금융 인프라는 **20:00 ET**를 거래일(Trade Date) 경계로 사용한다. DTCC/NSCC 및 은행 시스템의 결제주기와 정합성을 확보하기 위한 설계이다.

#### 거래일 할당 시나리오

| 시나리오 | 거래 시점 | 세션 | 거래일 (Trade Date) | 결제일 (T+1) |
|----------|-----------|------|---------------------|-------------|
| **A** | 월요일 15:30 ET | Regular Market | 월요일 (T) | 화요일 |
| **B** | 월요일 19:55 ET | Post-Market (Day) | 월요일 (T) | 화요일 |
| **C** | 월요일 20:00~21:00 ET | Maintenance Pause | 거래 불가 | - |
| **D** | 월요일 21:05 ET | Night Session | **화요일** (T+1) | 수요일 |
| **E** | 화요일 02:30 ET | Night Session | 화요일 (T+1) | 수요일 |
| **F** | 화요일 04:30 ET | Pre-Market (Day) | 화요일 (T+1) | 수요일 |
| **G** | 일요일 21:05 ET | Night Session (주 개시) | **월요일** | 화요일 |

**핵심 원칙**: "월요일 밤" Night Session의 거래는 법적으로 "화요일"에 해당한다. 이는 현금 결제가 항상 연방준비제도(Federal Reserve)의 Fedwire 시스템 운영일에 이루어지도록 보장하기 위함이다.

### 3.4 GTC 주문 완전 폐지 (2026년 2월~)

23/5 모델의 도입과 함께, NASDAQ은 **Good-Til-Cancelled(GTC) 주문을 시스템에서 완전히 폐지**한다.

- **시행 시기**: 2026년 2월
- **근거**: GTC 주문은 세션 간 경계를 넘어 무기한 존재할 수 있어, Double Flush 메커니즘의 목적을 무력화할 위험이 있음
- **대안**: 참여자는 각 세션별로 적합한 Time-in-Force(TIF) 지시를 사용해야 하며, Day 또는 SDAY(System Day) TIF는 해당 세션의 물리적 플러시에 의해 엄격히 제한됨
- **영향**: 장기 지정가 주문 전략을 사용하는 참여자는 자동 주문 관리 시스템을 구축하거나 매 세션 개시 시 주문을 재입력해야 함

---

## 4. Night Session 상세

Night Session은 23/5 모델에서 새롭게 도입되는 운영 구조로, 기존 Day Session과는 본질적으로 다른 규제 및 운영 환경을 가진다.

### 4.1 허용 주문유형

Night Session에서는 시장 복잡성과 변동성 리스크를 최소화하기 위해 주문유형을 극도로 제한한다.

| 주문유형 | 허용 여부 | 비고 |
|----------|-----------|------|
| **Limit Order (지정가)** | **허용** | 가격 확실성 확보를 위한 기본 주문 |
| **Intermarket Sweep Order (ISO)** | **허용** | Reg NMS 면제 환경에서의 다중 가격 수준 소화용 |

### 4.2 금지 주문유형

| 주문유형 | 금지 사유 |
|----------|-----------|
| **Market Order (시장가)** | 유동성이 얇은 환경에서 극단적 불리한 가격 체결 위험 |
| **Pegged Order** | 야간에는 통합 NBBO(National Best Bid and Offer)가 존재하지 않아 기준가 부재 |
| **MOO/LOO (Market/Limit-on-Open)** | Night Session에는 Opening Cross가 없음 |
| **MOC/LOC (Market/Limit-on-Close)** | Night Session에는 Closing Cross가 없음 |
| **Discretionary Order** | 매칭엔진 복잡성 감소 및 야간 유동성 환경에서의 예측 불가능한 체결 방지 |

### 4.3 Reg NMS Rule 611 미적용 -- 격리된 유동성 풀

Regular Market Session(09:30~16:00 ET)에서는 Rule 611(Order Protection Rule)이 적용되어, 타 거래소의 보호호가(Protected Quote)보다 불리한 가격으로의 체결(Trade-Through)이 금지된다. 그러나 **Night Session은 "Extended Hours"로 분류되어 Rule 611이 적용되지 않는다.**

이는 다음과 같은 실질적 의미를 갖는다:

- **보호 NBBO 부재**: 야간에는 통합된 최우선호가가 존재하지 않음
- **주문 회송(Routing) 의무 없음**: NASDAQ이 AAPL을 $150.00에 제시하고 Blue Ocean ATS가 $149.90에 제시하더라도, NASDAQ은 Blue Ocean으로 주문을 회송할 의무가 없음
- **격리된 유동성 풀**: Night Session은 사실상 독립적 유동성 풀(ECN과 유사)로 기능하며, 가격 형성(Price Discovery)이 해당 거래소에 국한됨

### 4.4 Clearly Erroneous Execution (Rule 11890): 야간 확대 허용범위

LULD(Limit Up-Limit Down) 메커니즘이 정규시간에만 적용되므로, Night Session에서는 **명백한 오류 체결(Clearly Erroneous Execution, CEE)** 규칙(Rule 11890)이 시장 무결성의 주요 방어선 역할을 한다.

| 구분 | 주간 (Regular Market) | 야간 (Night Session) |
|------|----------------------|---------------------|
| **LULD 적용** | 적용 (5분 내 5% 변동 시 거래 일시 정지) | **미적용** |
| **CEE 검토 기준** | 약 **3%** 이탈 | 약 **20%** 이탈 |
| **체결 취소 판단** | 엄격한 기준 적용 | 넓은 스프레드를 감안한 완화 기준 |

야간의 20% 허용범위는 유동성이 극도로 제한된 환경에서 정상적 스프레드 확대를 반영한 설계이다.

### 4.5 Volatility Guards (내부 Collars)

LULD 부재를 보완하기 위해, NASDAQ은 자체적인 **변동성 완화장치(Volatility Guards)**를 Night Session에 적용한다.

- **내부 칼라(Internal Collars)**: 최근 체결가(Last Sale Price) 대비 과도하게 공격적인 가격의 주문을 자동으로 거부
- **목적**: 얇은 주문대장을 단일 대형 주문이 전면 소화하여 발생하는 "Flash Crash" 시나리오 방지
- **작동 방식**: 정적 가격 밴드가 아닌, 동적으로 조정되는 참조가격 기반 필터

---

## 5. 기술 인프라

### 5.1 포트 분리: Day Ports vs Night Ports (물리적/논리적 분리)

NASDAQ은 Night Session을 위해 **별도의 논리적 포트(Logical Ports)**를 의무화한다. 기존 Day Session 연결을 Night Session에 사용할 수 없다.

| 포트 유형 | 운영시간 (ET) | 특성 |
|-----------|-------------|------|
| **Day Ports** | 04:00~20:00 | 기존 인프라, 해당 시간 외 주문 수신 거부 (Hard-Coded) |
| **Night Ports** | 21:00~04:00 | 신규 논리적 엔티티, 별도 주문 및 비용 발생 |

**리스크 격리(Risk Isolation)의 원칙**: 포트 분리를 통해 NASDAQ은 Night Session을 위한 독립적 매칭엔진 인스턴스 또는 파티션을 운영할 수 있다. Night Session 인스턴스에서 치명적 소프트웨어 장애(메모리 누수, 무한루프 등)가 발생하더라도, **Day Session 인프라는 영향을 받지 않는다**. 야간 장애의 "폭발 반경(Blast Radius)"이 물리적으로 차단되는 구조이다.

### 5.2 OUCH 5.0 프로토콜

OUCH는 NASDAQ의 네이티브 저레이턴시 바이너리 주문입력 프로토콜이다.

| 항목 | 사양 |
|------|------|
| **형식** | 바이너리(Binary) |
| **메시지 구조** | 고정 길이(Fixed-Length) |
| **설계 철학** | 속도 우선, FIX 대비 핸드셰이킹 오버헤드 제거 |
| **세션 구분** | Enter Order 메시지의 TIF 값(예: 99999 for Market Day)을 Day Port/Night Port에 따라 차별 해석 |
| **재접속 특성** | FIX와 달리 풍부한 체결보고 이력을 제공하지 않으므로, 참여자의 실시간 노출(Exposure) 추적 필수 |

### 5.3 ITCH 데이터 피드

ITCH는 NASDAQ의 아웃바운드 독점 데이터 피드로, **모든 개별 주문과 체결 정보(Level 3 데이터)**를 방송한다.

- **Complete Feed**: 23시간 전체 사이클을 단일 스트림으로 통합
- **Night Session Feed**: 야간 데이터만 수신하고자 하는 참여자를 위한 별도 피드 (대역폭 최적화)
- **SIP 대비 우위**: SIP(Consolidated Tape)가 최우선호가(Top-of-Book)만 집계하는 반면, ITCH는 **전체 호가 심도(Full Depth-of-Book)**를 제공
- **야간 중요성**: 유동성이 희박한 Night Session에서 주문대장의 "공백(Air Pockets)"을 파악하여 적절한 주문 규모를 결정하는 데 필수적

### 5.4 Core FIX Gateway

초저지연이 불필요한 참여자를 위해, NASDAQ은 **Core FIX(Financial Information eXchange)** 게이트웨이를 지원한다.

- FIX 메시지를 OUCH 명령으로 변환하여 매칭엔진에 전달
- 기존 FIX 인프라를 보유한 **해외 증권사(한국 증권사 포함)**의 진입 장벽을 낮춤
- OUCH 개발 자원이 부족한 참여자에게 실질적 대안 제공
- FIX Tag 75(TradeDate)를 통해 Night Session 거래의 결제주기를 명확히 식별 가능

### 5.5 Eqlipse 스택: 클라우드 네이티브(AWS), FPGA 가속, 커널 바이패스

Eqlipse는 NASDAQ의 23/5 운영을 뒷받침하는 차세대 기술 플랫폼이다.

| 기술 요소 | 상세 |
|-----------|------|
| **클라우드 네이티브** | AWS 파트너십 기반, 매칭엔진 인스턴스 동적 확장 가능 |
| **FPGA 가속 게이트웨이** | 하드웨어 수준의 주문 전처리로 결정론적 레이턴시 보장 |
| **커널 바이패스 네트워킹** | Solarflare/Xilinx 기반 기술로 OS 커널을 우회하여 네트워크 스택 지연 최소화 |
| **마이크로서비스 아키텍처** | 개별 컴포넌트(게이트웨이, 시장데이터 퍼블리셔 등) 독립 배포 가능 |

### 5.6 Rolling Restart / Evergreen Update

24시간 운영 환경에서 가장 핵심적 기술 요건은 **다운타임 없는 시스템 업데이트**이다.

- **Rolling Restart**: 매칭엔진이 활성 상태인 동안 개별 컴포넌트를 순차적으로 재시작
- **Evergreen Update**: 소프트웨어 패치를 무중단으로 적용하여, 1시간의 Maintenance Pause 내에 필수 업데이트를 완료
- **하드웨어 페일오버**: Maintenance Pause를 활용하여 하드웨어 교체 및 메모리 캐시 플러싱 수행

---

## 6. 리스크 관리

### 6.1 LULD: 정규시간만 적용

Limit Up-Limit Down(LULD) 메커니즘은 **Regular Market Hours(09:30~16:00 ET)에서만 작동**한다. 이는 LULD가 다수의 거래소가 동시에 운영되는 통합 시장 환경을 전제로 설계되었기 때문이다.

- 정규시간: 5분 내 참조가격 대비 약 5% 이상 변동 시 거래 일시 정지(Trading Pause)
- Pre-Market / Post-Market / Night Session: LULD 미적용

### 6.2 야간 변동성 관리

LULD 부재를 보완하는 Night Session의 변동성 관리 체계:

| 방어선 | 메커니즘 | 작동 방식 |
|--------|----------|-----------|
| **제1선** | 주문유형 제한 | Market Order 금지로 극단적 체결가 방지 |
| **제2선** | Volatility Guards | 최근 체결가 대비 과도한 가격 주문 자동 거부 |
| **제3선** | CEE Rule 11890 | 체결 후 20% 이상 이탈 시 명백한 오류로 판정, 체결 취소 가능 |
| **제4선** | Double Flush | 세션 간 진부화된 주문 자동 제거 |

### 6.3 브로커 고객 고지 의무

SEC 및 FINRA는 연장시간 거래에 대해 브로커가 고객에게 다음 리스크를 **명시적으로 고지**할 것을 의무화한다:

1. **유동성 저하(Lower Liquidity)**: 원하는 가격에 주문 체결이 어려울 수 있음
2. **변동성 증가(Higher Volatility)**: 정규시간 대비 가격 변동폭이 크게 확대될 수 있음
3. **가격 변동(Changing Prices)**: 표시 가격이 통합 시장 가치를 반영하지 못할 수 있음
4. **시장 비연결(Unlinked Markets)**: 한 거래소의 가격이 다른 거래소의 가격과 일치하지 않을 수 있음

---

## 7. 청산 및 결제 연동

24시간 거래의 가장 핵심적 병목지점은 주문 매칭이 아닌 **청산(Clearing)**이다. "거래시간"(24/7)과 "은행시간"(9-5)의 괴리가 심각한 신용 및 결제 리스크를 초래한다.

### 7.1 DTCC/NSCC UTC 24x5 확장 (Q3 2026 목표)

National Securities Clearing Corporation(NSCC)은 24/5 모델 지원을 위해 운영시간을 확장하고 있다.

| 항목 | 현행 | 확장 후 |
|------|------|---------|
| **청산 운영시간** | 은행 영업시간 기반 | UTC 24x5 연속 운영 |
| **목표 시행 시기** | - | **2026년 Q3** |
| **핵심 시스템** | 기존 배치 처리 | Universal Trade Capture (UTC) |
| **거래 보증** | T+1 일괄 처리 | 실시간 처리 |

### 7.2 실시간 Novation (CCP 보증)

현행 시스템에서 거래는 배치(Batch) 방식으로 처리되는 경우가 많다. 확장된 모델에서는 **즉시 중앙거래상대방(CCP) 보증**이 제공된다.

- **작동 원리**: NASDAQ에서 새벽 2시에 매칭된 거래가 NSCC에 보고되면, **신용 리스크가 양 거래 당사자에서 CCP로 즉시 이전**
- **의의**: 참여자가 비유동적 야간 시간에도 익명성과 신뢰를 가지고 거래할 수 있는 기반
- **실시간 Novation**: 배치 처리가 아닌, 거래 단위별 실시간 청산 보증 제공

### 7.3 야간 증거금: VaR 기반 Intraday 마진콜

야간 운영은 회원사의 증거금 부담을 증가시킨다.

| 구분 | 내용 |
|------|------|
| **증거금 산정** | VaR(Value-at-Risk) 기반 변동성 증거금 |
| **마진콜 시점** | 은행 영업시간 외에도 일중(Intraday) 마진콜 가능 |
| **리스크 요인** | 은행 폐장 시간에 시장이 급변할 경우 마진콜 충족 불가 위험 |
| **대응 전략** | VaR 가산금(Charge) 상향 또는 야간 활동 회원에 대한 추가 담보 요구 |

### 7.4 리테일 100% 사전예탁(Pre-funding) 정책

다수의 브로커는 야간 거래의 신용 리스크를 사실상 제거하기 위해 **리테일 고객에 대한 100% 사전예탁(Pre-funding)** 정책을 적용한다.

- **증거금 레버리지 금지**: 야간 거래 시 마진(신용) 매매 불허
- **근거**: 새벽 3시에 고객 계좌가 손실로 인해 마이너스가 되어도, 마진콜을 발행하거나 충족시킬 수 있는 시간이 없음
- **실질적 효과**: 리테일 투자자의 야간 손실이 자기자본 범위 내로 제한되어 브로커의 신용 노출 제거

---

## 8. 경쟁 환경 비교

### NASDAQ Night Session vs Blue Ocean ATS vs 24X National Exchange

| 비교 항목 | NASDAQ Night Session | Blue Ocean ATS | 24X National Exchange |
|-----------|---------------------|----------------|----------------------|
| **법적 구조** | 국가 증권거래소 (National Securities Exchange) | 대체거래시스템 (ATS, Broker-Dealer) | 국가 증권거래소 |
| **규제 체계** | Section 19(b) / SRO 규칙 | Regulation ATS | Section 19(b) / SRO 규칙 |
| **운영시간 (ET)** | 21:00~04:00 (7시간) | 20:00~04:00 (8시간) | 23시간/7일 (계획) |
| **시장 데이터** | ITCH (독점 + SIP) | 독점 피드 (SIP/벤더 배포) | 독점 피드 |
| **청산 방식** | NSCC (실시간 Novation) | NSCC (T+1 보고) | NSCC (실시간 Novation) |
| **주요 참여자** | 전 회원 (리테일 + 기관) | 리테일 어그리게이터 중심 (Robinhood, 삼성증권 등) | 리테일 + 기관 |
| **가격 보호** | Rule 11890 (엄격 밴드) | 내부 ATS 통제 | 거래소 규칙 |
| **유동성 원천** | 중앙지정가주문대장 (CLOB) | 마켓메이커 / 리테일 흐름 | 중앙지정가주문대장 |
| **선발 우위** | 거래소 브랜드 신뢰성 | 아시아 리테일 파트너십 구축 완료 | 레거시 부채 없는 신규 기술 스택 |

**경쟁 분석**:
- **Blue Ocean ATS**: 선발 우위와 한국 리테일 브로커와의 깊은 파트너십 보유. 그러나 거래상대방 리스크 및 규제 견고성 측면에서 거래소 대비 열위
- **NASDAQ**: 거래소의 "안전성" 프리미엄 제공. Blue Ocean에 참여하지 않는 기관투자자가 NASDAQ 규제 Night Session에는 참여할 가능성
- **24X**: "파괴자(Disruptor)" 위협. 레거시 기술 부채 없이 24/7 전용으로 설계된 거래소로서, NASDAQ의 개조(Retrofit) 스택 대비 낮은 비용 또는 우월한 기술을 제공할 잠재력 보유

---

## 9. SIFMA 가이드라인 및 운영 회복력

Securities Industry and Financial Markets Association(SIFMA)은 24/5 전환이 시스템적 리스크를 유발하지 않도록 워킹그룹을 구성하여 가이드라인을 수립하였으며, NASDAQ은 이를 대부분 채택하고 있다.

### 9.1 야간 인력 운영 ("Eyes on Glass")

23/5 모델은 전통적인 "Follow-the-Sun" 지원 모델에 도전한다.

| 운영 영역 | 요구사항 |
|-----------|----------|
| **거래 감시** | Night Session 기간 동안 "Eyes on Glass" 감시 역량 유지 필수 |
| **인력 배치** | 아시아 시간대 트레이딩 데스크 운영 또는 미국 내 교대근무(Rotation Shift) |
| **권한 위임** | 야간 운영 책임자에게 시장 중단 및 Self-Help 선언 권한 명확히 위임 |

### 9.2 사이버보안 SOC 24/7

- **보안운영센터(SOC)**: 24시간 365일 완전 가동 필수
- **야간 취약성**: "조용한" 야간 시간대는 사이버 공격의 주요 표적이 될 수 있음
- **모니터링 범위**: 네트워크 침입 탐지, 이상 거래 패턴 감시, DDoS 방어 등 포함

### 9.3 사고 대응 및 Self-Help 선언 권한

SIFMA 가이드라인은 야간 사고 발생 시 명확한 에스컬레이션 경로를 강조한다.

- **시나리오**: 새벽 2시에 매칭엔진 장애 발생 시, 시장 중단(Halt) 또는 "Self-Help" 상황 선언 권한이 누구에게 있는가?
- **NASDAQ 대응**: 야간 운영 책임자(Night-Shift Operations Lead)에게 의사결정 권한을 명시적으로 위임하는 프로토콜 수립
- **Self-Help 선언**: 다른 거래소의 시스템 장애 시, 해당 거래소의 보호호가를 무시하고 자체적으로 거래를 계속할 수 있는 권한

---

## 10. KRX와의 비교 및 시사점

### 기술, 규제, 운영 측면 비교

| 비교 항목 | NASDAQ 23/5 | KRX 현행 |
|-----------|-------------|----------|
| **거래시간** | 23시간/주 5일 (제안) | 약 6.5시간 (정규) + 시간외 |
| **매칭엔진** | Genium INET → Eqlipse (클라우드 네이티브) | EXTURE 3.0 (50µs, 9.4억건/일) |
| **프로토콜** | OUCH 5.0 (바이너리), FIX, ITCH | KRX 독자 프로토콜, FIX |
| **야간 거래** | Night Session (21:00~04:00 ET) 신설 | 미운영 |
| **청산 인프라** | NSCC 24x5 실시간 Novation (Q3 2026) | KSD 영업시간 내 처리 |
| **결제 연동** | Fedwire 연동, T+1 | BOK-Wire+ 연동, T+1 (2024~) |
| **변동성 관리** | LULD(주간) + CEE + Volatility Guards(야간) | 가격제한폭(상하한가) + VI(Volatility Interruption) |
| **포트 분리** | Day/Night 물리적 분리 | 단일 세션 구조 |
| **GTC 주문** | 2026.2 폐지 | 운용 중 |
| **규제 프레임워크** | Reg NMS(주간) / 면제(야간) 이원 체계 | 자본시장법 단일 체계 |

### KRX 도입 시 핵심 권고사항

**전략적 권고**:

1. **정비 창(Maintenance Window) 도입**: 24시간 연속 운영을 즉시 시도하지 말고, NASDAQ의 20:00~21:00 ET 모델처럼 안전한 거래일 전환 및 시스템 정비를 위한 중단 시간 확보. 청산 시스템의 날짜 처리 오류 리스크 감소
2. **거래소 브랜드 활용**: ATS 대비 규제된 SRO로서의 감시, 명확한 오류 정책, 자본 요건을 강조하여 기관 자본 유치. Blue Ocean 등 "무규제" 야간 시장과의 차별화
3. **KSD 동시 협력**: 한국예탁결제원을 초기부터 핵심 파트너로 참여시켜 실시간 거래 포착 및 청산 보증 체계 구축. 이 없이는 미담보 신용 리스크만 축적

**기술적 권고**:

4. **매칭엔진 분리**: 야간 세션을 위한 독립 논리 포트 또는 별도 매칭엔진 파티션 사용. 저거래량 야간 세션의 기술적 장애가 KOSPI/KOSDAQ 정규 시장 개장에 절대 영향을 미치지 않도록 "에어갭(Air-Gap)" 리스크 격리
5. **주문유형 단순화**: 야간 세션은 지정가 주문만 허용. 시장가, 페그, 복합 알고리즘 주문 제거. 매칭엔진 부하 감소 및 얇은 시장에서의 "Fat Finger" 오류 보호
6. **프로토콜 정합성**: KRX FIX 게이트웨이 및 KOSCOM 인프라가 "익일(Next Day)" 거래 보고 플래그를 처리할 수 있도록 보장. 체결보고(Execution Report)의 Tag 75(TradeDate)를 통해 참여자에게 결제주기 명확히 전달

**규제적 권고**:

7. **"연장시간" 명시적 정의**: 외국 시장이 폐장된 상태에서 충족 불가능한 "최선 집행(Best Execution)" 또는 "Trade-Through" 의무를 면제하는 별도의 규제 범주 신설
8. **엄격한 변동성 칼라 도입**: 한국 주식이 야간에 유동적 참조가격을 가지지 못할 수 있으므로, 국내 종가 대비 ±15% 등 엄격한 가격 밴드를 적용하여 비현실적 벤치마크 설정을 방지

---

## 참고자료

1. Nasdaq Proposes Near-24-Hour Trading | Cadwalader, Wickersham & Taft LLP - JDSupra
   [jdsupra.com/legalnews/nasdaq-proposes-nea...](https://www.jdsupra.com/legalnews/nasdaq-proposes-near-24-hour-trading-6538509/)

2. Nasdaq looks to extend trading hours as Wall Street eyes 24/7 move | Daily Sabah
   [dailysabah.com/business/finance/nasdaq-looks...](https://www.dailysabah.com/business/finance/nasdaq-looks-to-extend-trading-hours-as-wall-street-eyes-247-move)

3. Nasdaq Seeks SEC Approval For 23-Hour, Five-Day Trading Schedule | Nasdaq
   [nasdaq.com/articles/nasdaq-seeks-sec-app...](https://www.nasdaq.com/articles/nasdaq-seeks-sec-approval-23-hour-five-day-trading-schedule)

4. Blue Ocean ATS Joins Pyth Network: Institutional Overnight Hours US Equity Data
   [blueocean-tech.io/2025/09/25/pyth-blue-ocean-at...](https://blueocean-tech.io/2025/09/25/pyth-blue-ocean-ats-joins-pyth-network-institutional-overnight-hours-us-equity-data/)

5. Blue Ocean: Overnight trading could reach 10% of total volumes | Global Trading
   [globaltrading.net/blue-ocean-overnight-trading-...](https://www.globaltrading.net/blue-ocean-overnight-trading-could-reach-10-of-total-volumes/)

6. Market Spotlight: 24 Hour Trading | BlackRock
   [blackrock.com/corporate/literature/whitepap...](https://www.blackrock.com/corporate/literature/whitepaper/blackrock-market-spotlight-24-hour-trading.pdf)

7. Nasdaq Proposes to Extend Trading Hours During Weekdays | Practical Law - Westlaw
   [content.next.westlaw.com/practical-law/document/I52f98...](https://content.next.westlaw.com/practical-law/document/I52f988cfdaa111f098028aa0904d44cc/Nasdaq-Proposes-to-Extend-Trading-Hours-During-Weekdays?viewType=FullText&transitionType=Default&contextData=(sc.Default))

8. SR-NASDAQ-2025-106 | NASDAQ Listing Center
   [listingcenter.nasdaq.com/assets/rulebook/nasdaq/filing...](https://listingcenter.nasdaq.com/assets/rulebook/nasdaq/filings/SR-NASDAQ-2025-106.pdf)

9. Extended Trading Hours: A New Frontier for US Equity Markets | SIFMA
   [sifma.org/news/blog/extended-trading-ho...](https://www.sifma.org/news/blog/extended-trading-hours-a-new-frontier-for-us-equity-markets)

10. Self-Regulatory Organizations; The Nasdaq Stock Market LLC; Notice of Filing of Proposed Rule Change | Federal Register
    [federalregister.gov/documents/2026/01/13/2026-004...](https://www.federalregister.gov/documents/2026/01/13/2026-00416/self-regulatory-organizations-the-nasdaq-stock-market-llc-notice-of-filing-of-proposed-rule-change)

11. Nasdaq Global Trading Hours FAQs | Nasdaq
    [nasdaq.com/docs/nasdaq-global-trading-ho...](https://www.nasdaq.com/docs/nasdaq-global-trading-hours-faqs)

12. 24-Hour Market Trading Regulation Issues | Exegy
    [exegy.com/24-hour-market-trading-regula...](https://www.exegy.com/24-hour-market-trading-regulation-issues/)

13. Nasdaq Proposes "Night Session" Trading | Find Know Do
    [findknowdo.com/news/01/13/2026/nasdaq-propos...](https://www.findknowdo.com/news/01/13/2026/nasdaq-proposes-night-session-trading)

14. Future-Ready Markets - Preparing for 24/7 Trading | Nasdaq
    [nasdaq.com/solutions/fintech/resources/w...](https://www.nasdaq.com/solutions/fintech/resources/whitepapers/future-ready-markets-continuous-trading-hours)

15. O*U*C*H Protocol Specification | Nasdaq Trader
    [nasdaqtrader.com/content/technicalsupport/spec...](https://www.nasdaqtrader.com/content/technicalsupport/specifications/TradingProducts/ouch2.0a.pdf)

16. Two Sides to Every Match | Nasdaq
    [nasdaq.com/articles/two-sides-every-matc...](https://www.nasdaq.com/articles/two-sides-every-match-2014-10-08)

17. NASDAQ TotalView-ITCH 4.1 Specification | Nasdaq Trader
    [nasdaqtrader.com/content/technicalsupport/spec...](https://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/nqtv-itch-v4_1.pdf)

18. Protocol Quick Reference | Nasdaq Trader
    [nasdaqtrader.com/content/ProductsServices/Trad...](https://www.nasdaqtrader.com/content/ProductsServices/Trading/Protocols_quickref.pdf)

19. Achieving Ultra-Low Latency in Trading Infrastructure | Exegy
    [exegy.com/ultra-low-latency-trading-inf...](https://www.exegy.com/ultra-low-latency-trading-infrastructure/)

20. Nasdaq Reaches 'New Base Camp' with Eqlipse | Markets Media
    [marketsmedia.com/nasdaq-reaches-new-base-camp-...](https://www.marketsmedia.com/nasdaq-reaches-new-base-camp-with-eqlipse/)

21. THE SHIFT TO 24X5 TRADING | DTCC
    [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/theshiftto24x5trading.pdf)

22. DTCC's NSCC to Increase Clearing Hours to Support Extended Trading | DTCC
    [dtcc.com/news/2025/march/18/dtccs-nscc...](https://www.dtcc.com/news/2025/march/18/dtccs-nscc-to-increase-clearing-hours-to-support-extended-trading)

23. DTCC prepares for 24-hour trading onslaught | Global Trading
    [globaltrading.net/dtcc-prepares-for-24-hour-tra...](https://www.globaltrading.net/dtcc-prepares-for-24-hour-trading-onslaught/)

24. 24X National Exchange; Application for Registration | SIFMA
    [sifma.org/advocacy/letters/24x-national...](https://www.sifma.org/advocacy/letters/24x-national-exchange-application-for-registration)

25. Equity Market Structure | SIFMA
    [sifma.org/issues/market-structure/equit...](https://www.sifma.org/issues/market-structure/equity-market-structure)

26. Extended Trading Hours | SIFMA
    [sifma.org/issues/market-structure/exten...](https://www.sifma.org/issues/market-structure/extended-trading-hours)

27. The Future of Trading Is Always On: Why Market Infrastructure Must Lead the Way | Nasdaq
    [nasdaq.com/articles/fintech/always-on-ma...](https://www.nasdaq.com/articles/fintech/always-on-market-infrastructure-must-lead-way)
