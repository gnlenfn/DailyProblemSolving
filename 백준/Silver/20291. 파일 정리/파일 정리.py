import sys
from collections import Counter

n = int(sys.stdin.readline())
files = []

for _ in range(n):
    file_name = sys.stdin.readline().strip()
    extension = file_name.split(".")[-1]
    files.append(extension)

ret = Counter(files)
ret = list(ret.items())

ret.sort()
for ex, num in ret:
    print(ex, num)