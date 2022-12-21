from collections import Counter
import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
mode = nums[0]   # 최빈값 초기화
mode_count = 1   # 최빈값 카운트
current = 1      # 현재 수 카운트

for i in range(1, n):
    if nums[i] == nums[i-1]:  # 같은 수면 카운트 증가
        current += 1
    else:
        current = 1           # 다른 수면 처음부터 카운트
    
    if mode_count < current:  # 최빈값 보다 현재값 카운트가 크면
        mode_count = current  # 최빈값 갱신
        mode = nums[i]

print(mode)
