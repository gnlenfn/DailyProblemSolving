import sys
input = sys.stdin.readline

from datetime import datetime, timedelta
from collections import defaultdict

n, l, f = input().split()

day = int(l.split("/")[0])
hour = int(l.split("/")[1].split(":")[0])
minute = int(l.split("/")[1].split(":")[1])
duration = timedelta(minutes=24 * 60 * day + 60 * hour + minute)  # 대여기간 분 단위
f = int(f)

book = defaultdict(dict)
fare = defaultdict(int)
for _ in range(int(n)):
    date, time, part, name = input().split()
    date_time = datetime.strptime(date + " " + time,"%Y-%m-%d %H:%M")

    if name in book and part in book[name]:
        # 이번 기록은 반납기록!
        borrow_duration = date_time - book[name][part]
        if borrow_duration > duration:  # 사용한 기간이 대여기간보다 길다
            pay = (borrow_duration - duration).total_seconds() // 60 * f  # 분당 벌금 적용
            fare[name] += pay  # 한 사람이 서로 다른 부품들에 대해 벌금을 낼 수있지만 벌금 계산은 이름아래 한번만

        del book[name][part]  # 어쨌든 반납하면 내역 삭제
    
    else:
        # 대여 기록
        book[name][part] = date_time

if fare:
    for name, f in sorted(fare.items()):  # 벌금 낸 사람 이름 사전순 정렬
        print(name, int(f))  # 벌금은 float형태로 들어가있으므로 int로 변경
else:
    print(-1)
