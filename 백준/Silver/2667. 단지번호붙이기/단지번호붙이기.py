n = int(input())
grid = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dfs(row, col, count):
    visited[row][col] = 1

    for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        nx, ny = row + dx, col + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
            count = dfs(nx, ny, count + 1)
    
    return count

answer = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            num = dfs(i, j, 1)
            answer.append(num)

print(len(answer))
for n in sorted(answer):
    print(n)