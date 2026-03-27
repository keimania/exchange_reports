# CME 그룹 24시간 거래 인프라 및 규제 프레임워크 분석

> **작성일**: 2026-03-26
> **목적**: CME Group의 거의 24시간 연속 파생상품 거래 인프라를 기술적·운영적·규제적 관점에서 분석하고, 한국거래소(KRX) 주식시장 거래시간 연장에 대한 전략적 시사점을 도출한다.

---

## 1. 기관 개요

### 1.1 CME Group 구조

CME Group Inc.는 세계 최대의 파생상품 거래소 운영 기업으로, 네 개의 지정 계약 시장(DCM)을 통합 운영한다.

| 거래소 | 설립연도 | 주요 자산 클래스 | 대표 상품 |
|--------|---------|----------------|----------|
| **CME** (Chicago Mercantile Exchange) | 1898 | 주가지수, 외환, 금리 | E-mini S&P 500, Eurodollar |
| **CBOT** (Chicago Board of Trade) | 1848 | 곡물, 금리, 주가지수 | Treasury Futures, Corn, Wheat |
| **NYMEX** (New York Mercantile Exchange) | 1882 | 에너지 | WTI Crude Oil, Natural Gas |
| **COMEX** (Commodity Exchange) | 1933 | 금속 | Gold, Silver, Copper |

CME Group은 단일 청산소(CME Clearing)를 통해 4개 거래소의 모든 거래를 보증하며, 일일 평균 **2,000만 건 이상**의 거래를 처리한다. 이 수직 통합 구조는 교차 증거금(cross-margining), 통합 리스크 관리, 단일 담보 풀(collateral pool) 운영을 가능하게 하는 핵심 기반이다.

### 1.2 Globex 플랫폼 개요

CME Globex는 1992년 도입된 전자거래 플랫폼으로, 현재 일요일 17:00 CT부터 금요일 16:00 CT까지 거의 24시간 연속 운영된다. 주중 일일 유지보수 창은 단 **1분**(16:00~16:01 CT)에 불과하며, 이는 전 세계 주요 거래소 중 가장 짧은 중단 시간이다.

### 1.3 자산 클래스 커버리지

| 자산 클래스 | 주요 상품 | 일일 평균 거래량(ADV) |
|------------|----------|---------------------|
| 주가지수선물 | E-mini S&P 500, E-mini NASDAQ-100, Micro E-mini | 약 600만 계약 |
| 금리 | 10-Year T-Note, Eurodollar, SOFR | 약 1,200만 계약 |
| 외환(FX) | EUR/USD, JPY/USD, GBP/USD | 약 100만 계약 |
| 에너지 | WTI Crude Oil, Henry Hub Natural Gas | 약 300만 계약 |
| 농산물 | Corn, Soybeans, Wheat, Live Cattle | 약 150만 계약 |
| 금속 | Gold, Silver, Copper | 약 80만 계약 |

---

## 2. 거래 세션 및 시간 구조

### 2.1 운영 시간: 일요일 17:00 CT ~ 금요일 16:00 CT

CME Globex의 핵심 운영 원칙은 **거의 연속적인 시장 접근성**이다. 주간 총 운영 시간은 약 **119시간**(주 168시간 중 약 71%)에 달하며, 이는 전통적 주식거래소의 주 32.5시간(6.5시간 x 5일) 대비 약 **3.7배**에 해당한다.

| 구분 | 시간 (CT) | 시간 (KST) | 비고 |
|------|-----------|-----------|------|
| 주간 개장 | 일요일 17:00 | 월요일 08:00 | 아시아 시장 개장에 맞춤 |
| 주간 폐장 | 금요일 16:00 | 토요일 07:00 | 미국 정규장 종료 후 |
| 일일 정산 | 16:00 CT | 07:00 KST | 일일 결제가격 산출 |

### 2.2 일일 유지보수 윈도우: 16:00~16:01 CT (1분)

CME Globex의 가장 주목할 만한 기술적 성취는 일일 유지보수 창을 **단 1분**으로 압축한 것이다. 이 1분 동안 매칭엔진은 Close 상태로 전환된 후 즉시 Open 상태로 복귀한다. 시퀀스 리셋은 수행되지 않으며, 모든 미체결 주문(working orders)은 그대로 보존된다.

| 유지보수 유형 | 운영 시간 (CT) | Pre-Open/Open (CT) | 시퀀스 리셋 | 빈도 |
|-------------|---------------|--------------------|-----------|----|
| **일일 유지보수** | 16:00~16:01 | 16:01 Open | 아니요 | 월~금 매일 |
| **화요일 연장** | 02:00~03:45 | 03:45~04:00 Pre-Open | 아니요 | 매주 화요일 |
| **토요일 연장** | 02:00~03:45 | 03:45~04:00 Pre-Open | 예 | 매주 토요일 |

### 2.3 확장 유지보수: 화/토 03:45~04:00 CT (15분 Pre-Open)

광범위한 시스템 업그레이드, 시퀀스 리셋 및 연장된 데이터베이스 유지보수를 위해 CME Globex는 두 가지 주요 연장 유지보수 창을 운영한다.

- **화요일 연장 유지보수** (02:00~03:45 CT): 약 1시간 45분간 시스템 중단. 03:45~04:00 CT에 15분간 Pre-Open 상태 운영. 시퀀스 리셋 미수행.
- **토요일 연장 유지보수** (02:00~03:45 CT): 동일한 시간대이나 주간 시퀀스 리셋이 수행됨. 이는 주간 누적 데이터를 초기화하고 다음 주 거래를 준비하는 유일한 완전 리셋 시점.

### 2.4 Market State 관리

CME Globex 매칭엔진은 다음과 같은 명시적 시장 상태(Market State)를 순환한다:

```
Pre-Open → Open → [Halt] → [Pre-Open] → Close
```

| 상태 | 주문 입력 | 주문 매칭 | 주문 취소 | 설명 |
|------|---------|---------|---------|------|
| **Pre-Open** | 허용 | 불가 | 허용 | 호가 수집 단계, 이론가격 산출 |
| **Open** | 허용 | 허용 | 허용 | 정상 연속 거래 상태 |
| **Halt** | 불가 | 불가 | 불가 | 비상 중단, 모든 활동 정지 |
| **Close** | 불가 | 불가 | 불가 | 일일 정산 및 유지보수 |

Pre-Open 상태에서는 FAK(Fill-and-Kill) 및 FOK(Fill-or-Kill) 주문이 거부된다. 이 조건부 주문 유형들은 오직 Open 상태에서만 허용된다.

---

## 3. 주문 유형 및 매칭 로직

### 3.1 기본 주문 유형

| 주문 유형 | 설명 | Pre-Open | Open |
|----------|------|---------|------|
| **Limit Order** | 지정가 주문. 지정 가격 이하(매수) 또는 이상(매도)에서만 체결 | 허용 | 허용 |
| **Market-Limit Order** | 최우선 호가에서 가능한 수량 체결 후, 잔여분을 해당 가격의 지정가 주문으로 전환 | 불가 | 허용 |
| **Protected Market Order** | 시장가 주문에 보호 가격 밴드 적용. 지정 범위를 초과하는 가격에서의 체결 방지 | 불가 | 허용 |

Protected Market Order는 CME Globex 고유의 안전장치로, 유동성이 낮은 야간 시간대에 시장가 주문이 비정상적 가격에서 체결되는 것을 방지한다.

### 3.2 FAK(Fill-and-Kill) 및 FOK(Fill-or-Kill)

| 조건부 유형 | 동작 | Open 상태만 허용 이유 |
|------------|------|---------------------|
| **FAK** | 가능한 수량 즉시 체결, 미체결 잔량 즉시 취소 | Pre-Open에서는 매칭이 불가하므로 전량 취소됨 |
| **FOK** | 전량 즉시 체결 가능 시에만 체결, 불가 시 전량 취소 | 동일 사유 |

### 3.3 BTIC (Basis Trade at Index Close)

BTIC는 CME 주가지수선물 시장에 특화된 혁신적 주문 유형이다. 거래 참가자가 선물 계약을 현물 지수 종가(Index Close) 대비 베이시스(basis, 선물-현물 스프레드)로 거래할 수 있게 한다.

- **거래 방식**: 참가자는 베이시스 포인트를 지정하여 주문 제출. 당일 현물 종가 확정 후 최종 선물 가격이 결정됨.
- **활용 사례**: 기관투자자의 현물-선물 베이시스 트레이딩, 인덱스 펀드 리밸런싱
- **거래 시간**: Globex 정규 거래시간 동안 전자적으로 거래 가능

### 3.4 TACO (Trade at Cash Open)

TACO는 BTIC의 개장가 버전으로, 선물 계약을 다음 날 현물 시장 개장가(Cash Open) 대비 베이시스로 거래한다.

- **거래 방식**: 참가자가 개장가 대비 베이시스를 지정. 다음 거래일 현물 개장가 확정 후 최종 가격 결정.
- **활용 사례**: 오버나이트 포지션 구축, 아시아/유럽 시간대 투자자의 미국 현물 개장가 기준 헤징
- **전략적 의의**: 야간 세션에서 다음날 현물 개장가에 연동된 거래를 사전 확보할 수 있어, 시간대 차이에 따른 리스크를 효과적으로 관리

### 3.5 GTC/GTD 주문의 세션 간 Timestamp Priority 보존

연속 시장에서 **타임스탬프 우선순위(timestamp priority)**는 핵심 원칙으로 간주된다.

- **GTC (Good-Till-Cancelled)**: 명시적 취소 시까지 유효. 세션 경계를 넘어 타임스탬프 우선순위가 엄격하게 유지됨.
- **GTD (Good-Till-Date)**: 지정일까지 유효. GTC와 동일하게 세션 간 우선순위 보존.

**우선순위 상실 조건**:
1. 작업 수량(working quantity) 증가
2. 절대 가격 변경
3. 계좌 번호 수정

이 세 가지 조건 중 하나라도 발생하면 주문은 즉시 대기열의 맨 뒤로 이동하며, 새로운 타임스탬프가 부여된다.

---

## 4. 매칭엔진 아키텍처

### 4.1 Market Segment 수평 파티셔닝

CME Globex 매칭엔진은 **마켓 세그먼트(Market Segment)** 단위로 수평 파티셔닝된다. 각 마켓 세그먼트는 관련 상품군(예: E-mini 주가지수 그룹, 에너지 그룹)을 포함하며, 독립적인 매칭엔진 인스턴스에서 처리된다.

이 아키텍처의 핵심 장점:
- **장애 격리**: 한 세그먼트의 장애가 다른 세그먼트에 영향을 미치지 않음
- **독립적 확장**: 거래량 증가에 따라 세그먼트별로 독립 확장 가능
- **결정론적 성능**: 세그먼트별 전용 리소스로 일관된 레이턴시 보장

### 4.2 Market Segment Gateway (MSGW) 패러다임

CME Globex는 두 가지 접속 게이트웨이를 제공한다:

| 게이트웨이 | 대상 | 특성 |
|-----------|------|------|
| **CGW** (Customer Gateway) | 일반 참가자 | 단일 연결로 다수 세그먼트 접근. 편의성 중심 |
| **MSGW** (Market Segment Gateway) | 초저지연 참가자 | 세그먼트 직접 연결. 결정론적 레이턴시 최적화 |

MSGW는 초저지연(ultra-low latency) 참가자와 구조적 결정론을 위해 설계되었다. 참가자는 전용 마켓 세그먼트에 직접 연결하며, 단일 세션 ID, 비밀번호, 포트를 사용하되 특정 마켓 세그먼트의 기본 및 백업 게이트웨이에 해당하는 **최대 17개의 고유 IP 주소**에 각각 연결해야 한다.

### 4.3 Session ID 기반 다중 세그먼트 접속

MSGW 모델에서 세션 ID는 여러 MSGW 간에 공유된다. 이는 참가자가 하나의 논리적 세션 아이덴티티로 복수의 마켓 세그먼트에 접속할 수 있음을 의미하며, 세션 관리의 복잡성을 줄이면서도 세그먼트별 직접 연결의 이점을 유지한다.

### 4.4 마이크로초 결정론적 레이턴시

CME Globex의 매칭엔진은 **마이크로초(microsecond)** 단위의 결정론적 레이턴시를 목표로 설계되었다. 주요 특성:

- **FIFO (선입선출)**: 대부분의 주가지수선물, 에너지 등 주요 상품에 적용
- **Pro-Rata (비례배분)**: Eurodollar 등 특정 금리 상품에 적용
- **LMM (Lead Market Maker)**: 지정 시장조성자에게 우선권 부여
- **TOP (Top Order Priority)**: 최우선 주문에 추가 우선순위 할당

매칭 알고리즘은 개별 상품의 유동성 프로필에 맞춰 FIFO, Pro-Rata, LMM/TOP 등의 복합 변형이 적용된다.

---

## 5. 프로토콜 계층

### 5.1 iLink 3 (FIXP 세션 계층 + SBE 애플리케이션 계층)

글로벌 24시간 시장의 대역폭과 지연 시간 요구 사항을 충족하기 위해 CME는 전통적 ASCII 기반 FIX 프로토콜 대신 고도로 최적화된 바이너리 프레임워크를 도입했다.

| 계층 | 프로토콜 | 역할 |
|------|---------|------|
| 세션 계층 | **FIXP** (FIX Performance) | 연결 관리, 시퀀스 번호, 하트비트 |
| 애플리케이션 계층 | **SBE** (Simple Binary Encoding) | 비즈니스 페이로드 인코딩/디코딩 |
| 시장 데이터 | **MDP 3.0** (Market Data Platform) | 실시간 시세, 호가 데이터 배포 |

### 5.2 FIXP: 경량 P2P, UUID 기반 세션 지속성

FIXP 프로토콜의 핵심 특성:

- **경량 포인트-투-포인트 세션**: 기존 ASCII FIX에 내재된 장황한 헤더 및 트레일러 오버헤드를 완전 제거
- **UUID 기반 세션 식별**: 각 세션에 범용 고유 식별자(UUID) 할당. 네트워크 중단 후 세션 복구 시 동일 UUID로 재접속하여 시퀀스 상태 복원
- **결정론적 시퀀스 관리**: 양방향 시퀀스 번호로 메시지 무결성 보장. 갭(gap) 발생 시 자동 재전송 요청

### 5.3 SBE: 바이너리 인코딩, ASCII FIX 대비 오버헤드 제거

SBE는 애플리케이션 계층에서 메시지의 인코딩 및 디코딩 속도를 극적으로 높인다.

| 특성 | ASCII FIX | SBE |
|------|----------|-----|
| 필드 길이 | 가변 (태그=값 쌍) | **고정 길이** |
| 필드 위치 | 순차 파싱 필요 | **고정 위치** (오프셋 직접 접근) |
| 바이트 순서 | ASCII 텍스트 | **리틀 엔디안 바이너리** |
| 메모리 매핑 | 불가 (파싱 필요) | **네트워크→메모리 직접 매핑** |
| 파싱 복잡도 | 상태 기반 순차 파싱 | **제로 카피(zero-copy)** |

SBE의 고정 길이 필드, 고정 위치 및 리틀 엔디안 바이트 순서를 통해 클라이언트 거래 시스템은 수신 네트워크 데이터를 애플리케이션 메모리 버퍼에 직접 매핑할 수 있다.

MDP 3.0 시장 데이터 프로토콜은 **tag 5799-MatchEventIndicator**를 활용하여 매칭 이벤트 경계의 명확한 종료를 신호한다. 이를 통해 클라이언트 애플리케이션이 부분적으로 업데이트된 주문장에 기초하여 자동화된 실행 로직을 섣불리 발동하는 것을 방지한다.

---

## 6. CME Clearing (청산·결제)

### 6.1 CCP 역할: 일 2,000만+ 거래 보증

CME Clearing은 중앙청산상대방(CCP)으로서 모든 거래의 매수자에 대해서는 매도자 역할을, 매도자에 대해서는 매수자 역할을 수행한다. 일일 **2,000만 건 이상**의 거래를 보증하며, 이는 단일 CCP로서 세계 최대 규모이다.

### 6.2 Trade Submission 윈도우 및 배치 스케줄

CME Clearing의 거래 제출 및 처리는 엄격한 시간표에 따라 운영된다.

| 시간 (CT) | 이벤트 |
|-----------|--------|
| 16:00 | 일일 정산가격 산출, Globex 유지보수 창 시작 |
| 16:01 | Globex 재개장 |
| 16:30 | GC2 신용한도 일일 리셋 |
| ~18:00 ET | 장마감 정산 처리 완료 |
| 19:00 ET | OTC 거래 제출 마감 |

### 6.3 Front-End Clearing (FEC)

Front-End Clearing은 청산 회사가 Globex 체결 전에 거래를 사전 승인할 수 있는 메커니즘이다. 이를 통해 청산 회사는 자사 고객의 거래가 청산소에 도달하기 전에 신용한도, 포지션 한도 등을 검증할 수 있다.

### 6.4 CME ClearPort (OTC): 도쿄 16:00, 런던 16:00 기준 호가

CME ClearPort는 장외(OTC) 파생상품의 청산 서비스를 제공하는 플랫폼이다. 글로벌 참가자를 위해 지역별 기준 시간을 설정한다:

| 지역 | 기준 시간 | 용도 |
|------|---------|------|
| 도쿄 | 16:00 JST | 아시아 OTC 거래의 일일 정산 기준 |
| 런던 | 16:00 GMT/BST | 유럽 OTC 거래의 일일 정산 기준 |
| 뉴욕 | 16:00 ET | 미국 OTC 거래의 일일 정산 기준 |

### 6.5 OTC 제출 마감: 19:00 ET

모든 OTC 거래의 당일 청산을 위한 최종 제출 마감은 **19:00 ET**(동부시간)이다. 이 마감 이후 제출된 거래는 다음 영업일 처리로 이월된다.

### 6.6 BAMS (Banking and Margin System): FIXML API, SFTP

BAMS는 CME Clearing의 뱅킹 및 증거금 관리 시스템으로, 담보 예치·인출의 완전 자동화를 실현한다.

**주요 뱅킹 타임라인:**

| 시간 (CT) | 뱅킹 및 담보 관리 작업 |
|-----------|---------------------|
| 08:30 | 외화(CAD, EUR, GBP, MXN) 당일 가치 결제 BAMS 입출금 요청 마감 |
| 10:30 | 외화(AUD, JPY, SEK, SGD) 익일 가치 결제 BAMS 요청 마감 |
| 11:00 | 일중 정산 처리 전 모든 담보 요청 마감 |
| 11:30~13:00 | 일중 정산 주기, 예상·최종 결제 의무 사항 확인 |
| 14:00 | 비현금 담보 입출금 요청 최종 마감 |
| 14:30 | USD 현금 입금 및 DTC 주식/ETF/회사채 인출 요청 마감 |

BAMS는 **FIXML 기반 API**와 **SFTP**를 통해 운영되며, 청산 회사가 프로그래밍 방식으로 담보를 관리할 수 있도록 한다.

---

## 7. 리스크 관리

### 7.1 Globex Credit Controls (GC2)

GC2 시스템은 청산 회사가 고객의 거래 활동에 대해 수학적으로 결정론적인 신용 한도를 실시간으로 설정할 수 있도록 하는 **체결 전(pre-execution) 리스크 관리 프레임워크**이다.

#### Executing Firm ID x Exchange Group 교차점 신용한도

리스크 관리자는 **실행 회사 ID(Executing Firm ID)**와 **거래소 그룹(Exchange Group)**의 정확한 교차점에서 한도를 설정한다.

| 통제 유형 | 설명 | 적용 방식 |
|----------|------|---------|
| **노출 한도 (Exposure Limits)** | 선물·옵션 전반의 매수·매도 포지션에 적용되는 통화 기반 한도 | Firm ID x Exchange Group |
| **최대 수량 한도 (Max Quantity)** | 단일 주문의 최대 허용 크기 절대 상한선 | 주문별 |
| **보수적 논리 (Conservative Logic)** | 노출·수량 한도 동시 활성 시, 더 엄격한 제약 적용 | 자동 |

#### 포지션 로직: 미체결+체결 연속 계산

포지션은 지속적으로 계산된다:

```
Total Futures Long = Σ(미결제 매수 수량) + Σ(체결 매수) - Σ(체결 매도)
```

이 계산은 실시간으로 이루어지며, 매칭엔진 내에서 각 주문의 제출·수정·취소·체결 시마다 갱신된다.

#### 16:30 CT 일일 리셋

끊임없는 포지션 누적을 방지하기 위해, 체결된 포지션은 매일 정확히 **16:30 CT**에 시스템적으로 '0'으로 재설정된다. 이는 일일 유지보수 창(16:00~16:01) 종료 후 약 30분 뒤에 수행되어, 청산 처리가 완료된 후 깨끗한 상태에서 새 거래일을 시작할 수 있게 한다.

### 7.2 Kill Switch (1초 이내 작동, GUI)

Kill Switch는 비상 상황에서 특정 참가자의 모든 미체결 주문을 **1초 이내**에 일괄 취소하는 기능이다.

| 특성 | 세부사항 |
|------|---------|
| 작동 시간 | 1초 이내 |
| 인터페이스 | GUI 기반 (CME 리스크 관리 포털) |
| 범위 | 특정 Firm ID 또는 세션 단위 |
| 복구 | 취소 후 즉시 새로운 주문 제출 가능 |

### 7.3 Self-Match Prevention (SMP)

SMP는 동일 참가자의 매수·매도 주문이 서로 체결되는 **자기 거래(wash trading)**를 방지하는 매칭엔진 내장 기능이다.

- **SMP ID**: 각 참가자에게 고유 SMP ID 부여
- **매칭 시점 검사**: 두 반대편 주문의 SMP ID가 동일할 경우, 매칭엔진이 자동으로 체결을 방지
- **처리 방식**: 기존 대기 주문(resting order)이 취소되거나, 공격적 주문(aggressor)이 취소됨 (설정에 따라 상이)

### 7.4 Dynamic Price Bands (롤링 참조가격 기반)

동적 가격 밴딩은 비정상적 가격 변동으로부터 시장을 보호하는 자동화된 서킷 브레이커 역할을 한다.

| 구성 요소 | 설명 |
|----------|------|
| **참조 가격** | 직전 체결가 또는 정산가로부터 동적 산출 |
| **밴드 폭** | 상품별로 설정된 변동 허용 범위 (틱 단위) |
| **롤링 업데이트** | 체결 발생 시마다 참조 가격이 갱신 |
| **위반 시 동작** | 밴드 초과 주문은 거부 또는 일시 보류 |

야간 저유동성 시간대에는 밴드 폭이 자동으로 축소되어, 플래시 크래시(flash crash) 리스크를 완화한다.

---

## 8. 인프라 및 재해복구

### 8.1 Blue-Green 배포 (Dual Zone Architecture)

23시간 이상의 연속 가동 시간을 제공하기 위해 CME Group은 **블루-그린 배포(Blue-Green Deployment)** 방법론을 채택한다.

| 환경 | 역할 | 상태 |
|------|------|------|
| **블루(Blue)** | 현재 운영 중인 프로덕션 환경 | 라이브 트래픽 처리 |
| **그린(Green)** | 업데이트가 적용된 대기 환경 | 모의 부하 테스트 완료 상태 |

블루-그린 전환 프로세스:
1. 그린 환경에 업데이트 배포 및 검증
2. 로드 밸런서 뒤에서 모의 부하 테스트 수행
3. 라이브 트래픽을 블루에서 그린으로 즉시 라우팅
4. 문제 발생 시 블루 환경으로 즉각 롤백

이를 통해 유지보수로 인한 다운타임을 **제로(Zero-downtime)**로 유지하며, 1분 유지보수 창 내에서 수천만 건의 주문 상태를 보존한 채 시스템 전환을 완료한다.

### 8.2 Aurora 데이터센터 (CyrusOne), 등거리 코로케이션

| 시설 | 위치 | 역할 | 운영사 |
|------|------|------|-------|
| **Aurora DC** | 일리노이주 오로라 | 기본 데이터센터, 매칭엔진 운영 | CyrusOne (매각 후) |
| **NYDC** | 뉴저지/뉴욕 | 백업 DR 시설 | CME Group |

Aurora 데이터센터의 코로케이션 서비스 핵심 특성:

- **등거리 케이블링**: 모든 코로케이션 참가자에게 동일 길이의 네트워크 케이블 제공. 물리적 거리 차이에 따른 레이턴시 불공정을 원천 제거
- **CME GLink**: CME 전용 네트워크로, Secaucus 및 Slough(런던) 접속 지점을 포함한 글로벌 연결 제공
- **크로스 커넥트**: 표준화된 크로스 커넥트 규격으로 참가자 장비와 CME 인프라 간 직접 연결

### 8.3 NYDC 백업 시설

NYDC는 Aurora 데이터센터의 완전한 백업 시설로, 재해 복구(DR) 시나리오에서 Aurora의 모든 기능을 대체할 수 있다. 지리적으로 분리된 위치에 배치되어 자연재해, 정전 등 지역적 재해에 대한 복원력을 제공한다.

### 8.4 DR 프로세스 4단계

CME Globex의 재해 복구 프로세스는 4가지 명시적 상태로 엄격하게 구조화되어 있다:

| 단계 | 상태명 | 설명 |
|------|-------|------|
| **1단계** | Pre-Event | 정상 운영 중 DR 준비 상태. 실시간 데이터 복제 진행 |
| **2단계** | Disaster Recovery | 기본 시설 장애 감지, DR 사이트로 페일오버 실행 |
| **3단계** | Recovery | DR 사이트에서 거래 서비스 재개. 참가자 재접속 |
| **4단계** | Post-Recovery | 기본 시설 복구 후 원래 사이트로 역전환 |

### 8.5 45분 스테이징 기간 (모든 참가자 재접속 시간)

DR 페일오버 실행 시, CME는 **45분의 스테이징 기간**을 제공한다. 이 기간 동안:

1. 모든 시장 참가자에게 DR 상태 전환을 API 및 GCC를 통해 통지
2. 참가자들이 DR 사이트의 IP 주소로 재접속 수행
3. 미체결 주문 상태 확인 및 필요 시 재제출
4. Pre-Open 상태에서 호가 수집 후 정상 거래 재개

### 8.6 Cancel-on-Disconnect (CoD) 의무화

CME Globex는 **Cancel-on-Disconnect(CoD)** 정책을 의무화한다. 참가자의 네트워크 연결이 끊어질 경우, 해당 참가자의 모든 미체결 주문이 자동으로 취소된다.

| CoD 특성 | 세부사항 |
|---------|---------|
| 적용 범위 | 모든 Globex 연결에 의무 적용 |
| 작동 조건 | 세션 하트비트 실패 감지 시 |
| 처리 대상 | 해당 세션의 모든 미체결 주문 |
| 목적 | 무인 주문(orphaned orders)에 의한 의도치 않은 체결 방지 |

이는 특히 24시간 운영 환경에서 야간 네트워크 장애로 인한 비의도적 포지션 누적을 방지하는 핵심 안전장치이다.

---

## 9. 글로벌 운영 모델

### 9.1 Global Command Center (GCC)

CME Group의 글로벌 커맨드 센터(GCC)는 Globex 플랫폼의 24시간 운영을 감독하는 중앙 통제 기관이다.

| GCC 기능 | 설명 |
|---------|------|
| 시장 감시 | 실시간 거래 활동 모니터링, 이상 거래 탐지 |
| 사고 대응 | 시스템 장애, 시장 혼란 등 비상 상황 대응 |
| 참가자 지원 | 접속 문제, 주문 오류 등 기술 지원 |
| DR 조율 | 재해 복구 절차 실행 및 참가자 커뮤니케이션 |
| 에스컬레이션 | 사고 심각도에 따른 단계적 대응 체계 |

### 9.2 Follow-the-Sun 교대 운영

GCC는 **Follow-the-Sun(FTS)** 모델에 기반한 교대 운영을 수행한다. 3개 주요 지역에 운영 센터를 배치하여 24시간 연속 인력 커버리지를 확보한다.

| 지역 | 커버리지 시간 (현지) | 주요 담당 시장 |
|------|-------------------|-------------|
| **미주 (Americas)** | 07:00~19:00 CT | 미국 정규장, 남미 |
| **EMEA** (유럽/중동/아프리카) | 07:00~19:00 GMT | 유럽, 중동, 아프리카 |
| **APAC** (아시아태평양) | 07:00~19:00 SGT/HKT | 아시아, 오세아니아 |

### 9.3 오버래핑 시프트를 통한 정보 핸드오버

FTS 모델의 핵심은 **교차 근무(overlapping shifts)**를 통한 원활한 정보 핸드오버이다.

- **인수인계 시간**: 각 지역 교대 시 1~2시간의 중복 근무 시간 설정
- **인수인계 항목**: 진행 중인 사고 대응, 사이버 보안 모니터링 현황, 복잡한 기술적 이상 현상
- **통합 보고 체계**: 모든 지역 팀이 통합된 운영 표준에 보고하며, 글로벌 사고 대응 및 DR 실행을 위한 확정적 에스컬레이션 포인트 역할 수행

---

## 10. Cross-Margining (교차증거금)

### 10.1 CME-DTCC/FICC 교차증거금

CME Group과 DTCC/FICC(Fixed Income Clearing Corporation) 간의 교차증거금 프로그램은 파생상품 시장과 현물 채권 시장 간의 증거금 효율성을 극대화하는 획기적 제도이다.

| 구분 | 세부사항 |
|------|---------|
| 참여 기관 | CME Clearing, DTCC/FICC |
| 대상 상품 | CME 금리선물 ↔ FICC 현물 국채 |
| 효과 | 상관관계가 높은 포지션 간 증거금 상계 |
| 확대 계획 | 2025년 12월, DTCC가 최종 고객까지 교차증거금 확대 신청 |

### 10.2 주가지수선물-현물 간 증거금 상계 가능성

교차증거금의 논리적 확장으로, 주가지수선물과 현물 주식 간의 증거금 상계가 이론적으로 가능하다. 예를 들어:

| 포지션 | 시장 | 증거금 (개별) | 교차증거금 후 |
|-------|------|-------------|------------|
| E-mini S&P 500 선물 매수 | CME | $12,000 | $7,200 |
| S&P 500 ETF (SPY) 매도 | NYSE | $15,000 | $9,000 |
| **합계** | | **$27,000** | **$16,200 (40% 절감)** |

*위 수치는 개념적 예시이며, 실제 상계 비율은 포지션 구성 및 시장 변동성에 따라 상이함.*

### 10.3 KRX KOSPI선물-현물 적용 시사점

KRX가 주식시장 거래시간을 연장할 경우, 교차증거금은 야간 유동성을 확보하기 위한 핵심 인센티브가 된다.

| 적용 시나리오 | KRX 대상 상품 | 기대 효과 |
|-------------|-------------|---------|
| **KOSPI200 선물 ↔ KOSPI200 ETF** | 선물시장 + 현물시장 | 증거금 30~40% 절감 예상 |
| **KOSPI200 옵션 ↔ 현물 바스켓** | 파생상품 + 현물 | 헤지 비용 감소, 야간 차익거래 활성화 |
| **개별주식선물 ↔ 현물** | ELW/선물 + 현물 | 시장조성자 참여 유인 강화 |

마진 콜이 야간 파생상품 노출과 분리되어 독립적으로 평가될 경우, 현물 주식 거래 시간의 연장은 필연적으로 청산 시스템 내에 막대한 양의 초과 담보를 묶이게 만든다. 교차증거금은 이 문제를 해결하는 가장 효과적인 수단이다.

---

## 11. KRX와의 비교 및 시사점

### 11.1 CME 모델에서 KRX가 벤치마킹해야 할 핵심 요소

| 비교 항목 | CME Group | KRX (현행) | KRX 벤치마킹 방향 |
|----------|----------|-----------|-----------------|
| **일일 유지보수** | 1분 (16:00~16:01 CT) | 수 시간 (야간 배치 처리) | 블루-그린 배포로 유지보수 창 최소화 |
| **주간 운영시간** | ~119시간 | ~32.5시간 (정규+시간외) | 단계적 확대 (12h → 18h → 23h) |
| **매칭엔진** | 세그먼트 파티셔닝, MSGW | 단일 매칭엔진 | 세그먼트별 독립 엔진 도입 |
| **프로토콜** | iLink 3 (FIXP+SBE) | FIX 기반 | 바이너리 프로토콜 전환 검토 |
| **리스크 관리** | GC2 실시간 신용통제 | 사전 증거금 시스템 | 실시간 포지션 계산 + Kill Switch |
| **DR** | 4단계 결정론적 프로토콜, 45분 스테이징 | 액티브-패시브 DR | 결정론적 DR + CoD 의무화 |
| **글로벌 운영** | FTS 3개 지역 GCC | 서울 단일 운영 | APAC/EMEA 운영센터 구축 |
| **교차증거금** | CME-DTCC/FICC | 미도입 | KOSPI 선물-현물 교차증거금 |

### 11.2 1분 유지보수 vs KRX의 야간 배치 의존

CME의 1분 유지보수 창은 다음 기술적 전제 조건에 기반한다:

1. **블루-그린 배포**: 병렬 환경에서 무중단 배포
2. **인크리멘탈 정산**: 배치 처리가 아닌 실시간/준실시간 정산
3. **상태 보존**: 유지보수 중에도 모든 미체결 주문 상태 보존
4. **시퀀스 무리셋**: 일일 유지보수에서는 시퀀스 리셋 미수행

KRX가 야간 배치 처리(T+2 결제, EOD 정산, 리스크 파라미터 갱신 등)에 의존하는 현 구조를 유지한다면, 24시간 연속 거래는 불가능하다. CME 모델을 참고하여 **실시간 정산 인프라**로의 전환이 선행되어야 한다.

### 11.3 교차증거금을 통한 야간 유동성 인센티브

야간 시간대 유동성 확보는 24시간 거래의 최대 과제이다. CME의 경험에서 도출된 핵심 교훈:

| 인센티브 | CME 사례 | KRX 적용 방안 |
|---------|---------|-------------|
| **증거금 절감** | CME-FICC 교차증거금으로 30~40% 절감 | KOSPI200 선물-현물 교차증거금 |
| **BTIC/TACO 유사 상품** | 현물 종가/개장가 연동 선물 주문 | 야간 KOSPI200 지수 연동 상품 개발 |
| **GC2 실시간 한도 관리** | 야간에도 동일한 신용통제 | 실시간 리스크 관리로 청산회사 참여 유도 |
| **CoD 의무화** | 네트워크 단절 시 자동 취소 | 무인 거래 리스크 관리 표준화 |

---

## 참고자료

1. CME GLOBEX REFERENCE GUIDE, 2월 19, 2026에 액세스, [cmegroup.com/globex/files/GlobexRefGd.pdf](https://www.cmegroup.com/globex/files/GlobexRefGd.pdf)
2. CME matching algorithms explained | Databento Blog, 2월 19, 2026에 액세스, [databento.com/blog/cme-matching-algorithms-...](https://databento.com/blog/cme-matching-algorithms-explained)
3. CME Globex Matching Algorithm Steps - Spaces - Confluence, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457218521)
4. CME Globex Market Segment - CME Group Client Systems Wiki, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457220437/iLink+Architecture)
5. Swap-Based Event Contracts and 24-7 Trading - CME Group Client Systems Wiki, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/988020743)
6. Order Qualifiers - CME Group Client Systems Wiki - Confluence, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Orde...](https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Order+Qualifiers)
7. Market Order with Protection - CME Group Client Systems Wiki, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Orde...](https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Order+Types+for+Futures+and+Options)
8. Basis Trade at Cash Open - CME Group Client Systems Wiki, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Basi...](https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Basis+Trade+at+Cash+Open)
9. Basis Trade at Index Close (BTIC) and BTIC+ - CME, 2월 19, 2026에 액세스, [cmegroup.com/trading/equity-index/btic-tra...](https://www.cmegroup.com/trading/equity-index/btic-transactions.html)
10. Trade at Cash Open (TACO) and TACO+ - CME, 2월 19, 2026에 액세스, [cmegroup.com/trading/equity-index/trade-at...](https://www.cmegroup.com/trading/equity-index/trade-at-cash-open.html)
11. Basis Trade at Index Close (BTIC) - CME, 2월 19, 2026에 액세스, [cmegroup.com/trading/equity-index/files/bt...](https://www.cmegroup.com/trading/equity-index/files/btic-block-trades-apac.pdf)
12. FAQ: BTIC+ and TACO+ - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/trading/equity-index/faq-btic...](https://www.cmegroup.com/trading/equity-index/faq-btic-and-taco.html)
13. CME Globex Notices: March 2, 2020, 2월 19, 2026에 액세스, [cmegroup.com/notices/electronic-trading/20...](https://www.cmegroup.com/notices/electronic-trading/2020/03/20200305.html)
14. CME Group Client Systems Wiki - Confluence (CME Clearing Services), 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457215607/CME+Clearing+Services)
15. Clearing - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/solutions/clearing.html](https://www.cmegroup.com/solutions/clearing.html)
16. Transaction Timelines - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/solutions/clearing/operations...](https://www.cmegroup.com/solutions/clearing/operations-and-deliveries/transaction-timelines.html)
17. CME Clearing: Principles for Financial Market Infrastructures Disclosure, 2월 19, 2026에 액세스, [cmegroup.com/clearing/risk-management/file...](https://www.cmegroup.com/clearing/risk-management/files/cme-clearing-principles-for-financial-market-infrastructures-disclosure.pdf)
18. CME Clearing Collateral API Specifications CSV Format, 2월 19, 2026에 액세스, [cmegroup.com/clearing/financial-and-collat...](https://www.cmegroup.com/clearing/financial-and-collateral-management/files/cme-collateral-api-csv.pdf)
19. CME Clearing's Collateral API via FIXML, 2월 19, 2026에 액세스, [cmegroup.com/clearing/risk-management/file...](https://www.cmegroup.com/clearing/risk-management/files/cme-collateral-api-fixml.pdf)
20. Matching Algorithms - CME Group Client Systems Wiki - Confluence, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457218479)
21. Blue-Green Deployments: A Definition and Introductory Guide - LaunchDarkly, 2월 19, 2026에 액세스, [launchdarkly.com/blog/blue-green-deployments-a...](https://launchdarkly.com/blog/blue-green-deployments-a-definition-and-introductory/)
22. Blue-green deployments: Zero-downtime deployments - Liquibase, 2월 19, 2026에 액세스, [liquibase.com/blog/blue-green-deployments-l...](https://www.liquibase.com/blog/blue-green-deployments-liquibase)
23. 20200330a - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/notices/electronic-trading/20...](https://www.cmegroup.com/notices/electronic-trading/2020/03/20200330a.html)
24. Session Layer Management Tests - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/tools-information/webhelp/acp...](https://www.cmegroup.com/tools-information/webhelp/acp-cgw-fo/Content/session-layer.html)
25. CME Globex - iLink 3 for CGW Session Guidelines, 2월 19, 2026에 액세스, [cmegroup.com/globex/files/ilink-3-cgw-sess...](https://www.cmegroup.com/globex/files/ilink-3-cgw-session-guidelines.pdf)
26. White Paper: CME MDP 3.0 - B2BITS, 2월 19, 2026에 액세스, [b2bits.com/product_support/e-library/whi...](https://www.b2bits.com/product_support/e-library/white-paper-cme-mdp-30)
27. Data Directly from the Market Data Platform - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/market-data/distributor/marke...](https://www.cmegroup.com/market-data/distributor/market-data-platform.html)
28. CME's Aurora Co-Lo: Quick Facts - A-Team Insight, 2월 19, 2026에 액세스, [a-teaminsight.com/blog/cmes-aurora-co-lo-quick-...](https://a-teaminsight.com/blog/cmes-aurora-co-lo-quick-facts/?brand=tti)
29. CME Group Announces Agreement to Sell Aurora, Ill. Data Center to CyrusOne, 2월 19, 2026에 액세스, [investor.cmegroup.com/news-releases/news-release-de...](https://investor.cmegroup.com/news-releases/news-release-details/cme-group-announces-agreement-sell-aurora-ill-data-center)
30. CME Co-Location Services, 2월 19, 2026에 액세스, [cmegroup.com/globex/files/CME-Co-Location-...](https://www.cmegroup.com/globex/files/CME-Co-Location-Services-Overview.pdf)
31. Co-Location and Data Center Services - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/solutions/co-location.html](https://www.cmegroup.com/solutions/co-location.html)
32. FEE SCHEDULE TO DATA CENTER CONNECTION AGREEMENT, 2월 19, 2026에 액세스, [cmegroup.com/globex/files/cme-globex-datac...](https://www.cmegroup.com/globex/files/cme-globex-datacenterfeeschedule.pdf)
33. CME GLink - CME Group Client Systems Wiki - Confluence, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457415665/CME+GLink)
34. GLink Cross Connect Specifications for Secaucus and Slough - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/globex/files/ebs/ebs-glink-cr...](https://www.cmegroup.com/globex/files/ebs/ebs-glink-cross-connect.pdf)
35. CME Globex Credit Controls (GC2), 2월 19, 2026에 액세스, [cmegroup.com/tools-information/webhelp/glo...](https://www.cmegroup.com/tools-information/webhelp/globex-credit-controls/Content/CME-Globex-Credit-Controls-Management.html)
36. CME Globex Credit Controls - CME Group Client Systems Wiki, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457219125/CME+Globex+Credit+Controls)
37. FAQ: Globex Self-Match Prevention Functionality - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/solutions/market-access/globe...](https://www.cmegroup.com/solutions/market-access/globex/trade-on-globex/faq-self-match.html)
38. CME Globex Reference Sheet - CME Group Client Systems Wiki, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457086986/GCC+Product+Resources)
39. About the Global Command Center (GCC) - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/solutions/market-access/globe...](https://www.cmegroup.com/solutions/market-access/globex/trade-on-globex/about-the-global-command-center.html)
40. Follow the sun trading: More trades, processing and reporting - FOW, 2월 19, 2026에 액세스, [fow.com/insights/follow-the-sun-tradi...](https://www.fow.com/insights/follow-the-sun-trading-more-trades-processing-and-reporting)
41. Strategies to take your customer support global - Intercom, 2월 19, 2026에 액세스, [intercom.com/blog/global-customer-support/](https://www.intercom.com/blog/global-customer-support/)
42. Staff Security Engineer - Operations - CME Group - Dice.com, 2월 19, 2026에 액세스, [dice.com/job-detail/eaca6dcf-8a09-44b1...](https://www.dice.com/job-detail/eaca6dcf-8a09-44b1-b688-0ec8e292d504?q=NICE)
43. API Development Requirements and Assistance - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/solutions/market-access/globe...](https://www.cmegroup.com/solutions/market-access/globex/develop-to-globex/api-development-requirements-and-assistance.html)
44. CME Globex Disaster Recovery Process - CME Group Client Systems Wiki, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457412471/CME+Globex+Disaster+Recovery+Process)
45. CME Customer Center Services Guide, 2월 19, 2026에 액세스, [cmegroup.com/education/files/cme-customer-...](https://www.cmegroup.com/education/files/cme-customer-center-services-guide.pdf)
46. DTCC Files to Expand CME Group Cross-Margining Arrangement to End User Clients, 2월 19, 2026에 액세스, [dtcc.com/news/2025/december/15/dtcc-fi...](https://www.dtcc.com/news/2025/december/15/dtcc-files-to-expand-cme-group-cross-margining-arrangement)
47. CME-FICC Cross Margining for Customers - Clearing Member Firms, 2월 19, 2026에 액세스, [cmegroup.com/markets/interest-rates/files/...](https://www.cmegroup.com/markets/interest-rates/files/cme-ficc-cross-margining-for-indirect-users.pdf)
48. Fixed-income cross-margin opportunities: A driver of change - CME, 2월 19, 2026에 액세스, [cmegroup.com/articles/files/2025/fixed-inc...](https://www.cmegroup.com/articles/files/2025/fixed-income-cross-margin-opportunities-driver-change.pdf)
49. CME Globex Disaster Recovery - CME Group Client Systems Wiki, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457412050/CME+Globex+Disaster+Recovery)
50. 101 Overview: Settlement - CME Group, 2월 19, 2026에 액세스, [cmegroup.com/articles/brochures-and-handbo...](https://www.cmegroup.com/articles/brochures-and-handbooks/101-overview-settlement.html)
51. 3 Best Practices For Zero-Downtime Database Migrations - LaunchDarkly, 2월 19, 2026에 액세스, [launchdarkly.com/blog/3-best-practices-for-zer...](https://launchdarkly.com/blog/3-best-practices-for-zero-downtime-database-migrations/)
52. iLink - CME Group Client Systems Wiki - Confluence, 2월 19, 2026에 액세스, [cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages...](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/714145834)
53. Business Continuity Management at CME Group, 2월 19, 2026에 액세스, [cmegroup.com/globex/files/business-continu...](https://www.cmegroup.com/globex/files/business-continuity-management-cme-group.pdf)
