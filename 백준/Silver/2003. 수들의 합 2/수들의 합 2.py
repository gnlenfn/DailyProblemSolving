import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
ans = 0

while left <= right and right < n:
    ret = sum(nums[left: right+1])

    if ret < m:
        right += 1
    elif ret > m:
        left += 1
    else:
        ans += 1
        right += 1

    if left > right:
        right += 1
print(ans)