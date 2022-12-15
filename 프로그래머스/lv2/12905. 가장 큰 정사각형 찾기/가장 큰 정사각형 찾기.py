def solution(board):
    answer = 0
    size = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            size[i+1][j+1] = board[i][j]

    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):
            if size[i][j] != 0:
                size[i][j] = min([size[i-1][j], size[i][j-1], size[i-1][j-1]]) + 1
                answer = max(answer, size[i][j])
    
    return answer ** 2