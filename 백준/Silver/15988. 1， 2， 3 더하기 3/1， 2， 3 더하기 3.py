import sys
input = sys.stdin.readline

dp = [0] * 1000004
dp[1], dp[2], dp[3] = 1, 2, 4  # 초기값
MOD = 1_000_000_009
cur = 4  # dp에 어디까지 기록했는지 저장

for _ in range(int(input())):
    num = int(input())
    if dp[num]:  # 이미 기록했던 숫자면 바로 리턴
        print(dp[num])
    else:
        for i in range(cur, num + 1): # 이전에 기록했던 부분부터 다시 for loop 시작
            dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % MOD
        print(dp[num])
        cur = num  # 다시 어디까지 기록했나 최신화
