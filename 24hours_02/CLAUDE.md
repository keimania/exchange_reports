# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research repository containing reference materials for analyzing global exchange extended/24-hour trading operations, with a specific focus on the **Korea Exchange (KRX)** transition from its current trading model to a 12-hour session (June 2026) and ultimately a 24-hour regime (December 2027).

## Repository Structure

All materials are in the `References/` directory. There is no code, build system, or tests.

### Reference Documents

Documents exist in both `.txt` formats.

- **Global comparison report** (`KRX 24-Hour Trading_ Global Comparison`) — The master comparative analysis covering all exchanges (NYSE Arca, NASDAQ, 24X, KRX) across trading mechanisms, system architecture, clearing/settlement, and gap analysis
- **NYSE Arca analysis** (`NYSE Extended Trading Analysis for KRX`) — Deep dive into NYSE Pillar architecture, 22-hour session design, auction mechanics, DTCC/NSCC clearing integration
- **24X Exchange analysis** (`24X Exchange Trading Operations Analysis`) — MEMX Memoir engine, 23/5 model, proprietary 24X Price Bands, overnight order restrictions
- **NASDAQ analysis** (`Technical Feasibility...NASDAQ 23_5 Global Trading Ecosystem`) — Genium INET architecture, Night Session design, OUCH 5 protocol
- **CME Group case study** (`Comprehensive Case Study on CME Group's 24-Hour Trading Infrastructure`) — Globex platform, futures/derivatives continuous trading precedent
- **NYSE Arca technical blueprint** (`Blueprinting the Near-Continuous Market...NYSE Arca 22-Hour Trading Transition`) — Detailed technical/regulatory analysis of the 22-hour transition
- **DTCC roadmap** (`DTCC 24_5 Clearing Roadmap Analysis`) — UTC system modernization, T+1 settlement in continuous markets, FIX Tag 715
- **Korean regulatory texts** (Korean-language `.txt` files) — KRX 유가증권시장 업무규정 (Securities Market Business Regulations) and 시행세칙 (Enforcement Rules)

## Key Domain Concepts

When working with these documents, the following technical terms and concepts are central:

- **KRX EXTURE 3.0**: Current KRX trading system (50μs latency, 940M daily transactions), built on stateful daily-cycle architecture
- **"One Board" system**: KRX's planned unified continuous order processing system enabling order persistence across sessions
- **Technical Pause**: Mandatory daily maintenance window (1-2 hours) used by all exchanges for batch processing, corporate actions, and trade date advancement
- **T+1 settlement**: Compressed settlement cycle; KRX plans to move from T+2 to T+1 alongside trading hour expansion
- **24X Price Bands**: Proprietary overnight volatility controls (20%/10%/6% tiers by price)
- **VI (Volatility Interruption)**: KRX's current mechanism that halts trading and triggers call auctions on extreme price moves
- **SIP (Securities Information Processor)**: US consolidated market data feed; its overnight availability is a prerequisite for extended US trading
- **Nextrade**: Korean ATS competing with KRX on extended hours (08:00-20:00)
- **FIX Tag 715**: Clearing Business Date field required for overnight trade date assignment in DTCC systems

## Working with This Repository

- Documents are research references, not generated outputs. Do not modify the reference files.
- The Korean regulatory texts use formal legal Korean (법률 용어). When referencing them, provide both Korean terms and English translations.
- The `.txt` files contain footnote reference numbers (superscript markers like `1`, `4`, `8`) embedded inline — these correspond to source citations in the original `.docx` files.
- When synthesizing across documents, note that the global comparison report integrates findings from all individual exchange analyses.
