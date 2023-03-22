import sys
input = sys.stdin.readline

from collections import defaultdict

cows = defaultdict(int)
n = int(input())

cnt = 0
position = dict()
for _ in range(n):
    num, pos = map(int, input().strip().split())
    if num in position and position[num] != pos:
        position[num] = pos
        cnt += 1
    else:
        position[num] = pos
    
print(cnt)
