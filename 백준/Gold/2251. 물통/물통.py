import sys
input = sys.stdin.readline

from collections import deque

a, b, c = map(int, input().split())
visited = [[0] * (b + 1) for _ in range(a + 1)]
answer = set()
q = deque()

def move(x, y):
    # 물 붓기는 총 6가지 가능
    # A -> B / A -> C
    # B -> A / B -> C
    # C -> A / C -> B
    if not visited[x][y]:
        visited[x][y] = 1
        q.append((x, y))

def bfs():
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        z = c - x - y # 두 개의 물 양을 알면 세 번째는 알 수 있음
        
        if not x:
            answer.add(z)

        """
        - 통에 물이 가득 찰 때 까지 or 통을 비울 때 까지 
        - target 통의 빈칸과 source 통의 물 양 중 작은 것 만큼 이동할 수 있음
        """

        # a에서 b로 물 붓기
        water = min(x, b - y) # b의 빈칸과 a에 담긴 물 중 작은것 선택
        move(x - water, y + water) # 작은 것 만큼 이동

        # a에서 c로 물 붓기
        water = min(x, c - z)
        move(x - water, y) # c로 물 이동은 b에 영향 안줌

        # b에서 a로 
        water = min(y, a - x)  
        move(x + water, y - water)  # b에서 빼고 그만큼 a에 더하고

        # b에서 c로
        water = min(y, c - z)
        move(x, y - water) # c로 물 이동은 a에 영향 안줌

        # c에서 a로
        water = min(z, a - x)
        move(x + water, y) # c로 물 이동은 b에 영향 안줌

        # c에서 b로
        water = min(z, b - y)
        move(x, y + water) # c로 물 이동은 a에 영향 안줌

bfs()
for ans in sorted(list(answer)):
    print(ans, end=" ")