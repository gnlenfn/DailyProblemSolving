import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
right, sums, answer = -1, 0, n + 1

for left in range(n):
    while right < n - 1 and sums < s: # right 인덱스니까 n-1까지
        right += 1           # -1 시작했으니까 더하면서 시작
        sums += nums[right]  # right까지의 합

    if sums >= s:
        answer = min(answer, right - left + 1)
    
    sums -= nums[left]  # left이동하므로 sum에서 다시 빼주기

if answer == n + 1:
    answer = 0
print(answer)