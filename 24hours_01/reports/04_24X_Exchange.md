# 24X National Exchange 거래 운영 체제 분석

## 1. 기관 개요

### 1.1 설립 배경 및 SEC 승인 경과

24X National Exchange LLC(이하 "24X")는 미국 증권거래위원회(SEC)로부터 국가 증권거래소(National Securities Exchange)로의 등록을 승인받아, **미국 최초의 23시간, 주 5일(23/5) 운영 증권거래소**로 역사적 의미를 갖는다. SEC는 2024년 11월 24X의 Form 1 신청을 최종 승인하였으며, 이후 24X는 2026년 2월 거래를 개시하였다.

24X는 Point72 Ventures를 포함한 주요 기관 투자자들로부터 자금을 유치하여 설립되었다. Point72 Ventures는 Steve Cohen이 운영하는 Point72 Asset Management의 벤처캐피탈 부문으로, 24X에 대한 전략적 투자를 통해 미국 주식시장의 시간적 장벽 해체에 대한 기관투자자들의 확고한 수요를 시장에 입증하였다.

### 1.2 전략적 존재 의의

수십 년간 미국 주식시장의 기본 아키텍처는 동부시간(ET) 기준 오전 9:30~오후 4:00라는 경직된 시간 창(temporal window)에 종속되어 왔다. 24X 모델은 이러한 시간적 장벽을 근본적으로 해체하여, 아시아태평양(APAC) 및 유럽-중동-아프리카(EMEA) 지역에서 급증하는 기관 및 리테일 수요에 대응하는 근연속적(near-continuous) 글로벌 유동성 접근 체계를 구축하였다.

---

## 2. 세션 아키텍처

24X 거래일(Trading Day)은 하나의 연속적인 23시간 운영 블록으로 구성된다. 거래 주기는 오후 9:00 ET에 공식 개시되어 다음 날 오후 8:00 ET에 종료된다. 이 시간적 전환은 거래소의 일일 개시 시점을 아시아 시장의 개장과 정렬시켜, 화요일의 미국 주식 거래일이 뉴욕 기준 월요일 늦은 밤에 시작될 수 있도록 한다.

| 세션 구분 | 시작 시간 (ET) | 종료 시간 (ET) | 운영 및 규제 특성 |
|---|---|---|---|
| **24X Market Session** | 21:00 | 04:00 | 야간 거래 창구. Reg NMS 미적용, LULD 비활성. 독자적 24X Price Bands 적용. Market Order 및 Pegged Order 금지 |
| **Pre-Market Session** | 04:00 | 09:30 | 기존 미국 장외시간 전 거래와 정렬. 표준 장전 리스크 통제 적용 |
| **Core Market Session** | 09:30 | 16:00 | 미국 정규 거래시간. 완전한 Reg NMS 준수 의무. SIP 완전 가동, 공식 NBBO 확립. LULD 메커니즘 완전 활성 |
| **Post-Market Session** | 16:00 | 20:00 | 전통적 장후 거래. 일일 시스템 리셋으로 직접 전환 |
| **Trading Pause** | 20:00 | 21:00 | 거래 완전 중단. 매칭엔진 정지, 미체결 주문 전량 강제 취소(Hard Flush), 배치 처리 및 시퀀스 리셋 수행 |

### 2.1 24X Market Session (21:00~04:00 ET): 야간 세션

24X Market Session은 24X 거래소의 핵심적 혁신 요소로, 전통적 미국 시장이 완전히 폐장된 시간대에 운영되는 야간 거래 창구이다. 이 세션의 가장 중요한 규제적 특징은 다음과 같다:

- **Reg NMS Rule 611(Order Protection Rule) 미적용**: SIP가 오프라인 상태이므로 공식 NBBO가 존재하지 않아 거래소 간 호가 보호 의무가 발생하지 않음
- **LULD(Limit Up-Limit Down) 메커니즘 비활성**: LULD 계산이 SIP의 통합 데이터에 전적으로 의존하므로, SIP 비가동 시 LULD 보호 기능이 완전히 정지
- **독자적 24X Price Bands로 변동성 관리**: LULD를 대체하는 자체 변동성 관리 체계 운영
- **Market Order 및 Pegged Order 전면 금지**: 유동성이 극히 얕은 야간 시장에서의 가격 왜곡 방지를 위해 지정가 주문(Limit Order)만 허용

이 세션은 격리된 유동성 풀(isolated liquidity pool)로 기능하며, 거래 참여자들은 완전히 독립적인 리스크 관리 체계 하에서 거래한다.

### 2.2 Pre-Market Session (04:00~09:30 ET)

Pre-Market Session은 기존 미국 거래소들의 장전 거래와 시간적으로 정렬되며, 표준 장전 리스크 통제 장치가 적용된다. 이 세션에서 SIP 데이터는 제한적이거나 비활성 상태로 유지된다. 24X Market Session에서 Pre-Market Session으로의 전환은 완전히 연속적(seamless)으로 이루어진다. 거래 중단이나 주문 불균형 공시, 별도의 교차 알고리즘 없이 매칭엔진이 수신된 주문을 시간 순서에 따라 계속 처리하며, 세션 파라미터에 따라 특정 주문 유형의 적격성만 자동으로 활성화 또는 비활성화된다.

### 2.3 Core Market Session (09:30~16:00 ET): 완전한 Reg NMS 적용

Core Market Session은 미국 정규 주식거래 시간을 나타내며, 다음의 완전한 규제 체계가 적용된다:

- **완전한 Reg NMS 준수 의무화**: Rule 611(Order Protection Rule) 완전 적용
- **SIP 완전 가동**: 모든 국가 거래소의 최우선호가 및 최종체결가 데이터를 집계하여 공식 통합 NBBO를 산출 및 배포
- **LULD 메커니즘 완전 활성**: 시장 전반의 서킷브레이커 및 변동성 차단 장치 가동
- **전체 주문 유형 허용**: Market Order, Pegged Order 포함 모든 주문 유형 이용 가능

### 2.4 Post-Market Session (16:00~20:00 ET)

Post-Market Session은 전통적인 장후 거래를 수용하며, 기관 마켓메이커의 참여가 통상 감소함에 따라 변동성 파라미터가 확대된다. 이 세션은 일일 시스템 리셋으로 직접 전환되며, 이 세션의 최종 체결가는 다음 24X Market Session의 Reference Price 결정에 1순위 기준으로 활용된다.

### 2.5 Trading Pause (20:00~21:00 ET): 전체 주문 강제 취소(Hard Flush)

Trading Pause는 24X 거래소 운영의 핵심적 기술 유지보수 시간이다. 정확히 오후 7:59:59 ET에 MEMX Memoir 매칭엔진은 시스템적 **"Hard Flush"**를 실행한다. 24X Book 상의 모든 미체결 잔존 주문 -- Day+ 확장시간 주문 포함 -- 이 시스템에 의해 자동으로 강제 취소된다.

이 공격적 취소 프로토콜은 단순한 기술적 편의가 아니라 **핵심적 시장 건전성 메커니즘**이다. 만약 주문이 60분간의 휴지 기간 동안 오더북에 잔존한다면, 오후 8:30 ET에 발표되는 거시경제 뉴스나 기업 실적이 증권의 공정가치를 급격히 변동시킬 수 있다. 매칭엔진이 오후 9:00에 재개될 때 고빈도 차익거래자들이 원래 호가 제공자가 가격 알고리즘을 갱신하기 전에 이러한 잔존 지정가 주문을 즉시 포착(pick off)할 수 있다. 오더북을 전량 소거함으로써, 24X는 모든 유동성 공급자가 오후 9:00에 적절히 가격이 책정된 신규 주문을 능동적으로 재접속 및 재제출하도록 강제하여, 휴지 경계를 넘어선 비대칭 정보 차익거래 리스크를 제거한다.

Trading Pause 기간에 수행되는 배치 처리 작업은 다음과 같다:

| 작업 | 상세 내용 |
|---|---|
| **배치 처리 및 아카이빙** | 이전 23시간 주기의 수백만 건 체결, 취소, 호가 갱신 데이터를 압축 및 규제 감사용 콜드스토리지에 보관 (CAT 등) |
| **데이터베이스 리인덱싱** | 연속 오더북 운영으로 발생한 DB 단편화를 정리, 마이크로초 매칭 속도 복원 |
| **FIX 시퀀스 리셋** | FIX 프로토콜의 순차 번호를 0으로 리셋, 정수 오버플로 방지 및 신규 거래일 경계 설정 |

---

## 3. 주문 유형 및 실행 로직

### 3.1 TIF(Time-in-Force) 한정자 및 멀티세션 호가 지속성

자정 경계, 유동성 체제 변동, 다일 세션을 아우르는 잔존 호가 관리를 위해, 24X는 연속 모델에 특화된 TIF 한정자를 지원한다:

| TIF 유형 | 설명 | 유효 기간 | 특이사항 |
|---|---|---|---|
| **Day+** (확장시간) | 24시간 거래자를 위한 핵심 TIF. 단일 24X Trading Day 전체에 걸쳐 체결 가능 | 제출 시점 ~ 19:59:59 ET | Trading Pause 1초 전 자동 만료 |
| **RHO** (Regular Hours Only) | 정규 거래시간 전용. 야간/장전 제출 시 매칭엔진이 수락하되 비활성 상태로 보류 | 09:30 ~ 16:00 ET | 오더북 미표시, Core Session 종료 시 미체결분 자동 만료 |
| **GTT** (Good-'til Time) | 마이크로초 단위 정밀 만료 시간 지정 가능 | 사용자 지정 (최대 20:00 ET) | 통계적 차익거래 알고리즘에 활용. Post-Market 종료 시점 초과 설정 불가 |
| **IOC** (Immediate-Or-Cancel) | 이용 가능한 잔존 유동성에 대해 즉시 공격적 체결, 미체결 잔량 즉시 취소 | 즉시 | 4개 전 세션에서 동일 작동. 오더북 미잔존 |
| **FOK** (Fill-Or-Kill) | 지정 수량 전량의 즉시 체결을 요구, 불가 시 전량 취소 | 즉시 | 4개 전 세션에서 동일 작동. 오더북 미잔존 |

### 3.2 금지 주문 유형

#### 3.2.1 Market Order 야간 금지

24X Market Session(21:00~04:00 ET) 중 가장 엄격한 운영 제약은 **비가격 리스크(unpriced risk)의 절대적 금지**이다. Market Order는 최적 표시가격에 즉시 매매하라는 지시로, 정규시간에는 LULD 변동성 밴드에 의해 급격한 가격 급등이 차단된다. 그러나 LULD가 SIP에 의존하고 SIP가 야간에 비가동이므로, 야간 시장에서 대형 Market Order가 극히 얇은 오더북을 수십 가격대에 걸쳐 스위핑하여 국지적 플래시 크래시를 촉발할 수 있다. 따라서 모든 야간 유동성 상호작용은 명시적으로 가격이 지정된 Limit Order를 통해서만 수행되어야 한다.

#### 3.2.2 Pegged Order 야간 금지

Pegged Order(Midpoint Peg, Primary Peg 등)는 SIP가 산출하는 통합 실시간 NBBO에 의존한다. Midpoint Peg는 National Best Bid와 National Best Offer의 정확한 중간값으로 잔존 가격을 동적 산출한다. SIP 운영위원회가 오후 8:00 ET에 인프라를 종료하므로, 24X Market Session 중에는 공식 NBBO가 존재하지 않는다. 외부 통합 참조점 없이 Pegged Order가 24X의 국지적, 잠재적으로 비유동적인 오더북에만 고정된다면, 심각한 지연 차익거래(latency arbitrage)와 조작적 호가 폭주(quote-stuffing)를 초래할 수 있다. 따라서 21:00~04:00 ET 사이에 제출된 페깅 지시가 포함된 주문은 자동 거부된다.

#### 3.2.3 LOO/MOO/LOC/MOC 주문

24X 아키텍처는 본질적으로 개장/폐장 교차 메커니즘이 없으므로, LOO(Limit-On-Open), MOO(Market-On-Open), LOC(Limit-On-Close), MOC(Market-On-Close) 주문을 내부적으로 해결할 방법론이 존재하지 않는다. 이러한 주문 유형이 제출될 경우:

- **라우팅 가능(Routable) 주문**: 24X 시스템이 제3자 라우팅 브로커를 통해 주문을 1차 상장 거래소로 즉시 전송 (예: AAPL의 MOC 주문을 Nasdaq Closing Cross로 전달)
- **Book Only / Do Not Route 주문**: 24X 매칭엔진이 FIX 프로토콜을 통해 즉시 거부 메시지 반환

### 3.3 오프닝/클로징 경매 없음 -- 100% 연속 매매

24X National Exchange와 NYSE, Nasdaq 등 1차 상장 거래소 간의 근본적 아키텍처 차이는 **개장/폐장 경매(opening/closing auction)의 완전하고 의도적인 부재**이다. 24X 생태계 내 모든 거래 종목은 엄격하게 비경매 적격(non-auction eligible)으로 지정된다.

전통적 시장 구조에서 개장/폐장 교차(cross)는 특정 정적 시점에 대규모 국지적 유동성을 집계하여 확정적 참조가격을 설정하는 핵심 가격 발견 메커니즘이다. 그러나 23시간 연속 거래 패러다임에서 단일 임의적 지리적 시점에 유동성을 집계하는 것은 운영 목표에 정면으로 모순된다. 24X의 목표는 글로벌 시간대에 걸쳐 유동성을 균등하게 분산시켜, 도쿄, 런던, 뉴욕에서 거시경제 뉴스가 발생할 때 유기적으로 가격 발견이 이루어지도록 하는 것이다.

결과적으로, 24X Market Session, Pre-Market Session, Core Market Session 간의 전환은 원활하게(seamlessly) 이루어진다. 거래 중단, 주문 불균형 공시, 이산적 교차 알고리즘의 배치가 없으며, 시스템은 가장 오래된 마이크로초 타임스탬프를 가진 주문부터 시간 순서대로 수신 주문을 계속 처리하고 매칭한다.

### 3.4 Self-Trade Prevention (STP) 메커니즘

고속 연속 시장에서 알고리즘 마켓메이커는 서로 다른 트레이딩 데스크 간에 자사의 매수-매도 주문을 실수로 매칭시킬 수 있다. MEMX 아키텍처는 전체 논리적 24X Book에 걸쳐 마이크로초 단위 점검을 실행하여 대응 회원 ID를 식별하고, 사전 설정된 지시에 따라 가장 오래된 주문, 가장 새로운 주문, 또는 양쪽 주문을 자동 취소하여 불법 가장매매(wash trade)를 방지한다.

---

## 4. MEMX Memoir 매칭엔진

### 4.1 기술 사양: 수백만 건/초, 마이크로초 결정론적 처리

Reg SCI(Regulation Systems Compliance and Integrity)의 엄격한 성능 및 복원력 요건을 충족하기 위해, 24X는 자체 엔진 개발 대신 **MEMX Technologies, LLC**로부터 핵심 거래 인프라를 라이선스하는 "시장 서비스(market-as-a-service)" 기술 패러다임을 채택하였다. 이는 DLSA(Delivery, Licenses and Services Agreement)를 통해 이루어진다.

MEMX **"Memoir"** 매칭엔진의 핵심 기술 사양은 다음과 같다:

| 항목 | 사양 |
|---|---|
| **처리 용량** | 초당 수백만 건(millions of messages per second) |
| **지연시간** | 마이크로초(microsecond) 수준 결정론적 처리 |
| **아키텍처** | 데이터 중심, 고병렬(highly parallelized) 분산 서버 네트워크 |
| **설계 철학** | 레거시 순차 처리 방식 폐기, 수평적 확장(horizontal scaling) |
| **일관성** | 오전 3:00의 지연시간 = 오전 9:30 피크 시간의 지연시간 (동일 보장) |

### 4.2 가격/시간 우선 모델(Price/Time Priority)

Memoir 엔진은 엄격한 **가격/시간 우선 모델**로 운영된다:

1. **가격 우선**: 수신 주문이 거래소 게이트웨이에 도달하면 매칭 코어로 즉시 라우팅되어 순차 랭킹. 가장 공격적인 가격(최고 매수호가 또는 최저 매도호가)을 제시한 주문에 체결 우선권 부여
2. **시간 우선**: 동일 가격대에 다수의 잔존 지정가 주문이 있는 경우, 고정밀 타임스탬프에 기반하여 마이크로초 단위로 먼저 게이트웨이에 도착한 주문에 절대적 우선권 부여

### 4.3 Equinix NY4 데이터센터 (물리적 분리 서버)

DLSA는 Reg SCI의 시스템 보안 요건을 충족하고 규제적 얽힘을 방지하기 위해 24X National Exchange와 MEMX Exchange 간의 엄격한 논리적 및 **물리적 분리**를 강제한다:

- 24X 플랫폼은 Memoir 소프트웨어의 **완전히 별도의 전용 인스턴스**로 운영
- **뉴저지 주 시커커스(Secaucus)의 Equinix NY4 데이터센터** 내 물리적으로 분리된 서버 하드웨어에 호스팅
- 24X 회원을 위한 별도 전용 통신 크로스 커넥트(cross-connect) 사용
- MEMX Exchange의 급격한 트래픽 급증이나 사이버 사건이 24X 운영에 영향을 미치지 않도록 격리

### 4.4 최대 주문: 1,000,000주 또는 $100M

24X Book은 다음의 최대 단일 주문 한도를 지원한다:

- **최대 수량**: 1,000,000주
- **최대 명목가치**: $100,000,000 (1억 달러)

### 4.5 라운드롯/혼합롯/오드롯 지원

24X Book은 라운드롯(round lot), 혼합롯(mixed lot), 오드롯(odd lot)의 수신 및 표시를 원천적으로 지원한다. 특히, 다수의 소형 주문이 특정 가격대에 누적되어 완전한 라운드롯(통상 100주)에 해당하게 되면, Memoir 엔진이 자동으로 이를 통합(consolidate)하여 집계된 수량을 최우선호가 피드에 공시용으로 승격시켜, 별도의 매칭 보드나 수동 개입 없이 최대 유동성 가시성을 보장한다.

### 4.6 논리적 통합 오더북 -- "24X Book"

레거시 거래소 인프라에서 "Board"는 물리적 거래 포스트나 경직된 하드웨어 파티션을 의미했다. MEMX Memoir 아키텍처는 경직된 물리적 보드 개념을 추상화하여, 탄력적으로 확장 가능한(elastically scalable) 매칭 노드 클러스터에 걸쳐 분산된 통합 논리적 오더북인 **"24X Book"**을 유지한다. 게이트웨이 서버는 정교한 부하분산(load-balancing) 알고리즘을 활용하여 수신 FIX 및 바이너리 메시지를 최적 매칭 노드로 동적 라우팅하여, 국지적 처리 큐를 방지한다.

---

## 5. 24X Price Bands (독자적 변동성 관리)

### 5.1 LULD 대체 메커니즘

Core Market Session 중 시스템적 변동성은 LULD(Limit Up-Limit Down) 메커니즘에 의해 억제된다. LULD는 최근 거래 활동을 기반으로 동적 가격 밴드를 계산하며, 증권 가격이 이 밴드를 벗어나 체결되려 하면 SIP가 모든 미국 거래소에 걸쳐 범시장적 거래 일시정지를 촉발한다.

그러나 **LULD의 수학적 계산은 전적으로 SIP가 제공하는 통합 데이터에 의존하고, SIP는 야간에 비가동이므로, LULD 보호 기능은 24X Market Session 중 완전히 비활성화된다.** 변동성 제어 장치 없이 중앙지정가 오더북을 운영하면, 얇은 유동성을 스위핑하는 오류 알고리즘에 의한 국지적 플래시 크래시 리스크가 발생한다.

이 문제를 해결하기 위해 24X는 통합 테이프(consolidated tape)에 독립적인, 견고한 국지적 대안으로 독자적 **"24X Price Bands"**를 설계 및 구현하였다.

### 5.2 가격대별 파라미터

24X Price Band는 현재 증권의 공정가치 주위에 수학적으로 정의된 엄격한 칼라(collar)를 설정한다. 매칭엔진은 이 임계값을 벗어나는 공격적 지정가 주문을 자동으로 거부하거나 재가격 책정하도록 프로그래밍되어 있다.

야간 세션이 자연적으로 주간보다 넓은 매수-매도 스프레드와 낮은 거래량을 경험함을 인식하여, 24X의 퍼센티지 파라미터는 주간 LULD 밴드보다 의도적으로 관대하게 설정되어, 정상적 야간 가격 발견으로 인한 시스템 동결을 방지한다:

| 증권 가격대 | 퍼센티지 파라미터 | 상한/하한 밴드 예시 (Reference Price $10 기준) |
|---|---|---|
| **$1 ~ $3** | **10%** | $0.90 ~ $1.10 ($1 기준) |
| **$3 ~ $50** | **5%** | $9.50 ~ $10.50 ($10 기준) |
| **$50 이상** | **3%** | $97.00 ~ $103.00 ($100 기준) |

산출된 수치는 상한 및 하한 밴드를 설정하기 위해 가장 가까운 $0.01로 반올림된다.

### 5.3 Reference Price 결정 로직

Price Band의 유효성은 기초 Reference Price의 정확성에 전적으로 의존한다. 24X는 이상 장외 체결가에 고정되는 것을 방지하기 위해, 오후 9:00 ET의 초기 Reference Price를 결정하는 엄격한 계층적 연속 구조를 활용한다:

```
Reference Price 결정 우선순위:

1순위: 직전 24X Post-Market Session의 최종 체결가
    ↓ (이용 불가 시)
2순위: 정규거래시간(Regular Trading Hours) 중 1차 상장 시장의 최종 종가
    ↓ (이용 불가 시)
3순위: 전일 공식 종가
```

### 5.4 동적 조정: 5분 이후 30초마다 재계산, 1% 이상 변동 시 갱신

24X Market Session이 **5분간 활성화**된 이후, 시스템은 정적 초기 가격을 포기하고 **동적, 연속적 계산**으로 전환한다:

- **매 30초마다** 매칭엔진이 직전 5분간 블록의 평균 가격을 산출
- 미세 변동성을 필터링하기 위해, 이 새로운 평균이 현재 활성 Reference Price 대비 **최소 1% 이상** 괴리될 경우에만 Reference Price가 공식 갱신

이 메커니즘은 정상적 시장 미세구조 잡음과 진정한 가격 이동을 구별하여, Price Band가 시장 상황에 적응적으로 반응하면서도 과도한 밴드 변경을 방지한다.

### 5.5 Crowdsourced Adjustment Valve (3개 회원, 30초, 100주 이상)

경직된 자동화 가격 밴드는 2차적 리스크를 수반한다: 진정한 거시경제 충격으로 증권의 대규모 재가격이 정당화되는 경우에도 합법적 가격 발견을 "잠금(lock out)"할 수 있다. 이를 완화하기 위해 24X는 고유한 **크라우드소싱 조정 밸브(Crowdsourced Adjustment Valve)**를 설계하였다.

작동 조건:

| 조건 | 파라미터 |
|---|---|
| **최소 참여 회원 수** | 3개의 서로 다른(distinct) 회원 |
| **주문 위치** | 상한 또는 하한 Price Band의 정확한 경계에 표시 |
| **최소 잔존 시간** | 30초 이상 중단 없이 연속 표시 |
| **최소 주문 수량** | 각 주문당 100주 이상 |

위 4가지 조건이 모두 충족되면, 시스템 로직은 시장이 이탈된 수준에서 거래하려는 합법적, 다자간 의도(multi-party intent)를 보유하고 있다고 결론짓는다. 이는 Reference Price를 해당 밴드 경계로 **즉시 강제 재계산**을 촉발하여, 새로운 가치 평가 수준에서 거래가 계속될 수 있도록 한다.

---

## 6. 규제 프레임워크

### 6.1 야간 Reg NMS Rule 611 미적용 -- 격리된 유동성 풀

Core Market Session 중 미국 체결 품질의 근간은 Regulation NMS의 **Rule 611(Order Protection Rule)**이다. Rule 611은 "trade-through"를 엄격히 금지하여, 거래소가 경쟁 거래소에 잔존하는 보호 표시 호가보다 열등한 가격에 주문을 체결할 수 없도록 한다. 이 시스템은 SIP의 통합 NBBO에 의존하여 집행된다.

**SIP가 비가동이고 공식 통합 NBBO가 존재하지 않는 24X Market Session 중에는, Reg NMS trade-through 금지가 근본적으로 적용 불가능하다.** 이 규제 배제의 2차적 영향은 체결 품질에 심대하다:

- 오전 2:00 ET에 24X에서 공격적 지정가 주문을 체결하는 리테일 또는 기관 투자자가, Blue Ocean 등 비연결 ATS(Alternative Trading System)에서 동일 증권을 훨씬 유리한 가격으로 매도하는 잔존 지정가 주문이 있음을 인지하지 못할 수 있음
- Reg NMS의 의무적 중앙집중 라우팅 우산 없이, 시장은 **격리된 유동성 섬(isolated liquidity islands)**으로 파편화

### 6.2 Clearly Erroneous Execution (CEE) 야간 정지

통합 테이프의 부재는 알고리즘 오류나 "뚱뚱한 손가락(fat finger)" 거래의 해소를 극적으로 복잡하게 만든다. 표준 거래소 규칙에서는 명백히 비정상적 가격으로 체결된 거래가 CEE(Clearly Erroneous Execution) 심사를 거쳐 취소 또는 무효화된다.

그러나 인력이 적고 변동성이 높은 야간 시간대에 주관적 CEE 심사를 관리하는 것은 운영상 불가능하다. 24X 규정집은 **24X Market Session 중 표준 CEE 심사가 일반적으로 정지**됨을 명시한다. 거래소는 극단적 체결 확정성 정책을 시행한다: 참여자가 자동화된 24X Price Bands 또는 Reference Price 계산이 MEMX 매칭엔진 자체의 **시스템적 기술 오작동**으로 인해 정상 작동하지 못했음을 수학적으로 입증할 수 있는 경우에만 거래가 심사 및 무효화된다.

이 규칙은 **운영 및 재무적 리스크를 전적으로 거래 참여자에게 전가**한다.

### 6.3 NBBO 부재 -- SOR의 자체 NBBO 합성 필요

최적 체결의 부담이 거래소에서 벗어나 참여 **브로커-딜러가 운영하는 Smart Order Router(SOR)**로 완전히 이전된다. 야간 시간대에 고객에게 최적 가격을 보장하기 위해, 이들 브로커는:

1. 운영 중인 모든 장외시간 거래소의 독점 데이터 피드를 구독, 수신, 합성
2. **합성 내재화 NBBO(synthetic, internalized NBBO)**를 구축

이는 고도로 복잡하고 자본 집약적인 기술적 부담이다.

### 6.4 SIP 확장 대기 (SIP 24x5: 일~금 20:00-20:00 ET)

SIP 운영위원회는 진화하는 시장 구조에 맞추어 운영 시간을 **24x5 일정**으로 확장하는 수정안을 제안하였다. 완전 구현 시, SIP는 일요일 오후 8:00 ET에 가동을 개시하여 금요일 오후 8:00 ET까지 중단 없이 운영될 예정이다. 이 시스템적 업그레이드가 보류 중인 동안, 야간 미국 주식시장은 전적으로 분산적, 독점적 데이터 솔루션에 의존하는 상태를 유지한다.

---

## 7. 청산-결제

### 7.1 DTCC/NSCC UTC 통합

24시간 주식거래소의 실현은 단순한 프론트오피스 매칭 과제가 아니라, 근본적으로 **백오피스 청산 및 결제 딜레마**이다. DTCC(Depository Trust & Clearing Corporation)와 그 중앙 거래상대방 자회사인 NSCC(National Securities Clearing Corporation)가 관리하는 미국 청산 인프라는 역사적으로 오전 9:30~오후 4:00 시장의 시간적 현실에 맞추어 설계되었다. 다자간 상계(multilateral netting), 리스크 마진 산출, 결제 처리에 필요한 대규모 연산 작업을 수행하기 위해, DTCC는 광범위한 야간 배치 처리 창구에 의존하여 UTC(Universal Trade Capture) 시스템을 심야 및 새벽 시간대에 사실상 오프라인으로 운영하였다.

### 7.2 Phase 1 (2024년 9월): UTC 01:30 ET 개시, 야간 양자 신용리스크 잔존

야간 청산 공백(novation gap)을 단축하기 위한 중간 단계로, NSCC는 UTC 시스템의 개장 시간을 **2.5시간 앞당겨**, 시장 센터가 레거시 개장 시간인 오전 4:00 ET 대신 **오전 1:30 ET**에 체결 거래의 청산 제출을 시작할 수 있도록 하였다.

이 조치는 아시아 조기 거래 시간대의 일부 리스크를 완화하였으나, **오후 8:00~오전 1:30 ET 사이에 체결된 거래는 여전히 양자간 채무(bilateral obligations)로 부유**하는 구조적 한계가 잔존하였다.

**양자 신용리스크의 메커니즘**: 두 브로커-딜러가 오후 10:00 ET에 24X에서 거래를 체결하되 NSCC 시스템이 오프라인인 경우, 해당 거래는 야간 내내 **비연계(un-novated)** 상태로 유지된다. 이 수 시간의 "novation gap" 동안 체결 브로커-딜러는 양자간 거래상대방 신용리스크를 부담해야 한다. 매도 브로커-딜러가 오전 1:00에 파산할 경우, 매수 브로커-딜러는 NSCC 청산기금의 보호 없이 전액 재무 손실에 노출된다.

### 7.3 Phase 2 (2026년 6월 목표): 24x5 완전 운영, 즉시 Novation

야간 novation gap을 완전히 제거하기 위해, NSCC는 **연속 24x5 운영 일정**으로 전환한다:

| 항목 | Phase 2 사양 |
|---|---|
| **UTC 가동 개시** | 일요일 오후 8:00 ET |
| **UTC 가동 종료** | 금요일 오후 8:00 ET |
| **운영 방식** | 중단 없는 연속 운영 |
| **Novation 시점** | 제출 즉시 (real-time) |
| **CCP 보증** | 제출 시점에 NSCC 중앙 거래상대방 보증 즉시 적용 |

Phase 2 배치 시, 24X에서 심야 시간대에 체결된 거래는 UTC 시스템으로 전송되어 실시간으로 수신된다. 이 즉시 검증은 제출 정확한 시점에 NSCC의 중앙 거래상대방 보증 적용을 촉발하여, 역사적으로 장외시간 거래를 괴롭혀온 양자간 거래상대방 리스크를 사실상 제거한다.

### 7.4 Trade Date 전환: 20:00 ET 기준

연속 운영 모델은 "거래일(Trade Date)"의 정의와 T+1 가속 결제 규칙 준수에 관한 심각한 시간적 복잡성을 초래한다. 미국 업계 합의는 공식 **Trade Date 전환 시점을 정확히 오후 8:00 ET**로 설정한다.

따라서:
- 월요일 오후 9:05 ET에 24X 엔진에서 매칭된 주식 거래는 법적/운영적으로 **화요일 체결**로 정의
- 이 거래는 화요일의 일중 마진 계산에 적용
- T+1 요건 충족을 위해 **수요일에 결제**

### 7.5 FIX Tag 715 의무화

이 시간적 오프셋을 관리하기 위해 전문화된 메시징 프로토콜이 필요하다. 장외시간 거래에 참여하려면, DTCC는 모든 체결 브로커-딜러 및 청산 회사가 FIX 연결을 업그레이드하여 새로운 데이터 필드인 **FIX Tag 715 (Clearing Business Date)**를 지원하도록 의무화한다.

24X가 UTC에 체결 보고서를 전송할 때, FIX Tag 715의 포함은 하류 청산 시스템에 월요일 밤에 체결된 거래가 화요일 청산 배치에 속함을 명확히 알린다. 이는 프라임 브로커와 리스크 관리 시스템이 월요일 밤의 리스크 노출을 월요일 주간의 결제 의무와 부적절하게 혼합하는 것을 방지한다.

### 7.6 별도 9A/9B CORR/QSR 관계

야간 변동성이 정규시간 마진 콜을 촉발하는 것을 방지하기 위해, NSCC는 청산 회원에게 야간 세션 전용의 **별도 9A/9B Correspondent Clearing(CORR) 및 Qualified Special Representative(QSR) 관계**를 수립하도록 요구한다.

이 이중 관계 구조는 야간 신용 노출을 주간 거래 활동으로부터 격벽화(compartmentalize)하여, 청산 회사가 고객의 야간 알고리즘 전략에 대해 보다 엄격한 리스크 한도를 부과할 수 있도록 한다.

### 7.7 $1B 야간 거래 상한

NSCC는 또한 UTC 내에 **자동화된 사전 거래 검증 검사**를 운용하여, 저유동성 시간대에 **$10억(USD 1 Billion)의 고가치 임계값**을 초과하는 이상 Correspondent Clearing 거래를 즉각 거부한다. 이는 알고리즘 폭주(algorithmic runaway)에 대한 안전장치로 기능한다.

---

## 8. 글로벌 인프라 및 TNS 파트너십

### 8.1 Trans-oceanic 초저지연 네트워크

24시간 미국 주식거래의 근본적 수요 동인은 자국의 현지 주간 업무 시간에 미국 자산을 거래하고자 하는 APAC 지역(도쿄, 홍콩, 싱가포르)의 기관 데스크와 리테일 어그리게이터에서 기인한다. 그러나 표준 인터넷 프로토콜을 통한 태평양 횡단 주문 흐름 라우팅은 심각한 비결정론적 지연시간과 패킷 손실 취약성을 유발하며, 이는 고빈도 마켓메이킹 알고리즘에 치명적이다.

글로벌 23/5 거래의 지리적 마찰을 해결하기 위해, 24X는 **Transaction Network Services(TNS)**와 전략적 인프라 파트너십을 체결하였다. TNS는 공용 인터넷을 완전히 우회하는 최적화된 **대양 횡단 해저 케이블(trans-oceanic subsea cables)**을 활용하는 맞춤형 초저지연 금융 네트워크를 운영한다.

### 8.2 APAC 브로커-딜러 직접 연결

TNS와의 직접 통합을 통해, 24X는 독점적 24X Top 및 24X Depth 시장 데이터 피드를 APAC 기반 브로커-딜러의 서버에 직접 파이프할 수 있다. 이 전용 연결 아키텍처는 다음을 가능하게 한다:

- 홍콩의 자기매매 회사가 미국 야간 가격 데이터를 수신
- 복잡한 라우팅 결정을 실행
- FIX 주문을 뉴저지 Equinix NY4 데이터센터의 MEMX Memoir 매칭엔진으로 태평양을 횡단하여 **결정론적 밀리초 수준 정밀도**로 전송

이 기술적 가교는 야간 시장에서 심각한 변동성을 방지하는 데 필요한 깊고 안정적인 기관 유동성 풀을 배양하는 데 핵심적이다.

### 8.3 데이터센터: NY4(Primary), LD4(Mirror), CH4(DR)

| 데이터센터 | 위치 | 역할 |
|---|---|---|
| **Equinix NY4** | 뉴저지 주 시커커스(Secaucus, NJ) | 1차(Primary) -- 매칭엔진 및 게이트웨이 운영 |
| **Equinix LD4** | 런던(London) | 미러(Mirror) -- 유럽 지역 데이터 복제 및 접근 |
| **Equinix CH4** | 시카고(Chicago) | 재해복구(Disaster Recovery) -- 비상 시 운영 전환 |

---

## 9. 시장 데이터

정규시간(9:30~16:00) 중 24X는 최우선호가 및 최종체결가 데이터를 SIP(CTA 및 UTP 플랜)에 원활하게 전송한다. 그러나 야간에는 이 중앙집중 투명성 장치가 붕괴된다. SIP 운영위원회가 오후 8:00 ET에 통합 인프라를 종료하므로, 오전 2:00 ET에 24X에서 체결된 거래는 SIP가 수신, 처리, 표시할 수 없다.

이 대규모 투명성 격차를 해소하기 위해, 24X는 자체 독점 직접 시장 데이터 상품을 생성 및 배포한다:

### 9.1 24X Top (최우선호가)

| 항목 | 상세 |
|---|---|
| **데이터 유형** | 최우선호가(Top-of-Book) 피드 |
| **내용** | 24X Book에 독점적으로 잔존하는 최우선 매수호가(Best Bid) 및 최우선 매도호가(Best Offer) |
| **용도** | 리테일 플랫폼 및 Smart Order Router(SOR)를 위한 실시간 가격 벤치마크 |
| **지연시간** | 초저지연(low-latency) |

### 9.2 24X Depth (전 호가 비집계)

| 항목 | 상세 |
|---|---|
| **데이터 유형** | 전 호가 수준(Full Depth) 피드 |
| **내용** | 거래소 모든 가격대에 걸친 잔존 지정가 주문, 체결 보고서, 주문 수정, 취소 메시지 |
| **집계 여부** | 비집계(unaggregated) -- 개별 주문 수준 정보 제공 |
| **용도** | 브로커-딜러의 내부 유동성 파악 및 합성 NBBO 구축에 필수 |

24X Market Session 중 공식 통합 NBBO가 이용 불가하므로, 이러한 독점 피드가 **가격 발견의 절대적 진실 원천(absolute source of truth)**이 된다. 야간 세션에 참여하는 브로커-딜러는 자체 시장 유동성 내부 표현을 구축하기 위해 24X Depth 피드를 직접 수신해야 하며, 이는 상당한 연산 오버헤드와 정교한 데이터 파싱 역량을 요구한다.

---

## 10. 주간 유지보수

일일 1시간 Trading Pause(20:00~21:00 ET) 외에, 24X는 보다 심층적인 인프라 업그레이드를 위한 **확장 주간 유지보수 창구**를 운영한다:

| 항목 | 상세 |
|---|---|
| **시간** | 매주 토요일 08:00 ~ 11:00 ET (3시간) |
| **수행 작업** | 심층 인프라 업그레이드, 물리적 하드웨어 교체, 의무적 백업 시스템 스트레스 테스트 |
| **대상 데이터센터** | NY4(Primary), LD4(Mirror), CH4(DR) 전체 |
| **거래 영향** | 토요일 비거래일이므로 시장 운영에 직접 영향 없음 |

---

## 11. KRX와의 비교 및 시사점

### 11.1 24X vs KRX 비교표

| 비교 항목 | 24X National Exchange | KRX (한국거래소) |
|---|---|---|
| **거래 시간** | 23시간/일 (21:00~20:00 ET) | 6.5시간/일 (09:00~15:30 KST), 야간 파생상품 별도 |
| **주요 대상 시간대** | APAC + EMEA + 미국 전체 | 한국 국내 (KST) |
| **오프닝/클로징 경매** | 없음 (100% 연속 매매) | 동시호가 (개장 08:30~09:00, 폐장 15:20~15:30) |
| **야간 변동성 관리** | 독자적 24X Price Bands | 해당 없음 (야간 주식 거래 미운영) |
| **LULD 동등 체계** | Price Bands: $1-$3(10%), $3-$50(5%), $50+(3%) | 가격제한폭: 기준가 대비 ±30% (정적) |
| **매칭엔진** | MEMX Memoir (라이선스) | EXTURE 3.0 (자체 개발, 50µs) |
| **데이터센터** | Equinix NY4/LD4/CH4 | 부산 DR센터, 여의도 |
| **청산 기관** | DTCC/NSCC | KSD (한국예탁결제원) |
| **결제 주기** | T+1 | T+2 (2024 하반기 T+1 전환 논의) |
| **야간 청산** | Phase 1: UTC 01:30 개시, Phase 2: 24x5 연속 | 해당 없음 |
| **SIP/통합 테이프** | 야간 비가동 → 독점 피드 의존 | 거래소 단일 운영으로 해당 없음 |
| **Trade Date 기준** | 20:00 ET | 거래 당일 (단일 세션) |
| **주문 유형 제한 (야간)** | Market Order, Pegged Order 금지 | 해당 없음 |
| **일일 유지보수** | 1시간 (20:00~21:00 ET) Hard Flush | 장전/장후 시스템 점검 시간 |
| **주간 유지보수** | 토요일 08:00~11:00 ET | 토/일 정기 점검 |
| **최대 단일 주문** | 1,000,000주 또는 $100M | 종목별 상이 |
| **글로벌 연결** | TNS 초저지연 해저케이블 | FIX 기반 해외 접속 |

### 11.2 KRX 도입 시 24X 모델에서 벤치마킹할 요소

KRX가 야간 또는 장시간 거래 도입을 검토할 경우, 24X 모델에서 다음의 핵심 요소를 벤치마킹할 수 있다:

#### (1) 세션 분리 및 규제 차등 적용 모델
24X는 4개 세션 구조를 통해 각 세션별로 상이한 규제 체계를 적용하는 유연한 프레임워크를 구축하였다. KRX가 야간 세션을 도입할 경우, 정규 세션과 분리된 규제 체계를 설계하여 야간 유동성 특성에 맞는 투자자 보호 장치를 운영할 필요가 있다.

#### (2) 독자적 변동성 관리 메커니즘
기존 시장 인프라(SIP, LULD 등)가 야간에 비가동될 경우의 대안적 변동성 관리 체계로서 24X Price Bands 모델은 중요한 참조점이다. 특히 가격대별 차등 파라미터 설정, 동적 Reference Price 재계산, Crowdsourced Adjustment Valve의 3중 구조는 야간 시장의 유동성 특성을 반영한 정교한 설계로, KRX의 야간 변동성 관리 체계 구축 시 직접적 벤치마크가 될 수 있다.

#### (3) 청산-결제 인프라의 선행 현대화
24X 사례에서 가장 중요한 전략적 교훈은 **연속 매칭은 연속 Novation 없이 불가능하다**는 것이다. 브로커-딜러를 장기간의 비연계 양자간 신용리스크에 노출시키면, 야간 유동성 안정화에 필수적인 기관 마켓메이커의 참여가 적극적으로 저해된다. 23/5 모델로의 전환은 반드시 실시간 CCP 보증을 확보하기 위한 백오피스 청산 역량의 업그레이드가 선행되어야 한다. KSD의 야간 청산 시스템 현대화가 전제 조건이다.

#### (4) 일일 유지보수 창구의 필수성
진정한 중단 없는 24/7/365 운영은 규제된 거래소가 요구하는 마이크로초 결정론, 순차적 FIX 메시징, 방대한 규제 데이터 아카이빙에 있어 기술적으로 불가능하다. 24X의 일일 Hard Flush와 유지보수 창구는 이러한 기술적 한계를 인정하면서도 시장 건전성을 보호하는 현실적 해법이며, KRX 역시 유사한 시스템 안정화 창구를 설계해야 한다.

#### (5) 오프닝/클로징 경매 배제의 전략적 논리
24X는 23시간 연속 매매에서 특정 시점에 유동성을 인위적으로 집중시키는 경매가 운영 목표에 모순된다고 판단하였다. KRX가 글로벌 시간대를 대상으로 한 연속 거래를 도입할 경우, 동시호가 메커니즘의 유지 여부와 연속 매매와의 조화 방안을 신중히 검토해야 한다.

#### (6) 글로벌 저지연 연결 인프라
TNS 파트너십을 통한 APAC 직접 연결 모델은 KRX가 해외 투자자의 야간 참여를 유도하기 위한 인프라 구축에 중요한 참조가 된다. 특히 미국-한국 간 초저지연 금융 네트워크 구축은 KRX 야간 시장의 성공적 유동성 확보에 핵심적 요소가 될 것이다.

#### (7) 주문 유형의 세션별 차등 규제
야간 시장에서 Market Order와 Pegged Order를 금지하고 Limit Order만 허용하는 24X의 접근법은, 유동성이 얇은 장외시간 시장에서의 투자자 보호 및 시장 안정성 확보를 위한 실용적 모델이다. KRX 역시 야간 세션 도입 시 주문 유형의 세션별 차등 규제를 검토할 필요가 있다.

---

## 참고자료

1. 24X National Exchange Opens for Trading as First SEC-Approved 23/5 Stock Exchange, PRNewswire, [prnewswire.com/news-releases/24x-national-ex...](https://www.prnewswire.com/news-releases/24x-national-exchange-opens-for-trading-as-first-sec-approved-235-stock-exchange-302581303.html)
2. Market Spotlight: 24 Hour Trading, BlackRock, [blackrock.com/corporate/literature/whitepap...](https://www.blackrock.com/corporate/literature/whitepaper/blackrock-market-spotlight-24-hour-trading.pdf)
3. 24X National Exchange Partners With TNS to Provide Market Data Connectivity, Business Wire, [businesswire.com/news/home/20250909964940/en/](https://www.businesswire.com/news/home/20250909964940/en/)
4. 24X Exchange Beats Nasdaq to Market with TNS Partnership, Finance Magnates, [financemagnates.com/forex/24x-exchange-beats-nasd...](https://www.financemagnates.com/forex/24x-exchange-beats-nasdaq-to-market-with-tns-partnership-for-extended-hours-trading/)
5. 24X National Exchange LLC User Manual, SEC.gov, [sec.gov/files/rules/other/2022/24x/24...](https://www.sec.gov/files/rules/other/2022/24x/24x-form-1-exhibit-e-1-amended-marked.pdf)
6. 24X National Exchange LLC; Order Instituting Proceedings, SEC.gov, [sec.gov/files/rules/other/2024/34-100...](https://www.sec.gov/files/rules/other/2024/34-100254.pdf)
7. SR-NASDAQ-2025-109, Nasdaq, [listingcenter.nasdaq.com/assets/rulebook/nasdaq/filing...](https://listingcenter.nasdaq.com/assets/rulebook/nasdaq/filings/SR-NASDAQ-2025-109.pdf)
8. 24X National Exchange LLC Date of Filing, SEC.gov, [sec.gov/files/rules/other/2024/24x-am...](https://www.sec.gov/files/rules/other/2024/24x-amend-exhibit-e-redline.pdf)
9. Equities Clearing Enhancements: UTC 24/5 Extended Trading Hours, DTCC, [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/UTC-24-x-5-Extended-Trading-Hours.pdf)
10. SR-24X-2025-07, 24X Exchange, [equities.24exchange.com/api/media/file/SR-24X-2025-07...](https://equities.24exchange.com/api/media/file/SR-24X-2025-07-Trading-Hours-Website.pdf)
11. Addendum E-1 24X National Exchange User Manual, SEC.gov, [sec.gov/files/rules/other/2024/24x-fo...](https://www.sec.gov/files/rules/other/2024/24x-form-1-exhibit-e-1.pdf)
12. Nasdaq Proposes Near-24-Hour Trading, Cadwalader Quorum, [cadwalader.com/quorum/index.php](https://www.cadwalader.com/quorum/index.php?nid=20&eid=93)
13. Rules of 24X National Exchange LLC, SEC.gov, [sec.gov/files/rules/other/2024/24x-am...](https://www.sec.gov/files/rules/other/2024/24x-amend-exhibit-b-1.pdf)
14. Order Type Differences, NYSE, [nyse.com/publicdocs/nyse/markets/nyse/...](https://www.nyse.com/publicdocs/nyse/markets/nyse/Pillar_Differences.pdf)
15. Application of 24X National Exchange LLC for Registration, SIFMA, [sifma.org/advocacy/letters/application-...](https://www.sifma.org/advocacy/letters/application-of-24x-national-exchange-llc-for-registration-as-a-national-securities-exchange)
16. The Shift to 24x5 Trading, DTCC, [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/theshiftto24x5trading.pdf)
17. 24X National Exchange Application for Registration, SIFMA, [sifma.org/advocacy/letters/24x-national...](https://www.sifma.org/advocacy/letters/24x-national-exchange-application-for-registration)
18. Extended Trading Hours, SIFMA, [sifma.org/issues/market-structure/exten...](https://www.sifma.org/issues/market-structure/extended-trading-hours)
19. 24x5 Trading Update Important Notice, DTCC, [dtcc.com/-/media/Files/pdf/2026/1/7/A9...](https://www.dtcc.com/-/media/Files/pdf/2026/1/7/A9689.pdf)
20. What is 24X? Inside the Exchange Powering 23/5 Trading, Exegy, [exegy.com/what-is-24x-exchange-23-5-tra...](https://www.exegy.com/what-is-24x-exchange-23-5-trading/)
21. Rules of 24X National Exchange LLC (Redline), SEC.gov, [sec.gov/files/rules/other/2024/24x-am...](https://www.sec.gov/files/rules/other/2024/24x-amend-exhibit-b-1-redline.pdf)
22. Uninterrupted FIX Connectivity for 24x7 Trading, B2BITS, [b2bits.com/insights/fixconnect247](https://www.b2bits.com/insights/fixconnect247)
23. SRO 24X National Exchange LLC Market Data Fees, Federal Register, [federalregister.gov/documents/2025/09/30/2025-190...](https://www.federalregister.gov/documents/2025/09/30/2025-19011/)
24. Limit Up-Limit Down FAQ, Nasdaq Trader, [nasdaqtrader.com/content/MarketRegulation/LULD...](https://www.nasdaqtrader.com/content/MarketRegulation/LULD_FAQ.pdf)
25. MEMX Technology Helps Improve Venue Performance, Markets Media / Blue Ocean, [blueocean-tech.io/2025/02/25/markets-media-memx...](https://blueocean-tech.io/2025/02/25/markets-media-memx-technology-helps-improve-venue-performance/)
