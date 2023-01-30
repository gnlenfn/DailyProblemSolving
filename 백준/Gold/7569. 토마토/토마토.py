import sys
input = sys.stdin.readline

from collections import deque

m, n, h = map(int, input().split())  # m: 가로, n: 세로, h: 높이
boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]  # 3차원 형태로 행렬 구성

q = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if boxes[z][y][x] == 1:
                q.append((z, y, x, 0))  # 토마토가 있는 위치 기록, 그리고 그 위치는 익는데 0일 걸림

while q:
    z, y, x, days = q.popleft()

    for dz, dy, dx in zip([1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]):  # 각 위치로 한 칸씩 이동 가능
        nz, ny, nx = z + dz, y + dy, x + dx
        ndays = days + 1

        if 0 <= ny < n and 0 <= nx < m and 0 <= nz < h:
            if boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = 1
                q.append((nz, ny, nx, ndays))
# while문이 끝나면 마지막으로 도착하는 점의 days가 저장됨 -> 최소 days만큼 걸림(최대값)

for i in range(h):
    for j in range(n):
        if boxes[i][j].count(0) > 0:  # 하나라도 안 익은 토마토가 있으면 -1 출력
            days = -1
            break

print(days)