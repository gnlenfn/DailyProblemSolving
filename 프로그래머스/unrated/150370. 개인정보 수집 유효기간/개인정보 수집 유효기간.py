from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    today = datetime.strptime(today, "%Y.%m.%d")
    policy = defaultdict(int)
    # 약관 정리
    for t in terms:
        name, period = t.split(" ")
        policy[name] = int(period)
    
    # 만료 날짜 계산
    for idx, p in enumerate(privacies, 1):
        date, term = p.split(" ")
        date = datetime.strptime(date, "%Y.%m.%d")
        expired = date + relativedelta(months = policy[term])
        
        if expired <= today:
            answer.append(idx)

    return answer