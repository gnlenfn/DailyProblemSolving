import sys
input = sys.stdin.readline

import heapq

n = int(input())
nums = []

for _ in range(n):
    x = int(input())

    if x:
        heapq.heappush(nums, (abs(x), x))
    else:
        if not nums:
            print(0)
        else:
            tmp = heapq.heappop(nums)
            print(tmp[1])
    