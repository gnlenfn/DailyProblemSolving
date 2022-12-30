import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

R, ans, lions = -1, -1, 0

for L in range(n):
    while R + 1 < n and lions < k:
        R += 1
        if nums[R] == 1:
            lions += 1
    
    if lions == k:
        if ans == -1:
            ans = R - L + 1
        ans = min(ans, R - L + 1)
    
    if nums[L] == 1:
        lions -= 1

print(ans)