import sys
input = sys.stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)
current_max = float("-inf")
for idx, w in enumerate(ropes, 1):
    current_max = max(current_max, w * idx)

print(current_max)