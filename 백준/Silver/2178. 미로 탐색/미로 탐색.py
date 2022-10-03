from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def bfs(row, col):
    global answer
    queue = deque([(row, col)])
    visited[row][col] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
        

bfs(0, 0)
print(visited[n-1][m-1])