# NYSE 및 NYSE Arca 확장 거래시간 체제 분석

---

## 1. 기관 개요

### 1.1 NYSE Group 구조

뉴욕증권거래소(New York Stock Exchange, NYSE)는 **Intercontinental Exchange(ICE)** 산하의 글로벌 최대 주식 거래소 그룹이다. NYSE Group은 다음 네 개의 주요 거래소로 구성된다:

| 거래소 | 특징 | 주요 기능 |
|--------|------|-----------|
| **NYSE** | 물리적 플로어 + 전자 거래 하이브리드 | 대형주 주 상장 시장, DMM(Designated Market Maker) 제도 운영 |
| **NYSE Arca** | 완전 전자식(Fully Electronic) | ETF 최대 상장 시장, 확장 거래시간 추진 주체 |
| **NYSE American** | 완전 전자식 | 중소형주(Small-Cap) 전문 거래소, 구 NYSE MKT |
| **NYSE Chicago** | 완전 전자식 | 시카고 기반 지역 거래소, Maker-Taker 수수료 모델 |

NYSE는 시가총액 기준 약 **28조 달러** 이상의 상장 기업을 보유하고 있으며, 미국 전체 상장 주식의 약 **1.5백만 개** 이상의 거래 가능 종목(instruments)이 Pillar 매칭 엔진을 통해 처리된다. NYSE Closing Auction은 매일 수백억 달러 규모의 거래를 처리하며, 전체 통합(consolidated) 시장 거래량의 약 **10%**를 차지한다.

### 1.2 ICE 소속 및 글로벌 위상

NYSE Group은 2013년 ICE에 인수된 이후 에너지, 금리, 주식, ETF, 옵션 등 다양한 자산 클래스를 아우르는 글로벌 거래소 네트워크의 핵심 축을 담당하고 있다. ICE의 기술 인프라 투자와 NYSE Pillar 플랫폼의 개발을 통해 초저지연(ultra-low-latency) 결정론적(deterministic) 매칭 아키텍처를 구현하였으며, 이를 기반으로 22시간 이상의 준연속(near-continuous) 거래 체제로의 전환을 추진 중이다.

---

## 2. 현행 거래시간 제도

### 2.1 정규 세션 (Core Trading Session: 09:30-16:00 ET)

정규 세션은 미국 주식 시장의 핵심 유동성 이벤트가 집중되는 6.5시간의 거래 시간이다.

#### Opening Auction 메커니즘

본장 오픈 경매(Core Open Auction)는 야간 글로벌 거시경제 전개에 대한 가격 안정을 보장하기 위해 엄격한 시간적 동결(freeze) 프레임워크를 사용한다:

| 시간 (ET) | 이벤트 | 상세 |
|-----------|--------|------|
| 08:00 | Auction Imbalance Information 배포 시작 | 미체결 주식에 대한 실시간 불균형 데이터를 1초 간격으로 게시 |
| 09:29:00 | MOO/LOO 취소 거부 시작 | 시장가 오픈 주문(MOO) 및 지정가 오픈 주문(LOO)의 취소 또는 수량 감소 요청 일괄 거부 |
| 09:29:55 | **Imbalance Freeze** 시작 | 새로운 MOO/LOO 주문 즉각 거부; 불균형 상쇄 지정가 주문은 흡수되나 공개 불균형 계산에서 의도적으로 마스킹 |
| 09:30:00 | 매칭 엔진 교차 체결(Cross) | 사전 정의된 Auction Collars 내에서 엄격하게 제한; 주 상장 시장 경매 불가 시 10:00 ET까지 대기 |

Imbalance Freeze 기간(09:29:55~09:30:00)에 전송된 주문은 **Pending-Imbalance Freeze** 상태를 나타내는 FIX 또는 Binary 승인 메시지를 수신한다. 이 5초의 마이크로 윈도우는 알고리즘에 의한 시가 게임화(gamification)를 방지하기 위해 설계되었다.

#### Closing Auction 메커니즘

종가 경매(Closing Auction)는 뮤추얼 펀드 NAV 계산 및 파생상품 결제에 사용되는 **공식 종가(Official Closing Price)**를 결정하는 거래일의 가장 중요한 유동성 이벤트이다.

| 시간 (ET) | 이벤트 | 상세 |
|-----------|--------|------|
| ~15:50 | **Closing Imbalance Period** 시작 | MOC/LOC 주문 자유 입력·수정·취소 마감; 이후 MOC/LOC 입력은 게시된 Significant Imbalance의 contra-side에만 허용 |
| 16:00 | 종가 경매 체결 | 경매 기준가: 거래일 마지막 통합 round-lot 가격; 'M' sale condition으로 OCP 배포 |

- **MOC (Market-On-Close)**: 종가에 시장가로 체결되는 주문
- **LOC (Limit-On-Close)**: 종가에 지정가로 체결되는 주문
- **D-Orders**: NYSE 물리적 플로어 전용, 플로어 브로커를 통해 제출; NYSE Arca 전자 매칭 엔진에서는 처리되지 않음
- **Closing Offset (CO) Orders**: 다른 종가 주문에 양보하도록 설계된 엄격한 지정가 주문; 불균형 반대편에서만 체결

NYSE Closing Auction은 전체 통합 시장 거래량의 약 **~10%**를 차지하며, 매일 수십억 달러 규모의 거래를 처리한다.

### 2.2 프리마켓 (Extended Early: 04:00-09:30 ET)

현행 프리마켓 세션은 오전 4:00 ET에 시작되며, 주로 야간 뉴스 및 글로벌 매크로 이벤트에 대한 초기 가격 반응을 포착한다. Early Open Auction을 통해 세션이 개시되며, Indicative Match Price(IMP) 계산에 기반한 경매 메커니즘이 작동한다.

### 2.3 애프터마켓 (Late Trading: 16:00-20:00 ET)

Late Trading Session은 장 마감 후 실적 발표 반응 및 포트폴리오 리밸런싱을 포착한다. 이 세션에서의 체결 건에는 **'.T' 식별자(modifier)**가 부착되어 다음을 보장한다:

- 야간 체결이 공식 일일 고가/저가/최종 거래가 계산에서 **제외**
- 주요 시장 지수 및 벤치마크가 장외 시간의 비정상적 변동성으로부터 **격리**
- SIP(CTS/CQS)에 보고 시 '.T' sale condition이 명시적으로 추가

---

## 3. NYSE Arca 22시간 거래 체제 (확장 계획)

### 3.1 SEC 승인 경과

NYSE Arca의 확장 거래시간 이니셔티브는 다음의 규제 경로를 통해 진행되었다:

| 규제 문서 | 내용 |
|-----------|------|
| **SR-NYSEARCA-2024-89** | SEC 규칙 제출: 임시 규칙 Rule 7.34-E(T) 채택 및 Rules 1.1, 7.34-E 개정 제안 |
| **Amendment No. 1** | 초기 22시간(01:30~23:30 ET) 모델에서 SIP/DTCC 조율을 통한 23시간 모델로 발전 |
| **Amendment No. 2** | SEC 최종 승인 (Release No. 34-102400) |
| **Rule 7.34-E(T)** | 확장된 거래 세션의 시간적 경계 및 주문 관리 규칙을 규정하는 임시 규칙 |

당초 22시간(01:30 ET ~ 23:30 ET)으로 제안되었으나, SIP 및 DTCC와의 조율을 거쳐 **21:00 ET ~ 20:00 ET(익일)**의 23시간 체제를 목표로 발전하였다.

### 3.2 확장된 세션 구조

| 세션 명칭 | 현행 시간 (ET) | 목표 확장 시간 (ET) | 지속시간 | 운영 특성 |
|-----------|----------------|---------------------|----------|-----------|
| **Maintenance Pause** | 20:00 ~ 04:00 | **20:00 ~ 21:00** | 1시간 | 시스템 초기화, DB 백업, 거래일 전환, 기업행위 처리, 소프트웨어 배포 |
| **Extended Early Session** | 04:00 ~ 09:30 | **21:00 ~ 09:30** | **12.5시간** | APAC/EMEA 가격 발견 촉진; 야간 글로벌 유동성 집계; LULD 대신 Double-Wide Collars 적용 |
| **Core Trading Session** | 09:30 ~ 16:00 | 09:30 ~ 16:00 | 6.5시간 | 주요 유동성 이벤트; 표준 LULD 변동성 메커니즘 활성 |
| **Late Trading Session** | 16:00 ~ 20:00 | 16:00 ~ 20:00 | 4시간 | 장 마감 후 실적 반응, 포트폴리오 리밸런싱; '.T' 식별자 활용 |

**총 거래 가능 시간: 23시간** (유지보수 점검 1시간 제외)

진정한 24/7 영구 가동 모델을 추구하지 않는 이유는 Regulation NMS가 요구하는 결정론적 순서 지정(deterministic sequencing)과 충돌하는 비동기식 분산 원장 또는 핫스왑 가능한 이중화 매칭 엔진의 극도로 높은 비용과 운영 복잡성 때문이다.

### 3.3 Trade Date 전환 로직

**20:00 ET**를 기준으로 논리적 거래일(Trade Date)이 변경된다. 이 변곡점은 DTCC의 UTC(Universal Trade Capture) 시스템과 동기화되어 T+1 결제 주기를 유지한다.

#### FIX Tag 715 (Clearing Business Date) 적용

DTCC는 확장된 FIX 메시징 스키마에서 **FIX Tag 715(Clearing Business Date)**를 의무화하였다. 이 태그는 청산 참가자에게 체결의 로컬 타임스탬프를 무시하고 해당 트랜잭션에 적용 가능한 정확한 영업일을 명시적으로 지시한다.

#### Trade Date/Settlement Date 전환 예시

| 체결 시각 (ET) | 달력 날짜 | 할당 거래일 (TD) | Tag 715 청산일 | 결제일 (T+1) |
|----------------|-----------|------------------|----------------|--------------|
| 화요일, 15:45 | 화요일 | 화요일 | 화요일 | 수요일 |
| 화요일, 19:55 | 화요일 | 화요일 | 화요일 | 수요일 |
| 화요일, 19:59 | 화요일 | 화요일 | 화요일 | 수요일 |
| 화요일, 20:00~21:00 | - | **System Maintenance Pause** | - | - |
| 화요일, 21:05 | 화요일 | **수요일** | **수요일** | **목요일** |
| 수요일, 01:15 | 수요일 | 수요일 | 수요일 | 목요일 |
| 수요일, 02:30 | 수요일 | 수요일 | 수요일 | 목요일 |
| 수요일, 09:30 | 수요일 | 수요일 | 수요일 | 목요일 |

이 엄격한 분리는 CNS(Continuous Net Settlement) 배치 프로세스, 일말 잔고 정산 루틴, 기업행위 권리(record date, ex-dividend date) 인식이 표준 일일 배치 사이클에 영향 없이 유지되도록 보장한다.

---

## 4. Pillar 매칭엔진 기술 아키텍처

NYSE Pillar는 주식 및 옵션 거래를 통합하는 결정론적(deterministic), 초저지연(ultra-low-latency) 매칭 아키텍처이다.

### 4.1 Trading Unit (TXN) 구조: 14개 파티션

Pillar 매칭 엔진은 단일 모놀리식 프로세스가 아닌, **14개의 독립적 Trading Unit(TXN)**으로 분산 구성된다. 이 설계의 핵심 목적은 다음과 같다:

- **지연시간 최소화**: 단일 서버 클러스터의 병목 현상 제거
- **단일 장애점(Single Point of Failure) 방지**: 개별 TXN 장애가 전체 시스템에 영향을 미치지 않음
- **결정론적 샤딩(Sharding)**: 전체 1.5백만+ 종목이 14개 TXN에 결정론적으로 배분

### 4.2 심볼 매핑 ($Market$SymbolMapping_YYYYMMDD.xml)

매일 야간 유지보수 시간 중 **Symbol Index Mapping** 프로토콜이 실행된다:

- 파일 형식: `$Market$SymbolMapping_YYYYMMDD.xml`
- 공개 FTP 서버를 통해 배포
- 각 티커 심볼이 어느 TXN(서버 클러스터)에서 주문장을 관리할지 결정
- **Symbol Index Mapping Message (Msg Type 3)**: 최소 가격 단위(MPV), 가격 척도 코드(진정한 소수점 값 결정을 위해 가격을 10,000으로 나누어야 하는지 여부) 등의 참조 데이터 포함

### 4.3 DealID 구조 (8바이트: SystemID + MarketID + TradeID)

비동기적 22시간 타임라인에서 데이터 충돌 없이 수백만 건의 주문 및 체결을 추적하기 위해 복합 식별 전략을 사용한다:

| 구성 요소 | 크기 | 설명 |
|-----------|------|------|
| **SystemID** | 1 byte | 원천 Pillar 심볼 파티션의 고유 ID (Symbol Index Mapping에서 파생) |
| **MarketID** | 2 bytes | 원천 거래소 ID (NYSE, NYSE Arca, NYSE American 등 식별) |
| **TradeID** | 4 bytes | XDP Market Data 피드에서 발행하는 체결 ID (개별 TXN 내에서만 고유) |
| **DealID (합계)** | **8 bytes** | FIX Tag 9483에 매핑; 전체 거래소 컴플렉스에 걸쳐 절대적 글로벌 고유성 보장 |

이 구조는 중앙 집중식 지연 유발 시퀀스 생성기 없이 모든 주문 및 체결에 대해 글로벌 고유성을 달성한다.

### 4.4 Binary Gateway 프로토콜 (MsgType 100-103)

Pillar Integrated Feed의 주문 상태 관리는 다음 바이너리 메시지 유형으로 처리된다:

| MsgType | 명칭 | 기능 |
|---------|------|------|
| **100** | Add Order | 신규 유동성을 주문장에 추가 |
| **101** | Modify Order | 기존 대기 주문의 가격 또는 수량 조정 |
| **102** | Delete Order | 주문 완전 제거 |
| **103** | Order Execution | 매칭 발생 신호 |
| **1** | Sequence Number Reset | 일일 유지보수 후 시퀀스 번호 초기화 |
| **3** | Symbol Index Mapping | 심볼-TXN 매핑 정보 및 참조 데이터 배포 |

**OrderID**: "good for current day only"로 정의되어 있으며, 매일 유지보수 시간에 시퀀스가 리셋된다. 레거시 일정에서 NYSE Arca 시퀀스 리셋은 02:03 ET, NYSE American은 02:01 ET에 수행되었으며, 확장 체제에서는 유지보수 시간(20:00~21:00 ET) 종료 시점으로 재조정된다.

### 4.5 FIX Gateway 프로토콜

참가자 연결은 **Pillar FIX Gateway(FIX 4.2/4.4)** 및 **Pillar Native Binary Gateway**를 통해 관리된다:

- **듀얼 IP 배포 모델**: Primary/Secondary 대상 IP를 통한 고가용성 보장
- **Drop Copy**: 별도의 FIX Gateway 인터페이스를 통해 모든 주문 활동의 실시간 사본 제공
- **세션 연속성**: Secondary IP 로그인 시 Primary IP에서의 마지막 애플리케이션 계층 메시지부터 시퀀스 번호가 계속됨

---

## 5. 주문 관리 및 세션 전환

### 5.1 FIX Tag 336 (TradingSessionID) 및 Tag 59 (TimeInForce)

NYSE Pillar 아키텍처는 주문의 실행 경계를 다음 FIX 태그로 규정한다:

| FIX 태그 | 명칭 | 역할 |
|----------|------|------|
| **Tag 336** | TradingSessionID | 주문이 체결 가능한 세션을 명시적으로 지정 (Extended Early, Core, Late) |
| **Tag 59** | TimeInForce | 주문 유효기간 설정 (Day=0, GTC, GTD 등) |

**세션 지정 규칙**: 연장 시간대에 주문 효력을 유지하려면 참가자가 **특정 연장 시간대 식별자(Tag 336)**를 명시적으로 지정해야 한다. Extended Early Session 지정이 없는 주문이 해당 시간에 제출되면 Pillar Gateway가 **체계적으로 거부(reject)**한다.

### 5.2 GTC 주문의 세션 간 유지

| 주문 유형 | 유지보수 시간(20:00~21:00 ET) 동작 | 비고 |
|-----------|-------------------------------------|------|
| **Day Order (TIF=0)** | 20:00 ET Late Session 종료 시 매칭 엔진 RAM에서 **일괄 삭제** | 다음 세션으로 이월 불가 |
| **GTC (Good-Til-Cancelled)** | **디스크에 영구 저장**; DR 클러스터(시카고 Cermak 데이터 센터)에 다크 파이버로 동시 복제 | 30~90일간 지속 |
| **GTD (Good-Til-Date)** | GTC와 동일한 지속 메커니즘; 지정 일자까지 유효 | - |

**콜드 스타트 시 주문장 복원 프로세스** (21:00 ET):
1. 매칭 엔진이 영구 데이터 저장소에서 GTC 주문을 로드
2. **Restatement 메시지** 생성: `ExecTransType = 3 (Status)`, `ExecType = D (Restated)`
3. FIX Drop Copy 및 독점 데이터 피드를 통해 참가자에게 복원 확인 브로드캐스트
4. 대량의 **Add Order (MsgType 100)** 메시지 burst 발생 (Extended Early Auction 시작 수 밀리초 전)

**주문 수정 시 큐 우선순위**:
- **가격 변경 또는 표시 수량 증가**: 시간 우선순위(time priority) **즉시 상실**
- **수량 감소만**: 원래 큐 위치 **유지**

### 5.3 MOO/LOO/MOC/LOC 주문의 세션 제한

경매 전용 주문은 특정 본장 유동성 이벤트에 근본적으로 연결된다:

| 주문 유형 | 체결 가능 세션 | 연장 프리마켓 중 동작 |
|-----------|----------------|----------------------|
| **MOO (Market-On-Open)** | Core Open Auction (09:30 ET)만 | 접수되나 즉각적 연속 거래 자격 박탈; 09:30 경매까지 수동 대기 |
| **LOO (Limit-On-Open)** | Core Open Auction (09:30 ET)만 | 동일 |
| **MOC (Market-On-Close)** | Closing Auction (16:00 ET)만 | 해당 시간대에 입력 불가 |
| **LOC (Limit-On-Close)** | Closing Auction (16:00 ET)만 | 해당 시간대에 입력 불가 |

### 5.4 Cancel on Disconnect (COD) 기능

네트워크 장애로 브로커-딜러의 연결이 끊어지면, Pillar Gateway가 **경매 주문을 제외한** 모든 대기 주문에 대해 즉각적이고 자동적인 취소를 개시한다. 이 프로토콜의 핵심 목적:

- 야간 시간대의 얇은 유동성 속에서 약탈적 알고리즘에 의한 stale quote 체결 방지
- 참가자의 의도치 않은 야간 노출(exposure) 차단
- Secondary IP 로그인 시 시퀀스 번호가 Primary IP의 마지막 메시지부터 이어져 주문 상태 매끄러운 보존

### 5.5 DoS 보호 (100회 실패 시 60초 차단)

Pillar Gateway는 엄격한 서비스 거부(DoS) 방어 메커니즘을 시행한다:

| 조건 | 동작 |
|------|------|
| 특정 SenderCompID 또는 Target IP에서 **100회** 로그인 실패 또는 세션 레벨 거부 발생 | **DoS 모드** 진입 |
| DoS 모드 진입 시 | 해당 SenderCompID의 모든 오픈 주문을 COD 설정에 따라 **즉시 취소** |
| 냉각 기간 | 해당 Target IP로부터의 모든 연결 시도를 **60초간** 거부 |

또한 Binary Gateway는 메시지 레이트 스로틀링(throttling)을 통해 매칭 엔진을 보호한다:

| 설정 모드 | 동작 |
|-----------|------|
| **Queue and Process** | 초과 메시지를 Gateway 메모리에 버퍼링, 엔진 읽기 속도에 맞춰 시간순 처리 |
| **Queue and Reject** | 초과 신규 주문은 `<78 - Throttle Reject>` 코드로 즉시 거부; 단, 취소 요청 및 cancel-replace는 여전히 큐잉 후 처리 |

---

## 6. 리스크 관리 및 변동성 통제

### 6.1 Market-Wide Circuit Breaker (MWCB): 7%/13%/20%

S&P 500 지수 기준으로 작동하는 시장 전체 서킷 브레이커:

| 레벨 | 하락 폭 | 동작 | 적용 시간 |
|------|---------|------|-----------|
| **Level 1** | **7%** | 15분 거래 중단 (15:25 ET 이전) | 정규 세션만 |
| **Level 2** | **13%** | 15분 거래 중단 (15:25 ET 이전) | 정규 세션만 |
| **Level 3** | **20%** | 당일 잔여 세션 거래 완전 중단 | 정규 세션만 |

**중요**: MWCB는 역사적으로 정규 거래 시간(09:30~16:00 ET)에만 적용되도록 설계되었다. 현행 시간외 세션에서는 이 산업 전반의 메커니즘이 **완전 비활성** 상태이다.

### 6.2 Limit Up-Limit Down (LULD) -- 정규시간만 적용

LULD 메커니즘은 후행 5분 평균 기준 가격에 기초하여 허용 가능한 가격 밴드를 동적으로 재계산한다:

| 구분 | Tier 1 (S&P 500, Russell 1000 등) | Tier 2 (기타) |
|------|-----------------------------------|---------------|
| 가격 밴드 | 일반적으로 **5%** | 더 넓은 밴드 |
| 적용 시간 | **정규 세션(09:30~16:00 ET)에만** | 동일 |
| 연장 세션 적용 | **미적용** | **미적용** |

연장 프리마켓 세션(오전 3시 등)에 5%의 좁은 밴드를 강제하면 지속적이고 연쇄적인 거래 정지가 발생하여 야간 시장의 효용성을 심각하게 저하시키므로, LULD는 의도적으로 시간외 세션에 적용되지 않는다.

### 6.3 확장시간 Double-Wide Collars (20%/10%/6%)

LULD가 적용되지 않는 연장 세션에서의 가격 보호를 위해 NYSE Arca는 Pillar Gateway 내 독점적 **Limit Order Price Protection**에 의존한다:

| 기준 가격 범위 | Double-Wide Collar 비율 |
|----------------|------------------------|
| 고가 증권 | **6%** |
| 중가 증권 | **10%** |
| 저가 증권 | **20%** |

기업들은 기본 증권의 기준 가격에 따라 지정가 주문 거부 임계값을 동적으로 확장하는 "Double-Wide" 가격 확인을 프로그래밍 방식으로 구성할 수 있다.

### 6.4 Pillar Risk Controls (Risk Entities, SubID, GRMP)

#### Risk Entity 구조

Pillar는 다음 세 가지 요소를 연결하여 프로그래밍 방식의 "Risk Entity"를 생성한다:

| 요소 | 설명 |
|------|------|
| **Symbol** | 기본 증권 기호 |
| **MPID** | 브로커의 Market Participant Identifier |
| **SubID** | 4자리 영숫자 식별자 (선택적) |

#### 주요 제한 사항 및 파라미터

| 파라미터 | 값/범위 |
|----------|---------|
| MPID/SubID 쌍당 최대 심볼 수 | **400개** |
| 슬라이딩 윈도우 시간 범위 | **100ms ~ 300s** |
| 모니터링 지표 | 거래량, 총 주식 거래량, 백분율 한도 |
| 한도 위반 시 자동 동작 | **Cancel Non-Auction Orders & Block** 명령 실행 |
| 위반 추적 | **GRMP (Gross Risk Multiplier)** 카운터 증가 |

이 아키텍처를 통해 청산 회사는 APAC 시간대에서 활동하는 특정 퀀트 데스크의 총 명목 노출을 회사 전체 주간 운영과 독립적으로 조절할 수 있다. 한도 위반 시 위반 엔티티의 야간 유동성 프로필이 즉시 0으로 만들어지며 GRMP 카운터가 증가한다.

---

## 7. 청산 및 결제 연동 (DTCC/NSCC)

### 7.1 UTC 24x5 Phase 1 (2024.9) / Phase 2 (2026.6 목표)

DTCC의 주식 청산 자회사인 NSCC는 UTC(Universal Trade Capture) 시스템을 24x5 일정으로 근본적으로 변경 중이다:

| 단계 | 시기 | 내용 |
|------|------|------|
| **Phase 1** | **2024년 9월** 구현 완료 | UTC 시스템 개장 시간을 01:30 ET로 확대; 레거시 04:00 ET 대비 2.5시간 조기 야간 거래 제출 가능 |
| **Phase 2** | **2026년 6월** 목표 (규제 검토 대기) | UTC를 **일요일 20:00 ET ~ 금요일 20:00 ET** 완전 24x5 운영으로 전환 |

Phase 2 완료 시:
- UTC가 FIX 및 MQ 메시지를 지속적으로 수신
- NSCC의 CCP(Central Counterparty) 보증이 야간 거래에 **즉각적으로 적용**
- **즉각적인 계약 갱신(novation)**: 과거 야간 장외 ATS에서의 양자간 신용 위험 제거

### 7.2 T+1 결제 체제

2024년 5월 도입된 T+1 결제 주기는 23시간 프레임워크 내에서도 엄격하게 유지된다:

- **20:00 ET Trade Date Cutoff**: 불변의 거래일 전환 기준점
- NSCC 리스크 시스템: **15분마다** 회원 노출 평가 및 동적 증거금 콜(margin call) 발행 가능
- **Margin Requirement Differential (MRD) charge**: 본장 유동성 도착 전 야간 포지션의 비순환(un-netted) 위험 해소

### 7.3 별도 9A/9B 야간 청산 관계

야간 세션 참가자는 **완전히 분리된** Correspondent Clearing(CORR) 및 Qualified Special Representative(QSR) 9A/9B 관계를 설정해야 한다:

| 구분 | 주간 청산 | 야간 청산 |
|------|-----------|-----------|
| 9A/9B 관계 | 기존 주간 운영용 | **별도 설정 필수** |
| 목적 | 표준 본장 거래 청산 | APAC 시간대 알고리즘 오류/대규모 방향성 베팅이 주간 증거금 한도를 침범하지 않도록 리스크 구획화 |

### 7.4 High-Value Threshold

UTC 시스템은 대규모 오류 거래를 차단하기 위한 하드코딩된 유효성 검사를 구현한다:

| 시간대 | 임계값 | 대상 |
|--------|--------|------|
| **야간 (Overnight)** | **$1 Billion** | 장외(OTC) Correspondent Clearing 트랜잭션 |
| **주간 (Daytime)** | **$1.5 Billion** | 동일 |

이 임계값을 초과하는 거래는 자동으로 플래그되어 억제(contain)되며, "fat finger" 입력이 하위 CNS 체인을 손상시키기 전에 차단된다.

---

## 8. 시장 데이터 배포

### 8.1 SIP (CTS/CQS) 확장 -- 일~금 21:00-20:00 ET

확장 거래시간의 실행 가능성은 통합 시장 데이터의 지속적 가용성에 전적으로 의존한다. SEC 및 SIFMA는 SIP가 완전 가동되지 않으면 NYSE Arca가 확장 세션을 운영할 수 **없다**고 강조하였다.

| 항목 | 현행 | 확장 목표 |
|------|------|-----------|
| **SIP 운영시간** | ~04:00~20:00 ET | **일요일 21:00 ET ~ 금요일 20:00 ET** (23시간 패러다임) |
| **데이터 품질** | 본장과 동일 | 본장과 **동등한** 지연시간, 신뢰성, 범위 보장 필수 |
| **야간 체결 식별** | '.T' sale condition | 야간 체결이 Last Sale eligible이 아님을 명시 |
| **공식 종가** | 'M' sale condition (16:00 ET Closing Auction) | **변경 없음**: OCP는 16:00 ET에 고정 |

### 8.2 NYSE Integrated Feed (XDP)

NYSE Arca의 독점(proprietary) 데이터 피드:

- **Pillar Integrated Feed**: 심층 주문장(deep book) 가시성 제공
- **BQT (Best Quote and Trade) Feed**: 최우선 호가 및 체결 정보
- 연속 운영: 23시간 내내 비스로틀(un-throttled) 데이터 제공
- 참가자는 세션 경계 전반에 걸쳐 **8바이트 OrderID** 및 **4바이트 TradeID** 페이로드를 엄격하게 매핑해야 함

### 8.3 MoldUdp64 프로토콜

UTP 및 CTA SIP 데이터는 **MoldUdp64** 프로토콜을 통해 게시된다:

- 바이너리 페이로드의 **순차적 전달** 보장
- NBBO(National Best Bid and Offer) 업데이트를 포함
- 23시간 세션 동안 VWAP(Volume Weighted Average Price) 및 기관 거래 추적에 필수적인 결정론적 시퀀싱 제공

---

## 9. Maintenance Pause (20:00-21:00 ET) 상세

매일 1시간의 유지보수 시간은 NYSE Arca 확장 체제의 **아키텍처 핵심**이다. 외부 FIX 트래픽을 정확히 60분간 중단함으로써 라이브 매칭 엔진에서 실행하기에는 위험한 기능들을 안전하게 수행한다.

### 자동화 작업 파이프라인

| 순서 | 작업 | 상세 |
|------|------|------|
| 1 | **데이터베이스 백업** | 모든 영구 주문, 사용자 구성, 라우팅 지시, 리스크 한도 활용 상태 스냅샷 |
| 2 | **시퀀스 리셋** | FIX 시퀀스 번호, 매칭 엔진 실행 ID, XDP 피드 Symbol Sequence Numbers를 **1로 초기화** (MsgType 1); 정수 오버플로 방지 및 깨끗한 진단 기준선 제공 |
| 3 | **기업행위 처리** | 배당금 적용, 주식 분할 실행, 심볼 변경, 배당락 조정 계산; 조정된 종가 및 참조 데이터를 SIP의 Symbol Reference Data 메시지(CQS/CTS)로 배포 |
| 4 | **소프트웨어 배포** | OS 패치, 매칭 엔진 로직 업데이트, 네트워크 라우팅 최적화; 자동화된 회귀 테스트 실행; 21:00 오픈 전 오류 시 이전 상태로 즉각 롤백 가능 |
| 5 | **심볼 매핑 파일 배포** | `$Market$SymbolMapping_YYYYMMDD.xml`을 공개 FTP 서버에 게시 |

### 콜드 스타트 시 주문장 복원 프로세스

매칭 엔진의 "sleep/wake" 시퀀스:

1. **20:00 ET**: 일시적 상태 데이터 RAM에서 삭제; 영구 데이터(GTC 주문 등) 로컬 디스크 저장 + Cermak DR 클러스터로 다크 파이버 동시 복제
2. **20:00~21:00 ET**: 위 자동화 작업 파이프라인 실행
3. **~20:55 ET**: Extended Early Session 주문 접수 시작 (5분 주문 축적 윈도우)
4. **21:00 ET**: 콜드 스타트 완료
   - 영구 데이터 저장소에서 GTC 주문 로드
   - **Restatement 메시지 생성**: `ExecTransType = 3 (Status)`, `ExecType = D (Restated)`
   - FIX Drop Copy 및 독점 피드를 통해 참가자에게 복원 확인 브로드캐스트
   - 대량 Add Order (MsgType 100) 메시지 burst
   - Extended Early Open Auction 실행

---

## 10. KRX와의 비교

### 10.1 종합 비교표

| 비교 항목 | NYSE / NYSE Arca | KRX (현행) |
|-----------|-------------------|------------|
| **총 거래시간** | 23시간 (목표) | 6.5시간 (09:00~15:30 KST) |
| **정규 세션** | 09:30~16:00 ET (6.5h) | 09:00~15:30 KST (6.5h) |
| **프리마켓** | 21:00 ET(전일)~09:30 ET (12.5h 목표) | 08:00~09:00 KST (동시호가, 1h) |
| **애프터마켓** | 16:00~20:00 ET (4h) | 15:30~16:00 KST (장 마감 동시호가, 0.5h) |
| **유지보수 시간** | 20:00~21:00 ET (1h) | 해당 없음 (야간 전체 비운영) |
| **오프닝 옥션** | Imbalance Info 08:00 시작, Freeze 09:29:55 | 동시호가 08:00~09:00 (단일가매매) |
| **클로징 옥션** | Closing Imbalance 15:50 시작, D-Orders | 장 마감 동시호가 15:20~15:30 (단일가매매) |
| **매칭 엔진** | Pillar (14 TXN 분산 파티션) | EXTURE 3.0 (시장별 멀티 매칭, 50µs) |
| **서킷 브레이커** | MWCB 7%/13%/20% (정규시간만) | KOSPI 8%/15%/20% (3단계) |
| **변동성 완화** | LULD (정규), Double-Wide Collars (연장) | VI (Volatility Interruption) + 정적 가격제한폭 (±30%) |
| **결제 주기** | T+1 (2024.5 시행) | T+2 (일부 T+1 논의 중) |
| **청산기관** | DTCC/NSCC (UTC 24x5) | KSD (한국예탁결제원) |
| **야간 체결 식별** | '.T' sale condition | 해당 없음 |
| **주문 프로토콜** | FIX 4.2/4.4 + Native Binary | FIX + 독자 프로토콜 |
| **시장 데이터** | SIP(CTS/CQS) + XDP(Proprietary) | KOSCOM 통합 데이터 피드 |

### 10.2 KRX 도입 시 참고할 핵심 시사점

#### (1) 동적 가격 제한폭 (Dynamic Collars) 도입 필요

- 현행 KRX의 정적 일일 상하한가(±30%)를 야간에 그대로 적용하는 것은 부적절
- NYSE Arca의 Double-Wide Collars(20%/10%/6%) 모델을 벤치마킹하여 **유동성 깊이에 따라 동적으로 확장되는 가격 제한폭** 설계 필요
- 야간 전용 "LULD-Lite" 알고리즘 구현 권장: 임계값(예: ±10%) 위반 시 해당 종목 연속 거래 중단 -> 5분 동결 -> 재개장 경매

#### (2) 시장 데이터 동등성 확보

- 야간 세션 데이터 품질이 정규 세션 대비 열화되어서는 안 됨
- KOSCOM과의 기술적 합의를 통해 야간 체결 건의 분류 체계 구축
- KOSPI 200 등 국내 지수 계산에서 야간 가격 데이터를 **격리**하는 식별자 프로토콜 필수
- 야간 체결 건의 '.T' 유사 식별자 도입으로 기술적 분석 차트, 자동 증거금 계산의 왜곡 방지

#### (3) 청산 인프라 현대화

- KSD의 UTC 동등 시스템을 24x5로 확장하는 로드맵 수립
- T+1 결제 전환과 연장 거래시간의 동시 추진 시 FIX Tag 715 수준의 Clearing Business Date 메커니즘 도입
- 야간 전용 9A/9B 유사 청산 관계의 분리 설정
- 15분 주기 증거금 재계산 및 동적 마진콜 역량 구축

#### (4) 운영 인력 체계 재구성

- "Follow-the-Sun" 3교대 운영 모델 도입
- 야간 전담 Market Surveillance, IT Operations, 회원 지원 팀 설치
- 야간 감시는 ML 기반 결정론적 경보 메커니즘으로 전환 (스푸핑, 레이어링, 시세조종 탐지)
- 야간 근무자 건강관리, 피로 관리, 경력 개발 경로 제도화

#### (5) 리테일 투자자 보호

- 야간 거래의 구체적 위험(유동성 감소, 변동성 확대, 넓은 스프레드, NBBO 보호 부재)에 대한 **필수 고지** 규정 마련
- 개인 투자자의 야간 주문 라우팅 전 명시적 위험 동의 절차 의무화

---

## 참고자료

### SEC 규제 문서
- Self-Regulatory Organizations; NYSE Arca, Inc.; Notice of Filing of Proposed Rule Change (SR-NYSEARCA-2024-89): [federalregister.gov/documents/2024/11/14/2024-264...](https://www.federalregister.gov/documents/2024/11/14/2024-26418/self-regulatory-organizations-nyse-arca-inc-notice-of-filing-of-proposed-rule-change-to-adopt)
- SEC Release No. 34-101985: [sec.gov/files/rules/sro/nysearca/2024...](https://www.sec.gov/files/rules/sro/nysearca/2024/34-101985.pdf)
- Amendment No. 1: [federalregister.gov/documents/2024/12/30/2024-309...](https://www.federalregister.gov/documents/2024/12/30/2024-30903/self-regulatory-organizations-nyse-arca-inc-notice-of-filing-of-amendment-no-1-to-a-proposed-rule)
- Amendment No. 2 and Order Granting Approval (Release No. 34-102400): [sec.gov/files/rules/sro/nysearca/2025...](https://www.sec.gov/files/rules/sro/nysearca/2025/34-102400.pdf)
- SR-NYSEARCA-2024-89 Am. 2: [nyse.com/publicdocs/nyse/markets/nyse-...](https://www.nyse.com/publicdocs/nyse/markets/nyse-arca/rule-filings/filings/2025/SR-NYSEArca-2024-89_Am._2.pdf)
- Federal Register Filing: [public-inspection.federalregister.gov/2025-02688.pdf](https://public-inspection.federalregister.gov/2025-02688.pdf)
- Rule 7.34-E(T) Exhibit 5: [sec.gov/files/rules/sro/nysearca/2024...](https://www.sec.gov/files/rules/sro/nysearca/2024/34-101985-ex5.pdf)

### NYSE 공식 문서
- Extended Hours Trading: [nyse.com/extended-hours-trading](https://www.nyse.com/extended-hours-trading)
- Extended-Hours Trading FAQ: [nyse.com/publicdocs/nyse/NYSE_Extended...](https://www.nyse.com/publicdocs/nyse/NYSE_Extended_Hours_Trading_FAQ.pdf)
- NYSE Closing Auction Insights: [nyse.com/data-insights/nyse-closing-au...](https://www.nyse.com/data-insights/nyse-closing-auction-price-discovery-opportunities-reach-new-highs)
- NYSE Rules: [nyse.com/publicdocs/nyse/regulation/ny...](https://www.nyse.com/publicdocs/nyse/regulation/nyse/NYSE_Rules.pdf)
- Auctions: [nyse.com/trade/auctions](https://www.nyse.com/trade/auctions)
- Opening and Closing Auctions Fact Sheet: [nyse.com/publicdocs/nyse/markets/nyse/...](https://www.nyse.com/publicdocs/nyse/markets/nyse/NYSE_Opening_and_Closing_Auctions_Fact_Sheet.pdf)
- Trading Information: [nyse.com/trade/trading-information](https://www.nyse.com/trade/trading-information)

### NYSE Pillar 기술 사양
- NYSE Pillar: [nyse.com/pillar](https://www.nyse.com/pillar)
- Pillar Risk Controls: [nyse.com/publicdocs/nyse/NYSE_Pillar_R...](https://www.nyse.com/publicdocs/nyse/NYSE_Pillar_Risk_Controls.pdf)
- Pillar Integrated Feed Client Specification v2.5c: [nyse.com/publicdocs/nyse/data/Pillar_I...](https://www.nyse.com/publicdocs/nyse/data/Pillar_Integrated_Feed_Client_Specification_v2.5c.pdf)
- Pillar Common Client Specification v2.6c: [nyse.com/publicdocs/nyse/data/Pillar_C...](https://www.nyse.com/publicdocs/nyse/data/Pillar_Common_Client_Specification_v2.6c.pdf)
- Pillar Gateway FIX Protocol Specification: [nyse.com/publicdocs/nyse/NYSE_Pillar_G...](https://www.nyse.com/publicdocs/nyse/NYSE_Pillar_Gateway_FIX_Protocol_Specification.pdf)
- Pillar Gateway Binary Protocol Specification: [nyse.com/publicdocs/nyse/NYSE_Pillar_G...](https://www.nyse.com/publicdocs/nyse/NYSE_Pillar_Gateway_Binary_Protocol_Specification.pdf)
- NYSE Group Security Master Client Specification v4.0.9: [nyse.com/publicdocs/nyse/data/NYSE_Gro...](https://www.nyse.com/publicdocs/nyse/data/NYSE_Group_Security_Master_Client_Specification_v4.0.9.pdf)
- NYSE BQT Common Client Specification: [nyse.com/publicdocs/nyse/data/NYSE_BQT...](https://www.nyse.com/publicdocs/nyse/data/NYSE_BQT_Common_Client_Specification.pdf)
- Pillar Options Common Client Specification: [nyse.com/publicdocs/nyse/data/Pillar_O...](https://www.nyse.com/publicdocs/nyse/data/Pillar_Options_Common_Client_Specification.pdf)

### DTCC/NSCC 문서
- Preparing US Equity Markets for 24x5 Trading: [dtcc.com/dtcctransformation/24x5](https://www.dtcc.com/dtcctransformation/24x5)
- THE SHIFT TO 24X5 TRADING: [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/theshiftto24x5trading.pdf)
- UTC 24x5 Extended Trading Hours: [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/UTC-24-x-5-Extended-Trading-Hours.pdf)
- Universal Trade Capture (UTC) 24x5 FAQ: [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/Universal-Trade-Capture-FAQs.pdf)
- 24x5 Trading Update (A9689): [dtcc.com/-/media/Files/pdf/2026/1/7/A9...](https://www.dtcc.com/-/media/Files/pdf/2026/1/7/A9689.pdf)
- 24x5 Executive Summary: [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/dtcc-24x5-Executive-Summary.pdf)
- DTCC FAQ: [dtcc.com/dtcctransformation/faqs](https://www.dtcc.com/dtcctransformation/faqs)
- Shortening the US Equities Settlement Cycle: [dtcc.com/ust1](https://www.dtcc.com/ust1)

### SIP 및 시장 데이터
- SIPs Submit Plan Amendment for Overnight Trading: [prnewswire.com/news-releases/sips-submit-pla...](https://www.prnewswire.com/news-releases/sips-submit-plan-amendment-to-extend-operating-hours-to-accommodate-overnight-trading-302647034.html)
- UTP Plan Participants Propose Extended Hours: [findknowdo.com/news/01/09/2026/utp-plan-part...](https://www.findknowdo.com/news/01/09/2026/utp-plan-participants-propose-extended-global-trading-hours)
- UTP Binary Output Specification (MoldUdp64): [utpplan.com/DOC/UtpBinaryOutputSpec_Fract...](https://utpplan.com/DOC/UtpBinaryOutputSpec_Fractional.pdf)

### 기타 참고
- ICE Insights - Expanding Market Hours: [ice.com/insights/ice-vox/expanding-ma...](https://www.ice.com/insights/ice-vox/expanding-market-hours-key-considerations-and-the-nyses-approach-v92y9h4ox1)
- SIFMA Extended Trading Hours: [sifma.org/issues/market-structure/exten...](https://www.sifma.org/issues/market-structure/extended-trading-hours)
- LULD Plan: [luldplan.com/](https://www.luldplan.com/)
- CAT Reporting Technical Specifications: [catnmsplan.com/sites/default/files/2020-05/C...](https://catnmsplan.com/sites/default/files/2020-05/CAT-Reporting-Technical-Specifications-for-Industry-Members-v2.2.1-r5-REDLINE.pdf)
- FINRA Trading Terms: [finra.org/investors/insights/time-param...](https://www.finra.org/investors/insights/time-parameters-qualifiers-stock-orders)
- NYSE LULD Enhancement Testing: [nyse.com/publicdocs/nyse/markets/nyse/...](https://www.nyse.com/publicdocs/nyse/markets/nyse/NYSE_Group_LULD_12_testing.pdf)
- NYSE Disaster Recovery FAQ: [nyse.com/publicdocs/support/DisasterRe...](https://www.nyse.com/publicdocs/support/DisasterRecoveryFAQs.pdf)
- Is 24/7 Trading Better? (SSRN): [papers.ssrn.com/sol3/Delivery.cfm/4942934.pdf](https://papers.ssrn.com/sol3/Delivery.cfm/4942934.pdf?abstractid=4942934)

---

*본 보고서는 SEC 규칙 제출 문서, NYSE 공식 기술 사양서, DTCC 변환 프로그램 문서 및 관련 학술 자료를 기반으로 작성되었습니다.*
