import sys
input = sys.stdin.readline

import heapq

h = []
n = int(input())

for _ in range(n):
    num = int(input())

    if num > 0:
        heapq.heappush(h, -num)
    else:
        if h:
            t = heapq.heappop(h)
            print(-t)
        else:
            print(0)
