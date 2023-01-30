import sys
input = sys.stdin.readline

from collections import deque

m, n, h = map(int, input().split())  # m: 가로, n: 세로, h: 높이
box = [list(map(int, input().split())) for _ in range(n * h)]  # 쌓아올리는 상자는 행 방향으로 늘림
# 이후 위, 아래 이동 시 n만큼 이동

tomatos = [(i, j) for j in range(m) for i in range(n * h) if box[i][j] == 1]  # 토마토가 있는 칸 찾기
visited = [[-1] * m for _ in range(n * h)]
def bfs():
    q = deque(tomatos)
    for row, col in tomatos:
        visited[row][col] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in zip([0, 0, 1, -1, n, -n], [1, -1, 0, 0, 0, 0]):  # 네 방향 이동 + 층 간 이동
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= h * n or ny < 0 or ny >= m:
                continue
            if abs(dx) != n and nx // n != x // n:  # 그냥 +n -n을 하면 상하 이동 시에 층간 이동이 발생할 수 있음
                continue
            if visited[nx][ny] != -1 or box[nx][ny] == -1:  # 이미 방문했거나 토마토가 없는 칸
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            box[nx][ny] = 1


def check_whole_boxes():
    # 모든 토마토가 익었는지 확인
    for i in range(n * h):
        for j in range(m):
            if box[i][j] == 0:
                # 하나라도 익지 않았으면 false
                return False
    return True


def count_days():
    # 최소 며칠이 거리는지 세기
    cnt = 0
    for i in range(n * h):
        tmp = max(visited[i])
        cnt = max(tmp, cnt)
    return cnt

bfs()

if check_whole_boxes():
    # 최소 며칠인지 출력
    print(count_days())
else:
    # 안 익은 토마토 있음
    print(-1)