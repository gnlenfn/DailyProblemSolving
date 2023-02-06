import sys
input = sys.stdin.readline

n = int(input())    
price = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = price[1]
dp[2] = max(price[2], price[1] * 2)


for i in range(3, n + 1):
    dp[i] = price[i]

    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[n])
