import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
h, w, sr, sc, fr, fc = map(int, input().split())
sr, sc, fr, fc = sr - 1, sc - 1, fr - 1, fc - 1


walls = []
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            walls.append((i, j))

def wall_check(row, col):  # 직사각형 내에 벽이 존재하는가?
    for wr, wc in walls:
        if row <= wr < row + h and col <= wc < col + w:
            return False  # 벽 있음, 못감
    return True  # 갈 수 있음

def bfs():
    queue = deque()
    visited[sr][sc] = 0
    queue.append((sr, sc))

    while queue:
        x, y = queue.popleft()

        if x == fr and y == fc:
            return visited[fr][fc]

        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if nx + h - 1 >= n or ny + w - 1 >= m:  
                # 사각형이 격자 밖으로 벗어나지 못해
                # 좌상단 기준이기 때문에 가로, 세로만큼 늘어난 것만 체크
                continue
            if visited[nx][ny] != -1:
                continue
            if wall_check(nx, ny):  # 사각형 내에 벽이 없으면
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return -1

print(bfs())