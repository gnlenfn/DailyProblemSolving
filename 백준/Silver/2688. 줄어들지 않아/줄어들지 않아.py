import sys
input = sys.stdin.readline

t = int(input())    
for _ in range(t):
    n = int(input())
    dp = [[0] * 10 for _ in range(n + 1)]

    for i in range(10):
        dp[1][i] = 1  # 한 자리는 다 1개 씩
    
    for i in range(2, n + 1):  # 자릿수
        for j in range(10):    
            dp[i][j] = sum(dp[i-1][j:])  # 이번 자릿수에서 j로 끝나는 경우, 그 보다 큰 경우 모두 더하기

    print(sum(dp[n]))
