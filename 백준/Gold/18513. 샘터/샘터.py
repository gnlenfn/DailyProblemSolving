import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
pools = list(map(int, input().split()))


def bfs():
    visited = set()
    queue = deque()  
    for p in pools:
        visited.add(p)  # 샘물 위치는 집 놓을 수 없음
        queue.append((p, 1))  # 샘물 위치를 먼저 큐에 넣는다, dist는 이번 위치에서 더해질 값

    distance = 0  # 불행도
    houses = 0  # 지어진 집의 수
    while queue:
        cur, dist = queue.popleft()

        for d in [1, -1]:  # 현재위치의 앞뒤로 이동 가능
            nxt = cur + d
            if nxt in visited:
                continue

            queue.append((nxt, dist + 1))
            visited.add(nxt)
            distance += dist
            houses += 1

            if houses == k:  # 집 다 지었음
                return distance

    return distance


print(bfs())
