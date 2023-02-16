import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
coins = deque()
cnt = 0

for _ in range(n):
    coins.appendleft(int(input()))  # 내림차순 정렬

for c in coins:
    cnt += k // c
    k %= c

print(cnt)
