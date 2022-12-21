from collections import Counter
import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

ret = Counter(nums).most_common()
ret.sort(key=lambda x: (-x[1], x[0]))

print(ret[0][0])
