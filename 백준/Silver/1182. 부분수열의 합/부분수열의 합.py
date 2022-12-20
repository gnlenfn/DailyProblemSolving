from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

for i in range(1, len(nums) + 1):
    candidates = combinations(nums, i)
    for cand in candidates:
        if sum(cand) == s:
            answer += 1

print(answer)