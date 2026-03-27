# 07. 런던증권거래소 (London Stock Exchange / LSEG)

## 1. 개요

런던증권거래소(London Stock Exchange, LSE)는 1801년 공식 설립된 세계에서 가장 오래된 증권거래소 중 하나로, 현재 런던증권거래소그룹(London Stock Exchange Group, LSEG)의 핵심 거래소로 운영되고 있다. LSEG는 단순한 거래소를 넘어 데이터, 분석, 청산, 결제까지 아우르는 글로벌 금융 인프라 기업으로 성장했다.

### 주요 재무 지표 (2025~2026)

| 항목 | 수치 |
|------|------|
| 연간 매출 (2025년 12월 기준) | 약 $12.3B (약 16조 원) |
| 시가총액 (2026년 2월 기준) | 약 $58.1B (약 76조 원) |
| 주가 (2026년 2월 26일) | $115.24 |
| 발행주식수 | 약 5.04억 주 |
| 임직원 수 | 약 25,000명 이상 |

---

## 2. LSEG 그룹 구조

LSEG는 크게 세 가지 핵심 사업 부문으로 구성된다.

### 2.1 데이터 & 애널리틱스 (Data & Analytics) — 매출 비중 약 70%

| 사업부 | 주요 기능 |
|--------|----------|
| Refinitiv | 실시간 시장 데이터, 뉴스, 거래 플랫폼 (Eikon/Workspace) |
| FTSE Russell | 글로벌 지수 산출 (FTSE 100, FTSE All-Share, Russell 2000 등) |
| Risk Intelligence | World-Check 등 컴플라이언스/리스크 관리 솔루션 |

2021년 Refinitiv 인수(약 $27B)를 통해 LSEG는 데이터 사업 비중을 대폭 확대하였으며, Bloomberg Terminal과 경쟁하는 Workspace 플랫폼을 운영하고 있다.

### 2.2 자본시장 / 거래 (Capital Markets / Trading)

| 거래소/플랫폼 | 설명 |
|--------------|------|
| London Stock Exchange (LSE) | 영국 주요 주식 거래소, Main Market 및 AIM 운영 |
| Turquoise | 범유럽 다자간 거래 시설(MTF), 다크풀 포함 |
| LSEG FX | 외환 거래 플랫폼 (FXall 포함) |
| Tradeweb | 채권, 파생상품 전자거래 플랫폼 (LSEG 지분 보유) |

### 2.3 포스트 트레이드 (Post Trade)

| 사업부 | 주요 기능 |
|--------|----------|
| LCH Group | 글로벌 중앙청산소(CCP), 금리스왑 청산 세계 1위 |
| Acadia | 마진 관리, 담보 관리 |
| Quantile | 포트폴리오 압축, 자본 최적화 |

#### 2025년 포스트 트레이드 사업부 은행 투자

2025년 Q3 실적 발표와 함께, LSEG는 Post Trade Solutions 사업부의 20% 지분을 11개 글로벌 은행(Bank of America, Barclays, BNP Paribas, Citi, Deutsche Bank, HSBC, J.P. Morgan, Morgan Stanley, Nomura, Societe Generale, UBS)에 매각했다. 해당 사업부 기업가치는 약 £850M(약 1.4조 원)으로 평가되었다.

SwapClear 수익 배분 구조도 변경되어, 창립 은행들의 수익 배분 비율이 2025년 30%에서 15%로, 2026년에는 10%로 축소되며, LSEG가 이에 대해 2년간 £1.15B를 지급하고 성과 연동 추가 £200M을 지불하기로 했다.

---

## 3. Turquoise — 범유럽 거래 플랫폼

### 3.1 역사와 구조

Turquoise는 2008년 주요 투자은행들이 공동 설립한 다자간 거래 시설(MTF)로, 2009년 12월 LSE가 60% 지분을 인수하면서 LSEG 산하로 편입되었다. 기존 LSE의 Baikal Global 거래 시설과 통합 운영된다.

### 3.2 주요 서비스

| 서비스 | 설명 |
|--------|------|
| Turquoise Lit | 공개 주문장(lit order book) 기반 거래 |
| Turquoise Plato | 대형 블록 거래용 다크풀(dark pool) |
| Turquoise Plato Block Discovery | 기관 투자자 간 대량 거래 매칭 |
| Turquoise Plato Uncross | 정기적 경매 기반 거래 |

### 3.3 유럽 운영

EU 내에서 LSEG는 다음과 같은 금융 인프라를 운영한다:
- **프랑스**: LCH S.A., BeyonRatings
- **네덜란드**: Turquoise Europe, Regulatory Reporting, Quantile
- **아일랜드**: Refinitiv MTF, FXAll

---

## 4. 거래 시간 및 세션 구조

### 4.1 LSE 거래 시간표

| 세션 | 시간 (GMT/BST) | 설명 |
|------|---------------|------|
| 프리 트레이딩 (Pre-Trading) | 05:05 ~ 07:50 | 주문 입력/수정/취소만 가능, 실제 체결 없음 |
| 개장 경매 (Opening Auction) | 07:50 ~ 08:00 | 주문 수집 후 단일가 매매 |
| 연속 거래 (Continuous Trading) | 08:00 ~ 16:30 | SETS 기반 연속 매매 |
| 폐장 경매 (Closing Auction) | 16:30 ~ 16:35 | 종가 결정을 위한 단일가 매매 |
| 포스트 트레이딩 (Post-Trading) | ~17:15까지 | 미체결 주문 처리, 포지션 정리 |

### 4.2 경매(Auction) 시스템

LSE는 세 가지 유형의 경매를 운영한다:

1. **개장 경매 (Opening Auction, 1997년 도입)**: 장 시작 전 주문을 수집하여 단일 가격으로 체결
2. **폐장 경매 (Closing Auction, 2000년 도입)**: 종가 결정의 투명성을 위해 도입
3. **장중 경매 (Intra-day Auction, 2016년 도입)**: 가격 변동성 관리를 위한 추가 경매

경매에서 신뢰할 수 있는 가격이 형성되지 않을 경우, Price Monitoring Extension이 자동으로 발동되어 호가 수집 기간이 5분씩 최대 2회 연장된다.

---

## 5. SETS / SETSqx 매칭 시스템

### 5.1 SETS (Stock Exchange Electronic Trading Service)

SETS는 LSE의 핵심 전자 주문 매칭 시스템으로, FTSE 100, FTSE 250을 포함한 유동성이 높은 종목을 처리한다.

| 특성 | 상세 |
|------|------|
| 거래 방식 | 연속 양방향 경매(continuous double auction) |
| 거래 시간 | 08:00 ~ 16:30 GMT |
| 대상 종목 | FTSE 100, FTSE 250, 주요 ETF, GDR 등 |
| 주문 유형 | 지정가, 시장가, 빙산(iceberg), 숨김(hidden) 주문 등 |

### 5.2 SETSqx (Stock Exchange Electronic Trading Service — Quotes and Crosses)

SETSqx는 유동성이 낮은 종목을 위한 하이브리드 거래 시스템으로, 정기 경매와 마켓 메이커의 연속 호가를 결합한다.

| 특성 | 상세 |
|------|------|
| 거래 방식 | 정기 경매 + 마켓 메이커 호가 |
| 경매 시간 | 08:00, 09:00, 11:00, 14:00, 16:30 (2014년 도입) |
| 대상 종목 | AIM 종목, 소형주 등 저유동성 종목 |
| 마켓 메이커 | 등록 마켓 메이커가 스프레드 의무와 함께 양방향 확정 호가 제공 |

SETSqx의 정기 경매는 유동성이 얇아 실제 참여가 활발하지 않은 경우가 많다.

### 5.3 SEAQ (Stock Exchange Automated Quotations)

SEAQ는 가장 유동성이 낮은 종목을 위한 순수 마켓 메이커 기반 호가 시스템이다.

---

## 6. Millennium Exchange 기술 플랫폼

### 6.1 도입 배경

LSE는 기존 TradElect 시스템의 성능 한계를 극복하기 위해 새로운 매칭 엔진을 모색했다. 자체 개발 대신 2009년 스리랑카 소재 MillenniumIT를 £18M에 인수하여 Linux 기반 Millennium Exchange 플랫폼을 도입했다.

### 6.2 기술 사양

| 항목 | 사양 |
|------|------|
| 운영체제 | Linux 기반 |
| 지연시간(Latency) | 126 마이크로초 (2010년 세계 기록) |
| 아키텍처 | 수평 확장 가능한 분산 처리 |
| 주요 특징 | 서브 밀리초(sub-millisecond) 거래 속도 |

2010년 10월, Turquoise 다크풀에서 126 마이크로초 거래 속도를 기록하며 당시 세계 최고 속도를 달성했다.

### 6.3 글로벌 판매

Millennium Exchange 플랫폼은 LSE 외에도 다수의 글로벌 거래소에 판매되었다:
- BYMA (아르헨티나)
- 요하네스버그 증권거래소 (남아프리카공화국)
- 리마 증권거래소 (페루)

---

## 7. LCH 청산 및 결제

### 7.1 LCH 그룹 구조

LCH는 세계 최대의 금리스왑(Interest Rate Swap) 청산 기관으로, LSEG가 과반 지분을 보유하고 있다.

| 법인 | 관할 | 주요 청산 자산 |
|------|------|--------------|
| LCH Ltd | 영국 | 주식, 채권, FX, 금리, 레포 |
| LCH SA | 프랑스/EU | CDS, CDS 옵션, 레포, 채권, 디지털 자산 |

### 7.2 청산 대상 자산 클래스 (7개)

| 자산 클래스 | 서비스명 |
|------------|---------|
| 금리스왑 | SwapClear |
| 신용부도스왑(CDS) | CDSClear |
| 주식 | EquityClear |
| 채권 | RepoClear |
| 외환(FX) | ForexClear |
| 상장 파생상품 | Listed Derivatives Clearing |
| 디지털 자산 | Digital Asset Clearing |

SwapClear는 글로벌 금리스왑 시장의 지배적인 청산 서비스로, 은행 부도 시 시장 전체의 붕괴를 방지하는 금융 시스템의 핵심 인프라 역할을 수행한다.

### 7.3 영국 T+1 결제 전환 계획 (2027년)

| 시기 | 주요 내용 |
|------|----------|
| 2022년 12월 | 영국 재무장관, 결제 가속화 태스크포스(AST) 출범 |
| 2024년 3월 | AST 보고서: 2027년 말까지 T+1 전환 권고 |
| 2025년 2월 | 기술그룹 보고서 발간 (12개 '필수' + 26개 '강력 권고' 조치) |
| 2025년 | 계획 수립 및 예산 편성 단계 |
| 2026년 | 솔루션 구축 및 구현 단계 |
| 2027년 10월 11일 | **T+1 결제 공식 시행일** |

영국의 T+1 전환은 EU 및 스위스와 동일한 날짜(2027년 10월 11일)로 조율되었다. 이는 미국이 2024년 5월 이미 T+1을 시행한 것에 대응하는 조치이다.

현재 Euroclear UK & International의 CREST 시스템이 결제를 담당하고 있으며, 영국 국채(Gilts)는 이미 T+1로 결제되고 있다. 2025년 Q3 설문조사에 따르면 95%의 금융사가 T+1 전환 준비에 착수했다.

---

## 8. 거래 시간 연장 논의

### 8.1 24시간 거래 검토

LSEG는 영국 상장 주식의 24시간 거래를 가능하게 하는 급진적인 계획을 검토 중이다. CEO David Schwimmer은 런던 시장의 매력을 높이기 위한 의지를 지속적으로 표명해왔다.

### 8.2 추진 배경

| 요인 | 상세 |
|------|------|
| 리테일 투자자 수요 | 미국에서 Gen Z 세대의 스마트폰 기반 장외 시간 거래 증가 |
| 암호화폐 경쟁 | 24/7 거래되는 암호화폐 시장과의 경쟁 |
| 영국 시장 침체 | 거래량 감소, 신규 상장 부족 |
| 글로벌 경쟁 | NYSE, Nasdaq, Cboe 등 미국 거래소들의 시간 연장 추진 |

### 8.3 과제와 반대 의견

- **종가 기준 문제**: 기관 투자자들이 종가를 기준으로 펀드 가치를 산정하는데, 24시간 거래 시 종가 설정이 복잡해짐
- **유동성 분산**: 장외 시간대의 낮은 유동성으로 인한 급격한 가격 변동 우려
- **성과 측정**: 24/7 데이터로 인한 포트폴리오 성과 측정의 복잡성 증가
- **규제 조율**: 영국 FCA 등 규제 기관과의 협의 필요

### 8.4 타임라인

LSEG는 아직 24시간 거래의 구체적인 일정을 확인하지 않았으나, 유럽 및 영국에서 최초로 24시간 거래를 도입하는 거래소가 될 가능성이 있다. 기술적, 규제적 함의를 면밀히 검토 중이다.

---

## 9. KRX와의 비교

### 9.1 기본 구조 비교

| 항목 | LSE / LSEG | KRX |
|------|-----------|-----|
| 설립 | 1801년 | 2005년 (통합) |
| 그룹 구조 | LSEG (데이터 70% + 거래 + 포스트트레이드) | KRX (유가증권 + 코스닥 + 파생상품) |
| 매칭 시스템 | Millennium Exchange (126μs) | EXTURE 3.0 (50µs) |
| 청산 기관 | LCH (별도 법인, 다자산 클래스) | KRX 자체 청산 |
| 결제 주기 | T+2 → T+1 (2027.10) | T+2 |
| 시가총액 | 약 $3.4T (FTSE All-Share) | 약 $1.8T (KOSPI + KOSDAQ) |

### 9.2 거래 시간 비교

| 항목 | LSE | KRX |
|------|-----|-----|
| 정규 거래 시간 | 08:00~16:30 GMT (8.5시간) | 09:00~15:30 KST (6.5시간) |
| 개장 경매 | 07:50~08:00 | 08:30~09:00 (동시호가) |
| 폐장 경매 | 16:30~16:35 | 15:20~15:30 (동시호가) |
| 시간외 거래 | 프리/포스트 트레이딩 세션 | 시간외 종가매매, 시간외 단일가매매 |
| 24시간 거래 논의 | LSEG 24시간 거래 플랫폼 검토 중 | Nextrade ATS 등장으로 12시간 거래 검토 |

### 9.3 경쟁 환경 비교

| 항목 | LSE | KRX |
|------|-----|-----|
| 대체 거래소 | Turquoise, Cboe Europe, Aquis | Nextrade (2025년 3월 출범) |
| ATS 시장 점유율 | Turquoise 등 MTF가 상당 점유율 보유 | Nextrade가 빠르게 30% 이상 점유율 확보 |
| 대응 전략 | 24시간 거래 검토 | 12시간 거래(08:00~20:00) 검토 |

### 9.4 시사점

1. **데이터 사업의 중요성**: LSEG 매출의 70%가 데이터/분석에서 발생하는 점은 KRX에도 중요한 시사점을 제공한다. KRX도 시장 데이터의 상업적 가치를 극대화할 필요가 있다.

2. **독립적 청산 기관**: LCH는 다자산 클래스 글로벌 청산을 수행하는 반면, KRX는 자체 청산을 수행한다. 글로벌 상호운용성 측면에서 KRX 청산 시스템의 개방성 확대를 검토할 필요가 있다.

3. **T+1 전환 대비**: 영국, EU, 스위스가 2027년 10월 T+1로 동시 전환 예정이므로, 한국도 글로벌 정합성을 고려한 결제 주기 단축을 검토해야 한다.

4. **거래 시간 연장 경쟁**: LSE가 24시간 거래를 검토하고, KRX가 Nextrade에 대응하여 12시간 거래를 검토하는 것은 글로벌적으로 거래 시간 연장이 불가피한 추세임을 보여준다.

---

## 10. 참고 자료

- LSEG 그룹 구조: [lseg.com/en/post-trade/clearing/about-...](https://www.lseg.com/en/post-trade/clearing/about-lch/structure-and-governance/company-structure)
- LSEG Wikipedia: [en.wikipedia.org/wiki/London_Stock_Exchange_Gr...](https://en.wikipedia.org/wiki/London_Stock_Exchange_Group)
- Millennium Exchange: [en.wikipedia.org/wiki/Millennium_Exchange](https://en.wikipedia.org/wiki/Millennium_Exchange)
- SETS/SETSqx 설명: [shiftingshares.com/sets-setsqx-seaq/](https://www.shiftingshares.com/sets-setsqx-seaq/)
- LSE 거래 시간: [tradinghours.com/markets/lse](https://www.tradinghours.com/markets/lse)
- LSE 경매 설명: [aim-watch.com/project/lse-auctions-explaine...](https://aim-watch.com/project/lse-auctions-explained/)
- LSE 24시간 거래 검토: [fstech.co.uk/fst/London_Stock_Exchange_Con...](https://fstech.co.uk/fst/London_Stock_Exchange_Considers_24_Hour_Trading.php)
- LSEG 24시간 거래 (The TRADE): [thetradenews.com/is-lseg-set-to-become-first-v...](https://www.thetradenews.com/is-lseg-set-to-become-first-venue-to-move-to-24-hour-in-europe-and-the-uk/)
- 영국 T+1 전환: [gov.uk/government/publications/accel...](https://www.gov.uk/government/publications/accelerated-settlement-t1)
- UK T+1 최종 계획: [acceleratedsettlement.co.uk/](https://acceleratedsettlement.co.uk/)
- UK T+1 2027년 10월: [grip.globalrelay.com/uk-will-move-to-t1-cycle-for-...](https://www.grip.globalrelay.com/uk-will-move-to-t1-cycle-for-securities-settlement-from-october-2027/)
- LCH 청산 서비스: [lseg.com/en/post-trade/clearing](https://www.lseg.com/en/post-trade/clearing)
- KRX 12시간 거래 검토: [koreaherald.com/article/10548345](https://www.koreaherald.com/article/10548345)
- Nextrade 승인: [fsc.go.kr/eng/pr010101/83967](https://www.fsc.go.kr/eng/pr010101/83967)
