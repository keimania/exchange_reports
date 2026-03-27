# DTCC 24/5 청산·결제 로드맵 분석

> **작성일**: 2026년 3월 26일
> **분류**: 글로벌 자본시장 인프라 · 청산결제 체계 전환
> **핵심 키워드**: DTCC, NSCC, UTC, CCP, 24/5, T+1, FIX Tag 715, Good Night Protocol

---

## 1. 기관 개요

### 1.1 DTCC 지주회사 구조

DTCC(Depository Trust & Clearing Corporation)는 미국 증권시장의 거래 후(post-trade) 처리를 총괄하는 핵심 금융 인프라 기관이다. DTCC는 세 개의 주요 자회사를 통해 미국 자본시장의 청산·결제·예탁 기능을 수행한다.

| 자회사 | 정식 명칭 | 핵심 기능 |
|--------|-----------|-----------|
| **DTC** | Depository Trust Company | 증권 예탁·보관, 장부상 소유권 이전, 배당·이자 지급 대행 |
| **NSCC** | National Securities Clearing Corporation | 주식·ETF·채권의 청산(clearing) 및 네팅(netting) 수행 |
| **FICC** | Fixed Income Clearing Corporation | 국채(GSD)·모기지증권(MBSD) 전문 청산 |

NSCC는 미국 주식시장 일일 거래의 사실상 전량을 처리하며, 24/5 확장 운영의 중심축이다. NSCC의 Universal Trade Capture(UTC) 시스템이 거래 수집·검증·보고의 핵심 플랫폼 역할을 담당한다.

### 1.2 미국 증권시장 청산·결제의 핵심 인프라

미국 증권시장에서 체결된 모든 주식 거래는 거래소(NYSE, Nasdaq 등)나 대체거래시스템(ATS)에서 실행된 후 NSCC로 전송되어 청산 처리된다. NSCC는 다수의 매수·매도 포지션을 상계(netting)하여 결제해야 할 순 의무(net obligation)를 산출하고, 이를 DTC를 통해 최종 결제한다. 이 과정에서 참가 증권사들의 증거금(margin) 요구량이 대폭 절감되며, 결제 리스크가 체계적으로 관리된다.

### 1.3 CCP(중앙거래상대방) 역할

NSCC는 CCP(Central Counterparty)로서 법적 채무인수(novation) 메커니즘을 통해 **모든 매도자에 대한 매수자** 이자 **모든 매수자에 대한 매도자** 역할을 수행한다. 거래가 UTC 시스템에 의해 검증·수락되는 순간, NSCC가 거래의 양쪽 상대방으로 개입하여 개별 참가자 간의 양자 간(bilateral) 신용 리스크를 제거한다.

이 CCP 보증은 특히 야간 시간대에 결정적 의미를 갖는다. 기존에는 야간 ATS에서 체결된 거래가 다음 영업일 아침까지 양자 간 담보 없는 채무로 남아 있었으나, 24/5 모델에서는 야간 거래에도 CCP 보증이 **즉시** 적용되어 체계적 리스크(systemic risk)를 획기적으로 감소시킨다.

---

## 2. 24/5 전환 배경

### 2.1 글로벌 수요 조사 결과

DTCC와 Ernst & Young(EY)이 공동 발간한 백서 *"The Shift to 24x5 Trading: What It Means for U.S. Equity Markets"*에 따르면, **설문 참여 시장참여자의 72%가 글로벌 수요, 특히 아시아태평양(APAC) 투자자 수요를 24/5 전환의 핵심 동인으로 인식**하고 있다. APAC 투자자들은 미국 시장에 영향을 미치는 실적 발표, 지정학적 사건, 거시경제 지표에 자국 시간대에서 즉시 대응할 수 있는 능력을 요구하고 있다.

### 2.2 야간 거래 비중 전망

EY/DTCC 공동 연구에 따르면, **2028년까지 미국 주식 총 거래량의 1~10%가 야간 세션으로 이동**할 것으로 전망된다. 초기 채택은 리테일 브로커리지가 주도하고, 거시경제 스트레스 기간에는 기관투자자의 참여가 크게 확대될 것으로 예상된다.

### 2.3 디지털 자산 시장의 영향

암호화폐 거래소와 전통 증권거래의 융합으로 인해, 투자자 베이스 전반에 "항시 가동(always-on)" 유동성에 대한 기대가 형성되었다. 24시간 무중단으로 운영되는 암호화폐 시장의 경험은 전통 증권시장에 대한 연속 거래 요구를 가속화하는 핵심 촉매가 되었다.

### 2.4 산업계 준비 현황

EY/DTCC 조사에서 **참여 기업의 약 60~72%가 새로운 연속 거래 요건에 부합하기 위해 상당한 기술 및 리스크 관리 업그레이드를 계획**하고 있다고 응답했다. 이는 24/5 전환이 단순한 운영시간 연장이 아닌 산업 전반의 인프라 재구축을 요구함을 시사한다.

---

## 3. 구현 타임라인

### 3.1 Phase 1 (2024년 9월 완료): UTC 01:30 ET 개시

Phase 1은 NSCC의 UTC 현대화 첫 단계로, **2024년 9월에 성공적으로 배포**되었다. 이 단계에서 승인된 거래센터, ATS, 전자거래 플랫폼이 **동부시간(ET) 01:30부터** 체결 거래를 제출할 수 있게 되었다.

**기존 프로세스**: 심야 시간대 체결 거래는 집행 브로커의 양자 간 큐(queue)에 보관 후, 핵심 시스템이 온라인 되는 약 04:00 ET에 NSCC로 전송
**변경 후**: 영업 개시를 2.5시간 앞당겨 01:30 ET부터 UTC 시스템이 거래 수집 시작

이 단계를 통해 검증된 사항:
- FIX 엔진의 조기 수집 용량(capacity) 검증
- 아시아·유럽 시간대 참여자의 비동기(asynchronous) 거래 흐름 처리 능력
- 08:30 ET Consolidated Trade Summary(CTS) 보고 주기와의 정합성
- 지연시간(latency) 병목 현상 식별 및 해소

### 3.2 Industry Testing (2026년 1월 11일~): PSE 환경 테스트

DTCC는 2026년 6월 프로덕션 론칭을 위한 전제 조건으로, **2026년 1월 11일부터 Participant Services Environment(PSE)에서 산업 전반 테스트**를 의무화했다.

**테스트 필수 검증 항목**:

| 검증 항목 | 세부 내용 |
|-----------|-----------|
| FIX Tag 715 파싱 | Clearing Business Date 필드의 정확한 해석 및 하위 시스템 전파 |
| EOD 밸런싱 | 일일 원장 마감 및 잔액 조정 프로토콜 정합성 |
| 세션 리사이클링 | FIX 세션 종료·재접속·시퀀스 리셋의 무손실 처리 |
| Good Night 메시지 | 영업일 전환 신호의 정확한 송수신 및 처리 |
| High-Value Threshold | 야간/주간 고액 거래 임계값 검증 ($1B/$1.5B) |

60~72% 참여 기업이 기술 및 리스크 관리 업그레이드를 계획하고 있으며, PSE 인증을 통과하지 못한 기관은 야간 세션 참여가 기술적으로 차단된다.

### 3.3 Special Representative Facility (2026년 3월 30일): 9A/9B 야간 관계 설정

**2026년 3월 30일**부터 Automated Special Representative Facility를 통해 청산 회원사가 야간 세션 전용의 **별도 9A/9B 승인 관계**를 구축할 수 있다. 이는 야간 청산의 선택적(opt-in) 승인·거부 모델의 기반이 된다.

### 3.4 Phase 2 (2026년 6월 28일 목표): 완전 24/5 프로덕션

SEC의 규칙 변경 최종 승인을 조건으로, **2026년 6월 28일 Phase 2 프로덕션 론칭**이 예정되어 있다.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    24/5 연속 운영 스케줄                              │
│                                                                     │
│  일요일 20:00 ET ──────────────────────────── 금요일 20:00 ET       │
│  │                                                            │     │
│  │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐        │     │
│  │  │ 일~월 │  │ 월~화 │  │ 화~수 │  │ 수~목 │  │ 목~금 │        │     │
│  │  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘        │     │
│  │                                                            │     │
│  │  매일 20:00~21:00 ET: 기술 점검 윈도우 (거래소/SIP 일시중단)   │     │
│  │  NSCC UTC 시스템: 점검 중에도 계속 운영                       │     │
│  │                                                            │     │
│  │  미국 공휴일 전야: 익일 거래 수락 중단                        │     │
│  └────────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.5 Full UTC Modernization (Q4 2027)

**2027년 4분기**는 모든 잔여 회원사가 현대화된 DTCC 표준으로 연결성을 업데이트해야 하는 최종 규제·기술 기한이다.

### 3.6 종합 타임라인 요약

| 단계 | 핵심 마일스톤 | 일정 | 전략적 목표 |
|------|--------------|------|-------------|
| Phase 1 | UTC 확장 제출 | 2024.9 (완료) | UTC 영업 개시를 01:30 ET로 앞당겨 조기 수집 검증 |
| Industry Testing | PSE 클라이언트 테스트 | 2026.1.11~ (진행 중) | FIX Tag 715 파싱, EOD 밸런싱, 세션 리사이클링 산업 전반 검증 |
| Infrastructure | Special Rep. Facility | 2026.3.30 (예정) | 청산사의 야간 전용 9A/9B 승인 관계 구축 |
| Phase 2 | 완전 24/5 프로덕션 | 2026.6.28 (목표) | 일 20:00 ET~금 20:00 ET 연속 주식 청산, CCP 보증 즉시 적용 |
| Modernization | 전면 UTC 현대화 | Q4 2027 (장기) | 전 회원사 현대화 DTCC 표준 연결성 최종 기한 |

---

## 4. Universal Trade Capture (UTC) 시스템

### 4.1 핵심 기능: 실시간 검증, 표준화, 보고

UTC는 거래소 또는 적격 특별대리인(QSR)이 NSCC에 제출하는 주식 거래를 **실시간으로 검증(validate), 표준화(standardize), 보고(report)**하는 핵심 기술 플랫폼이다. 24/5 청산 패러다임을 지원하기 위해 DTCC는 FIX(Financial Information eXchange) 메시징 아키텍처와 MQ(Message Queue) 프로토콜을 전면 개편하고 있다.

핵심 개편 목표는 **거래 체결 시점과 법적 청산 시점 간의 시간적 불일치(temporal dissonance)를 관리**하기 위한 결정론적(deterministic) 데이터 필드의 도입이다.

### 4.2 FIX Tag 715 (Clearing Business Date)

#### Trade Date와 CBD 분리 로직

24/5 환경에서 가장 핵심적인 기술 변경 사항은 **FIX Tag 715(Clearing Business Date, CBD)**의 의무적 통합이다.

**기존(09:30~16:00 ET 거래일)**: Trade Date = Clearing Business Date (동일)
**24시간 환경**: Trade Date와 CBD의 선형적 시간 관계가 완전히 단절

UTC 시스템은 송신 기관의 특정 처리일(processing day)에 기초하여 CBD를 체계적으로 배정한다. NSCC의 운영시간이 20:00 ET에 시작되면, 시스템은 즉시 **다음 영업일의 Trade Date로 지정된 거래 활동을 수집**하기 시작한다.

#### 시나리오별 매핑 표

| 체결 시각 (ET) | 거래 분류 | 실제 캘린더 날짜 | 배정 Trade Date | FIX Tag 715 (CBD) | 결제일 (T+1) |
|---------------|-----------|-----------------|----------------|-------------------|-------------|
| **월요일 14:00** | Regular Way | 월요일 | 월요일 | 월요일 | 화요일 |
| **월요일 19:59** | Regular Way | 월요일 | 월요일 | 월요일 | 화요일 |
| **월요일 20:01** | Next Trade Date | 월요일 | **화요일** | **화요일** | **수요일** |
| **일요일 21:00** | Next Trade Date | 일요일 | **월요일** | **월요일** | **화요일** |

> **핵심 원리**: 20:00 ET를 기준으로 영업일이 전환된다. 20:00 ET 이후에 체결된 거래는 캘린더상 당일이 아닌 **익영업일**의 Trade Date와 CBD를 부여받는다.

Tag 715가 없으면 레거시 시스템이 월요일 22:00 거래를 월요일 청산 의무로 잘못 분류하여, 화요일 아침 T+1 결제 실패를 초래할 수 있다. 이 변경은 UTC 입력 메시지 포맷에는 영향을 미치지 않으나, **실시간 출력 피드(UTCO)를 수신하는 모든 클라이언트에게 필수적**이다.

### 4.3 FIX Tag 336 (TradingSessionID)

NSCC는 24x5 처리 환경에 참여하는 모든 기관에 대해 **FIX Tag 336(TradingSessionID)**의 조건부 사용을 의무화하고 있다. 이 영숫자 문자열은 **최대 3자(characters)**로 제한되며, 거래의 시간적 출처를 결정론적으로 분류한다.

| Tag 336 값 | 세션 명칭 | 시간대 (ET) |
|------------|----------|-------------|
| **PRE** | Pre-market (장전) | 04:00 ~ 09:30 |
| **REG** | Regular core (정규) | 09:30 ~ 16:00 |
| **PST** | Post-market (장후) | 16:00 ~ 20:00 |
| **OVN** | Overnight (야간) | 20:00 ~ 04:00 |

Tag 336은 리스크 관리 프레임워크에 계산적으로 핵심적이다:
- UTC 시스템의 입력 파서가 청산사가 설정한 **특정 9A/9B 거래 관계를 즉시 검증**
- 예: 'REG' 관계만 승인한 청산사의 'OVN' 태그 거래는 자동 거부
- **올바른 High-Value Threshold 로직 실시간 적용** ($1B for OVN vs $1.5B for REG)

### 4.4 Real-Time Output (UTCO) 요건

UTC 실시간 출력(UTCO) 메시지에 Tag 715가 포함됨으로써, 회원사의 하위 회계·리스크·담보 관리 시스템이 야간 거래를 올바르게 분류할 수 있다. 모든 UTCO 수신 클라이언트(청산사, 커스터디언, 서비스 뷰로)는 PSE 테스트 단계에서 새로운 FIX 태그가 포함된 시뮬레이션 테스트 스크립트를 수집하고 성공적으로 처리해야 한다.

### 4.5 "Good Night" 프로토콜 상세

"Good Night" 메시지는 **영업일 간 결정론적·암호학적 경계선** 역할을 하며, 회계 원장의 디지털 마감을 수행한다. 프로토콜은 엄격한 순차 로직으로 운영된다.

#### 5단계 프로토콜

```
┌─────────────────────────────────────────────────────────────────┐
│                   Good Night 프로토콜 5단계                       │
│                                                                 │
│  [1단계] 당일 완료                                               │
│    └─ 송신 기관이 당일 거래 완료, 내부 원장 밸런싱,               │
│       NSCC에 공식 "Good Night" FIX 메시지 전송                   │
│                     │                                           │
│                     ▼                                           │
│  [2단계] 세션 단절/재접속                                        │
│    └─ FIX 엔진 또는 MQ 인터페이스 연결 해제 후                   │
│       세션 리사이클을 위한 재접속 (상태 데이터 퍼지)               │
│                     │                                           │
│                     ▼                                           │
│  [3단계] 시퀀스 리셋                                             │
│    └─ 재접속 후 Next Trade Date 거래 제출 시작                   │
│       반드시 Sequence Number 1부터 시작                          │
│                     │                                           │
│                     ▼                                           │
│  [4단계] UTC 검증                                                │
│    └─ Good Night 미처리 상태에서 Next Trade Date 거래 제출 시     │
│       UTC 매칭 엔진이 유효하지 않은 Trade Date로 자동 거부        │
│                     │                                           │
│                     ▼                                           │
│  [5단계] As-of 거래 처리                                         │
│    └─ Good Night 처리 후 전일 지연 거래 발견 시                   │
│       "As-of" 거래로 수집, 다음 CTS 주기(08:30 AM)에 보고        │
└─────────────────────────────────────────────────────────────────┘
```

### 4.6 Master Good Night (자정 프로토콜)

**약 00:00 ET(자정)**에 UTC 시스템 자체가 작동하여, 아웃바운드 실시간 메시지를 수신하는 **모든 청산사에 최종 권위적 Good Night 메시지를 송신**한다. 이 전송 후 청산사들은 출력 피드에서 **의도적인 짧은 일시정지(intentional brief pause)**를 경험하며, 이 동안 DTCC가 마스터 데이터베이스를 롤(roll)하고 전체적인 결제 의무를 확정한다.

이 프로토콜은 연속 거래가 금융 부문 전반의 **결정론적 일일 복식부기(deterministic daily double-entry accounting)** 기본 요건을 훼손하지 않도록 보장한다.

---

## 5. 청산 라이프사이클

### 5.1 단계별 타임라인 표

아래 표는 표준 장후 세션 마감과 야간 세션 개시 사이의 핵심 전환 기간(critical handoff period)에서 ATS가 UTC에 거래를 제출하는 정확한 데이터 흐름과 프로토콜 요건을 나타낸다.

| 단계 | 시각 (ET) | 수행 주체 | 행위 상세 | 시스템적 영향 |
|------|----------|----------|----------|--------------|
| **1** | **19:55** | ATS 매칭 엔진 | 당일 최종 "Regular Way" 거래 체결 | 현재 Trade Date 및 CBD 배정. Tag 336 = 'PST' |
| **2** | **20:00** | ATS FIX 게이트웨이 | UTC에 공식 "Good Night" 메시지 전송 | 해당 입력 스트림의 당일 처리 종료 공식 선언 |
| **3** | **20:00** | UTC 시스템 | Good Night 메시지 검증, ATS 일일 원장 밸런싱 | 이후 전일 거래 제출 시 "As-of" 상태 강제 적용 |
| **4** | **20:01** | ATS FIX 게이트웨이 | 세션 강제 단절, FIX 엔진 리사이클, UTC 재접속 | 메모리 캐시 클리어, 시퀀스 중복 방지를 위한 연결 상태 리셋 |
| **5** | **20:05** | ATS 매칭 엔진 | 야간 주문 매칭 재개, 신규 세션 첫 거래 제출 | Sequence Number 1부터 시작. Tag 715(CBD) = 내일. Tag 336 = 'OVN' |
| **6** | **00:00** | UTC 시스템 | 모든 수신 청산사에 마스터 "Good Night" 메시지 방송 | DTCC 데이터베이스 롤을 위한 시스템 전반 기술 일시정지 |

### 5.2 CCP 보증 즉시 적용 (Novation)

Phase 2의 24/5 모델에서 가장 핵심적인 변화는 야간 거래에 대한 **CCP 보증의 즉시 적용**이다.

**기존 모델**: 야간 ATS 체결 거래는 다음 날 아침 NSCC에 수집·검증·노베이션 처리될 때까지 **무담보 양자 간 채무**로 존재
**24/5 모델**: UTC 시스템이 거래를 검증하는 즉시 NSCC가 CCP로서 개입

이 변화의 의의:
- **20:00 ET ~ 04:00 ET 변동성 높은 시간대**에 NSCC가 보편적 매수자·매도자로 기능
- 글로벌 참여자가 양자 간 상대방 부도 리스크 없이 대규모 블록 트레이드 및 리스크 관리 포지션 집행 가능
- 마켓메이커·HFT 업체가 야간 체결의 즉각적 NSCC 보증을 기반으로 더 타이트한 호가 스프레드 제시 → **전반적 시장 유동성 심화**

---

## 6. 결제 및 리스크 관리

### 6.1 T+1 결제 통합 (2024년 5월 28일 시행)

24/5 주식시장의 안전한 운영은 **T+1(거래일 + 1영업일) 결제 주기**의 성공적 시행과 불가분의 관계에 있다. 미국 시장은 **2024년 5월 28일** T+2에서 T+1으로 결제 주기를 단축했다.

T+1 전환의 효과:
- 상대방 신용 리스크 노출 기간 24시간 단축
- 청산사에 예치해야 하는 상호화된 증거금(mutualized margin) 요구량 수십억 달러 규모 절감

24/5 모델에서 T+1 결제 로직:

| 체결 시각 | Trade Date | 결제일 |
|----------|-----------|--------|
| 월요일 14:00 ET | 월요일 | 화요일 |
| 월요일 21:00 ET | 화요일 | 수요일 |
| 일요일 21:00 ET | 월요일 | 화요일 |

> 20:00 ET 이후 체결된 거래는 현재 캘린더 날짜를 청산 목적상 "건너뛰고" 익영업일을 공식 Trade Date로 채택한다.

### 6.2 TradeSuite ID 강화

TradeSuite ID는 DTCC의 기관 거래 배분·확인·확약(allocation, confirmation, affirmation) 플랫폼이다.

| 구분 | 기존 | 강화 (2026.6~) |
|------|------|----------------|
| **확약 마감** | 21:00 ET (T-0) | 21:00 ET 유지 (주간 거래) |
| **야간 기관 거래** | 미지원 | **21:20 ET부터 미래 Trade Date(+1) 확인 지원** |

21:20 ET부터의 미래 Trade Date 확인 기능은 아시아 오전 시간대(미국 저녁)에 대규모 블록 트레이드를 집행하는 기관 자산운용사가 **체결 즉시 거래를 확약**할 수 있게 해준다. 이를 통해 T+1 결제 기한 충족에 필요한 STP(Straight-Through Processing)를 보존하고, 야간 수동 배분 병목 현상을 방지한다.

### 6.3 별도 9A/9B 거래 관계

#### 야간 청산 선택적 승인/거부 (Opt-in 모델)

현행 체계에서 대형 청산 브로커딜러는 표준 9A/9B 잠금 합의(locked-in agreement)를 통해 소규모 통신 브로커나 집행 시설 대신 거래를 청산하고 재정적 책임을 부담한다. 그러나 청산사가 **새벽 3시에 통신 고객사의 고변동성 거래를 무조건적으로 보증**할 야간 리스크 관리 인력, 자동화 유동성 예비, 또는 기관적 리스크 선호도를 갖추지 못할 수 있다.

**NSCC의 해결책**: 거래관계관리(Trading Relationship Management) 시스템을 이원화(bifurcation)

- CORR(통신 청산) 및 QSR 관계 회원은 **야간 세션 전용 별도 승인 계약**을 설정·유지해야 함
- **2026년 3월 30일**부터 Automated Special Representative Facility를 통해 접근 가능
- 청산사가 **특정 고위험 고객에 대한 야간 청산 서비스를 명시적으로 승인 또는 거부** 가능
- 주간 핵심 관계에는 영향 없음

### 6.4 High-Value Trade Thresholds

야간 유동성 부족 시간대의 "팻 핑거(fat-finger)" 운영 오류, 폭주 알고리즘 거래 이상, 시장 조작 리스크를 완화하기 위해 정교하게 보정된 고액 거래 임계값이 적용된다.

| 세션 | 적용 거래 유형 | 임계값 | 시행일 |
|------|--------------|--------|--------|
| **야간 (OVN)** | CORR / OTC | **$1 Billion (10억 달러)** | 2026.6.28 (Phase 2) |
| **주간 (REG/PRE/PST)** | CORR / OTC | **$1.5 Billion (15억 달러)** | **2026.2.5~** |

이 이원적(bifurcated) 구조는 **유동성 조정 체계적 리스크 차단기(liquidity-adjusted systemic risk circuit breaker)** 접근법을 구현한다. 단일 오류 주문이 야간 디폴트 기금을 고갈시키는 것을 방지한다.

### 6.5 Intraday VaR 모니터링

배치 기반 거래에서 연속 거래로의 전환은, 일말(end-of-day) 리스크 루틴에서 **준연속적(near-continuous) 시장 감시**로의 전환을 필수적으로 요구한다.

**24/5 프레임워크의 VaR 모니터링 체계**:

```
┌─────────────────────────────────────────────────────────┐
│              Intraday VaR 모니터링 아키텍처               │
│                                                         │
│   거래 수집 ──→ 포트폴리오 리스크 프로파일                │
│        │          │                                     │
│        │          ▼                                     │
│        │    15분 주기 재계산 ←── VaR 모델                │
│        │          │                 (MRD 차지 포함)      │
│        │          ▼                                     │
│        │    임계값 위반 감지                              │
│        │          │                                     │
│        │    ┌─────┴─────┐                               │
│        │    │ 정상 범위  │ 초과 변동성/방향성 노출/       │
│        │    │ → 계속    │ 글로벌 시장 악화               │
│        │    └───────────┘    │                          │
│        │                     ▼                          │
│        │              동적 마진콜 발동                    │
│        │              (추가 담보 즉시 요구)               │
│        │                     │                          │
│        │                     ▼                          │
│        └──────── 회원사 담보 충당 ──→ 디폴트 기금 보호    │
└─────────────────────────────────────────────────────────┘
```

- Good Night 메시지 이전 수신 거래: SOD(Start-of-Day) 증거금 계산에 통합
- Good Night 전후 야간 거래: NSCC의 장중(intraday) UTC 모니터링 프로토콜로 포착
- NSCC는 **증거금 콜 임계값을 동적으로 낮출 수 있는 명시적 규제 재량권** 보유
- 전통적 미국 개장 전에 발생하는 이상 가격 변동에 대해 CCP의 완전 담보화 유지

---

## 7. 기술 인프라 요건

### 7.1 FIX/MQ 프로토콜 준수

24/5 환경에 참여하는 모든 기관은 DTCC의 현대화된 FIX 메시징 및 MQ 프로토콜 표준을 준수해야 한다. 핵심 요건:

| 요건 | 세부 사항 |
|------|-----------|
| FIX Tag 715 통합 | Clearing Business Date의 정확한 수신·해석·하위 시스템 전파 |
| FIX Tag 336 사용 | PRE/REG/PST/OVN 값을 통한 세션 시간대 분류 (최대 3자) |
| Good Night 메시지 처리 | 수신·검증·응답의 순차적 처리 |
| 세션 리사이클링 | 연결 해제·재접속·시퀀스 넘버 리셋의 무손실 수행 |
| UTCO 피드 처리 | 실시간 출력 메시지의 비동기적 Trade Date/CBD 정확 파싱 |

### 7.2 PSE 시뮬레이션 인증 필수

**UTCO 수신 기관**: 새로운 FIX 태그가 포함된 시뮬레이션 테스트 스크립트를 수집하고 성공적으로 처리하여, 내부 파싱 로직과 하위 회계 데이터베이스가 비동기 거래·청산 날짜에 대해 치명적 실패나 자본 오배분을 일으키지 않음을 확인해야 한다.

**송신 기관(ATS, 거래소, 집행 브로커)**: 포괄적 엔드투엔드 시뮬레이션을 수행해야 하며, 다음을 명시적으로 증명해야 한다:
1. 거래의 정확한 시퀀싱 능력
2. Good Night 메시지의 정확한 처리
3. 패킷 손실 없는 FIX 세션 리사이클
4. 후속 처리일을 위한 원활한 재접속

### 7.3 인증 실패 시 야간 세션 참여 불가

NSCC 통합팀(Integration Team)에 이러한 프로세스를 공식 인증하지 못한 기관은 **야간 세션 참여가 기술적으로 차단**된다. 이는 국지적 운영 장애로부터 광범위한 시장을 보호하기 위한 조치이다. 연속 시장의 궁극적 성공은 체인에서 **가장 약한 기술적 연결 고리의 복원력**에 달려 있다.

---

## 8. KRX/KSD 적용 시사점

한국거래소(KRX)는 현재 전략적으로 중대한 변곡점에 위치하고 있다. 한국 정부가 "코리아 디스카운트" 해소를 위해 외국인 투자자 접근성 강화, 공시 개선, 자본 효율성 향상을 추진하는 가운데, 글로벌 24시간 거래 전환 흐름을 무시할 수 없다. 2025년 3월 넥스트레이드(Nextrade)의 성공적 출범은 국내 경쟁 환경을 근본적으로 변화시키고 있다.

### 8.1 KSD 로컬 FIX Tag 715 등가물 개발

연속 거래에서 가장 심각한 체계적 리스크는 **일일 복식부기 원장의 손상**이다.

**권고사항**: KRX와 KSD는 DTCC의 FIX Tag 715 및 "Good Night" 메시지 프로토콜에 대한 **자체적(proprietary), 현지화된 등가 시스템**을 공동 개발해야 한다.

- KRX가 한국시간(KST) 02:00에 야간 세션을 운영할 경우, 해당 체결 거래는 전일 결제 배치에 포함될 수 없음
- **일일 기술 일시정지**(예: 30분 유지보수 윈도우) 동안 KSD가 청산일 확정, SOD 증거금 산출, 암호학적 "End-of-Day" FIX 메시지 방송 수행
- 이 신호 이후 체결된 모든 거래는 자동으로 **전진 일자 Clearing Business Date** 배정

### 8.2 비동기 Opt-in 청산 관계 (KSD 디지털 관계 관리)

**핵심 마찰점**: 국내 증권업계 노동조합의 야간 업무 부담, 시스템 모니터링, 야간 인력 배치 요건에 대한 강한 반발

**권고사항**: NSCC의 별도 9A/9B 관계와 유사한 **세분화된 승인 인프라** 도입

- KSD는 **디지털 관계 관리 시설(digital relationship management facility)** 배포
- 청산 브로커가 **고객별(client-by-client) 기준으로 야간 청산에 대해 명시적 opt-in/opt-out** 가능
- 런던 소재 외국인 기관투자자가 DMA 알고리즘으로 KST 04:00에 한국 주식 거래 시, 서울의 국내 청산 브로커에 해당 시간대 리스크를 명시적으로 승인하는 별도 자동화 계약 필요
- KSD에 야간 청산 승인이 등록되지 않은 주문은 KRX 매칭 엔진이 **사전 거부(pre-trade rejection)**
- 이를 통해 국내 브로커를 무자금 야간 노출로부터 보호하고, 한국 증권업계 전반의 24/7 수동 인력 배치 필요성 완화

### 8.3 유동성 조정 리스크 관리 (야간 30-50% 축소 임계값)

한국 시장의 심야 연속 거래는 필연적으로 심각한 유동성 분절(liquidity fragmentation)을 초래한다. 구조적으로 더 넓은 호가 스프레드와 가격 조작·플래시 크래시·알고리즘 오류에 대한 높은 취약성이 수반된다.

**권고사항**: **실시간 15분 주기 VaR 모니터링** + **비대칭 High-Value Thresholds** 배포

| 항목 | 세부 권고 |
|------|-----------|
| 데이터 흐름 | KRX 매칭 엔진 → KSD 청산소 간 마이크로초 지연시간으로 거래 데이터 전송 (배치 전송 폐기) |
| VaR 재계산 | KSD 연속 리스크 엔진이 15분마다 상대방 노출 재계산 (DTCC 프레임워크 직접 모사) |
| 야간 임계값 | **KST 18:00~08:00 시간대에 최대 주문 규모(High-Value Threshold) 30~50% 축소** |
| 자동 마진콜 | 야간 변동성으로 회원 노출이 VaR 임계값 위반 시 KSD 시스템이 자동화된 장중 마진콜 발행 |

### 8.4 Nextrade 교차 결제 (KSD 단일 진실점)

넥스트레이드가 완전 운영 ATS로 출범함에 따라, 우량 한국 주식의 유동성이 복수 시설에 걸쳐 분절될 것이다. 미국 생태계에서는 다수의 독립 ATS(MOON ATS, 24X National Exchange 등) 거래가 모두 DTCC의 중앙화된 UTC 시스템으로 유입되어, 체결 장소와 무관하게 브로커당 **단일 네팅 프로세스 및 단일 증거금 요건**이 산출된다.

**권고사항**: KSD가 KRX와 넥스트레이드 야간 체결 거래의 **단일 진실점(single point of truth)**으로 기능

- KSD는 KRX 매칭 엔진과 넥스트레이드 매칭 엔진에서 FIX 메시지를 **동시 수집**하도록 거래 수집 애플리케이션 업그레이드
- DTCC의 Tag 336(TradingSessionID)에 해당하는 **현지화 표준 FIX 메시지** 강제
- 예: KST 14:00 KRX 매수 포지션과 KST 20:00 넥스트레이드 매도 포지션의 수학적 상계 가능
- 포괄적 교차 시설 네팅으로 자본 효율성 극대화, 증거금 부담 대폭 감소

### 8.5 토큰화 자산/자동 유동성 풀 검토

야간 변동성으로 인한 마진콜 시 전통적 국내 은행 채널(BOK-Wire+ 등)이 운영 중단 상태일 수 있다. 결제 실패를 방지하기 위해 KSD는 **선진 담보 관리 프레임워크**를 모색해야 한다.

**검토 대상**:
- **토큰화 자산(tokenized assets)** 활용
- **자동 유동성 풀(automated liquidity pools)** 구축
- 상업은행 재무부서의 인적 개입 없이 **24/7 즉각적 증거금 담보 재배분** 가능한 시스템

---

## 9. SIP 확장 연동

### 9.1 SIP 운영시간 확장

SIP(Securities Information Processor)는 전국 시장 시스템(National Market System) 전반에 걸쳐 실시간 호가 및 거래 데이터를 통합·배포하는 핵심 인프라로, 가격 발견(price discovery)에 결정적 역할을 한다.

2025년 5월 6일, SIP 운영위원회(Operating Committees)는 SEC에 운영시간 확장 계획 수정안을 제출하여 NSCC의 제안 스케줄과 **정확히 일치하는 운영시간**을 확보하고자 했다.

| 항목 | 세부 사항 |
|------|-----------|
| **확장된 SIP 운영시간** | **일요일 20:00 ET ~ 금요일 20:00 ET** |
| **일일 기술 점검** | **20:00 ~ 21:00 ET (월~목)** |
| **점검 중 NSCC UTC** | 완전 운영 유지 (지연 거래 보고, ATS 체결, 내부 교차 네트워크 제출 수집·검증·보증) |

```
┌──────────────────────────────────────────────────────────────────┐
│                SIP / NSCC 동기화 운영 스케줄                       │
│                                                                  │
│  일 20:00 ET                                      금 20:00 ET   │
│  ┃                                                         ┃    │
│  ┃  SIP: ━━━━━╸20:00~21:00╺━━━━━━━━━━━━━━━━━━━━━━━━━━    ┃    │
│  ┃         (기술점검)  ↑ 매일 반복 (월~목)                    ┃    │
│  ┃                                                         ┃    │
│  ┃  NSCC UTC: ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    ┃    │
│  ┃           (연속 운영, 점검 중에도 온라인)                   ┃    │
│  ┃                                                         ┃    │
└──────────────────────────────────────────────────────────────────┘
```

### 9.2 주요 거래소 확장 계획

SIP 확장과 병행하여 주요 거래소들도 적극적으로 운영시간 확장을 추진하고 있다:
- **Nasdaq**: SEC에 23/5 미국 주식 거래 제안서 제출
- **NYSE**: 평일 거래를 22시간으로 확장하는 제안

이러한 거래소·SIP·NSCC의 삼중 동기화는 24/5 생태계의 원활한 가동을 위한 필수 전제 조건이다.

---

## 참고자료

1. APAC investors push for 24-hour trading in US markets - Financial Standard
   [financialstandard.com.au/news/apac-investors-push-for-...](https://www.financialstandard.com.au/news/apac-investors-push-for-24-hour-trading-in-us-markets-179810857)

2. 24x5 Trading: DTCC and EY Share Insights
   [dtcc.com/news/2025/december/04/dtcc-an...](https://www.dtcc.com/news/2025/december/04/dtcc-and-ey-share-insights-on-24x5-equity-trading)

3. Preparing US Equity Markets for 24x5 Trading - DTCC
   [dtcc.com/dtcctransformation/24x5](https://www.dtcc.com/dtcctransformation/24x5)

4. Implementing Overnight Financial Trading Strategy | TNS
   [tnsi.com/resource/fin/what-to-consider...](https://tnsi.com/resource/fin/what-to-consider-when-implementing-an-overnight-trading-strategy-blog/)

5. THE SHIFT TO 24X5 TRADING - DTCC
   [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/theshiftto24x5trading.pdf)

6. Crypto Matching Engine Guide: How It Impacts Your Trades - ChainUp
   [chainup.com/blog/crypto-matching-engine-g...](https://www.chainup.com/blog/crypto-matching-engine-guide/)

7. Equities Clearing Enhancements: UTC - 24/5 Extended Trading Hours - DTCC
   [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/UTC-24-x-5-Extended-Trading-Hours.pdf)

8. Important Notice - National Securities Clearing Corporation - DTCC
   [dtcc.com/-/media/Files/pdf/2025/1/30/A...](https://www.dtcc.com/-/media/Files/pdf/2025/1/30/A9551.pdf)

9. DTCC's NSCC to Increase Clearing Hours to Support Extended Trading
   [dtcc.com/news/2025/march/18/dtccs-nscc...](https://www.dtcc.com/news/2025/march/18/dtccs-nscc-to-increase-clearing-hours-to-support-extended-trading)

10. UNIVERSAL TRADE CAPTURE (UTC) 24x5 TRADE PROCESSING FAQ - DTCC
    [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/Universal-Trade-Capture-FAQs.pdf)

11. A9670 - DTCC
    [dtcc.com/-/media/Files/pdf/2025/11/5/A...](https://www.dtcc.com/-/media/Files/pdf/2025/11/5/A9670.pdf)

12. DTCC's NSCC To Increase Clearing Hours To Support Extended Trading - Financial IT
    [financialit.net/news/trading-systems/dtccs-ns...](https://financialit.net/news/trading-systems/dtccs-nscc-increase-clearing-hours-support-extended-trading)

13. DTCC unveils industry-wide testing phase for US equities 24/5 trading - The TRADE
    [thetradenews.com/dtcc-unveils-industry-wide-te...](https://www.thetradenews.com/dtcc-unveils-industry-wide-testing-phase-for-us-equities-24-5-trading/)

14. Extended Trading Hours - SIFMA
    [sifma.org/issues/market-structure/exten...](https://www.sifma.org/issues/market-structure/extended-trading-hours)

15. Extended Trading Hours: A New Frontier for US Equity Markets - SIFMA
    [sifma.org/news/blog/extended-trading-ho...](https://www.sifma.org/news/blog/extended-trading-hours-a-new-frontier-for-us-equity-markets)

16. The Future of U.S. Listed Options: Practical Steps Towards Continuous Trading
    [focus.world-exchanges.org/articles/future-us-listed-opt...](https://focus.world-exchanges.org/articles/future-us-listed-options)

17. 24x5 trading update - Important Notice
    [dtcc.com/-/media/Files/pdf/2026/1/7/A9...](https://www.dtcc.com/-/media/Files/pdf/2026/1/7/A9689.pdf)

18. NSCC to increase clearing hours - Asset Servicing Times
    [assetservicingtimes.com/assetservicesnews/clearingand...](https://www.assetservicingtimes.com/assetservicesnews/clearingandsettlementarticle.php?article_id=16545)

19. Universal Trade Capture (UTC) - DTCC Learning Center
    [dtcclearning.com/products-and-services/equitie...](https://dtcclearning.com/products-and-services/equities-clearing/utc.html)

20. UTC Overview - DTCC Learning Center
    [dtcclearning.com/products-and-services/equitie...](https://dtcclearning.com/products-and-services/equities-clearing/utc/1807-utc-overview.html)

21. Universal Trade Capture (UTC) 24x5 Trade Processing FAQ - DTCC
    [dtcc.com/initiatives//Content/1-utc_fa...](https://www.dtcc.com/initiatives//Content/1-utc_faqs/1_utc-faq.htm)

22. THE SHIFT TO 24X5 TRADING: WHAT IT MEANS FOR U.S. EQUITY MARKETS - DTCC
    [dtcc.com/-/media/Files/Downloads/Trans...](https://www.dtcc.com/-/media/Files/Downloads/Transformation/dtcc-24x5-Executive-Summary.pdf)

23. NSCC Important Notice - a7030 - REVISED August 23, 2010 - DTCC
    [dtcc.com/globals/pdfs/2010/july/21/a70...](https://www.dtcc.com/globals/pdfs/2010/july/21/a7030)

24. Frequently Asked Questions - The Future of Clearing & Securities Services | DTCC
    [dtcc.com/dtcctransformation/faqs](https://www.dtcc.com/dtcctransformation/faqs)

25. Understanding Settlement Cycles: What Does T+1 Mean for You? | FINRA.org
    [finra.org/investors/insights/understand...](https://www.finra.org/investors/insights/understanding-settlement-cycles)

26. 8 Things to Know About T+1 Settlement - Charles Schwab
    [schwab.com/learn/story/7-things-to-know-...](https://www.schwab.com/learn/story/7-things-to-know-about-t1-settlement)

27. JP Morgan US T+1 Securities Settlement FAQ
    [jpmorgan.com/insights/securities-services/...](https://www.jpmorgan.com/insights/securities-services/regulatory-solutions/us-t-plus-1securities-services-markets-faq)

28. NSCC Updates Universal Trade Capture for 24x5 Trading Expansion | Find Know Do
    [findknowdo.com/news/01/08/2026/nscc-updates-...](https://www.findknowdo.com/news/01/08/2026/nscc-updates-universal-trade-capture-24x5-trading-expansion)

29. NSCC Risk Margin Component Guide - DTCC Learning Center
    [dtcclearning.com/documents/equities-clearing/n...](https://dtcclearning.com/documents/equities-clearing/nscc-risk-management/risk-management-nscc/3992-nscc-risk-margin-component-guide.html)

30. Trends and Challenges in Extending Stock Market Trading Hours - KOREA CAPITAL MARKET INSTITUTE
    [kcmi.re.kr/en/publications/pub_detail_vi...](https://www.kcmi.re.kr/en/publications/pub_detail_view?syear=2025&zcd=002001017&zno=1878&cno=6647)

31. Trends and Challenges in Extending Stock Market Trading Hours (PDF)
    [kcmi.re.kr/common/downloadw](https://www.kcmi.re.kr/common/downloadw?fid=28428&fgu=002001&fty=004003)

32. Can Nextrade help cut the 'Korea discount'? - East Asia Forum
    [eastasiaforum.org/2025/05/31/can-nextrade-help-...](https://eastasiaforum.org/2025/05/31/can-nextrade-help-cut-the-korea-discount/)

33. FSC Grants Final Approval to Nextrade for Operation of ATS
    [fsc.go.kr/eng/pr010101/83967](https://www.fsc.go.kr/eng/pr010101/83967)

34. KRX Plans 24-Hour Trading and Virtual Asset Products | Bitget News
    [bitget.com/news/detail/12560605129090](https://www.bitget.com/news/detail/12560605129090)

35. A Milestone for Global Market Infrastructure in Seoul - World Federation of Exchanges
    [focus.world-exchanges.org/articles/krx-clearing](https://focus.world-exchanges.org/articles/krx-clearing)

36. KRX pushes for extended trading hours amid global 24-hour trading trend
    [koreatimes.co.kr/economy/20260116/krx-pushes-f...](https://www.koreatimes.co.kr/economy/20260116/krx-pushes-for-extended-trading-hours-amid-global-24-hour-trading-trend)

37. Technology Annual 2025 - Securities Finance Times
    [securitiesfinancetimes.com/sltimes/Tech%20Annual%202025....](https://www.securitiesfinancetimes.com/sltimes/Tech%20Annual%202025.pdf)

38. Legal & Regulatory - Legal Important Notices | DTCC
    [dtcc.com/legal/important-notices](https://www.dtcc.com/legal/important-notices?business=clearing-services)

---

> **본 보고서는 DTCC 공식 발간물, EY/DTCC 공동 백서, NSCC Important Notices, SIFMA 정책 브리프, KCMI 연구보고서 등 38개 1차 자료를 기반으로 작성되었습니다.**
