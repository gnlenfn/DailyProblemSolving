import sys
input = sys.stdin.readline

from collections import deque

n, m, t = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mat[i][j] == 2:
            gram = (i, j)

def bfs(start, target):
    ret = 10005
    visited = [[-1] * m for _ in range(n)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + dx, y + dy

            if nx == target[0] and ny == target[1]: # 공주칸 도착
                return min(ret, visited[x][y] + 1)

            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 그래프 범위 초과
                continue
            if visited[nx][ny] != -1:  # 이미 방문 했는지 확인
                continue

            if mat[nx][ny] == 0:  # 해당 칸으로 이동 가능
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            
            elif mat[nx][ny] == 2:  # 그램 획득
                visited[nx][ny] = visited[x][y] + 1
                ret = min(ret, visited[nx][ny] + abs(n - 1 - nx) + abs(m - 1 - ny))
                # 그램 발견하면 해당 위치에서 (n, m)까지 맨해튼거릭 바로 구해서 더하면 됨
                # 그것과 현재의 ret중 최소값을 저장

    return ret
        

ans = bfs((0, 0), (n-1, m-1))
print("Fail" if ans > t else ans)