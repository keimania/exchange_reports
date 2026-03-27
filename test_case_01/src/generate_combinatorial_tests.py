#!/usr/bin/env python3
"""
KRX 유가증권시장 단일호가 전차원 교차 조합 테스트 케이스 생성기

모든 차원의 경우의 수를 교차 조합(Cross-product)하고,
규정 기반 규칙 엔진으로 각 조합의 기대결과를 판정한다.
"""

import json
import itertools
from collections import Counter, defaultdict
from datetime import datetime

# ============================================================
# 1. 차원 정의
# ============================================================

ORDER_TYPES = [
    "지정가", "시장가", "조건부지정가", "최유리지정가",
    "최우선지정가", "경쟁대량매매", "중간가", "스톱지정가"
]

SIDES = ["매도", "매수"]

CONDITIONS = ["없음", "IOC", "FOK"]

SESSIONS = [
    "시가단일가",      # 08:00~09:00
    "접속매매",        # 09:00~15:20
    "종가단일가",      # 15:20~15:30
    "VI단일가",        # 접속매매 중 VI 발동
    "시간외종가_장전",  # 08:30~08:40
    "시간외종가_장후",  # 15:40~16:00
    "시간외단일가",     # 16:00~18:00
    "장중경쟁대량",     # 09:00~15:00
    "시간외경쟁대량"    # 08:00~09:00
]

STOCK_STATUSES = [
    "일반종목", "정리매매종목", "단기과열종목", "이상급등종목",
    "투자유의종목", "관리종목", "투자경고종목", "투자위험종목",
    "저유동성종목", "종류주식종목", "공매도과열종목", "신규상장종목"
]

SECURITIES = [
    "주권", "외국주식예탁증권", "ETF", "ETN",
    "신주인수권증서", "신주인수권증권", "ELW", "수익증권", "채무증권"
]

PRICE_CONDITIONS = [
    "적정가격",       # 범위 내 정상 가격
    "상한가",         # 상한가 정확히 일치
    "하한가",         # 하한가 정확히 일치
    "호가단위불일치",   # 호가가격단위에 맞지 않는 가격
    "가격제한초과",    # 상한가 초과 또는 하한가 미만
    "기준가경계"       # 호가가격단위 구간 경계값
]

# ============================================================
# 2. 규칙 엔진: 각 조합에 대해 기대결과를 판정
# ============================================================

# 단일가매매 전환 종목상태 (정규시장에서 접속매매 없이 30분 간격 단일가만)
SINGLE_PRICE_ONLY_STATUSES = {
    "정리매매종목", "단기과열종목", "이상급등종목",
    "투자유의종목", "저유동성종목", "종류주식종목"
}

# 접속매매 전용 호가유형
CONTINUOUS_ONLY_TYPES = {"최유리지정가", "최우선지정가", "중간가", "스톱지정가"}

# 경쟁대량매매 전용 시간대
BULK_SESSIONS = {"장중경쟁대량", "시간외경쟁대량"}

# 시간외 시장 시간대
AFTER_HOURS_SESSIONS = {"시간외종가_장전", "시간외종가_장후", "시간외단일가"}

# 단일가매매 시간대 (접속매매가 아닌 시간대)
SINGLE_PRICE_SESSIONS = {"시가단일가", "종가단일가", "VI단일가"}

# 지정가만 허용하는 증권종류
LIMIT_ONLY_SECURITIES = {"신주인수권증서", "신주인수권증권", "ELW", "수익증권", "채무증권"}

# 주권류 (대부분의 호가유형 허용)
EQUITY_LIKE_SECURITIES = {"주권", "외국주식예탁증권", "ETF", "ETN"}

# 시장가 불가 종목상태
MARKET_ORDER_BANNED_STATUSES = {"정리매매종목", "단기과열종목"}

# 조건부지정가 불가 종목상태
CONDITIONAL_BANNED_STATUSES = {"정리매매종목", "단기과열종목", "투자유의종목"}

# VI 비적용 종목상태
VI_EXEMPT_STATUSES = {
    "정리매매종목", "단기과열종목", "이상급등종목",
    "투자유의종목", "저유동성종목", "종류주식종목", "신규상장종목"
}

# 경쟁대량매매 불가 종목상태
BULK_BANNED_STATUSES = {"정리매매종목", "관리종목"}

# IOC/FOK 적용 가능 호가유형
IOC_FOK_ALLOWED_TYPES = {"지정가", "시장가", "최유리지정가", "경쟁대량매매", "중간가"}

# IOC/FOK 불가 호가유형 (명시적)
IOC_FOK_BANNED_TYPES = {"최우선지정가", "조건부지정가", "스톱지정가"}


def evaluate_combination(ot, side, cond, session, status, security, price):
    """
    하나의 조합에 대해 규칙 체인을 적용하여 기대결과를 판정한다.

    Returns: (result, reason, article)
      result: "접수성공" | "접수거부" | "조건부성공"
      reason: 사유 설명
      article: 근거 조항
    """
    reasons = []

    # ── Rule 0: 시장가/경쟁대량 등 가격 불요 유형에 가격조건은 N/A 처리 ──
    price_relevant = True
    if ot == "시장가":
        price_relevant = False
    if ot == "경쟁대량매매":
        price_relevant = False

    # ── Rule 1: 증권종류 vs 호가유형 ──
    if security in LIMIT_ONLY_SECURITIES and ot != "지정가":
        return ("접수거부",
                f"{security}은(는) 지정가호가만 허용",
                "세칙 제10조제1항")

    # ── Rule 2: 경쟁대량매매 전용 시간대 검증 ──
    if ot == "경쟁대량매매":
        if session not in BULK_SESSIONS:
            return ("접수거부",
                    "경쟁대량매매호가는 전용시간대만 가능",
                    "규정 제4조제3항")
        if status in BULK_BANNED_STATUSES:
            return ("접수거부",
                    f"{status}은(는) 경쟁대량매매 불가",
                    "세칙 제14조제2항제3호")
    elif session in BULK_SESSIONS:
        # 경쟁대량매매가 아닌 호가유형은 경쟁대량매매 시간대에 접수 불가
        if ot != "경쟁대량매매":
            return ("접수거부",
                    "경쟁대량매매 시간대에는 경쟁대량매매호가만 가능",
                    "규정 제4조제3항")

    # ── Rule 3: 접속매매 전용 호가유형 vs 시간대 ──
    if ot in CONTINUOUS_ONLY_TYPES:
        # 단일가 시간대에서는 사용 불가
        if session in SINGLE_PRICE_SESSIONS or session in AFTER_HOURS_SESSIONS:
            return ("접수거부",
                    f"{ot}은(는) 접속매매 시간에만 가능",
                    "세칙 제14조")
        # 단일가전환 종목에서도 실질적으로 접속매매가 없으므로 거부
        if status in SINGLE_PRICE_ONLY_STATUSES:
            return ("접수거부",
                    f"{status}은(는) 단일가매매만 가능하여 {ot} 사용 불가",
                    "세칙 제56조")

    # ── Rule 4: 시장가 제한 ──
    if ot == "시장가":
        if session in AFTER_HOURS_SESSIONS:
            return ("접수거부",
                    "시장가호가는 시간외시장 불가",
                    "세칙 제14조")
        if status in MARKET_ORDER_BANNED_STATUSES:
            return ("접수거부",
                    f"{status}은(는) 시장가호가 불가",
                    "세칙 제14조제2항")

    # ── Rule 5: 조건부지정가 제한 ──
    if ot == "조건부지정가":
        if session in AFTER_HOURS_SESSIONS:
            return ("접수거부",
                    "조건부지정가호가는 시간외시장 불가",
                    "세칙 제14조")
        if status in CONDITIONAL_BANNED_STATUSES:
            return ("접수거부",
                    f"{status}은(는) 조건부지정가호가 불가",
                    "세칙 제14조제2항")

    # ── Rule 6: 정리매매 종목 특수 제한 ──
    if status == "정리매매종목":
        if ot in {"시장가", "조건부지정가", "경쟁대량매매", "중간가", "스톱지정가"}:
            return ("접수거부",
                    f"정리매매종목은 {ot} 불가",
                    "세칙 제56조")

    # ── Rule 7: IOC/FOK 조건 검증 ──
    if cond in ("IOC", "FOK"):
        # 호가유형 제한
        if ot in IOC_FOK_BANNED_TYPES:
            return ("접수거부",
                    f"{ot}은(는) {cond} 조건 부여 불가",
                    "세칙 제14조제2항")
        # 단일가매매 시간대 제한
        if session in SINGLE_PRICE_SESSIONS:
            return ("접수거부",
                    f"단일가매매 참여호가 접수시간에는 {cond} 불가",
                    "세칙 제14조제2항")
        # 시간외 시장 제한
        if session in AFTER_HOURS_SESSIONS:
            return ("접수거부",
                    f"시간외시장에서는 {cond} 불가",
                    "세칙 제14조제2항")
        # VI단일가도 단일가매매
        if session == "VI단일가":
            return ("접수거부",
                    f"VI단일가 시간에는 {cond} 불가",
                    "세칙 제14조제2항")
        # 정리매매종목 IOC/FOK 불가
        if status == "정리매매종목":
            return ("접수거부",
                    f"정리매매종목은 {cond} 불가",
                    "세칙 제14조제2항")
        # 신규상장 최초가격 결정시 IOC/FOK 불가
        if status == "신규상장종목" and session == "시가단일가":
            return ("접수거부",
                    f"신규상장종목 최초가격 결정시 {cond} 불가",
                    "세칙 제14조제2항")
        # 단일가전환 종목 (실질 단일가매매) - IOC/FOK 불가
        if status in SINGLE_PRICE_ONLY_STATUSES:
            return ("접수거부",
                    f"{status} 단일가매매 중 {cond} 불가",
                    "세칙 제14조제2항")

    # ── Rule 8: 시간외종가매매 ──
    if session in ("시간외종가_장전", "시간외종가_장후"):
        if ot != "지정가":
            return ("접수거부",
                    f"시간외종가매매에서는 지정가호가만 가능",
                    "규정 제34조")

    # ── Rule 9: 시간외단일가 ──
    if session == "시간외단일가":
        if ot not in ("지정가",):
            # 시간외단일가에서는 지정가만
            return ("접수거부",
                    f"시간외단일가매매에서는 지정가호가만 가능",
                    "규정 제34조의2")

    # ── Rule 10: 가격조건 검증 ──
    if price_relevant and price == "가격제한초과":
        if status == "정리매매종목":
            # 정리매매는 가격제한 없음 → 허용
            pass
        else:
            return ("접수거부",
                    "가격제한(상한가/하한가) 초과",
                    "규정 제20조")

    if price_relevant and price == "호가단위불일치":
        return ("접수거부",
                "호가가격단위에 부적합",
                "세칙 제32조제2항")

    # ── Rule 11: 공매도 과열종목 매도(차입공매도) 특수 ──
    # (일반 매도는 허용, 차입공매도만 제한 - side만으로는 구분 불가하므로 패스)

    # ══ 여기까지 통과하면 접수 성공 ══

    # 성공이지만 특수조건이 붙는 경우
    special_notes = []

    # 단일가전환 종목
    if status in SINGLE_PRICE_ONLY_STATUSES and session == "접속매매":
        special_notes.append(f"{status} 단일가매매 전환")

    # 조건부지정가 → 종가단일가 시 시장가 전환
    if ot == "조건부지정가" and session == "종가단일가":
        special_notes.append("시장가호가로 전환")

    # VI 관련
    if session == "VI단일가":
        if status in VI_EXEMPT_STATUSES:
            special_notes.append("VI비적용종목(단일가유지)")

    # 증거금 특수
    if status in ("투자경고종목", "투자위험종목", "투자유의종목") and side == "매수":
        special_notes.append("현금증거금100%")

    # 신규상장 확대가격제한폭
    if status == "신규상장종목":
        special_notes.append("확대가격제한폭(상한400%/하한60%)")

    # IOC 부분체결
    if cond == "IOC":
        special_notes.append("부분체결후잔량취소")
    elif cond == "FOK":
        special_notes.append("전량체결불가시전량취소")

    if special_notes:
        return ("조건부성공",
                "; ".join(special_notes),
                "")

    return ("접수성공", "", "")


# ============================================================
# 3. 전체 조합 생성 및 판정
# ============================================================

def generate_all():
    print("전차원 교차 조합 생성 중...")

    dimensions = {
        "order_type": ORDER_TYPES,
        "side": SIDES,
        "condition": CONDITIONS,
        "session": SESSIONS,
        "stock_status": STOCK_STATUSES,
        "security": SECURITIES,
        "price": PRICE_CONDITIONS
    }

    dim_sizes = {k: len(v) for k, v in dimensions.items()}
    total_space = 1
    for v in dim_sizes.values():
        total_space *= v

    print(f"  차원: {' × '.join(f'{k}({v})' for k,v in dim_sizes.items())}")
    print(f"  전체 조합 수: {total_space:,}")

    # 결과 수집
    results = []
    result_counts = Counter()
    reject_reasons = Counter()

    # 차원별 커버리지 추적
    dim_coverage = {
        "order_type": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "side": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "condition": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "session": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "stock_status": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "security": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "price": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
    }

    # 2차원 교차 매트릭스 (주요 조합)
    cross_matrices = {
        "order_type×session": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "order_type×stock_status": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "order_type×security": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "order_type×condition": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "session×stock_status": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "order_type×price": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "condition×session": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "security×session": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
    }

    # 3차원 교차 (핵심)
    cross_3d = {
        "order_type×session×stock_status": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "order_type×condition×session": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
        "order_type×security×stock_status": defaultdict(lambda: {"성공":0,"거부":0,"조건부":0}),
    }

    # 거부 사유 분류
    reject_by_rule = defaultdict(int)

    tc_id = 0
    for ot, side, cond, session, status, sec, price in itertools.product(
        ORDER_TYPES, SIDES, CONDITIONS, SESSIONS, STOCK_STATUSES, SECURITIES, PRICE_CONDITIONS
    ):
        tc_id += 1
        result, reason, article = evaluate_combination(ot, side, cond, session, status, sec, price)

        # 결과 분류
        if "성공" in result and "조건부" not in result:
            rkey = "성공"
        elif "거부" in result:
            rkey = "거부"
        else:
            rkey = "조건부"

        result_counts[rkey] += 1
        if rkey == "거부":
            reject_reasons[reason] += 1
            # 규칙별 분류
            rule_name = reason.split("은(는)")[0] if "은(는)" in reason else reason[:20]
            reject_by_rule[rule_name] += 1

        # 1차원 커버리지
        dim_coverage["order_type"][ot][rkey] += 1
        dim_coverage["side"][side][rkey] += 1
        dim_coverage["condition"][cond][rkey] += 1
        dim_coverage["session"][session][rkey] += 1
        dim_coverage["stock_status"][status][rkey] += 1
        dim_coverage["security"][sec][rkey] += 1
        dim_coverage["price"][price][rkey] += 1

        # 2차원 교차
        cross_matrices["order_type×session"][(ot,session)][rkey] += 1
        cross_matrices["order_type×stock_status"][(ot,status)][rkey] += 1
        cross_matrices["order_type×security"][(ot,sec)][rkey] += 1
        cross_matrices["order_type×condition"][(ot,cond)][rkey] += 1
        cross_matrices["session×stock_status"][(session,status)][rkey] += 1
        cross_matrices["order_type×price"][(ot,price)][rkey] += 1
        cross_matrices["condition×session"][(cond,session)][rkey] += 1
        cross_matrices["security×session"][(sec,session)][rkey] += 1

        # 3차원 교차
        cross_3d["order_type×session×stock_status"][(ot,session,status)][rkey] += 1
        cross_3d["order_type×condition×session"][(ot,cond,session)][rkey] += 1
        cross_3d["order_type×security×stock_status"][(ot,sec,status)][rkey] += 1

        # 결과 저장 (샘플 및 전체)
        results.append({
            "id": tc_id,
            "order_type": ot,
            "side": side,
            "condition": cond,
            "session": session,
            "stock_status": status,
            "security": sec,
            "price": price,
            "result": result,
            "reason": reason,
            "article": article
        })

    print(f"  생성 완료: {tc_id:,}건")
    print(f"  접수성공: {result_counts['성공']:,}  조건부성공: {result_counts['조건부']:,}  접수거부: {result_counts['거부']:,}")

    return {
        "metadata": {
            "title": "KRX 유가증권시장 단일호가 전차원 교차조합 테스트",
            "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "dimensions": dim_sizes,
            "total_combinations": total_space,
            "results_summary": dict(result_counts)
        },
        "dimensions": dimensions,
        "dim_coverage": {k: {kk: dict(vv) for kk,vv in v.items()} for k,v in dim_coverage.items()},
        "cross_2d": {
            name: {
                f"{k[0]}|{k[1]}" if len(k)==2 else str(k): dict(v)
                for k,v in matrix.items()
            }
            for name, matrix in cross_matrices.items()
        },
        "cross_3d": {
            name: {
                f"{k[0]}|{k[1]}|{k[2]}": dict(v)
                for k,v in matrix.items()
            }
            for name, matrix in cross_3d.items()
        },
        "reject_reasons_top50": dict(reject_reasons.most_common(50)),
        "all_results": results
    }


# ============================================================
# 4. 실행 & 저장
# ============================================================

if __name__ == "__main__":
    data = generate_all()

    # 전체 결과 (대용량이므로 분리)
    all_results = data.pop("all_results")

    # 메타데이터 + 커버리지 매트릭스 저장
    with open("krx_combinatorial_coverage.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  커버리지 매트릭스 저장: krx_combinatorial_coverage.json")

    # 전체 TC 저장 (CSV-like JSON Lines for size efficiency)
    with open("krx_combinatorial_all_cases.jsonl", "w", encoding="utf-8") as f:
        for r in all_results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"  전체 TC 저장: krx_combinatorial_all_cases.jsonl ({len(all_results):,}건)")

    # 거부 사유 통계 출력
    print("\n=== 접수거부 사유 Top 20 ===")
    for reason, count in sorted(data["reject_reasons_top50"].items(), key=lambda x:-x[1])[:20]:
        print(f"  {count:>8,}건  {reason}")
