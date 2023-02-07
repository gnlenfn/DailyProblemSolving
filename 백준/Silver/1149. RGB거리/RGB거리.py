import sys
input = sys.stdin.readline

n = int(input())    
cost = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (3) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]  # 현재 칸을 0번 색으로 칠하기 위한 최소값
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]  # 현재 칸을 1번 색으로 칠하기 위한 최소값
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]  # 현재 칸을 2번 색으로 칠하기 위한 최소값

print(min(dp[n]))
