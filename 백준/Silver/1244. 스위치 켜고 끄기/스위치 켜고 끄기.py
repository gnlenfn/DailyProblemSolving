import sys
input = sys.stdin.readline


def male(num):
    for idx, _ in enumerate(status, 1):
        if idx % num:
            continue

        status[idx - 1] = int(not status[idx - 1])


def female(num):
    num -= 1  # index로 맞게
    status[num] = int(not status[num])
    step = 1
    while num - step >= 0 and num + step < n:
        if status[num - step] == status[num + step]:
            status[num - step] = int(not status[num - step])
            status[num + step] = int(not status[num + step])
        else:
            break
        step += 1

    
n = int(input())
status = list(map(int, input().strip().split()))
t = int(input())

for _ in range(t):
    s, num = map(int, input().strip().split())

    if s == 1:  # 남자
        male(num)
    else:  # 여자
        female(num)

for idx, ans in enumerate(status):  # 20개씩 출력
    if idx and not idx % 20:
        print() 
    print(ans, end=" ")
