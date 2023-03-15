import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n
dp[0] = nums[0]
for idx in range(1, n):
    dp[idx] = max(dp[idx - 1] + nums[idx], nums[idx])
    """_summary_
    dp 리스트의 현재 인덱스는 현재값과 이전 최대값 + 현재값 중 더 큰수를 저장
    - 이전 최대값 + 현재값이 현재값보다 작다? 현재값만 있어도 최대값 가능
    - 이전 최대값 + 현재값이 더 크다? 연속된 최대 합 만들어가는 중
    """
print(max(dp))
