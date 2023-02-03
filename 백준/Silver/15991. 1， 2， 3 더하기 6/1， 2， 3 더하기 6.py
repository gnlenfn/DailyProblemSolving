import sys
input = sys.stdin.readline

MOD = 1_000_000_009
dp = [0, 1, 2, 2, 3, 3, 6] + [0] * 100_000  # dp로 전체 값 먼저 다 구해
for i in range(7, 100001):
    dp[i] = (dp[i - 6] + dp[i - 4]+ dp[i - 2]) % MOD

for _ in range(int(input())):
    n = int(input())
    print(dp[n])  # 테스트케이스 dp 배열에서 가져다가 출력
    