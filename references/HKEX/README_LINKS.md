# HKEX (Hong Kong Exchanges and Clearing) - References & Specifications

## 1. Trading Mechanism & Rules

- **[Trading Mechanism Overview](https://www.hkex.com.hk/Services/Trading/Securities/Overview/Trading-Mechanism?sc_lang=en)** - 매매 세션, 주문유형, 거래유형, 호가규칙, VCM 개요
- **[Closing Auction Session (CAS) Mechanism (PDF)](https://www.hkex.com.hk/eng/market/sec_tradinfra/vcm_cas/Documents/Trading%20Mechanism%20of%20the%20CAS%20in%20the%20Securities%20Market.pdf)** - 종가매매세션(CAS) 매매 메커니즘

## 2. Volatility Control Mechanism (VCM)

- **[VCM Trading Mechanism (PDF)](https://www.hkex.com.hk/-/media/HKEX-Market/Services/Trading/Derivatives/Trading-Mechanism/Volatility-Control-Mechanism-(VCM)/Trading-Mechanism-for-VCM-Eng.pdf)** - VCM 매매 메커니즘 상세 (파생상품)
- **[VCM Information Paper - Securities Market (PDF)](https://www.hkex.com.hk/-/media/HKEX-Market/Services/Trading/Securities/Overview/Trading-Mechanism/Trading-Mechanism-for-VCM_E.pdf?la=en)** - 증권시장 VCM 정보 문서

## 3. Orion Trading Platform (OTP) Specifications

- **[OTP Infrastructure Overview](https://www.hkex.com.hk/Services/Trading/Securities/Infrastructure/Overview?sc_lang=en)** - Orion Trading Platform 인프라 개요
- **[OCG Binary Trading Interface Specifications (PDF)](https://www.hkex.com.hk/-/media/HKEX-Market/Services/Trading/Securities/Infrastructure/Orion-Trading-Platform-Securities-Market-OTP-C/OTPC/HKEX_OCG_Binary_Trading_Interface_Specifications_v2_1.pdf?la=en)** - Orion Central Gateway Binary 매매 인터페이스 사양
- **[OCG FIX Drop Copy Interface Specifications (PDF)](https://www.hkex.com.hk/-/media/HKEX-Market/Services/Trading/Securities/Infrastructure/Orion-Trading-Platform-Securities-Market-OTP-C/OTPC/HKEX_OCG_FIX_Drop_Copy_Interface_Specifications_v2_1(With_Track_Changes).pdf?la=en)** - OCG FIX Drop Copy 인터페이스 사양

## 4. Market Data Platform (OMD)

- **[OMD-C Binary Interface Specifications (PDF)](https://www.hkex.com.hk/eng/prod/dataprod/Documents/HKEX_OMD-C_Binary_Interface_Specifications_v1.39b.pdf)** - 증권시장 시장데이터 Binary 인터페이스 사양
- **[OMD-D Developers Guide (PDF)](https://www.hkex.com.hk/-/media/HKEX-Market/Services/Market-Data-Services/Infrastructure/HKEX-Orion-Market-Data-Platform-Derivatives-Market-OMD-D/HKEX-OMDD-Developers-Guide-v1,-d-,26.pdf)** - 파생상품 시장데이터 개발자 가이드
- **[OMD-D DLite Interface Specifications (PDF)](https://www.hkex.com.hk/-/media/HKEX-Market/Services/Market-Data-Services/Infrastructure/HKEX-Orion-Market-Data-Platform-Derivatives-Market-OMD-D/Introduction-of-DLite/OMDD-Interface-Specifications-(DLite)-v1,-d-,4d-(for-G4).pdf?la=en)** - OMD-D DLite 인터페이스 사양

## Key Notes
- 거래시간: 09:30~12:00, 13:00~16:00 (HKT), CAS 16:00~16:10
- VCM: 5분 모니터링 기간 중 기준가 대비 ±10%(증권)/±5%(파생) 이탈 시 5분 냉각기간 발동
- Orion Trading Platform: 증권시장(OTP-C) 및 파생상품시장(OTP-D) 지원
