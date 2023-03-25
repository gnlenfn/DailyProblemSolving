n = int(input())
nums = [0] + list(map(int, input().split()))
psum = [0] * (n + 1)
for idx in range(1, n + 1):
    psum[idx] = psum[idx - 1] + nums[idx]

ans = 0
for idx in range(2, n + 1):
    ans += nums[idx] *  psum[idx - 1]

print(ans)