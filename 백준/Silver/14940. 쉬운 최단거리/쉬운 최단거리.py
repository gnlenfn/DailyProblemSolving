import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

def get_targets():
    # 원래 갈 수 없는 곳 찾기
    unreachable = []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                unreachable.append((i, j))
            if mat[i][j] == 2:
                # 목적지
                target = (i, j)
    
    return unreachable, target

def bfs(target):
    queue = deque()
    queue.append(target)
    visited[target[0]][target[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] != -1:
                continue
            if mat[nx][ny] == 0:
                continue
            
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))


def print_result(unreachable):
    for row, col in unreachable:
        visited[row][col] = 0
    
    for ret in visited:
        print(" ".join(map(str, ret)))


forbidden, arrive = get_targets()
bfs(arrive)
print_result(forbidden)
