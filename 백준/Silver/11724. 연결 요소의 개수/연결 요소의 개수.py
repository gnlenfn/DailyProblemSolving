import sys
input = sys.stdin.readline

from collections import defaultdict
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = defaultdict(list)
visited = [0] * (n + 1)
# 무방향 그래프, 양방향 이동 가능
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    """
    연결요소 -> 그래프가 몇 개로 나눠져있나?
    flood fill
    """

def dfs(node):
    visited[node] = 1
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)
