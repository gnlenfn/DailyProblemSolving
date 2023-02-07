nums = list(input())
L = len(nums)

dp = [0] * (L+1)
dp[0] = 1

if nums[0] == "0":
    dp[1] = 0
else:
    dp[1] = 1
    
for i in range(2, L+1):
    if 0 < int(nums[i-1]):
        dp[i] = dp[i-1]
    if 10 <= int(nums[i-2]+nums[i-1]) <= 26:
        dp[i] += dp[i-2]
        
print(dp[-1] % 1000000)