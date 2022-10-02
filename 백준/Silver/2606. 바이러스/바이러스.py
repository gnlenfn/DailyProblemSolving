from collections import defaultdict

n = int(input())
m = int(input())

grid = defaultdict(list)
visited = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    grid[x].append(y)
    grid[y].append(x)

def dfs(node):
    for v in grid[node]:
        if not visited[v]:
            visited[v] = 1
            dfs(v)

dfs(1)
print(sum(visited) - 1)
