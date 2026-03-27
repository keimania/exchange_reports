# KRX (한국거래소) — Exchange Report

---

## 1. Exchange Overview

**Full Legal Name**: Korea Exchange (한국거래소, KRX)
**Country**: Republic of Korea
**Founding Year**: 2005 (formed by merger of Korea Stock Exchange, KOSDAQ Stock Market, and Korea Futures Exchange) [REF:#4]
**Parent Group**: Self-regulatory organization under the Financial Services Commission (FSC) [REF:#4]

**Market Model**: Pure order-driven market with price-time priority matching [REF:#1]

**Asset Classes Traded**: [REF:#4] [REF:#8]
- Equities (KOSPI, KOSDAQ, KONEX)
- Derivatives (futures and options on indices, single stocks, currencies, interest rates, commodities)
- Bonds (government bonds, corporate bonds, REPO)
- ETFs, ETNs, ELWs (Equity-Linked Warrants)
- Carbon emission rights

**Regular Trading Hours (KST, UTC+9)**: [REF:#1]
- Regular session: 09:00–15:30
- Pre-market (장전 시간외): 08:00–09:00 (시간외종가매매: 08:30–08:40)
- Post-market (장후 시간외): 15:40–18:00 (시간외종가매매: 15:40–16:00; 시간외단일가매매: 16:00–18:00)

**Key Statistics**: [WEB:wikipedia] [WEB:statista]
- Listed companies: ~2,600+ (KOSPI ~800+, KOSDAQ ~1,700+, KONEX ~129)
- Market capitalization (KOSPI): ~₩3,299 trillion (as of Nov 2025)
- Total domestic market capitalization: ~₩3,775 trillion (as of Nov 2025)

**Recent Major Changes**: [REF:#2]
- 2025.02.05: Introduction of Stop-Limit Order (스톱지정가호가) — new order type
- 2025.02.27: Introduction of Midpoint Order (중간가호가) — new order type
- 2026.01.15: Enhanced IT fault handling procedures (전산장애 대응 강화)

---

## 2. Institutional Philosophy

**Primary Market Model**: Pure order-driven (주문주도형), auction-based [REF:#1]
- All price discovery occurs through the order book via continuous auction (접속매매) and periodic call auctions (단일가매매/동시호가) [REF:#1]
- No Designated Market Maker (DMM) system for price-setting — unlike NYSE's hybrid model [REF:#1]

**Design Rationale**: [REF:#5]
- KRX evolved from the Korean Stock Exchange (est. 1956), which adopted an order-driven model influenced by Japanese exchange practices
- The pure electronic order-driven approach was reinforced with the launch of EXTURE+ in 2014, emphasizing speed and transparency [REF:#8]
- All participants submit orders to a centralized, anonymous order book with equal access [REF:#1]

**Role of Intermediaries**: [REF:#1] [REF:#2]
- **Liquidity Providers (유동성공급자, LP)**: Voluntary contractual arrangements for ETFs, ETNs, ELWs, and low-liquidity stocks. LPs provide two-sided quotes but do not set prices [REF:#1 Art.20의2]
- **Market Makers (시장조성자)**: Introduced in 2016 for low-liquidity equities. Obligated to maintain two-sided quotes within contracted spread limits [REF:#2 Art.31의12-22]
- Neither LPs nor MMs have exclusive rights or informational advantages — they receive fee rebates as compensation [REF:#1 Art.20의11]

**Evolution**: Floor-based (1956) → electronic (1997 KOSDAQ) → fully electronic EXTURE (2009) → EXTURE+ (2014) [REF:#8] [WEB:finextra]

---

## 3. Order Types — Basic

### 3.1 Limit Order (지정가호가/지정가주문) [REF:#1 Art.2§4-1]
- Specifies security, quantity, and price
- Executes at specified price or better
- Applicable: All sessions (regular, pre-market, after-hours)
- Time-in-force: Day order (default, expires at session end)

### 3.2 Market Order (시장가호가/시장가주문) [REF:#1 Art.2§4-2]
- Specifies security and quantity; no price specified
- In call auction: treated as limit at upper/lower price limit [REF:#1 Art.23§3]
- In continuous trading: sweeps the book at available prices until filled [REF:#1 Art.24§2]
- Applicable: Regular session only (not accepted during pre-market 시간외종가매매) [REF:#2]

### 3.3 Conditional Limit Order (조건부지정가호가) [REF:#1 Art.2§4-3]
- Acts as a limit order during continuous trading
- Automatically converts to market order for the closing call auction (장종료 동시호가) [REF:#1 Art.23§1-4]
- Designed for investors who want limit execution during the day but participation in closing price discovery
- Applicable: Regular session continuous trading only

### 3.4 Stop-Limit Order (스톱지정가호가) [REF:#1 Art.2§4-8] — **NEW (2025.02.05)**
- Specifies security, quantity, limit price, and stop (trigger) price
- Activated as a limit order when the last traded price reaches the stop price [REF:#2 Art.4의3]
  - Sell stop: triggered when last price ≤ stop price
  - Buy stop: triggered when last price ≥ stop price
- Applicable: Regular session continuous trading

---

## 4. Order Types — Advanced

### 4.1 Best Limit Order (최유리지정가호가) [REF:#1 Art.2§4-4] [REF:#2 Art.3]
- Quantity specified; price automatically set to the best available counterparty price at time of receipt
  - Sell: set to highest buy order price
  - Buy: set to lowest sell order price
- If no counterparty exists: set to 1 tick beyond best same-side price [REF:#2 Art.3]
- Functions similarly to a "marketable limit order" on other exchanges

### 4.2 Best Quote Order (최우선지정가호가) [REF:#1 Art.2§4-5] [REF:#2 Art.4]
- Quantity specified; price automatically set to the best same-side price at time of receipt
  - Sell: set to lowest sell order price (joins the best ask)
  - Buy: set to highest buy order price (joins the best bid)
- Ensures placement at the top of the same-side book without crossing the spread

### 4.3 Midpoint Order (중간가호가) [REF:#1 Art.2§4-7] — **NEW (2025.02.27)**
- Price set to the arithmetic mean of best bid and best ask (중간가격) [REF:#2 Art.4의2]
- Fractional won below 1 is truncated
- Available only during continuous trading session
- Similar concept to midpoint peg orders on US exchanges, but implemented as a KRX-specific order type

### 4.4 Time-in-Force Conditions [REF:#2]
- **Day (당일 유효)**: Default; expires at session end
- **IOC / Fill-and-Kill (즉시체결-잔량취소)**: Executes immediately against available liquidity; unfilled portion cancelled
- **FOK / Fill-or-Kill (전량체결-전량취소)**: Must fill entirely or is cancelled completely
- Note: KRX does not offer GTC or GTD for equities — all orders are day orders [REF:#1]

---

## 5. Order Types — Exchange-Specific

### 5.1 최유리지정가호가 (Best Limit Order) [REF:#1 Art.2§4-4]
- Unique to KRX in its precise mechanism: auto-prices at counterparty best, not as a market order
- Differs from a market order because it becomes a limit at the best opposing price — does not sweep multiple levels
- Rationale: Provides price improvement opportunity while limiting adverse selection

### 5.2 최우선지정가호가 (Best Quote Order) [REF:#1 Art.2§4-5]
- Unique to KRX: auto-prices at own-side best
- No equivalent on NYSE/NASDAQ — closest analog is a "pegged to primary" order
- Rationale: Allows passive participation at best price without specifying a price level

### 5.3 중간가호가 (Midpoint Order) [REF:#2 Art.4의2] — **NEW (2025.02.27)**
- Introduced February 2025 as KRX's first midpoint execution type
- Unique implementation: calculated as simple arithmetic mean of BBO, truncated (not rounded)
- Available during continuous trading only
- Rationale: Provides price improvement for both sides, reduces spread cost

### 5.4 조건부지정가호가 (Conditional Limit Order) [REF:#1 Art.2§4-3]
- KRX-specific hybrid: limit during continuous trading → market at closing auction
- No equivalent on other major exchanges
- Rationale: Combines intraday discipline with closing price participation

### 5.5 시간외 Order Types [REF:#1 Art.33-36]
- **시간외종가매매 (After-hours at closing price)**: Trades at the day's closing price
- **시간외단일가매매 (After-hours single-price auction)**: 10-minute call auction intervals during 16:00–18:00
- **시간외대량매매 (After-hours block trade)**: Negotiated block trades at prices within daily limits
- **시간외경쟁대량매매 (Pre-market competitive block)**: Pre-open block at VWAP of subsequent regular session
- **시간외바스켓매매 (After-hours basket trade)**: Basket of securities traded as a unit

---

## 6. Matching Engine & Price Discovery

### Trading System: EXTURE+ [REF:#8] [WEB:global.krx]
- **Launch**: 2014 (replacing EXTURE, which launched 2009) [WEB:finextra]
- **Architecture**: Memory-based order book, layered/tiered architecture on x86 Linux servers [WEB:global.krx]
- **Throughput**: 100,000+ transactions per second (TPS) [WEB:global.krx]
- **Latency**: 30–50 microseconds average order processing [WEB:global.krx]
- **Data Delivery**: Solace PubSub+ messaging infrastructure [WEB:solace.com]
- **Protocol Support**: FIX/FAST for standard connectivity [WEB:global.krx]
- **Markets**: Single platform covering equities, bonds, derivatives, commodities, carbon [REF:#8]
- **Data Centers**: Dual — Seoul (equities) and Busan (derivatives) with failover and zero data loss [REF:#8]
- **Features**: Reference Data Service (RDS) for flexible product additions; Drop Copy and Risk Filter for DMA [WEB:global.krx]

### Matching Algorithm: Price-Time Priority (가격·시간 우선원칙) [REF:#1 Art.22]
1. **Price priority**: Lower sell prices and higher buy prices have priority
2. **Time priority**: Among same-price orders, earlier orders have priority
3. **Special rule for call auctions (동시호가)**: Quantity priority applies — larger orders get priority up to 100× lot size, then ½ remaining, then full remaining [REF:#2 Art.34]

### Opening Price Determination [REF:#1 Art.23§1-1]
- **Call auction (단일가매매)** from 08:00 (order acceptance) to 09:00
- Orders accumulated during 08:00–09:00 with random closing (+30 seconds)
- Single price determined to maximize matched volume [REF:#1 Art.23§3-5]
- Market orders treated as upper/lower limit price for matching purposes

### Closing Price Determination [REF:#1 Art.23§1-4]
- **Call auction** during final 10 minutes (15:20–15:30) with random closing (+30 seconds) [REF:#2 Art.35§1-3]
- Conditional limit orders (조건부지정가) convert to market orders for this auction
- Single price algorithm identical to opening auction

### Tick Size Regime [REF:#2 Art.32§2]

| Price Range (KRW) | Tick Size (KRW) |
|---|---|
| < 2,000 | 1 |
| 2,000–4,999 | 5 |
| 5,000–19,999 | 10 |
| 20,000–49,999 | 50 |
| 50,000–199,999 | 100 |
| 200,000–499,999 | 500 |
| ≥ 500,000 | 1,000 |

### Lot Size [REF:#2 Art.32§1, Art.33§1]
- Equities: 1 share (1주)
- ELWs: 10 warrants
- All other securities: 1 unit

---

## 7. Safeguard Mechanisms

### 7.1 Market-Wide Circuit Breakers (서킷브레이커) [REF:#1 Art.25]

| Stage | Trigger (KOSPI decline from prior close) | Duration | Notes |
|---|---|---|---|
| Stage 1 | ≥ 8%, sustained 1 minute | 20-min halt, then resume | Once per day [REF:#2 Art.39§2] |
| Stage 2 | ≥ 15%, sustained 1 minute (and ≥1% below Stage 1 halt level) | 20-min halt, then resume | Once per day [REF:#2 Art.39§1-1] |
| Stage 3 | ≥ 20%, sustained 1 minute (and ≥1% below Stage 2 halt level) | Trading terminated for the day | [REF:#1 Art.25§1-3] |

- Stages 1 & 2 not triggered after 14:50 (40 min before close); Stage 3 applies anytime [REF:#2 Art.39§2]
- Stage 1 timing starts after first minute post-open [REF:#2 Art.39§4]

### 7.2 Volatility Interruption (변동성완화장치, VI) [REF:#1 Art.26의2]

**Dynamic VI (동적VI)**: [REF:#2 Art.41의2§1]
- Triggered when tentative execution price deviates from last traded price by:
  - KOSPI 200 constituents: ≥ 3%
  - Other stocks: ≥ 6%
  - During closing auction: thresholds reduced to 2% / 4% respectively
- Action: Switches to 2-minute call auction [REF:#2 Art.35§1-4]

**Static VI (정적VI)**: [REF:#2 Art.41의2§2]
- Triggered when tentative execution price deviates from last auction-determined price by ≥ 10%
- Action: Switches to 2-minute call auction

**Exceptions**: VI not applied to delisting-pending stocks, overheated stocks, low-liquidity single-price stocks [REF:#2 Art.41의2§4]

### 7.3 Daily Price Limits (가격제한폭) [REF:#1 Art.20]
- **Equities**: ±30% from base price (전일종가) [REF:#1 Art.20§2]
- **Delisting-pending stocks (정리매매)**: No price limits [REF:#1 Art.20§3]
- Special base price calculation for newly listed, re-listed, and capital-reduction stocks [REF:#2 Art.30]

### 7.4 Trading Halts (매매거래정지) [REF:#1 Art.26]
- Material disclosure events (공시 관련)
- Regulatory suspension
- Technical system failures (전산장애) [REF:#1 Art.27]
- Resume via 10-minute call auction [REF:#2 Art.35§1-2]

### 7.5 Short-Selling Price Restriction [REF:#1 Art.18] [REF:#2]
- Uptick rule applies to covered short sales (차입공매도)
- Short sell orders must be at or above the most recent trade price

### 7.6 Erroneous Trade Relief (대규모착오매매 구제) [REF:#1 Art.28의2]
- Large erroneous trades may be remedied upon member application
- Relief price: ±10% from reference price [REF:#2 Art.43의2]

---

## 8. Special Sessions

### 8.1 Pre-Market Session (장개시전 시간외시장) [REF:#1 Art.4§3-2가]
- **Hours**: 08:00–09:00
- **시간외종가매매 (Closing price trade)**: 08:30–08:40; trades at prior day's closing price
- **시간외경쟁대량매매 (Competitive block)**: During pre-market hours; settles at subsequent regular session VWAP [REF:#1 Art.34의3]
- **Order types**: Limit orders only (no market orders) [REF:#2]

### 8.2 Opening Auction (장전 동시호가) [REF:#1 Art.23§1-1]
- **Hours**: 08:00–09:00 (order accumulation); price determined at 09:00 + random 30 sec
- **Mechanism**: Single-price call auction (단일가매매)
- **Order types**: All types accepted (limit, market, conditional limit, best limit, best quote)
- **Priority**: Simultaneous orders use quantity priority [REF:#2 Art.34]

### 8.3 Continuous Trading (접속매매) [REF:#1 Art.24]
- **Hours**: 09:00–15:20
- **Mechanism**: Continuous price-time priority matching (복수가격 개별경쟁매매)
- **All order types** available including newly added midpoint and stop-limit orders

### 8.4 Closing Auction (장종료 동시호가) [REF:#1 Art.23§1-4]
- **Hours**: 15:20–15:30 + random 30 sec
- **Mechanism**: Single-price call auction
- Conditional limit orders (조건부지정가) automatically convert to market orders [REF:#1 Art.2§4-3]

### 8.5 Post-Market Sessions (장종료후 시간외시장) [REF:#1 Art.33-36]
- **시간외종가매매**: 15:40–16:00 at day's closing price
- **시간외단일가매매**: 16:00–18:00 via periodic call auctions at 10-min intervals
  - Price range: within ±10% of closing price AND within daily price limits [REF:#1 Art.34의2§3]
- **시간외대량매매**: 15:40–18:00 negotiated block trades within daily limits [REF:#1 Art.35]
- **시간외바스켓매매**: 15:40–18:00 basket trades [REF:#1 Art.36]

### 8.6 Block Trade Facilities [REF:#1 Art.30의2, 31, 35]
- **장중경쟁대량매매 (Intraday competitive block)**: 09:00–15:00; settles at closing VWAP
- **장중대량매매 (Intraday block)**: During regular hours; price between day's high and low
- **장중바스켓매매 (Intraday basket)**: Basket trade within day's high/low per component
- Minimum quantity requirements set by 시행세칙 [REF:#2]

---

## 9. LP / Market Maker Obligations

### 9.1 Liquidity Provider Program (유동성공급자 제도) [REF:#1 Art.20의2-8] [REF:#2 Art.31의3-7]

**Structure**: Contractual arrangement between listed company and member firm [REF:#1 Art.20의3]

**Eligible Securities**: [REF:#1 Art.20의2§1]
- ETFs (상장지수집합투자기구 집합투자증권)
- ETNs (상장지수증권)
- ELWs (주식워런트증권)
- Low-liquidity equities (with issuer contract)

**Obligations**: [REF:#1 Art.20의4] [REF:#2 Art.31의5-6]
- Maintain two-sided quotes (양방향 호가) during regular trading hours [REF:#1 Art.20의5§4]
- Spread must be within contracted limits (호가스프레드비율) [REF:#1 Art.20의4]
- Minimum quote size: 10× lot size for equities [REF:#2 Art.31의6§4-1]
- Exemptions: When trading volume target met, or holding exceeds 2% of listed shares [REF:#2 Art.31의4§1-6, 6의2]

**Privileges**: [REF:#1 Art.20의8]
- Fee rebates based on LP performance evaluation
- No informational advantages or exclusive order types

### 9.2 Market Maker Program (시장조성자 제도) [REF:#1 Art.20의9-11] [REF:#2 Art.31의12-22]

**Introduced**: 2016 (for low-liquidity equities) [REF:#2 Art.31의12]

**Structure**: [REF:#1 Art.20의9]
- KRX selects low-liquidity stocks and assigns market makers via competitive process [REF:#2 Art.31의14-15]
- Market makers execute via dedicated market-making accounts (시장조성계좌) [REF:#2 Art.31의12§3]

**Obligations**: [REF:#2 Art.31의17]
1. Maintain two-sided quotes (매도+매수)
2. Spread within contracted obligation spread (의무스프레드) — measured in tick units
3. Minimum quote value (최소호가유지금액) on each side
4. Exemptions: First 3 min after open, during call auctions, when limit up/down reached, when daily traded value > 50% of average [REF:#2 Art.31의17§2]

**Qualification**: [REF:#2 Art.31의13]
- No prior regulatory sanctions within 1 year
- Minimum 2 designated market-making staff
- Internal controls for short-selling compliance

**Performance Evaluation**: Quarterly assessment on obligation compliance and active market-making [REF:#2 Art.31의20]

**Compensation**: Fee rebates (시장조성대가), differentiated by evaluation results [REF:#2 Art.31의22]

**Termination**: Contract ends if stock liquidity exceeds 15% daily turnover for 2 consecutive quarters [REF:#2 Art.31의16§3-1]

---

## 10. Source Bibliography

### Reference Sources (Priority 1 — README_LINKS.md)

[REF:#1] Korea Exchange, "유가증권시장 업무규정 (Securities Market Business Regulations)", 2026.01.29, Local file: references/KRX/유가증권시장 업무규정_전문_20260129.txt

[REF:#2] Korea Exchange, "유가증권시장 업무규정 시행세칙 (Securities Market Business Regulations Enforcement Rules)", 2026.02.09, Local file: references/KRX/유가증권시장 업무규정 시행세칙_전문_20260209.txt

[REF:#3] KRX, "KRX 법무포털 (Legal Portal)", https://rule.krx.co.kr/

[REF:#4] KRX, "Global KRX Main", https://global.krx.co.kr/main/main.jsp

[REF:#5] KRX, "KOSPI Market Trading Rules (English)", https://global.krx.co.kr/contents/GLB/06/0602/0602010201/GLB0602010201.jsp

[REF:#6] KRX, "KONEX Market Trading Rules (English)", https://global.krx.co.kr/contents/GLB/06/0602/0602030101/GLB0602030101.jsp

[REF:#7] KRX, "Derivatives Trading Hours & Rules", https://global.krx.co.kr/contents/GLB/06/0603/0603010300/GLB0603010300.jsp

[REF:#8] KOSCOM, "KRX Trading System (EXTURE+)", https://www.koscom.co.kr/eng/main/contents.do?menuNo=300005

[REF:#9] KRX, "EXTURE+ Trading — Global KRX", https://global.krx.co.kr/contents/GLB/04/0402/0402020000/GLB0402020000.jsp

[REF:#10] KRX, "KRX Data Marketplace", https://data.krx.co.kr/

[REF:#11] KOFIA, "Introduction to Trading at KRX Stock Markets (PDF)", https://eng.kofia.or.kr/files/eng/2011_Introduction_to_Trading_at_KRX_Stock_Market.pdf

[REF:#12] KRX, "KIND (KRX 공시시스템)", https://kind.krx.co.kr/

### Web Sources (Priority 3 — Gap Fill)

[WEB:wikipedia] Korea Exchange — Wikipedia, https://en.wikipedia.org/wiki/Korea_Exchange, Accessed 2026-03-27

[WEB:statista] South Korea: KRX listed companies market capitalization 2025, https://www.statista.com/statistics/1009441/south-korea-listed-companies-market-capitalization/, Accessed 2026-03-27

[WEB:finextra] "Korea Exchange launches new trading system", Finextra, https://www.finextra.com/pressarticle/26674/korea-exchange-launches-new-trading-system, Accessed 2026-03-27

[WEB:solace.com] "KRX — Korea Exchange", Solace, https://solace.com/company/customers/krx/, Accessed 2026-03-27

[WEB:global.krx] KRX Global EXTURE+ page, https://global.krx.co.kr/contents/GLB/04/0402/0402020000/GLB0402020000.jsp, Accessed 2026-03-27

---

*Report version: 1.0 | Batch: 1 | Created: 2026-03-27 | Language: English*
