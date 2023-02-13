import sys
input = sys.stdin.readline

import heapq

n = int(input())
nums = []

for _ in range(n):
    tmp = map(int, input().split())
    for t in tmp:
        if len(nums) < n:  # 힙의 길이가 n보다 작으면 항상 입력
            heapq.heappush(nums, t)
    
        elif t > nums[0]:  # top이 이번 수보다 작으면 top 뺴고 이번 수 입력
            heapq.heappop(nums)
            heapq.heappush(nums, t)

print(nums[0])  # heap에 큰 수 부터 n개가 들어있기 때문에 가장 처음 pop 되는 수가 n번째 큰 수
