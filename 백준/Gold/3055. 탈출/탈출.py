import sys 
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split());
mat = [input().strip() for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
water_dist = [[-1] * m for _ in range(n)]


def flood():
    q = deque()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '*':
                q.append((i, j))
                visit[i][j] = 1
                water_dist[i][j] = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 좌표 범위 초과
                continue
            if mat[nx][ny] != '.':  # 빈칸이 아니면 물이 넘칠 수 없음
                continue
            if visit[nx][ny]:  # 이미 방문한 곳은 안감
                continue

            q.append((nx, ny))
            visit[nx][ny] = 1
            water_dist[nx][ny] = water_dist[x][y] + 1  # 현재 칸에 물이 몇 번째 턴에 차는지 기록 -> 이후 고슴도치 이동 시 사용


def move():
    q = deque()
    for i in range(n):
        for j in range(m):
            visit[i][j] = 0
            if mat[i][j] == 'S':
                q.append((i, j))
                visit[i][j] = 1
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 좌표 범위 초과
                continue
            if mat[nx][ny] != "." and mat[nx][ny] != 'D':  # 빈칸이 아니거나 비버굴이 아니면 방문 안해
                continue
            if water_dist[nx][ny] != -1 and water_dist[nx][ny] <= dist[x][y] + 1:  # 물이 이미 넘친곳이거나 다음 턴에 물에 잠길 곳
                continue
            if visit[nx][ny]:  # 이미 방문한 좌표
                continue

            q.append((nx, ny))
            visit[nx][ny] = 1
            dist[nx][ny] = dist[x][y] + 1


flood()  # 물 먼저 이동
move()   # 고슴도치 이동

for i in range(n):
    for j in range(m):
        if mat[i][j] == 'D':
            if dist[i][j] == -1:
                print("KAKTUS")
            else:
                print(dist[i][j])