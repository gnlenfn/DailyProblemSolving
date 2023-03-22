import sys
input = sys.stdin.readline

def transit(i, stat):  # 1번 명령어
    status[i] = stat

def multi_transit(l, r):  # 2번 명령어
    for idx in range(l, r + 1):
        if status[idx]:
            status[idx] = 0
        else:
            status[idx] = 1

def turn_off(l, r):  # 3번 명령어
    status[l: r + 1] = [0] * (r - l + 1)

def turn_on(l, r):  # 4번 명령어
    status[l: r + 1] = [1] * (r - l + 1)


n, m = map(int, input().split())
status = list(map(int, input().strip().split()))
for _ in range(m):
    t, p, q = map(int, input().split())

    if t == 1:
        transit(p - 1, q)

    elif t == 2:
        multi_transit(p - 1, q - 1)

    elif t == 3:
        turn_off(p - 1, q - 1)
    
    elif t == 4:
        turn_on(p - 1, q - 1)

print(" ".join(map(str, status)))
