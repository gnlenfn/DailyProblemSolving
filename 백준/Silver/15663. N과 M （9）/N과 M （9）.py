from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split())) # sort를 위해 int로 변환

ret = sorted(list(permutations(nums, m))) # 모든 경우의 수 (순열)
used = set()  # 정답 중복 방지를 위해 set사용
for r in ret:
    if r not in used:
        print(" ".join(map(str, r)))
    used.add(r)