import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    n = int(input().strip())
    nums = sorted(list(map(int, input().strip().split())))
    print(nums[0], nums[-1])
