import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)
n, m = map(int, input().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]


def dfs(row, col):  # floodfill DFS
    visited[row][col] = 1
    for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        nx, ny = row + dx, col + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue
        dfs(nx, ny)


def count_water(row, col):  # 주위에 0이 몇개인지
    cnt = 0
    for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        nx, ny = row + dx, col + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            cnt += 1
    
    return (row, col, cnt)


land = 1
year = 0
while land < 2 and land > 0:  # 0개가 되거나 2개가 되면 멈춤
    land = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] > 0:
                dfs(i, j)
                land += 1

    if land > 1:  # 두 조각 이상이면 끝
        print(year)
        break      

    melt = []  # 올해 얼마나 녹을지 기록
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                melt.append(count_water(i, j))
    while melt:  # 기록한 만큼 녹아내림
        row, col, c = melt.pop()
        graph[row][col] -= c
        if graph[row][col] < 0:  # 0보다 작아지면 0으로
            graph[row][col] = 0
    
    year += 1

else:  # 빙하가 전부 사라지면 0 출력
    print(0)
