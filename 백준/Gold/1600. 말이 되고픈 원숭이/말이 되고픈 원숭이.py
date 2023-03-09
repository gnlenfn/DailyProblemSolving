import sys
input = sys.stdin.readline

"""
BFS로 최단거리 구하는데, 상하좌우 + 나이트이동
다만, 나이트이동 횟수를 같이 큐에 넣어 나이트이동 수를 제한한다
(0, 0)에서 (h-1, w-1)까지 이동
"""

from collections import deque

k = int(input())  # 나이트 이동 횟수
w, h = map(int, input().split())  # 가로 세로
mat = [list(map(int, input().split())) for _ in range(h)]

def bfs():
    visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
    """
    3차원인 이유:
        1
        5 3
        0 0 0 0 0
        0 0 x 0 1
        0 0 0 1 0
    위 케이스에서 x에 나이트이동으로 도착하면 목적지에 도달할 수 없다
    하지만 실제로는 x위치에 원숭이 이동 후 나이트이동 1회로 도착할 수 있음

    따라서 몇 번의 나이트이동을 했는지도 visited에서 체크하면서 간다
    """
    queue = deque()
    queue.append((0, 0, k))  # (row, col, 나이트이동)

    while queue:
        x, y, cnt = queue.popleft()
        if x == h - 1 and y == w - 1:
            return visited[x][y][cnt]
        if cnt > 0:
            for dx, dy in zip([1, 2, 2, 1, -1, -2, -2, -1], [2, 1, -1, -2, -2, -1, 1, 2]):  # 나이트이동
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= h or ny < 0 or ny >= w:  # 격자범위 초과
                    continue
                if mat[nx][ny] == 1:  # 장애물
                    continue
                if visited[nx][ny][cnt - 1]:  # 이미 방문
                    continue

                visited[nx][ny][cnt - 1] = visited[x][y][cnt] + 1
                queue.append((nx, ny, cnt - 1))

        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0, ]):  # 상하좌우 이동
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:  # 격자범위 초과
                continue
            if visited[nx][ny][cnt]:  # 이미 방문
                continue
            if mat[nx][ny] == 1:  # 장애물
                continue

            visited[nx][ny][cnt] = visited[x][y][cnt] + 1
            queue.append((nx, ny, cnt))
            

    return -1

print(bfs())
