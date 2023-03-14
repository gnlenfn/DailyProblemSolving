import sys
input = sys.stdin.readline

"""_summary_
- BFS로 최단거리를 찾아갈 것
- 인접리스트 graph를 정렬하면 사전순 가장 먼저 오는 노드부터 탐색 시작
- path 리스트는 이전 노드를 저장한다
    - 다시 돌아가는 경로 찾을 때 같은곳 또 방문 하지 않기 위해 사용
    - visited를 모두 False으로 만든 후 이미 방문했던 곳은 다시 True로
- start -> end BFS의 최단거리 + end -> start BFS 최단거리 
- 두 거리의 합이 정답
"""

from collections import defaultdict, deque

graph = defaultdict(list)
n, m = map(int, input().split())
visited = [0] * (n + 1)
path = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
start, end = map(int, input().split())

for node in graph:  # 인접리스트 오름차순 정렬
    graph[node] = sorted(graph[node])

def bfs(depart, arrive):
    queue = deque()
    visited[depart] = 1
    queue.append((depart, 0))  # (노드, 거리)

    while queue:
        cur, dist = queue.popleft()

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = 1
                queue.append((nxt, dist + 1))
                path[nxt] = cur  # 이전 노드를 저장 -> 돌아가는 path 찾으면서 visited 다시 초기화 때 사용
            if nxt == arrive:
                return dist + 1

    return 0

def init():  # 돌아가는 경로 찾을 때 visited 적절하게 초기화
    visited = [0] * (n + 1)
    k = path[end]
    while True:
        visited[k] = 1
        k = path[k]
        if not k:
            break
    return visited

answer = 0
answer += bfs(start, end)
visited = init()
answer += bfs(end, start)
print(answer)