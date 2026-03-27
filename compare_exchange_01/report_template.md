# Exchange Report Template

> Use this template for every exchange report. Copy this file and rename to `{EXCHANGE}_report.md`.
> Replace all `{EXCHANGE}` placeholders with the exchange name.
> Fill each section following the guidance text. Remove guidance text once content is written.
> Cite every claim using `[REF:#N]` (numbered reference) or `[WEB:url]` (web source).

---

# {EXCHANGE} — Exchange Report

## 1. Exchange Overview

> **Guidance**: Provide foundational context for the exchange.
>
> Cover:
> - Full legal name, country, founding year, parent group (if applicable)
> - Market model classification (order-driven, quote-driven, hybrid)
> - Asset classes traded (equities, derivatives, fixed income, ETFs, etc.)
> - Regular trading hours (local time + UTC offset)
> - Pre-market, post-market, and extended hours (if applicable)
> - Key statistics: listed companies, average daily volume, market capitalization
> - Recent major changes or system upgrades

---

## 2. Institutional Philosophy

> **Guidance**: Explain the exchange's fundamental design choices.
>
> Cover:
> - Primary market model: auction-based, dealer-based, or hybrid
> - Order-driven vs. quote-driven vs. mixed approach
> - Role of intermediaries (DMMs, Market Makers, LPs) in the model
> - Design rationale: why this model was chosen (historical, regulatory, or market reasons)
> - How the philosophy differs from peer exchanges
> - Evolution over time (e.g., floor-based → electronic → hybrid)

---

## 3. Order Types — Basic

> **Guidance**: Document standard order types available to all participants.
>
> Cover each type with:
> - Name (English + local term if applicable)
> - Definition and behavior
> - Time-in-force options (Day, GTC, IOC, FOK, GTD, etc.)
> - Applicability by session (pre-market, continuous, auction, post-market)
>
> Typical basic types:
> - Market Order
> - Limit Order
> - Stop Order / Stop-Limit Order
> - Market-to-Limit Order

---

## 4. Order Types — Advanced

> **Guidance**: Document sophisticated order types for institutional or algorithmic use.
>
> Cover each type with:
> - Name and definition
> - Parameters (display qty, reserve qty, peg reference, conditions, etc.)
> - Use case and typical user profile
> - Interaction with matching engine priority rules
>
> Typical advanced types:
> - Iceberg / Reserve Order
> - Pegged Order (primary peg, midpoint peg, market peg)
> - Conditional / Triggered Orders
> - One-Cancels-the-Other (OCO)
> - Fill-or-Kill (FOK) / Fill-and-Kill (FAK)
> - Minimum Quantity Orders
> - Algo Order types (TWAP, VWAP, etc., if exchange-native)

---

## 5. Order Types — Exchange-Specific

> **Guidance**: Document order types unique to this exchange that don't exist elsewhere.
>
> Cover:
> - Name, definition, and origin/rationale
> - How it differs from similar types on other exchanges
> - Regulatory or structural reasons for its existence
> - Usage statistics or adoption (if available)
>
> Examples of exchange-specific types:
> - NYSE: D-Order (DMM interest)
> - LSE: Named Order (SETSqx)
> - ASX: Centre Point Order (dark midpoint)
> - HKEX: Special Limit Order, Enhanced Limit Order

---

## 6. Matching Engine & Price Discovery

> **Guidance**: Explain how orders are matched and prices are determined.
>
> Cover:
> - Matching algorithm: price-time priority, pro-rata, or hybrid
> - Trading system name and version (e.g., arrowhead 4.0, Pillar, T7)
> - Latency specifications (if publicly available)
> - Opening price determination mechanism (call auction / DMM / cross)
> - Closing price determination mechanism
> - Intraday price discovery process
> - Tick size regime (fixed vs. dynamic, tick size table)
> - Lot size requirements
> - Order book structure (visible vs. hidden depth)

---

## 7. Safeguard Mechanisms

> **Guidance**: Document all price stability and risk control mechanisms.
>
> Cover:
> - Circuit breakers: trigger thresholds, cooling-off period, resumption rules
> - Volatility interruptions / auctions: intra-session triggers
> - Daily price limits: percentage bands, baseline calculation
> - Limit Up-Limit Down (LULD) or equivalent
> - Trading halts: criteria (news, regulatory, technical)
> - Pre-trade risk controls: max order size, max order value, fat-finger checks
> - Kill switches and emergency procedures
> - Historical activation examples (if notable)

---

## 8. Special Sessions

> **Guidance**: Document all non-regular trading sessions and venues.
>
> Cover:
> - Pre-market session: hours, allowed order types, matching rules
> - After-hours session: hours, allowed order types, matching rules
> - Block trade facility: minimum size, price constraints, reporting
> - Dark pool / non-displayed venue: mechanism, eligibility, interaction with lit market
> - Negotiated trades / off-book trades: rules, reporting requirements
> - Any other special sessions (e.g., TSE Closing Auction Session, HKEX CAS)

---

## 9. LP / Market Maker Obligations

> **Guidance**: Document liquidity provision programs and obligations.
>
> Cover:
> - Market maker / LP program name and structure
> - Designation types (DMM, Primary Market Maker, Competitive Market Maker, etc.)
> - Obligations: quoting requirements (spread, size, time-in-market)
> - Privileges: fee rebates, information advantages, exclusive order types
> - Performance metrics and compliance monitoring
> - Number of active LPs / Market Makers (if available)
> - Comparison with peer exchange LP programs

---

## 10. Source Bibliography

> **Guidance**: List all sources cited in this report. Every `[REF:#N]` and `[WEB:url]` tag used above must appear here.
>
> Format:
> ```
> [REF:1] Author/Org, "Title", Date, URL or document path
> [REF:2] ...
> [WEB:url] Description of web resource, Access date
> ```
>
> Include:
> - Official exchange documentation (rules, guides, specifications)
> - Regulatory filings and circulars
> - Academic papers and industry reports
> - Third-party analysis (with reliability assessment)

---

*Template version: 1.0 | Created: 2026-03-27 | Project: compare_exchange_01*
