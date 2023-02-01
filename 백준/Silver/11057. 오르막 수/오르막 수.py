import sys
input = sys.stdin.readline

n = int(input())    
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(10):
    # 한 자릿 수 일 때 값을 초기화
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j, 10):
            # i는 자리수 
            # j는 마지막 자리수의 수
            # k는 j에 따른 새로 올 수 있는 수
            dp[i][k] += dp[i - 1][j]
    """ 마지막 숫자가 1이면 1 ~ 9가 올 수 있음  
        바로 전 단계의 마지막수가 같은 것을 더해간다
        최종 결과는 n번째 열의 합
    """

print(sum(dp[n]) % 10007)
