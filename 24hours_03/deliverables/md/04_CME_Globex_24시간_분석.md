# CME Globex 24시간 거래 인프라 분석

> 작성일: 2026년 3월 27일 | 프로젝트: KRX 24시간 거래 도입 전략

## 목차

- [1. Executive Summary (요약)](#1-executive-summary-요약)
- [2. 시장 세션 라이프사이클](#2-시장-세션-라이프사이클)
  - [2.1 거래 세션 구조](#21-거래-세션-구조)
  - [2.2 주간 유지보수 일정](#22-주간-유지보수-일정)
  - [2.3 60초 일일 리셋](#23-60초-일일-리셋)
- [3. 주문 유형 및 미니 옥션 메커니즘](#3-주문-유형-및-미니-옥션-메커니즘)
  - [3.1 표준 주문 유형](#31-표준-주문-유형)
  - [3.2 BTIC/TACO 메커니즘](#32-btictaco-메커니즘)
  - [3.3 옥션 및 가격 발견](#33-옥션-및-가격-발견)
- [4. 시스템 아키텍처](#4-시스템-아키텍처)
  - [4.1 MSGW (Market Segment Gateway)](#41-msgw-market-segment-gateway)
  - [4.2 SBE (Simple Binary Encoding) 프로토콜](#42-sbe-simple-binary-encoding-프로토콜)
  - [4.3 매칭엔진 성능](#43-매칭엔진-성능)
  - [4.4 이중화 및 장애 복구](#44-이중화-및-장애-복구)
- [5. GC2 신용통제 프레임워크](#5-gc2-신용통제-프레임워크)
  - [5.1 실시간 신용 관리](#51-실시간-신용-관리)
  - [5.2 24시간 리스크 모니터링](#52-24시간-리스크-모니터링)
- [6. 청산결제 및 포스트-트레이드](#6-청산결제-및-포스트-트레이드)
  - [6.1 CME Clearing 구조](#61-cme-clearing-구조)
  - [6.2 담보 관리 및 뱅킹 타임라인](#62-담보-관리-및-뱅킹-타임라인)
  - [6.3 결제 사이클](#63-결제-사이클)
- [7. Follow-the-Sun 운영 모델](#7-follow-the-sun-운영-모델)
  - [7.1 글로벌 운영 센터](#71-글로벌-운영-센터)
  - [7.2 인력 운영 전략](#72-인력-운영-전략)
  - [7.3 KRX 인력 운영 시사점](#73-krx-인력-운영-시사점)
- [8. KRX 시사점 및 도입 권고](#8-krx-시사점-및-도입-권고)
  - [8.1 기술적 시사점](#81-기술적-시사점)
  - [8.2 운영적 시사점](#82-운영적-시사점)
  - [8.3 파생상품 시장 연계](#83-파생상품-시장-연계)
  - [8.4 핵심 Gap 분석](#84-핵심-gap-분석)
- [9. CME Globex 일일 라이프사이클 다이어그램](#9-cme-globex-일일-라이프사이클-다이어그램)
- [참고문헌](#참고문헌)

---

## 1. Executive Summary (요약)

CME Group은 CME Globex 전자 거래 플랫폼을 통해 전 세계에서 가장 성숙하고 검증된 24시간 연속 거래 모델을 운영하고 있다. 일요일 오후 5시(CT)부터 금요일 오후 4시(CT)까지 주 5일간 거의 24시간 연속으로 작동하며, 매일 수천만 건의 거래를 금리, 주가지수, 외환, 에너지, 농산물 등 극도로 다양한 자산군에 걸쳐 처리한다. 이 플랫폼의 일일 유지보수 중단은 단 60초(오후 4:00~4:01 CT)에 불과하며, 이 미세한 시간 동안 거래일 이월(Trade Date Roll), 시퀀스 상태 체크포인트, 로그 전환 등 핵심 시스템 작업을 완료한다. CME Globex는 비동기식 처리 아키텍처, 결정론적 매칭 알고리즘, 마이크로초 수준의 체결 전 신용 통제(GC2) 시스템이라는 세 가지 기술적 축을 통해 이러한 연속 가용성을 달성한다.

KRX가 2026년 9월 14일 12시간 거래 시행(연기 확정)과 2027년 12월 24시간 거래 달성을 목표로 하는 상황에서, CME Globex는 연속 거래가 운영적으로 실현 가능하다는 가장 강력한 실증적 검증 사례를 제공한다. 그러나 CME의 사례는 동시에, 24시간 거래가 단순한 운영 시간 연장이 아니라 근본적으로 다른 인프라 패러다임을 요구한다는 점을 명확히 보여준다. 17개의 분리된 마켓 세그먼트로 수평 분할된 매칭엔진 아키텍처, FIXP/SBE 기반의 초저지연 바이너리 프로토콜, 듀얼 존(Dual Zone) 무중단 배포 전략, 그리고 시카고-런던-싱가포르를 잇는 "Follow-the-Sun" 운영 인력 모델은 모두 KRX의 EXTURE 3.0(50us latency, 일 9.4억 건 처리) 기반 24시간 전환 설계에 직접적인 기술적, 운영적 참조 프레임워크를 구성한다.

---

## 2. 시장 세션 라이프사이클

### 2.1 거래 세션 구조

CME Globex 전자 거래 플랫폼은 일요일 오후 5시(CT)에 개장하여 금요일 오후 4시(CT)에 마감하는 형태로 주 5일간 거의 24시간 연속 운영된다. 이 과정에서 플랫폼은 글로벌 참여를 촉진하는 동시에 핵심 시스템 운영, 시퀀스 리셋(sequence resets) 및 거래일 이월(Trade Date Rolling)을 위한 마이크로 윈도우(micro-windows)를 허용하는 고도로 구조화된 일일 및 주간 수명주기를 활용한다.

상품 그룹별로 정확한 거래 시간은 다소 상이하나, 대부분의 주요 선물 상품(E-mini S&P 500, Eurodollar, WTI Crude Oil 등)은 아래의 표준 세션 구조를 따른다.

| 세션 구분 | 시간 (CT) | 상태 | 비고 |
|---|---|---|---|
| **주간 개장** | 일요일 17:00 | Open | 주간 거래 시작 |
| **연속 거래** | 일~금 17:00-16:00 | Active Trading | 23시간 연속 |
| **일일 유지보수** | 월~목 16:00-16:01 | Close/Open | 60초 중단 |
| **주간 마감** | 금요일 16:00 | Close | 주간 거래 종료 |
| **주말 휴장** | 금 16:00 ~ 일 17:00 | Closed | 시스템 유지보수 |

특히 일부 상품(Swap 기반 이벤트 계약 등)은 24/7 거래를 지원하여 주말 및 공휴일에도 연속 거래가 가능하다. 이러한 24/7 상품군의 경우 전통적인 주중/주말 구분 없이 연속적인 유동성 접근을 제공하며, CME Globex의 아키텍처적 유연성을 극명히 보여준다.

### 2.2 주간 유지보수 일정

CME Globex는 보다 광범위한 시스템 업그레이드, 시퀀스 리셋 및 연장된 데이터베이스 유지보수를 위해 연속 거래 상품에 맞춘 두 가지 주요 연장 유지보수 창(Extended Maintenance Window)을 운영한다. 이 시간 동안 매칭엔진은 질서 있는 시장 재개를 보장하기 위해 뚜렷한 운영 상태로 전환된다.

| 유지보수 창 | 운영 시간 (CT) | Pre-Open/Open 상태 (CT) | 시퀀스 리셋 |
|---|---|---|---|
| **화요일 연장** | 02:00 a.m. ~ 03:45 a.m. | Pre-Open 03:45 ~ Open 04:00 | 아니요 |
| **토요일 연장** | 02:00 a.m. ~ 03:45 a.m. | Pre-Open 03:45 ~ Open 04:00 | **예** |
| **월~금 일일** | 04:00 p.m. ~ 04:01 p.m. | Open 상태만 - 04:01 p.m. | 아니요 |

**화요일 연장 유지보수(02:00~03:45 CT):** 약 1시간 45분 동안 시장이 정지되며, 이 기간에 소프트웨어 패치, 구성 변경(configuration changes), 펌웨어 업데이트 등이 수행된다. 화요일 유지보수는 FIX 시퀀스 번호의 하드 리셋을 수반하지 않으므로, 클라이언트 시스템은 짧은 중단 시간 동안 세션 영속성과 연속 시퀀스 로직을 유지해야 한다.

**토요일 연장 유지보수(02:00~03:45 CT):** 화요일과 동일한 시간대에 수행되지만, 결정적으로 FIX 시퀀스 번호의 하드 리셋(hard reset)이 수반된다. 이는 주간 단위의 시퀀스 번호 누적을 초기화하여 오버플로우를 방지하고, 클라이언트 시스템이 새로운 시퀀스 기준점에서 재동기화할 수 있도록 한다.

두 유지보수 창 모두에서 시장은 CT 기준 오전 3:45부터 4:00까지 15분간 **"Pre-Open(개장 전)"** 상태로 전환된다. 이 Pre-Open 상태는 일시 정지 후 복구되는 연속 시장에서 핵심적인 미시구조 메커니즘으로, 시장 참여자들은 주문을 입력, 수정, 취소할 수 있으며, 중앙 지정가 주문장(CLOB)이 실제 체결 없이 유동성을 모으고 예상 개장가(indicative opening prices)를 계산한다. 이를 통해 정지된 시장이 즉시 연속 매칭으로 전환될 경우 발생할 수 있는 극심한 변동성과 가격 괴리를 방지한다.

### 2.3 60초 일일 리셋

CME Globex의 가장 주목할 만한 운영 특성은 일일 유지보수 중단이 정확히 **60초**(오후 4:00~4:01 CT)에 불과하다는 점이다. 이 1분간의 중단은 장시간의 휴장 없이 논리적인 '하루'를 마감하고 다음 날을 준비하기 위한 고도로 최적화된 프로세스이다.

**60초 동안 수행되는 핵심 작업:**

1. **거래일 이월(Trade Date Roll):** 현재 거래일(Trade Date)을 다음 영업일(Business Date)로 전환한다. 오후 4:00 정각에 시장이 일시 정지(Close)되면, CME Globex는 MDP 3.0 시장 데이터 플랫폼을 통해 Security Status 메시지(tag 35=f)를 전송하여 글로벌 클라이언트 시스템에 거래일 이월 및 시장 상태 변경을 브로드캐스트한다.
2. **시퀀스 상태 체크포인트:** 일일 시퀀스 번호의 논리적 분리점을 설정하여 거래일 간 감사 추적(audit trail)을 명확히 한다. 단, 일일 리셋에서는 시퀀스 번호의 하드 리셋은 수행하지 않는다(토요일 유지보수에서만 수행).
3. **포지션 집계 초기화:** GC2 프레임워크의 체결된 포지션(filled positions)은 매일 오후 4:30 CT에 시스템적으로 '0'으로 재설정되어, 끊임없는 포지션 누적을 방지한다.
4. **로그 전환(Log Rotation):** 시스템 로그 파일의 논리적 분리 및 아카이빙을 수행한다.

**60초 후 즉시 재개:** 오후 4:01이 되면 시장은 별도의 유동성 집중을 위한 경매 시간인 'Pre-Open' 상태를 거치지 않고, 연속 거래가 가능한 'Open' 상태로 **즉시 전환**된다. 이는 연장 유지보수 창(화/토)의 15분 Pre-Open 과정과 대조적이며, 1분이라는 극히 짧은 중단이 시장에 미치는 영향을 최소화하기 위한 설계적 선택이다.

**KRX와의 비교:** CME의 60초 리셋이 가능한 것은 파생상품 시장의 구조적 특성에 기인한다. 파생상품은 기초자산의 실시간 가격을 참조하므로 독립적인 가격 발견 경매가 불필요하며, 증거금 기반 거래 구조는 결제 실패 리스크가 현물 주식 대비 낮다. 현물 주식 거래소인 KRX의 경우 -- NBBO 재계산, SIP 동기화, 청산결제 배치 처리 등 추가적인 시스템 작업이 필요하므로 -- 60초가 아닌 보다 긴 유지보수 창이 불가피하며, 이는 NYSE Arca(2시간)나 24X(1시간)의 설계 선택과 일치한다.

---

## 3. 주문 유형 및 미니 옥션 메커니즘

### 3.1 표준 주문 유형

CME Globex는 24시간 연속 거래 환경에서 변동성이 큰 기간 동안 참가자를 보호하도록 설계된 다양한 주문 유형 분류 체계를 지원한다.

| 주문 유형 | 설명 | 시장 상태 제한 |
|---|---|---|
| **지정가 주문 (Limit Order)** | 지정 가격 이내에서만 체결. 잔량은 주문장에 잔류 | Open, Pre-Open |
| **시장-지정가 주문 (Market-Limit Order)** | 시장가로 즉시 체결 후, 미체결 잔량은 최종 체결가의 지정가 주문으로 전환 | Open만 |
| **보호 시장 주문 (Market Order with Protection)** | 현재 최우선 호가에서 사전 정의된 보호 범위(protection range) 내에서만 체결. 범위 밖의 가격 슬리피지를 구조적으로 차단 | Open만 |
| **스톱 주문 (Stop Order)** | 트리거 가격 도달 시 시장 주문으로 전환 | Open만 |
| **스톱-지정가 주문 (Stop-Limit Order)** | 트리거 가격 도달 시 지정가 주문으로 전환 | Open만 |

**FAK (Fill-and-Kill):** 대기 유동성에 대해 즉시 체결되도록 설계되며, 체결되지 않은 잔여 물량은 매칭엔진에 의해 즉각적이고 자동으로 취소된다. 참가자는 FAK 주문에 대해 최소 체결 수량(minimum execution quantity)을 지정할 수 있으며, 주문 도달 시 이 최소 수량을 충족할 수 없으면 전체 주문이 거부된다.

**FOK (Fill-or-Kill):** 전체 주문 수량의 즉각적이고 절대적인 체결을 요구한다. 기술적으로 CME Globex에서 FOK는 최소 체결 수량 매개변수를 전체 주문 수량과 정확히 동일하게 설정한 FAK 주문을 제출함으로써 구현된다. iLink 3 프로토콜에서는 tag 59-TimeInForce=3과 tag 110-MinQty를 tag 38-OrderQty 값과 동일하게 설정하는 FIX 태그 조합으로 제출된다.

**시장 상태별 제한:** FAK 및 FOK 주문은 모두 "Open(개장)" 시장 상태에서만 독점적으로 허용된다. 참가자가 "Pre-Open" 상태나 정지 상태 중에 이러한 공격적인 조건(aggressive qualifier)을 제출하면, 매칭엔진은 예상 시초가 계산의 무결성을 보존하기 위해 시스템적으로 이를 거부한다.

**주문 영속성:** GTC(Good-Till-Cancelled) 및 GTD(Good-Till-Date) 주문에 대해서는 타임스탬프 우선순위가 세션 경계를 넘어 엄격하게 유지된다. 오후 4:00 CT에 시장이 잠시 정지했다가 오후 4:01 CT에 재개될 때, 이 1분간의 중단 중에도 영속적 주문들은 취소되지 않으며 대기열 내의 타임스탬프 우선순위를 정확하게 보존한다. 반면 DAY 주문은 우선순위 변경 이벤트(수량 증가, 가격 변경, 계좌 번호 수정) 발생 시 즉시 대기열 맨 뒤로 이동한다.

### 3.2 BTIC/TACO 메커니즘

24시간 연속 거래 환경에서는 전통적인 시가 지정가 주문(LOO), 종가 지정가 주문(LOC)의 효용성에 근본적인 도전이 제기된다. 물리적인 개장/폐장 벨이 없는 24시간 시장에서 현물 개장 및 종가 노출(exposure)은 CME 고유의 특화된 파생상품 메커니즘을 통해 관리된다.

**BTIC (Basis Trade at Index Close):** 시장 참가자가 기초 현물 지수의 공식 종가를 기준으로 베이시스(basis) 거래를 체결할 수 있는 메커니즘이다. 참가자들은 선물 가격을 직접 거래하는 대신, 미래의 현물 종가에 대한 개별 지수 포인트 스프레드(베이시스)를 협상한다. 기초 현물 주식 시장이 공식적으로 마감되고 지수 수준이 발표되면, 선물 거래는 종가 지수 수준에 합의된 베이시스를 더한 가격으로 청산된다.

**TACO (Trade at Cash Open):** BTIC와 동일한 원리로 기능하되, 현물 시장의 시초가 경매에 대한 확실성을 제공한다. 주식 시장이 물리적으로 개장하기 한참 전에 해당 날짜의 공식 현물 지수 시가를 기준으로 베이시스 거래를 할 수 있게 한다.

**BTIC+/TACO+:** 실제 선물 계약으로 구조화되어 T-plus(T+) 거래를 도입한 변형이다. 참가자들이 수일 전에 시가 또는 종가의 확실성을 확보할 수 있도록 하여 시간적 유연성을 크게 확장한다.

**KRX 파생상품 시장에 대한 시사점:** BTIC/TACO와 유사한 베이시스 거래 메커니즘을 도입하는 것은 24시간 야간 세션과 주요 일일 유동성 이벤트 간의 가격 차이를 해소하는 데 필수적이다. KRX의 KOSPI 200 선물 야간 거래(18:00~05:00 KST)는 이미 이러한 가격 연계 기능의 기초를 제공하고 있으며, 현물 시장의 24시간 확장 시 파생상품과의 가격 연계 메커니즘을 보다 정교화할 필요가 있다.

### 3.3 옥션 및 가격 발견

CME Globex는 전통적인 벨 기반(bell-based)의 개장/폐장 체계 없이 세션 전환 시 가격 발견을 관리하기 위해 구조화된 옥션 로직을 활용한다.

**Pre-Open 옥션 로직:** 연장 유지보수(화/토) 후 시장 재개 시, 15분간의 Pre-Open 상태에서 주문 입력, 수정, 취소가 허용되지만 실제 체결은 발생하지 않는다. 이 기간에 중앙 지정가 주문장(CLOB)은 유동성을 집중시키고 예상 개장가(indicative opening prices)를 연속적으로 계산하여 시장 참여자에게 가격 신호를 제공한다. Pre-Open이 종료되고 시장이 Open 상태로 전환되면, 축적된 주문장에 대해 단일가 매칭(opening auction)이 실행되어 균형 가격에서 최대 체결량을 달성한다.

**일일 리셋 후 직접 Open:** 반면 일일 60초 리셋(16:00~16:01 CT) 후에는 Pre-Open 없이 연속 거래 상태로 즉시 전환된다. 이는 1분이라는 극히 짧은 중단이 주문장의 구조적 무결성을 충분히 유지할 수 있고, GTC/GTD 주문의 영속적 타임스탬프 우선순위가 보존되므로 별도의 유동성 집중 과정이 불필요하다는 판단에 기인한다.

**매칭 알고리즘 다양성:** CME Globex는 개별 상품의 유동성 프로필에 맞춘 정교한 매칭 알고리즘 매트릭스를 활용한다. 여기에는 엄격한 선입선출(FIFO), 비례 배분(Pro-Rata), 주도 시장 조성자(LMM, Lead Market Maker) 우선순위, 최우선 주문(TOP) 우선순위를 포함하는 복잡한 변형들이 포함된다. 이러한 알고리즘적 다양성은 각 상품의 유동성 특성에 최적화된 가격 발견 메커니즘을 제공한다.

---

## 4. 시스템 아키텍처

### 4.1 MSGW (Market Segment Gateway)

CME Globex 매칭엔진은 단일한 모놀리식(monolithic) 엔티티로 작동하지 않는다. 아키텍처는 **"마켓 세그먼트(Market Segments)"**로 알려진 개별 거래 엔진 인스턴스로 수평적으로 분할(partitioning)되어 있으며, 현재 **17개의 분리된 마켓 세그먼트**로 구성되어 있다. 각 자산군을 격리하여 한 시장에서 거래량이 급증하더라도 다른 시장의 매칭엔진 성능에 영향을 주지 않도록 시스템을 격리한다.

CME는 참가자 주문을 이러한 세그먼트로 라우팅하기 위한 두 가지 구조적 모델을 제공한다:

**Convenience Gateway (CGW):**
- 중앙 집중식 라우팅 허브 역할
- 참가자는 단일 TCP 연결을 통해 접속
- CGW가 모든 하위 마켓 세그먼트에 대한 주문 입력 메시지의 라우팅을 투명하게 관리
- iLink Session ID는 단일하고 통합된 시퀀스 스트림을 활용하며 오직 하나의 CGW에만 존재
- 구축 및 운영이 단순하나 라우팅 홉(hop)으로 인한 추가 지연 시간 발생

**Market Segment Gateway (MSGW):**
- 초저지연(ultra-low latency) 참가자와 구조적 결정론을 위해 설계
- 참가자가 전용 마켓 세그먼트에 직접 연결
- 단일 세션 ID, 비밀번호, 포트를 사용하되 특정 마켓 세그먼트의 기본 및 백업 게이트웨이에 해당하는 **최대 17개의 고유 IP 주소**에 각각 연결
- 시퀀스 스트림은 MarketSegmentID와 Session ID의 정확한 조합에 따라 고유
- 여러 세그먼트에 로그인한 고객은 메시지 시퀀스 번호(tag 34-MsgSeqNum)가 완전히 동일한 다수의 체결 보고서를 동시에 수신 가능

MSGW는 엄격하게 정의된 **1,420바이트의 최대 전송 단위(MTU)**로 제한되는 엄격한 선입선출(FIFO) 메시지 처리 모델을 강제한다. 게이트웨이는 들어오는 데이터를 패킷 수준에서 평가하며, 불완전한 FIX 메시지가 포함된 패킷은 후속 패킷 도착까지 FIFO 대기열 밖에 보류한다. 후속 패킷의 데이터가 보류 중인 부분 메시지를 완성하지 못할 경우, 게이트웨이는 tag 10의 잘못된 체크섬(CheckSum)을 식별한 후 핵심 엔진의 무결성을 보호하기 위해 데이터를 폐기한다.

### 4.2 SBE (Simple Binary Encoding) 프로토콜

CME는 전통적인 ASCII 기반 FIX 프로토콜 사용을 중단하고, 글로벌 24시간 시장의 거대한 대역폭과 지연 시간 요구 사항을 충족하기 위해 고도로 최적화된 바이너리 프레임워크를 도입했다.

**iLink 3 (주문 입력 프로토콜):**
- 세션 계층: FIXP (FIX Performance) 프로토콜 -- 기존 ASCII FIX에 내재된 장황한 헤더 및 트레일러 오버헤드를 제거하는 매우 가벼운 포인트-투-포인트 세션 프로토콜
- 애플리케이션 계층: SBE (Simple Binary Encoding) -- 고정 길이 필드, 고정 위치, 기본 리틀 엔디안(little-endian) 바이트 순서를 활용
- SBE의 핵심 장점: 클라이언트 거래 시스템이 복잡하고 순차적인 상태 기반 파싱 없이 수신 네트워크 데이터를 애플리케이션 메모리 버퍼에 **직접 매핑(zero-copy deserialization)** 가능
- 세션 영속성: 물리적 TCP 연결이 단절되더라도 UUID(범용 고유 식별자) 기반으로 논리적 세션 상태를 유지하여, 재연결 시 끊어진 시점 이후의 시퀀스 번호만 동기화하여 즉각 거래 재개

**MDP 3.0 (시장 데이터 프로토콜):**
- 이중 피드(dual-feed) UDP 멀티캐스트 아키텍처 활용
- 극단적 변동성 기간에 네트워크 대역폭을 효율적으로 관리하기 위해 네트워크 패킷, FIX 메시지, 매칭 이벤트라는 개념을 분리
- 단일 매칭 이벤트가 여러 순차적 UDP 패킷에 걸칠 수 있고, 반대로 단일 UDP 패킷에 여러 고유 매칭 이벤트가 포함될 수 있음
- tag 5799-MatchEventIndicator를 통해 매칭 이벤트 경계의 명확한 끝을 신호하여, 부분적으로 업데이트된 주문장에 기초한 자동화 실행 로직의 오발동을 방지

**바이너리 프로토콜의 HFT 이점:** SBE/FIXP 기반의 바이너리 인코딩은 ASCII FIX 대비 메시지 크기를 대폭 축소하고 파싱 오버헤드를 거의 제거함으로써, 고빈도 거래(HFT) 참가자에게 결정론적이고 예측 가능한 초저지연 환경을 제공한다.

### 4.3 매칭엔진 성능

CME Globex 매칭엔진은 24시간 연속 운영 환경에서 결정론적 지연 시간(deterministic latency)을 유지하기 위해 다음과 같은 성능 특성을 갖추고 있다:

**처리량 및 지연 시간:**
- 일일 수천만 건의 거래 처리 능력
- 마이크로초(microsecond) 수준의 결정론적 지연 시간
- 17개 마켓 세그먼트의 수평 분할을 통한 부하 격리

**24시간 성능 일관성 보장 메커니즘:**
- **마켓 세그먼트 격리:** 한 자산군의 거래량 급증이 다른 자산군에 영향을 주지 않는 물리적 격리
- **등거리 코로케이션:** 모든 교차 연결 케이블이 정확히 동일한 광학적 길이로 엔지니어링되어 물리적 근접성만으로 마이크로초의 지연 시간 이점을 얻을 수 없음
- **듀얼 존 아키텍처:** 활성 존에서 라이브 거래를 처리하는 동안 대체 존에서 백그라운드 업그레이드를 수행하여 성능 저하 없이 시스템 전환
- **FIFO 패킷 처리:** MSGW의 엄격한 FIFO 메시지 처리 모델을 통한 순서 보장

**KRX EXTURE 3.0과의 비교:** KRX의 EXTURE 3.0은 50 마이크로초(50us) 지연 시간과 일 9.4억 건 처리 성능을 보유하고 있어, CME Globex의 파생상품 매칭엔진에 필적하는 현물 주식 처리 역량을 갖추고 있다. EXTURE 3.0은 2023년 1월 25일 매매체결/정보분배 시스템, 2023년 10월 4일 청산결제 시스템이 순차 가동되었으며, 24시간 확장 시 CME의 마켓 세그먼트 분할과 유사한 부하 격리 전략이 필요할 수 있다.

### 4.4 이중화 및 장애 복구

23시간 이상의 연속 가동을 위해 CME는 다계층 이중화 아키텍처와 엄격하게 구조화된 재해 복구(DR) 프로토콜을 운영한다.

**무중단 배포 전략:**

1. **듀얼 존 아키텍처(Dual Zones Architecture) 교대 운영:** CME는 프로덕션 거래를 두 개의 완전히 격리된 존(Zone)에서 번갈아 가며 운영한다. 활성 존(Active Zone)이 라이브 시장 거래를 처리하는 동안, 트래픽이 차단된 대체 존(Alternate Zone)에서 소프트웨어 패치 및 인프라 업그레이드가 백그라운드에서 수행된다. 이후 지정된 1분 유지보수 윈도우에 프로덕션 트래픽을 대체 존으로 스위칭한다.

2. **블루-그린 배포(Blue-Green Deployments):** 로드 밸런서 뒤에 현재 운영 중인 '블루' 환경과 동일한 '그린' 환경을 동시에 구축한다. 그린 환경에서 업데이트와 모의 부하 테스트 완료 후, 라이브 트래픽을 순식간에 라우팅하여 다운타임을 제거하고 문제 발생 시 즉각적 롤백이 가능하다.

3. **무중단 데이터베이스 마이그레이션 및 기능 플래그(Feature Flags):** 데이터베이스 스키마 변경 시 동적 기능 플래그를 활용하여, 기존 운영 데이터베이스에서 트랜잭션이 처리되는 동안 백그라운드에서 비동기적이고 점진적인 데이터 마이그레이션을 수행한다.

**데이터 센터 아키텍처:**

| 시설 | 위치 | 역할 | 규모 |
|---|---|---|---|
| **오로라 데이터 센터** | 시카고 서쪽 40마일 (CyrusOne) | 기본 프로덕션 | 428,000+ sq ft, Tier-3 |
| **뉴욕 데이터 센터 (NYDC)** | 뉴욕 | 재해 복구 전용 | 백업 |

CME 그룹은 일상적인 24시간 거래나 야간 유지보수를 위해 데이터 센터 간 트래픽을 이동시키지 않는다. 운영 서버는 오로라 데이터 센터 내에서 24시간 연속 구동되며, 각 계층(네트워크, 서버, 애플리케이션)마다 여러 겹의 다중 이중화(multiple layers of redundancy)가 구축되어 물리적 결함 발생 시 운영 환경 내에서 대기(standby) 컴포넌트로 즉각적 페일오버가 이루어진다.

**재해 복구(DR) 프로토콜:**
- **4단계 상태 모델:** Pre-Event -> Disaster Recovery -> Recovery -> Post-Recovery
- **45분 주문 대기 시간:** DR 환경 전환 시, 매칭엔진 재개 전 45분의 엄격한 주문 대기 시간을 강제하여 모든 글로벌 참여자가 FIX 세션을 재연결하고 시퀀스 번호를 동기화할 시간을 확보
- **Cancel on Disconnect (CoD):** 네트워크 연결이 예상치 않게 끊어질 경우, 매칭엔진이 자동으로 해당 세션의 모든 대기 주문을 취소하여 24시간 시장에서 담당 트레이더가 다른 시간대에서 부재 중일 때 낡은 의도(stale intent) 기반의 체결을 방지

---

## 5. GC2 신용통제 프레임워크

### 5.1 실시간 신용 관리

Globex 신용 통제(Globex Credit Controls, **GC2**) 시스템은 청산 회사가 고객의 거래 활동에 대해 수학적으로 결정론적인 신용 한도를 실시간으로 설정할 수 있도록 하는 체결 전(pre-execution) 리스크 관리 프레임워크이다. 리스크 관리자는 실행 회사 ID(Executing Firm ID)와 거래소 그룹(Exchange Group)의 정확한 교차점에서 한도를 설정한다.

**GC2 핵심 통제 요소:**

| 통제 유형 | 설명 |
|---|---|
| **노출 한도 (Exposure Limits)** | 선물 및 옵션 계약 전반의 매수 및 매도 포지션 모두에 시스템적으로 적용되는 통화 기반 한도 |
| **최대 수량 한도 (Maximum Quantity Limits)** | 단일 주문의 최대 허용 크기에 대한 절대적 상한선 |
| **보수적 논리 (Conservative Logic)** | 노출 한도와 수량 한도가 동시에 활성화된 경우, 두 제약 조건 중 가장 엄격한 것을 적용 |
| **포지션 논리 (Position Logic)** | 미결제 및 체결 포지션을 지속적으로 계산. Total Futures Long = 전체 매수 수량 + 체결 매수 - 체결 매도 |
| **일일 포지션 리셋** | 체결된 포지션은 매일 오후 4:30 CT에 시스템적으로 '0'으로 재설정 |

**킬 스위치(Kill Switch) 메커니즘:** GC2 프레임워크에는 GUI를 통한 반응성이 뛰어난 킬 스위치가 포함되어 있다. **1초 이내에 완전히 작동**할 수 있는 킬 스위치는 지정된 SenderComp ID와 관련된 모든 새로운 주문 입력을 즉시 차단하고, 대기 중인 모든 주문에 대량 취소 명령을 하달한다.

**자동화된 주말 제한 토글:** 청산 회사가 고객의 주말 거래를 제한하면, 주말 시간이 시작될 때 시스템이 자동으로 모든 노출 및 수량 한도를 절대적인 '0'으로 덮어써 수동 개입 없이 즉시 모든 활동을 종료하며, 일요일 저녁에 정상 주중 한도로 복원한다.

**자기 거래 방지(Self-Match Prevention, SMP):** 자동화 수준이 높은 시장에서 동일 회사 내 여러 알고리즘이 의도치 않게 서로 거래하는 것을 방지하기 위해, Globex는 의무적 SMP 메커니즘을 채택한다. 회사는 발신 주문에 고유한 SMP ID(iLink 3의 tag 2362)를 추가하고, 매칭엔진이 동일 SMP ID의 매수/매도 주문을 감지하면 사전 구성된 SMP 지시어에 따라 대기 주문, 진입 주문, 또는 둘 다를 체계적으로 취소하여 자전거래(wash-trade)를 **구조적으로 불가능**하게 만든다.

### 5.2 24시간 리스크 모니터링

연장된 거래 시간은 필연적으로 미국 시장 폐장과 아시아 시장 개장 사이의 시간적 간격에서 글로벌 유동성이 낮은 시기를 발생시킨다. CME 그룹은 이러한 취약한 야간 시간대의 위험을 관리하기 위해 다층적 기술 안전장치 제품군을 활용한다.

**동적 가격 밴딩(Dynamic Price Banding):** 얇은 야간 시장에서 극심한 변동성과 잘못된 주문 입력(fat-finger errors)을 억제하기 위해 동적 가격 밴드를 강제한다. 롤링 기준 가격(일반적으로 최근 거래가 또는 이론적 시초가)을 기준으로 주문 입력에 대한 절대 상한 및 하한을 지정하며, 이 제한 밴드를 벗어난 주문은 게이트웨이에서 즉시 거부된다. 글로벌 커맨드 센터(GCC)는 합법적인 거시경제 뉴스 이벤트(예: 아시아 거래 시간 중 예상치 못한 중앙은행 금리 발표)를 수용하기 위해 실시간으로 밴드를 수동 확대할 수 있는 규제 권한을 보유하며, 유동성 정상화 후 표준 수준으로 복원한다.

**자동 vs 수동 개입 임계값:**

| 구분 | 메커니즘 | 개입 방식 |
|---|---|---|
| **1차 방어선** | GC2 노출 한도/수량 한도 | 완전 자동 (매칭엔진 레벨) |
| **2차 방어선** | 동적 가격 밴딩 | 자동 거부 + GCC 수동 조정 가능 |
| **3차 방어선** | 킬 스위치 | 청산 회사 수동 발동 (1초 이내 작동) |
| **4차 방어선** | 주말 제한 토글 | 자동화된 스케줄 기반 |
| **5차 방어선** | Cancel on Disconnect (CoD) | 네트워크 장애 시 자동 발동 |

이러한 다층적 안전장치 체계는 24시간 연속 시장에서 인간 감독자가 물리적으로 부재하는 시간대(특히 야간 저유동성 구간)에도 시스템적으로 극단적 리스크를 억제할 수 있는 구조를 제공한다.

---

## 6. 청산결제 및 포스트-트레이드

### 6.1 CME Clearing 구조

CME Clearing은 매일 **2천만 건 이상**의 거래에 대한 중앙청산소(CCP)로 운영되며, 매칭된 모든 거래의 이행을 보증한다. 실행 장소(거래소)와 CCP 간의 통합은 연속 시장에서 가장 복잡한 시스템적 과제이다. 거래 후(post-trade) 아키텍처는 연속 매칭이라는 현실과, 글로벌 법정 화폐 시스템과 연계된 일괄 처리(batch) 기반 은행 및 결제 주기의 필요성을 조화시켜야 한다.

CME Clearing은 **엄격하게 정의된 거래 제출 시간(Trade Submission Windows)** 및 일괄 처리 일정을 통해 이러한 복잡한 이분법을 관리한다:

| 프로세스 | 마감 시간 (CT) | 대상 |
|---|---|---|
| **전자 거래 FEC 마감** | 오후 6:00 | CME/CBOT 전자 거래 제출 |
| **비전자 거래/양도 마감** | 오후 7:00 | 비전자 거래 및 Give-up 거래 |
| **E/A 프로세스 실행** | 오후 6:15 | 행사/포기(Exercise/Abandon) 처리, 최종 청산 보고서 생성 |
| **CGM 마감** | 오후 8:00 | 청산 보증 모듈(CGM) 주기 완료 |
| **OTC 거래 제출 마감** | 오후 7:00 (ET) | ClearPort 인터페이스 장외거래 |
| **개시 증거금 계산** | 오후 8:00 (ET) | 포트폴리오 전체 마진 계산 |
| **최종 결제 지시 전송** | 오후 10:00 (ET) | 결제 은행으로 지시 전송 |

**OTC 상품의 시간대별 호가 캡처:** ClearPort를 통해 청산되는 OTC 상품의 경우, 시스템은 현지 시장 시간에 맞춰 연속적으로 호가를 캡처한다(예: JPY는 도쿄 오후 4:00, EUR은 런던 오후 4:00). 이러한 시간대별 차등 처리는 글로벌 24시간 시장에서 다중 통화 결제의 복잡성을 관리하는 핵심 메커니즘이다.

### 6.2 담보 관리 및 뱅킹 타임라인

연속 24시간 시장에서 담보는 거시경제적 충격으로 인한 야간의 급작스러운 마진 콜(margin calls)을 충당할 수 있도록 높은 유동성을 유지해야 한다. CME Clearing은 예탁결제원(DTC)과 연동되며, 뱅킹 및 증거금 시스템(BAMS)을 FIXML 기반 API를 통해 운영하여 담보 예치 및 인출을 완전 자동화한다.

**일일 뱅킹 타임라인:**

| 시간 (CT) | 뱅킹 및 담보 관리 작업 |
|---|---|
| **08:30 a.m.** | 외화(CAD, EUR, GBP, MXN)의 당일 가치 결제를 위한 BAMS 입출금 요청 마감 |
| **10:30 a.m.** | 외화(AUD, JPY, SEK, SGD)의 익일 가치 결제를 위한 BAMS 요청 마감 |
| **11:00 a.m.** | 일중 정산 처리 전 모든 담보 요청 마감. 지연 항목은 일중 처리 완료까지 대기 |
| **11:30 a.m. ~ 1:00 p.m.** | 일중 정산 주기에 따른 예상 및 최종 결제 의무 확인 |
| **02:00 p.m.** | 모든 비현금 담보 입출금 요청의 최종 마감 |
| **02:30 p.m.** | USD 현금 입금 및 DTC로의 주식/ETF/회사채 인출 요청 마감 |

**BAMS API 자동화:** 청산 회원은 SFTP(Secure File Transfer Protocol)를 통해 고도로 구조화된 FIXML 메시지를 사용하여 프로그래밍 방식으로 요청 파일을 업로드할 수 있다. 담보 할당 메시지는 CollAsgn 요소를 사용하며, BizDt 속성(영업일), AsgnRsn 속성(증거금 입금 Reason 3 / 인출 Reason 4), PxQteCcy 속성(거래 통화)으로 구성된다. 이러한 자동화된 무인(no-touch) 프로세스는 야간 변동성에 대응하여 백오피스의 수동 개입 없이 마진 요구 사항을 신속하게 충족시킬 수 있도록 하는 필수 기능이다.

**뱅킹 시간 제약:** 담보 관리의 근본적 한계는 글로벌 법정 화폐 결제 시스템(Fedwire, CHIPS 등)이 24시간 운영되지 않는다는 점이다. CME는 통화별 차등 마감 시간(CAD/EUR/GBP/MXN은 08:30 CT, AUD/JPY/SEK/SGD는 10:30 CT)을 통해 이를 관리하지만, 은행이 폐장한 야간 시간에 발생하는 긴급 마진 콜은 익일 은행 개장까지 물리적 현금 이체가 불가능하다. 이러한 제약은 충분한 초기 증거금 수준과 자동화된 담보 재배치 메커니즘의 중요성을 강조한다.

### 6.3 결제 사이클

CME의 결제 사이클은 상품 유형에 따라 차등화되어 있으며, 연속 거래 환경에서 자정 경계(midnight boundary)를 가로지르는 결제를 관리하기 위한 엄격한 시간적 구조를 갖추고 있다.

**거래일 경계 관리:** CME Globex에서 거래일(Trade Date)의 논리적 전환은 오후 4:00 CT에 발생한다. 이 시점을 기준으로 이전에 체결된 거래는 당일(T) 결제 주기에, 이후 체결된 거래는 익일(T+1) 결제 주기에 귀속된다. 이는 물리적 자정(midnight)이 아닌 시장 운영 시간 기준의 논리적 거래일 개념을 사용함으로써, 글로벌 시간대를 가로지르는 연속 거래에서 결제일 귀속의 모호성을 제거한다.

**일중(Intraday) 결제:** CME는 시스템 리스크를 분리하기 위해 여러 건의 일중 정산 프로세스를 운영한다. 11:30~13:00 CT 사이에 일중 정산 주기가 실행되어 변동 증거금(variation margin) 결제 의무를 확인하고, 이를 통해 대규모 손실 누적을 방지한다.

**교차 증거금(Cross-Margining) 시너지:** CME Group과 DTCC-FICC(고정수익 청산회사) 간의 교차 증거금 약정은 교차 시장 시너지의 결정적 템플릿을 제공한다. 이 약정 하에, CME 금리 선물과 FICC 청산 미국 국채에서 상쇄되는 리스크 노출을 보유한 청산 회원은 통합된 순 리스크 계산 혜택을 받아 이행 보증금을 대폭 줄일 수 있다. 파생상품과 기초 현물 자산 간의 수학적 상관관계를 법적으로 인정함으로써, 자본 효율성을 극대화한다.

---

## 7. Follow-the-Sun 운영 모델

### 7.1 글로벌 운영 센터

CME 그룹의 글로벌 커맨드 센터(Global Command Center, **GCC**)는 24시간 시장 운영의 인적 기반을 구성하는 핵심 조직이다. GCC는 지리적으로 분산된 3개의 주요 운영 센터를 통해 연속적인 시장 감시 및 지원을 제공한다.

| 운영 센터 | 위치 | 주요 책임 시간대 | 핵심 기능 |
|---|---|---|---|
| **미주(Americas)** | 시카고 | CT 기준 주간 | 기본 운영 허브, 매칭엔진 모니터링, DR 지휘 |
| **EMEA** | 런던 | GMT/BST 기준 주간 | 유럽 시간대 운영 관리, 유럽 고객 지원 |
| **APAC** | 싱가포르 | SGT 기준 주간 | 아시아 시간대 운영 관리, 아시아 고객 지원 |

이 세 운영 센터의 현지 영업 시간을 결합하면 24시간 연속 커버리지가 달성된다. 각 지역 센터는 현지 표준 영업 시간에 운영되되, **교차 근무(overlapping shifts)**가 설계되어 정보의 원활한 인수인계를 촉진한다.

**통합된 사고 지휘 체계:** 모든 지역 팀은 통합된 운영 표준에 보고하며, 글로벌 사고 대응 및 재해 복구(DR) 실행을 위한 확정적인 에스컬레이션 포인트(escalation point) 역할을 수행한다.

**보편적 고객 커뮤니케이션:** CME는 통합된 GCC로 연결되는 현지화된 지원 전화번호, 통합 발권(ticketing) 시스템, 회사 수준의 관리 포털(보안 토큰 접근이 필요한 FirmSoft 등)을 활용한다. 이를 통해 글로벌 고객이 어느 시간대에 있든 주문 상태나 비상 취소와 관련하여 즉각적이고 인증된 지원을 받을 수 있다.

### 7.2 인력 운영 전략

CME의 "Follow-the-Sun"(FTS) 운영 인력 모델은 24시간 매칭엔진의 기술적 연속성을 보완하는 인적 연속성을 제공한다. 핵심 설계 원칙은 다음과 같다:

**구조화된 지역 인수인계(Structured Regional Handover):**
- 각 지역 센터는 현지 표준 영업 시간 동안 운영
- 교차 근무(overlapping shifts)를 통해 진행 중인 사고 대응, 사이버 보안 모니터링, 복잡한 기술적 이상 현상이 정보 손실 없이 한 지역 팀에서 다음 팀으로 원활하게 이전
- 인수인계 프로토콜에는 구조화된 브리핑 문서, 실시간 대시보드 공유, 에스컬레이션 이력 전달이 포함

**운영 인력 구성:**
- 시장 운영(Market Operations): 세션 상태 관리, 유지보수 창 조율, 비상 시장 정지/재개 관리
- 기술 운영(Technology Operations): 매칭엔진, 네트워크, 데이터베이스 모니터링 및 장애 대응
- 리스크 운영(Risk Operations): 실시간 포지션 모니터링, 가격 밴딩 조정, 킬 스위치 발동 판단
- 고객 지원(Client Support): 접속 장애, 주문 상태 확인, 비상 취소 처리
- 시장 감시(Market Surveillance): 이상 거래 패턴 탐지, 시장 남용 모니터링

### 7.3 KRX 인력 운영 시사점

KRX가 24시간 거래를 도입할 경우, CME의 FTS 모델을 참고하되 한국 고유의 노동법적, 조직적 제약을 고려한 맞춤형 운영 모델을 설계해야 한다.

**FTS 모델 적용 가능성:**
- KRX는 CME와 달리 3개 지역에 운영 센터를 보유하고 있지 않으므로, 초기에는 국내 교대 근무(shift work) 모델이 더 현실적
- 장기적으로 런던(EMEA)과 뉴욕(Americas) 또는 싱가포르(APAC)에 경량 운영 데스크를 설치하여 FTS 모델로 전환 가능

**한국 근로기준법 고려 사항:**
- 주 52시간 근무제(주 40시간 + 연장 12시간) 하에서 24시간 3교대 운영 시 인력 확보
- 야간 근무(22:00~06:00) 가산 수당(통상임금 50% 가산) 비용 고려
- 야간 근무자의 건강권 보호를 위한 정기 건강검진 의무 등 노동법적 요건 충족
- 교대 인수인계 프로토콜의 법적 기록 의무

**자동화 우선 전략:** 야간 시간대의 인력 부담을 최소화하기 위해, CME의 GC2, 동적 가격 밴딩, Kill Switch, Cancel on Disconnect 등에 상응하는 자동화된 리스크 관리 시스템의 구축이 선행되어야 한다. 인간 감독자의 역할은 자동화 시스템이 포착하지 못하는 비정형적 이상 상황에 대한 최종 판단권자로 한정하는 것이 효율적이다.

---

## 8. KRX 시사점 및 도입 권고

### 8.1 기술적 시사점

**CME의 24시간 아키텍처가 검증한 사항:**
1. **마이크로초 지연 시간의 24시간 유지:** CME Globex는 17개 마켓 세그먼트의 수평 분할과 등거리 코로케이션을 통해 24시간 내내 결정론적 지연 시간을 유지할 수 있음을 실증. KRX의 EXTURE 3.0(50us, 9.4억 건/일)은 이에 필적하는 성능을 보유.
2. **바이너리 프로토콜 도입:** iLink 3의 FIXP/SBE 기반 바이너리 프로토콜은 HFT 환경에서 필수적. KRX도 ASCII FIX 기반 인터페이스를 바이너리 프로토콜로 전환하는 로드맵 검토 필요.
3. **듀얼 존 무중단 배포:** CME의 듀얼 존/블루-그린 배포 전략은 1분 유지보수 창 내에서 시스템 전환을 가능하게 함. KRX의 유지보수 창이 CME(1분)보다 길더라도(예: 1시간), 무중단 배포 역량은 필수.
4. **세션 영속성(FIXP UUID 기반):** 물리적 연결 단절 시에도 논리적 세션 상태를 유지하는 메커니즘은 24시간 운영의 기본 요건.

### 8.2 운영적 시사점

**Follow-the-Sun 모델의 적용:**
- CME의 시카고-런던-싱가포르 3거점 FTS 모델은 글로벌 연속 운영의 황금 표준
- KRX 초기 단계에서는 국내 3교대 운영 + 자동화 시스템 강화가 현실적
- 중기적으로 글로벌 운영 데스크(해외 브로커 및 기관 지원용) 설치 검토

**자동화된 감시 요건:**
- GC2에 상응하는 실시간 체결 전 리스크 관리 시스템 필수
- 동적 가격 밴딩에 상응하는 야간 변동성 제어 메커니즘
- Kill Switch, Cancel on Disconnect 등 비상 안전장치의 24시간 작동 보장
- SMP(자기 거래 방지) 메커니즘의 EXTURE 3.0 통합

### 8.3 파생상품 시장 연계

KRX는 이미 파생상품 시장에서 연장된 거래 시간을 운영하고 있으며, 이는 현물 주식 24시간 확장의 전략적 기반을 제공한다.

**기존 파생상품 인프라 활용:**
- KOSPI 200 선물/옵션 야간 거래(18:00~05:00 KST): 이미 11시간의 야간 거래 경험 보유
- 야간 선물 가격은 현물 시장 개장 전 가격 발견 기능을 수행
- 이 인프라를 현물 주식 야간 거래의 가격 참조점(price reference)으로 활용 가능

**KOSPI 200 선물의 야간 가격 참조 역할:**
- CME의 E-mini S&P 500 선물이 미국 현물 시장 폐장 후 글로벌 가격 발견 기능을 수행하는 것과 유사
- KRX 현물 시장 24시간 확장 시, KOSPI 200 야간 선물 가격을 현물 주식의 이론적 가치 산출에 활용
- BTIC/TACO와 유사한 베이시스 거래 메커니즘 도입을 통해 파생상품-현물 간 가격 연계 강화

**교차 증거금(Cross-Margining) 개발:**
- CME-DTCC/FICC 교차 증거금 모델을 참조하여, 야간 KOSPI 선물 포지션과 연속 현물 주식 간의 마진 요구 사항을 동적으로 상쇄하는 교차 증거금 API 개발
- 자본 마찰 비용 감소를 통해 글로벌 유동성 제공자들의 야간 시장 조성(market making) 유인 강화
- FIXML 기반 API를 통한 자동화된 담보 할당으로 정규 업무 시간 외 긴급 마진 예치 가능

### 8.4 핵심 Gap 분석

| 비교 항목 | CME Globex | KRX (현재) | Gap 및 권고 |
|---|---|---|---|
| **운영 시간** | 23시간/일 (일~금), 60초 일일 중단 | 6.5시간/일 (09:00~15:30 KST) | 2026.9.14 12시간 시행(연기) -> 2027.12 24시간 목표 |
| **유지보수 창** | 60초 일일 + 화/토 1시간 45분 | 야간 전체 (15:30~09:00) | 최소 1시간 유지보수 창 설계 (현물 주식 특성 고려) |
| **시스템 아키텍처** | 17개 마켓 세그먼트 수평 분할, MSGW/CGW 이중 게이트웨이 | EXTURE 3.0 (50us, 9.4억 건/일) | 부하 격리를 위한 세그먼트 분할 전략 검토 |
| **프로토콜** | iLink 3 (FIXP/SBE 바이너리), MDP 3.0 (UDP 멀티캐스트) | FIX 기반 | 바이너리 프로토콜 전환 로드맵 수립 |
| **청산 통합** | CME Clearing 실시간 통합, 2천만 건/일 처리 | 한국예탁결제원(KSD) 배치 처리 | 실시간 청산 통합 API 개발, 야간 결제 프로세스 설계 |
| **리스크 관리** | GC2 (실시간 체결 전 신용 통제), 동적 가격 밴딩, Kill Switch, SMP | 정규장 리스크 관리 | GC2 수준의 24시간 자동화 리스크 관리 시스템 구축 |
| **인력 모델** | Follow-the-Sun (시카고/런던/싱가포르) | 단일 거점 (서울) | 초기 3교대 국내 운영 -> 중기 FTS 모델 전환 |
| **재해 복구** | 오로라(기본) + NYDC(백업), 4단계 DR, 45분 대기 | EXTURE 3.0 DR 센터 | 24시간 DR 프로토콜 강화, CoD 의무화 |
| **담보 관리** | BAMS/FIXML API 기반 자동화, 시간대별 차등 마감 | 정규 업무 시간 기반 | API 기반 야간 자동 담보 관리 시스템 개발 |
| **규제 프레임워크** | CFTC 규제, 24/7 상품 포함 | 금융위/금감원 규제 | 야간 거래 규제 프레임워크 정비, 투자자 보호 장치 |

---

## 9. CME Globex 일일 라이프사이클 다이어그램

```mermaid
gantt
    title CME Globex 일일 거래 라이프사이클 (CT 기준)
    dateFormat HH:mm
    axisFormat %H:%M

    section Globex 거래 세션
    야간 거래 (전일 17:00~)     :active, s1, 00:00, 02:00
    화/토 유지보수               :crit, m1, 02:00, 03:45
    Pre-Open (화/토)            :m2, 03:45, 04:00
    주간 거래                    :active, s2, 04:00, 16:00
    일일 60초 리셋              :crit, m3, 16:00, 16:01
    야간 거래 (익일분)           :active, s3, 16:01, 23:59

    section 청산결제 주기
    BAMS 외화 마감 (CAD등)      :b1, 08:30, 09:00
    BAMS 외화 마감 (AUD등)      :b2, 10:30, 11:00
    일중 정산 주기               :b3, 11:30, 13:00
    비현금 담보 마감             :b4, 14:00, 14:30
    USD 현금/DTC 마감            :b5, 14:30, 15:00
    전자거래 FEC 마감            :b6, 18:00, 18:15
    E/A 프로세스                :b7, 18:15, 18:30
    OTC 마감 (ET 19:00)         :b8, 18:00, 19:00
    CGM 마감                    :b9, 20:00, 20:30

    section KRX 파생상품 (KST 참조)
    KRX 정규장 (09:00-15:45 KST)  :krx1, 18:00, 00:45
    KRX 야간장 (18:00-05:00 KST)  :krx2, 03:00, 14:00
```

> **참고:** KRX 시간은 CT와 14~15시간의 시차가 있다 (KST = CT + 15시간, 서머타임 시 CT + 14시간). 위 다이어그램에서 KRX 시간은 CT 기준으로 환산하여 표시하였다. KRX 정규장(09:00~15:45 KST)은 대략 CT 18:00~00:45에, KRX 야간장(18:00~05:00 KST)은 대략 CT 03:00~14:00에 해당한다.

---

## 참고문헌

1. CME GLOBEX REFERENCE GUIDE, CME Group, https://www.cmegroup.com/globex/files/GlobexRefGd.pdf
2. CME matching algorithms explained, Databento Blog, https://databento.com/blog/cme-matching-algorithms-explained
3. CME Globex Matching Algorithm Steps, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457218521
4. CME Globex Market Segment - iLink Architecture, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457220437/iLink+Architecture
5. Swap-Based Event Contracts and 24-7 Trading, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/988020743
6. Order Qualifiers, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Order+Qualifiers
7. Order Types for Futures and Options, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Order+Types+for+Futures+and+Options
8. Basis Trade at Cash Open, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/Basis+Trade+at+Cash+Open
9. Basis Trade at Index Close (BTIC) and BTIC+, CME Group, https://www.cmegroup.com/trading/equity-index/btic-transactions.html
10. Trade at Cash Open (TACO) and TACO+, CME Group, https://www.cmegroup.com/trading/equity-index/trade-at-cash-open.html
11. Basis Trade at Index Close (BTIC) - APAC, CME Group, https://www.cmegroup.com/trading/equity-index/files/btic-block-trades-apac.pdf
12. FAQ: BTIC+ and TACO+, CME Group, https://www.cmegroup.com/trading/equity-index/faq-btic-and-taco.html
13. CME Globex Notices: March 2, 2020, CME Group, https://www.cmegroup.com/notices/electronic-trading/2020/03/20200305.html
14. CME Clearing Services, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457215607/CME+Clearing+Services
15. Clearing, CME Group, https://www.cmegroup.com/solutions/clearing.html
16. Transaction Timelines, CME Group, https://www.cmegroup.com/solutions/clearing/operations-and-deliveries/transaction-timelines.html
17. CME Clearing: Principles for Financial Market Infrastructures Disclosure, CME Group, https://www.cmegroup.com/clearing/risk-management/files/cme-clearing-principles-for-financial-market-infrastructures-disclosure.pdf
18. CME Clearing Collateral API Specifications CSV Format, CME Group, https://www.cmegroup.com/clearing/financial-and-collateral-management/files/cme-collateral-api-csv.pdf
19. CME Clearing's Collateral API via FIXML, CME Group, https://www.cmegroup.com/clearing/risk-management/files/cme-collateral-api-fixml.pdf
20. Matching Algorithms, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457218479
21. Blue-Green Deployments: A Definition and Introductory Guide, LaunchDarkly, https://launchdarkly.com/blog/blue-green-deployments-a-definition-and-introductory/
22. Blue-green deployments: Zero-downtime deployments, Liquibase, https://www.liquibase.com/blog/blue-green-deployments-liquibase
23. iLink 3 for CGW Session Guidelines, CME Group, https://www.cmegroup.com/globex/files/ilink-3-cgw-session-guidelines.pdf
24. Session Layer Management Tests, CME Group, https://www.cmegroup.com/tools-information/webhelp/acp-cgw-fo/Content/session-layer.html
25. White Paper: CME MDP 3.0, B2BITS, https://www.b2bits.com/product_support/e-library/white-paper-cme-mdp-30
26. Data Directly from the Market Data Platform, CME Group, https://www.cmegroup.com/market-data/distributor/market-data-platform.html
27. CME's Aurora Co-Lo: Quick Facts, A-Team Insight, https://a-teaminsight.com/blog/cmes-aurora-co-lo-quick-facts/?brand=tti
28. CME Group Announces Agreement to Sell Aurora Data Center to CyrusOne, CME Group, https://investor.cmegroup.com/news-releases/news-release-details/cme-group-announces-agreement-sell-aurora-ill-data-center
29. CME Co-Location Services, CME Group, https://www.cmegroup.com/globex/files/CME-Co-Location-Services-Overview.pdf
30. Co-Location and Data Center Services, CME Group, https://www.cmegroup.com/solutions/co-location.html
31. Data Center Connection Agreement Fee Schedule, CME Group, https://www.cmegroup.com/globex/files/cme-globex-datacenterfeeschedule.pdf
32. CME GLink, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457415665/CME+GLink
33. GLink Cross Connect Specifications, CME Group, https://www.cmegroup.com/globex/files/ebs/ebs-glink-cross-connect.pdf
34. CME Globex Credit Controls (GC2), CME Group, https://www.cmegroup.com/tools-information/webhelp/globex-credit-controls/Content/CME-Globex-Credit-Controls-Management.html
35. CME Globex Credit Controls, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457219125/CME+Globex+Credit+Controls
36. FAQ: Globex Self-Match Prevention Functionality, CME Group, https://www.cmegroup.com/solutions/market-access/globex/trade-on-globex/faq-self-match.html
37. GCC Product Resources, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457086986/GCC+Product+Resources
38. Follow the sun trading, FOW, https://www.fow.com/insights/follow-the-sun-trading-more-trades-processing-and-reporting
39. About the Global Command Center (GCC), CME Group, https://www.cmegroup.com/solutions/market-access/globex/trade-on-globex/about-the-global-command-center.html
40. Strategies to take your customer support global, Intercom, https://www.intercom.com/blog/global-customer-support/
41. Staff Security Engineer - Operations, CME Group (Dice.com), https://www.dice.com/job-detail/eaca6dcf-8a09-44b1-b688-0ec8e292d504
42. API Development Requirements and Assistance, CME Group, https://www.cmegroup.com/solutions/market-access/globex/develop-to-globex/api-development-requirements-and-assistance.html
43. CME Globex Disaster Recovery Process, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457412471/CME+Globex+Disaster+Recovery+Process
44. CME Customer Center Services Guide, CME Group, https://www.cmegroup.com/education/files/cme-customer-center-services-guide.pdf
45. DTCC Files to Expand CME Group Cross-Margining Arrangement, DTCC, https://www.dtcc.com/news/2025/december/15/dtcc-files-to-expand-cme-group-cross-margining-arrangement
46. CME-FICC Cross Margining for Customers, CME Group, https://www.cmegroup.com/markets/interest-rates/files/cme-ficc-cross-margining-for-indirect-users.pdf
47. Fixed-income cross-margin opportunities, CME Group, https://www.cmegroup.com/articles/files/2025/fixed-income-cross-margin-opportunities-driver-change.pdf
48. CME Globex Disaster Recovery, CME Group Client Systems Wiki, https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457412050/CME+Globex+Disaster+Recovery
49. 101 Overview: Settlement, CME Group, https://www.cmegroup.com/articles/brochures-and-handbooks/101-overview-settlement.html
50. 3 Best Practices For Zero-Downtime Database Migrations, LaunchDarkly, https://launchdarkly.com/blog/3-best-practices-for-zero-downtime-database-migrations/
