# 09. Blue Ocean ATS — 미국 야간 대체거래시스템

## 1. 개요

Blue Ocean ATS는 미국 최초의 야간(overnight) 대체거래시스템(Alternative Trading System)으로, 미국 정규 거래 시간 이후인 동부시간 오후 8시부터 오전 4시까지 미국 NMS(National Market System) 주식의 거래를 가능하게 한다. 2019년 설립된 Blue Ocean Technologies LLC가 운영하며, 미국 주식 거래를 글로벌 거래로 전환하겠다는 미션 아래 아시아태평양, 중동 등 다양한 시간대 투자자들에게 미국 주식 접근성을 제공하고 있다.

---

## 2. Blue Ocean Technologies LLC 회사 개요

| 항목 | 상세 |
|------|------|
| 회사명 | Blue Ocean Technologies LLC (BOT) |
| 설립 | 2019년 |
| 본사 | 미국 |
| CEO | Brian Hyndman (2022년 5월 취임) |
| 핵심 서비스 | Blue Ocean ATS (야간 대체거래시스템) |
| 규제 등록 | SEC 등록 ATS, FINRA 회원 |
| 미션 | 미국 주식 거래를 글로벌 24시간 거래로 전환 |

### 설립 배경

Blue Ocean Technologies는 미국 정규 거래 시간(09:30~16:00 ET) 이후 시간대에 거래 인프라가 부재했던 공백을 메우기 위해 설립되었다. 특히 아시아태평양 지역의 현지 업무 시간(미국 야간)에 미국 주식을 거래할 수 있는 투명한 전자 거래 플랫폼이 필요하다는 인식에서 출발했다.

---

## 3. 운영 시간 및 거래 구조

### 3.1 Blue Ocean Session

| 항목 | 상세 |
|------|------|
| 거래 시간 | **20:00 ~ 04:00 ET** (동부시간) |
| 운영 요일 | **일요일 ~ 목요일** (주 5일) |
| 거래 대상 | 미국 NMS 상장 주식 전체 |
| 세션명 | Blue Ocean Session |

### 3.2 미국 주식 거래 시간대별 배치

| 시간대 (ET) | 세션 |
|------------|------|
| 04:00 ~ 09:30 | Pre-Market (프리마켓) |
| 09:30 ~ 16:00 | Regular Trading Hours (정규 거래) |
| 16:00 ~ 20:00 | After-Hours (애프터아워스) |
| **20:00 ~ 04:00** | **Blue Ocean Session (야간)** |

이를 통해 미국 주식은 사실상 **24시간 연속 거래**가 가능해졌다. 프리마켓(04:00)에서 Blue Ocean Session(04:00)까지 하루 전체가 커버된다.

### 3.3 아시아태평양 현지 시간 환산

| 지역 | Blue Ocean Session 시간 |
|------|----------------------|
| 한국 (KST) | 09:00 ~ 17:00 (겨울) / 10:00 ~ 18:00 (여름) |
| 일본 (JST) | 09:00 ~ 17:00 (겨울) / 10:00 ~ 18:00 (여름) |
| 홍콩 (HKT) | 08:00 ~ 16:00 (겨울) / 09:00 ~ 17:00 (여름) |
| 시드니 (AEDT) | 11:00 ~ 19:00 (겨울) / 12:00 ~ 20:00 (여름) |

아시아태평양 투자자들에게 Blue Ocean Session은 정확히 현지 업무 시간대에 해당하여, 미국 주식을 "낮 시간"에 거래할 수 있다.

---

## 4. 거래 규칙 및 메커니즘

### 4.1 지정가 주문 전용 (Limit Order Only)

| 항목 | 상세 |
|------|------|
| 주문 유형 | **지정가(Limit) 주문만 허용** |
| 시장가 주문 | 불가 |
| 이유 | 야간 시간대 낮은 유동성에서 투자자 보호 |
| 가격 범위 제한 | 기준 가격 대비 **±20% 가격 밴드** 적용 |

시장가 주문을 금지하고 지정가 주문만 허용함으로써, 유동성이 상대적으로 얇은 야간 시간대에 급격한 가격 변동으로부터 투자자를 보호한다.

### 4.2 매칭 시스템 (BOATS)

| 항목 | 상세 |
|------|------|
| 시스템명 | BOATS (Blue Ocean Alternative Trading System) |
| 매칭 방식 | 가격-시간 우선 (Price-Time Priority) |
| 가격 밴드 | 기준가 대비 ±20% |
| 대상 종목 | 미국 NMS 주식 전체 |

---

## 5. 청산 및 결제

### 5.1 청산/결제 인프라

| 항목 | 상세 |
|------|------|
| 청산 기관 | **NSCC (National Securities Clearing Corporation)** |
| 결제 기관 | **DTCC (Depository Trust & Clearing Corporation)** |
| 결제 주기 | T+1 (미국 표준) |
| 특징 | 미국 정규 거래소와 동일한 청산/결제 인프라 사용 |

Blue Ocean ATS의 거래는 NSCC/DTCC를 통해 청산 및 결제되므로, 정규 거래소(NYSE, Nasdaq) 거래와 동일한 수준의 결제 안전성을 보장한다. 이는 ATS의 신뢰성을 담보하는 핵심 요소이다.

---

## 6. 데이터 유통 및 기술 파트너십

### 6.1 Bloomberg Terminal 통합 (2025년 9월)

2025년 9월 29일, Blue Ocean Technologies는 Bloomberg과 협업하여 실시간 시장 데이터를 Bloomberg Terminal에서 제공하기 시작했다.

| 항목 | 상세 |
|------|------|
| 거래소 코드 | **"OC"** (Bloomberg Terminal) |
| 제공 데이터 | Level 1 (Top-of-Book) + Level 2 (Market Depth) |
| 유통 채널 | Bloomberg Terminal, B-PIPE (실시간 데이터 피드), Bloomberg Data License |
| 구독자 | 실시간 데이터, 비구독자는 15분 지연 데이터 |

### 6.2 NYSE Cloud Streaming 통합 (2025년 10월)

2025년 10월 7일, Blue Ocean Technologies의 실시간 야간 데이터가 NYSE Cloud Streaming에 통합되었다.

| 항목 | 상세 |
|------|------|
| 데이터 피드 | BOT Top of Book + Last Sale 실시간 데이터 |
| 유통 채널 | NYSE Cloud Streaming (NYSE BQT 피드와 병행) |
| 의의 | NYSE라는 전통적 거래소 인프라와의 연결 |

### 6.3 Pyth Network 파트너십

Blue Ocean ATS는 2025년 9월 Pyth Network에 마켓 데이터 제공자로 합류했다.

| 항목 | 상세 |
|------|------|
| 파트너 | Pyth Network (온체인 오라클) |
| 독점 기간 | 2026년 말까지 |
| 데이터 | 야간 미국 주식 거래 데이터를 온체인으로 퍼블리싱 |
| 의의 | DeFi/블록체인 생태계와 전통 금융시장의 연결 |

Pyth Network는 Blue Ocean ATS의 야간 미국 주식 데이터를 온체인에 퍼블리싱하는 유일한 데이터 배포자로, 2026년 말까지 독점 파트너십을 유지한다.

### 6.4 기타 데이터 유통 파트너

| 파트너 | 유형 |
|--------|------|
| ICE (Intercontinental Exchange) | 데이터 벤더 |
| LSEG (Refinitiv) | 데이터 벤더 |
| TradingView | 차트/데이터 플랫폼 |

---

## 7. 거래량 및 성장 지표

### 7.1 주요 거래량 지표

| 지표 | 수치 | 시점 |
|------|------|------|
| 일평균 명목 거래대금 | **$1.2B+ (약 1.6조 원)** | 2025년 8월 |
| 역대 최고 일일 거래대금 | 기록 갱신 | 2025년 4월 7일 |
| 야간 보고 거래대금 | 약 $1B/야간 | 2025년 기준 |

### 7.2 성장 추이

Blue Ocean ATS는 2019년 설립 이후 지속적으로 거래량이 증가하고 있으며, 특히 2024~2025년 글로벌 야간 거래 수요 급증과 함께 폭발적 성장세를 보이고 있다. 2025년 8월 기준 일평균 $1.2B 이상의 명목 거래대금을 기록했다.

---

## 8. 브로커 파트너십

### 8.1 주요 브로커/기관 파트너

| 파트너 | 유형 | 파트너십 시기 |
|--------|------|-------------|
| **Robinhood** | 리테일 브로커 | — |
| **Charles Schwab** | 리테일/기관 브로커 | — |
| **Interactive Brokers** | 글로벌 브로커 | — |
| **삼성증권 (Samsung Securities)** | 한국 증권사 | **2022년 2월** |
| **Virtu Financial** | 마켓 메이커/트레이딩 펌 | — |
| **Jane Street** | 퀀트 트레이딩 펌 | — |
| **Score Priority Corp.** | 브로커 | — |
| **Firstrade** | 리테일 브로커 | 2025년 2월 |
| **Clear Street** | 프라임 브로커 | 2025년 3월 |

### 8.2 기술/인프라 파트너

| 파트너 | 유형 | 통합 시기 |
|--------|------|----------|
| FlexTrade | OMS/EMS 벤더 | — |
| LiquidityBook | 거래 기술 플랫폼 | 2025년 |
| Broadridge (NYFIX) | 주문 라우팅 네트워크 | 2022년 |
| GTN | 글로벌 핀테크 | 2024년 3월 |

### 8.3 삼성증권 파트너십 상세

2022년 2월 7일, Blue Ocean Technologies와 삼성증권은 MOU를 체결하여 전략적 파트너십을 구축했다.

| 항목 | 상세 |
|------|------|
| 서비스 개시 | 2022년 2월 6일 (미국 ET 기준) |
| 서비스명 | 미국 주식 주간 거래 서비스 |
| 한국 거래 시간 | 10:00 ~ 18:00 KST |
| 역사적 의의 | **세계 최초로 한국 현지 업무 시간에 미국 주식 거래 개시** |
| 일일 거래 가능 시간 | 20시간 30분 (애프터아워스 종료 3시간 후 ~ 프리마켓 시작 30분 전) |

삼성증권은 Blue Ocean ATS를 통해 한국에서 유일하게 미국 주식의 "주간 거래"를 제공하는 증권사가 되었으며, 이는 한국 투자자들의 미국 주식 접근성을 혁신적으로 개선했다.

---

## 9. KRX 및 한국 시장과의 비교 및 시사점

### 9.1 Blue Ocean ATS vs Nextrade 비교

| 항목 | Blue Ocean ATS | Nextrade (한국) |
|------|---------------|----------------|
| 유형 | 미국 ATS (야간 전문) | 한국 ATS (시간외 거래 포함) |
| 거래 대상 | 미국 NMS 주식 | 한국 상장 주식 |
| 시간외 거래 시간 | 20:00~04:00 ET (8시간) | 08:00~08:50 + 15:30~20:00 (5.3시간) |
| 주문 유형 | 지정가 전용 | 지정가 전용 (시간외) |
| 청산 | NSCC/DTCC | 한국예탁결제원 |
| 시장 점유율 | 미국 야간 거래의 지배적 점유율 | 약 30%+ (2025년 7월) |
| 출범 | 2019년 | 2025년 3월 |

### 9.2 한국 투자자에 대한 영향

| 영향 영역 | 상세 |
|----------|------|
| 미국 주식 접근성 | 삼성증권 등을 통해 한국 업무 시간에 미국 주식 거래 가능 |
| 리스크 관리 | 미국 장 마감 후 발생하는 이벤트에 즉각 대응 가능 |
| 글로벌 포트폴리오 | 24시간에 가까운 미국 주식 거래로 글로벌 분산투자 편의성 향상 |
| 시차 문제 해소 | 한국 투자자의 미국 주식 거래 시 야간 거래 부담 대폭 감소 |

### 9.3 KRX에 대한 시사점

1. **ATS 시간외 거래의 글로벌 추세**: Blue Ocean ATS의 성공은 야간/시간외 거래에 대한 글로벌 수요가 실재함을 입증한다. KRX도 Nextrade와의 경쟁에서 시간외 거래 확대가 불가피하다.

2. **지정가 전용 정책의 타당성**: Blue Ocean ATS의 지정가 전용 정책은 유동성이 낮은 시간대의 투자자 보호에 효과적임이 검증되었다. KRX/Nextrade의 시간외 거래에서도 유사한 투자자 보호 장치가 필요하다.

3. **데이터 유통의 중요성**: Bloomberg, NYSE Cloud Streaming, Pyth Network 등 다양한 채널을 통한 데이터 유통은 시장의 투명성과 신뢰성을 높인다. 한국 시장도 시간외 거래 데이터의 글로벌 유통을 확대할 필요가 있다.

4. **글로벌 브로커 네트워크**: Robinhood, Schwab, Interactive Brokers 등 글로벌 브로커와의 파트너십은 유동성의 핵심이다. 한국 시장의 해외 투자자 접근성 확대에도 유사한 전략이 필요하다.

5. **블록체인/DeFi 연결**: Pyth Network와의 파트너십은 전통 금융과 분산 금융의 융합이라는 새로운 패러다임을 보여준다. 한국 시장도 블록체인 기반 데이터 유통 및 토큰화된 증권(STO) 인프라 구축을 가속화해야 한다.

6. **삼성증권의 선제적 행보**: 삼성증권이 Blue Ocean ATS의 첫 해외 파트너가 된 것은 한국 증권업의 글로벌 혁신 역량을 보여준다. 이러한 파트너십 모델을 다른 한국 증권사들도 확대 적용할 수 있다.

---

## 10. 참고 자료

- Blue Ocean Technologies 공식: [blueocean-tech.io/](https://blueocean-tech.io/)
- Blue Ocean ATS 개요: [blueocean-tech.io/blue-ocean-ats/](https://blueocean-tech.io/blue-ocean-ats/)
- Blue Ocean ATS FAQ: [blueocean-tech.io/faq/](https://blueocean-tech.io/faq/)
- Bloomberg 통합 발표: [blueocean-tech.io/2025/09/30/pr-newswire-blue-o...](https://blueocean-tech.io/2025/09/30/pr-newswire-blue-ocean-technologies-real-time-overnight-trading-data-now-available-via-bloomberg-solutions/)
- NYSE Cloud Streaming 통합: [blueocean-tech.io/2025/10/07/pr-newswire-blue-o...](https://blueocean-tech.io/2025/10/07/pr-newswire-blue-ocean-technologies-integrates-real-time-overnight-data/)
- Pyth Network 파트너십: [pyth.network/blog/blue-ocean-ats-joins-pyt...](https://www.pyth.network/blog/blue-ocean-ats-joins-pyth-network-institutional-overnight-hours-us-equity-data)
- 삼성증권 파트너십: [blueocean-tech.io/2022/02/08/partnership-with-s...](https://blueocean-tech.io/2022/02/08/partnership-with-samsung-securities-offering-us-equity-trading-during-asia-pacific-business-hours/)
- Firstrade 파트너십: [firstrade.com/press/20250212](https://www.firstrade.com/press/20250212)
- MarketsWiki 프로필: [marketswiki.com/wiki/Blue_Ocean_ATS](https://www.marketswiki.com/wiki/Blue_Ocean_ATS)
- LiquidityBook 통합 (The TRADE): [thetradenews.com/liquiditybook-leverages-blue-...](https://www.thetradenews.com/liquiditybook-leverages-blue-ocean-ats-to-extend-overnight-trading/)
- NYSE Cloud Streaming (Yahoo Finance): [finance.yahoo.com/news/blue-ocean-technologies-...](https://finance.yahoo.com/news/blue-ocean-technologies-integrates-real-123000633.html)
- Bloomberg 통합 (PR Newswire): [prnewswire.com/news-releases/blue-ocean-tech...](https://www.prnewswire.com/news-releases/blue-ocean-technologies-real-time-overnight-trading-data-now-available-via-bloomberg-solutions-302569666.html)
