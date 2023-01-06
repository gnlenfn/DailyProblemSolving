import sys
input = sys.stdin.readline 

from collections import defaultdict, deque

n, m, v = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
def dfs(cur):
    visited[cur] = 1
    print(cur, end=" ")

    for node in sorted(graph[cur]):
        if not visited[node]:
            dfs(node)


def bfs():
    print()
    visited = [0] * (n + 1)
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for node in sorted(graph[cur]):
            if not visited[node]:
                visited[node] = 1
                q.append(node)

    
dfs(v)
bfs()
