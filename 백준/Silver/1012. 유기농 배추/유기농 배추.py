import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)  # 파이썬 재귀 깊이 제한은 1000

def dfs(row, col):
    visited[row][col] = 1
    for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        nx, ny = row + dx, col + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(nx, ny)



t = int(input())    
for _ in range(t):
    n, m, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    # 배추 심기
    for _ in range(k):
        r, c = map(int, input().split())
        grid[r][c] = 1
    
    # flood fill
    ans = 0 
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:  # 해당 칸이 배추가 있고 방문하지 않았으면 dfs실행
                dfs(i, j)
                ans += 1  # dfs가 끝났다? flood fill 한 칸 완료

    print(ans)      
