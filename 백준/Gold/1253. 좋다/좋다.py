import sys

input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))


def func(target_idx):
    l, r = 0, n - 1
    target = nums[target_idx]

    while l < r:
        if l == target_idx: l += 1
        elif r == target_idx: r -= 1
        else:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                return True
    return False

print(len([x for x in range(n) if func(x)]))