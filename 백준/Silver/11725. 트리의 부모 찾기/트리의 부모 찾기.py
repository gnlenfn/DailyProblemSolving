import sys
input = sys.stdin.readline

from collections import defaultdict, deque

""" BFS로 탐색하면서,
    다음 노드의 부모를 모두 현재로 기록한다,
    그 후 부모 노드를 기록한 리스트를 순회하며 출력
"""

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append(nxt)
                parent[nxt] = cur  # 다음 노드의 부모 노드는 현재 노드

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
parent = [0] * (n + 1)

bfs()

for i in range(2, n + 1):
    print(parent[i])