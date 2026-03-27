# Eurex Exchange - References & Specifications

## 1. Trading Rules & Order Types

- **[Eurex Order Types](https://www.eurex.com/ex-en/trade/order-book-trading/order-types)** - 주문유형 개요 (Limit, Market, Stop, OCO, Iceberg 등)
- **[Exchange Rules Circular (2024)](https://www.eurex.com/ex-en/find/circulars/circular-3763988)** - Eurex Deutschland 거래규칙 변경사항
- **[Exchange Rules Circular (2025)](https://www.eurex.com/ex-en/find/circulars/circular-4176840)** - Eurex Deutschland 거래규칙/조건/계약사양 변경

## 2. T7 Trading System

- **[T7 Release 13 Overview](https://www.eurex.com/ex-en/support/initiatives/t7-release13)** - T7 릴리즈 13 개요 및 변경사항
- **[T7 Enhanced Trading Interface (ETI) Manual (PDF)](https://www.eurexchange.com/resource/blob/297838/54cd4e591b23d7e3d60ef8e707c21a56/data/eurex_eti_manual_V31.pdf)** - ETI 매매 인터페이스 매뉴얼 (Cash & Derivatives)
- **[T7 Eurex Trader & Admin GUI Manual (PDF)](https://www.eurexchange.com/resource/blob/279888/c6872432b05d4085a6642319104cc320/data/Eurex-Trader-and-Admin-GUI-User-Manual.pdf)** - Eurex Trader/Admin GUI 사용자 매뉴얼
- **[T7 R13.1 Participant & User Maintenance Manual (PDF)](https://www.eurex.com/resource/blob/4332334/61e2e29f08a63ff88d20ee30c4dc2049/data/T7_R.13.1_Derivatives_Market_-_Participant_and_User_Maintenance_Manual_Version_1.pdf)** - 참가자 및 사용자 관리 매뉴얼

## 3. Simulation & Testing

- **[T7 R11.1 Participant Simulation Guide (PDF)](https://www.eurex.com/resource/blob/3470820/d69f12028fc9ad9f443095efd392196b/data/T7_R.11.1_Participant_Simulation_Guide_v.1.0.pdf)** - T7 R11.1 시뮬레이션 가이드
- **[T7 R10.0 Participant Simulation Guide (PDF)](https://www.eurex.com/resource/blob/2900446/3073bfef838e8a5762db9ad340143178/data/T7_R.10.0_Participant_Simulation_Guide_v.1.1.pdf)** - T7 R10.0 시뮬레이션 가이드

## Key Notes

### 주요 주문유형
- **Limit Order**: 지정가 주문
- **Market Order**: 시장가 주문
- **Stop Order (Stop-Loss)**: 특정 가격 도달 시 시장가로 전환
- **OCO (One-Cancels-the-Other)**: 지정가 + Stop 결합, 하나의 Order ID로 관리
- **Iceberg Order**: 일부 수량만 공개, 체결 시 다음 수량 노출

### T7 시스템
- Eurex와 Xetra 공용 매매 플랫폼
- ETI (Enhanced Trading Interface): 세션 기반 TCP/IP 접속
- Application Gateway를 통한 참가자 접속
- 사전거래통제(Pre-trade Controls): 최대 주문가치, 최대 주문수량 제한
