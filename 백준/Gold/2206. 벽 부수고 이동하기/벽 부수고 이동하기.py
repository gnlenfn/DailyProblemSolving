import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
"""
visited[x][y][0]은 아직 벽을 한번도 안 부순 경우, visited[x][y][1]은 한 번 부순 경우(더이상 못부숨)
"""

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = [1, 1]

    while queue:
        x, y, broke = queue.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 격자 볌위 초과
                continue
            
            if visited[nx][ny][broke] != -1:  # 최단거리 아님
                continue

            if not broke and mat[nx][ny]:  # 부순적이 없고 벽을 만남 -> 부술 수 있음
                queue.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][0] + 1    
                # 벽을 부수는 경우로 이동 거리 추가

            if mat[nx][ny]: # 벽 못지나감
                continue

            queue.append((nx, ny, broke))
            visited[nx][ny][broke] = visited[x][y][broke] + 1
            # 벽 부수기 여부에 관계없이 동일한 방법으로 이동 (부수기 현황 그대로 유지)

    ret = visited[n - 1][m - 1]  # 목적지
    if sum(ret) == -2:
        return -1  # 목적지 도착 불가 -> [-1, -1]
    
    return min(ret) if min(ret) >= 0 else max(ret)  
    # 최단거리 출력, but 작은값이 -1인 경우 0 이상인 값 출력 
    # 둘다 -1이 아니라면 아무튼 도착 가능이기 때문에 -1 아닌 값 출력해야함

print(bfs())
