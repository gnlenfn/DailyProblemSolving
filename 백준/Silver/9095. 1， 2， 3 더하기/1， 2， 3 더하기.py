import sys
input = sys.stdin.readline

dp = [0] * 15
dp[1], dp[2], dp[3] = 1, 2, 4
t = int(input())    
for _ in range(t):
    target = int(input())

    for i in range(4, target + 1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    print(dp[target])