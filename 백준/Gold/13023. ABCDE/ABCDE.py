import sys
input = sys.stdin.readline

from collections import defaultdict

def dfs(node, cnt):
    global flag
    if cnt == 4:
        flag = True
        return 
    
    for nxt in graph[node]:
        if flag:
            return
        if not visited[nxt]:
            visited[node] = 1
            dfs(nxt, cnt + 1)
            visited[node] = 0

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

flag = False
visited = [0] * n
for idx in range(n):
    visited[idx] = 1
    dfs(idx, 0)
    visited[idx] = 0

    if flag:
        break

print(int(flag))