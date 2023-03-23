import sys
input = sys.stdin.readline

board = [list(map(int, input().strip().split())) for _ in range(5)]
calls = []
for _ in range(5):
    for n in list(map(int, input().strip().split())):
        calls.append(n)


def remove_num(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0


def check_bingo():
    bingo = 0
    for row in board:
        if not sum(row):
            bingo += 1
    
    for col in list(zip(*board)):
        if not sum(col):
            bingo += 1

    left, right = 0, 0
    for i in range(5):
        left += board[i][i]
        right += board[i][4 - i]

    if not left:
        bingo += 1
    if not right:
        bingo += 1

    return bingo
    


for idx, c in enumerate(calls, 1):
    remove_num(c)

    bingo = check_bingo()


    if bingo >= 3:
        print(idx)
        break