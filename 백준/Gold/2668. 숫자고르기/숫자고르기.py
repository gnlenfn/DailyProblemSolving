import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

from collections import defaultdict

def dfs(cur, visited):
    visited.add(cur)
    check[cur] = 1
    for nxt in graph[cur]:
        if nxt not in visited:
            dfs(nxt, visited.copy())
        else:
            result.extend(list(visited))
            return

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))


graph = defaultdict(list)
for idx, num in enumerate(nums, 1):
    graph[num].append(idx)

check = [0] * (n + 1)
result = []

for i in range(1, n + 1):
    if not check[i]:
        dfs(i, set())

print(len(result))
for k in sorted(result):
    print(k)   
