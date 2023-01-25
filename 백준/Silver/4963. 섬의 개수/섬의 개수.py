import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(row, col):
    visited[row][col] = 1

    for dx, dy in zip([0, 0, 1, -1, 1, 1, -1, -1], [1, -1, 0, 0, 1, -1, 1, -1]):  # 대각선 이동까지 총 8개 방향
        nx = row + dx
        ny = col + dy

        if nx < 0 or nx >= h or ny < 0 or ny >= w:  # 좌표 범위 초과
            continue
        if visited[nx][ny] or grid[nx][ny] == 0:  # 이미 방문
            continue
        
        dfs(nx, ny)
    
    return 1

while True:
    w, h = map(int, input().split())
    if not (w + h):  # 입력이 0 0
        break

    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    ans = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j] == 1:
                ans += dfs(i, j)
    
    print(ans)