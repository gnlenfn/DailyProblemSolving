import sys
input = sys.stdin.readline

n = int(input())    
wines = [0]
for _ in range(n):
    wines.append(int(input()))
wines = wines + [0]  # index에러를 위해 뒤에 추가 (n이 2보다 작을 때)

dp = [0] * (n + 3)
dp[1] = wines[1]
dp[2] = dp[1] + wines[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + wines[i - 1]) + wines[i]  # 4번을 마실때 / 1 3 4, 2 4 비교
    dp[i] = max(dp[i], dp[i - 1])  # 현재 지점까지 가장 큰 값을 가장 뒤로 놓기

print(dp[n])
