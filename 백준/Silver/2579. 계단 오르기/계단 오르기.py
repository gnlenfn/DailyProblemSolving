import sys
input = sys.stdin.readline

n = int(input())    
dp = [0] * (n + 4)  # n이 3보다 작으면 out of range
stairs = [0] * (n + 4)
for i in range(1, n + 1):
    stairs[i] = int(input())


dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]  
dp[3] = stairs[3] + max(stairs[2], stairs[1])

for i in range(4, n + 1):
    dp[i] = stairs[i] + max(dp[i - 2], dp[i - 3] + stairs[i - 1])
    # 두 칸 전에서 한 번에 현재까지 오기
    # 세 칸 전에서 두 칸 뛰고 바로 이전 칸 들렀다가 오기

print(dp[n])
