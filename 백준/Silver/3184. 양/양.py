import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) # 최대 크기가 250x250 이라 재귀 많이 함

def dfs(row, col):
    global sheep, wolf
    if grid[row][col] == 'o':
        sheep += 1
    elif grid[row][col] == 'v':
        wolf += 1
    """DFS 순회 하면서 해당 영역(같은 울타리 내)에 늑대와 양이 몇 마리 있는지 카운트
       그 후 둘 중에 큰 값을 최종 정답에 추가
    """

    visited[row][col] = 1
    for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        nx = row + dx
        ny = col + dy

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if visited[nx][ny] or grid[nx][ny] == '#':
            continue
        
        dfs(nx, ny)


r, c = map(int, input().split())
ans = [0, 0]  # 전체 양과 늑대의 값 저장
grid = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if not visited[i][j] and grid[i][j] != '#':
            sheep, wolf = 0, 0  # 양과 늑대 초기값 (영역 별로 초기화)
            dfs(i, j)

            if sheep > wolf:
                ans[0] += sheep
            else:
                ans[1] += wolf

print(ans[0], ans[1])