import sys
input = sys.stdin.readline

from collections import defaultdict
import heapq

n, m, x = map(int, input().split())
graph = defaultdict(list)
INF = float("inf")

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))  # (cost, destination)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))  # (cost, destination)
    distance[start] = 0

    while queue:
        dist, cur = heapq.heappop(queue)

        if dist > distance[cur]:
            continue  # 현재 기록된 distance보다 크면 pass

        for w, nxt in graph[cur]:
            cost = dist + w
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(queue, (cost, nxt))

    return 

ret = [0] * (n + 1)
for i in range(1, n + 1):
    visited = [0] * (n + 1)  # 매번 다익스트라 실행 때마다 visited, distance 초기화
    distance = [INF] * (n + 1)
    dijkstra(i)  # i에서 다른 모든 점까지의 최단거리 구하기
    ret[i] += distance[x]  # 우리가 원하는 것은 x노드 까지의 거리 (파티로 모일 장소)

visited = [0] * (n + 1)
distance = [INF] * (n + 1)
dijkstra(x)  # 파티가 끝나고 집으로 돌아가는 최단거리 구하기
for i in range(1, n + 1):
    ret[i] += distance[i]  # 파티하러 오는데 걸릴 비용에 집으로 돌아가는 비용 더하기

print(max(ret))

