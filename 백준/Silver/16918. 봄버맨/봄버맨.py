r, c, n = map(int, input().strip().split())
mat = [list(input()) for _ in range(r)]  # 0초의 모습

def find_bomb():
    coord = []
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 'O':
                coord.append((i, j))
    return coord


def boom(bombs):
    for row, col in bombs:
        for dx, dy in zip([0, 0, 0, 1, -1], [0, 1, -1, 0, 0]):  # 현재위치, 상, 하, 좌, 우 폭발
            nx, ny = row + dx, col + dy
            if 0 <= nx < r and 0 <= ny < c:
                mat[nx][ny] = "."


def fill():
    map = [["O"] * c for _ in range(r)]
    return map


bombs = find_bomb()
for time in range(1, n + 1):
    if time == 1:  # 첫 1초 아무것도 안함
        continue

    if time % 2 == 0:  # 1초 후 빈 칸에 모두 폭탄 설치
        mat = fill()
        
    elif time % 2 == 1:  # 2턴 전에 설치한 폭탄 폭발
        boom(bombs)
        bombs = find_bomb()

        

result = ["".join(m) for m in mat]
for ret in result:
    print(ret)