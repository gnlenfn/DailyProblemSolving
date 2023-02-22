import sys
input = sys.stdin.readline

from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
tomatos = []
walls = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomatos.append((i, j))
        elif box[i][j] == -1:
            walls.append((i, j))

def bfs():
    queue = deque(tomatos)
    for row, col in queue:
        visited[row][col] = 0
    for row, col in walls:
        visited[row][col] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] != -1:
                continue
            if box[nx][ny] == -1:
                continue
            
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
    
bfs()
min_val, max_val = float("inf"), float("-inf")
for ret in visited:
    min_val = min(min_val, min(ret))
    max_val = max(max_val, max(ret))

if min_val == -1:
    print(-1)
else:
    print(max_val)
