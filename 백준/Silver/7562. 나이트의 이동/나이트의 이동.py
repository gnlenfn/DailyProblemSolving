import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    q = deque()
    q.append((row_start, col_start))
    visited[row_start][col_start] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in zip([1, 2, 2, 1, -1, -2, -2, -1], [2, 1, -1, -2, 2, 1, -1, -2]):  # 나이트가 이동가능한 곳 8개
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] != -1:
                continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


t = int(input())  
for _ in range(t):
    n = int(input())  # 체스판 한 변 길이
    row_start, col_start = map(int, input().split())  # 나이트 위치 좌표
    row_target, col_target = map(int, input().split())  # 목표 위치

    board = [[0] * n for _ in range(n)]
    visited = [[-1] * n for _ in range(n)]

    bfs()

    print(visited[row_target][col_target])