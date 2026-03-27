# ASX (Australian Securities Exchange) - References & Specifications

## 1. Trading Overview

- **[ASX Equities Trading](https://www.asx.com.au/markets/trade-our-cash-market/asx-equities-trading.html)** - ASX 주식 매매 개요 (Lit Markets, Centre Point, Auctions)
- **[ASX Order Controls](https://www.asx.com.au/markets/trade-our-cash-market/asx-equities-trading/order-controls)** - 주문 통제 메커니즘

## 2. Centre Point (Dark Pool)

- **[ASX Centre Point](https://www.asx.com.au/markets/trade-our-cash-market/asx-equities-trading/asx-centre-point.html)** - 호주 최대 다크풀 매칭 시스템 소개

## 3. Order Types

- **[ASX Trade New Order Types (PDF)](https://www.asx.com.au/documents/resources/asx_trade_new_order_types.pdf)** - ASX Trade 주문유형 안내

## 4. Operating Rules & Procedures

- **[ASX Operating Rules Procedures - Draft (PDF)](https://www.asx.com.au/documents/rules/Draft_ASX_Operating_Rules_procedures.pdf)** - ASX 운영규칙 절차 (드래프트)
- **[ASX Operating Rules Procedures - 2010 (PDF)](https://www.asx.com.au/documents/rules/asx_or_procedures.pdf)** - ASX 운영규칙 절차 (2010년)

## Key Notes

### ASX Trade 플랫폼
- Lit Markets, Centre Point, Auctions 통합 매매 플랫폼

### Centre Point Crossing
- 익명(anonymous) 다크풀 주문
- Day order 전용, 최소 주문 크기 없음
- 4자리 소수점 off-tick 체결 허용
- 크로스 개시 후 최대 30초간 활성 (CLOB 가격 변동과 무관)
- 체결 즉시 Course of Sales에 CXXT 코드로 보고

### 주요 주문유형
- **Fill-or-Kill (FOK)**: 전량 즉시 체결 또는 전량 취소
- **Good for Day (GFD)**: 당일 유효
- **Good-Till-Cancel (GTC)**: 취소 시까지 유효
- **Iceberg Order**: 대량 주문을 소량 자식 주문으로 분할 노출, 가격/시간 우선 적용

### 거래시간
- Pre-Open: 07:00~10:00 AEST
- Normal Trading: 10:00~16:00 AEST
- Closing Auction: 16:00~16:10 AEST
