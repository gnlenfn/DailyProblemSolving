import sys
input = sys.stdin.readline

from itertools import combinations
import copy

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def dfs(row, col, arr):
    arr[row][col] = 2

    for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        nx, ny = row + dx, col + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if arr[nx][ny] == 0:
            dfs(nx, ny, arr)

def count_safe(ret):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if ret[i][j] == 0:
                cnt += 1

    return cnt

# 벽 세울 수 있는 좌표 찾기
empty = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            empty.append((i, j))

ans = 0
candidates = combinations(empty, 3)
for case in candidates:
    mat = copy.deepcopy(grid)

    # 벽 세우기
    for row, col in case:
        mat[row][col] = 1

    # dfs로 바이러스 감염
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                dfs(i, j, mat)
    
    ans = max(ans, count_safe(mat))

print(ans)

"""
BFS가 맞았을지도
"""