import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 95

dp[0] = 0
dp[1] = 1
for idx in range(2, 95):
    dp[idx] = dp[idx - 1] + dp[idx - 2]

print(dp[n])
