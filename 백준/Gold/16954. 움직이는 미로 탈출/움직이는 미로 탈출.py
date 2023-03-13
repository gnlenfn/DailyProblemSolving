import sys
from collections import deque

input = sys.stdin.readline

maze = [[0] * 8 for _ in range(8)] + [list(input().strip()) for _ in range(8)]


def bfs():
    queue = deque()
    queue.append((7, 0))  # 첫 시작은 왼쪽 아래 모서리
    t = 0  # 몇 초가 지났는가!
    """
    1초가 지날 때 마다 슬라이딩 윈도우처럼 이동가능 격자를 한 칸씩 위로 올려 벽이 이동하는 효과!
    현재 위치나 이동할 위치의 열에 8만큼 더하고 흐른 시간 만큼 뺸다 -> 벽이 이동
    8초 이상 지나면 무조건 이동 가능해짐
    """

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if maze[x + 8 - t][y] == "#":  # 현재 위치가 벽
                continue

            for dx, dy in zip([1, -1, 0, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 0, 1, -1, 1, -1]):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= 8 or ny < 0 or ny >= 8: # 격자 볌위 초과
                    continue
                if maze[8 + nx - t][ny] == "#":  # 벽으로 이동 불가
                    continue

                if nx == 0 and ny == 7:  # 목적지 도착
                    return 1
                
                queue.append((nx, ny))
        
        if t < 8:
            t += 1

    return 0

print(bfs())
