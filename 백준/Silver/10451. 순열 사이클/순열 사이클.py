from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def dfs(x):
    for node in grid[x]:
        if not visited[node]:
            visited[node] = 1
            dfs(node)
    return 1


t = int(input())

for _ in range(t):
    n = int(input())
    p = map(int, input().split())
    grid = defaultdict(list)
    ret = 0

    for a, b in zip(range(1, n+1), p):
        grid[a].append(b)
    visited = [0] * (n + 1)

    for i in range(1, n+1):
        if not visited[i]:
            ret += dfs(i)

    print(ret)
