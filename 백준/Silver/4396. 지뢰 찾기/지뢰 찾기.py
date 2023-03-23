import sys
input = sys.stdin.readline

n = int(input())
mines = [list(input().strip()) for _ in range(n)]
bomb = [(row, col) for row in range(n) for col in range(n) if mines[row][col] == "*"]
played = [list(input().strip()) for _ in range(n)]
board = [['.'] * n for _ in range(n)]

def check_mines(row, col):
    cnt = 0
    for dx, dy in zip([1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, -1, 1]):
        nx, ny = row + dx, col + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if mines[nx][ny] == "*":
            cnt += 1
    
    return cnt


def sol():
    is_safe = True
    for row in range(n):
        for col in range(n):
            if played[row][col] == "x": 
                mcount = check_mines(row, col)
                board[row][col] = str(mcount)
            if mines[row][col] == "*" and played[row][col] == 'x':
                is_safe = False
    
    if not is_safe:
        for row, col in bomb:
            board[row][col] = "*"

    for ret in board:
        print("".join(ret))

sol()
