import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = [1, 1]

    while queue:
        x, y, broke = queue.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if visited[nx][ny][broke] != -1:
                continue

            if not broke and mat[nx][ny]:
                queue.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][0] + 1    

            if mat[nx][ny]:
                continue
            queue.append((nx, ny, broke))
            visited[nx][ny][broke] = visited[x][y][broke] + 1

    ret = visited[n - 1][m - 1]
    if sum(ret) == -2:
        return -1
    
    return min(ret) if min(ret) >= 0 else max(ret)

print(bfs())
