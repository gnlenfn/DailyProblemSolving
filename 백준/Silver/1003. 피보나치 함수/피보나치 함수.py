import sys
input = sys.stdin.readline


def count_func(n, is_zero):
    dp = [0] * (n + 2)

    if is_zero:
        dp[0], dp[1] = 1, 0
    else:
        dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n]

for _ in range(int(input())):
    num = int(input())
    print(count_func(num, True), count_func(num, False))
    