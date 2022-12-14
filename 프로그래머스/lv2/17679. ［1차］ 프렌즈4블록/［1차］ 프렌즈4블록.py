def solution(m, n, board):
    answer = 0
    b = list(map(list,zip(*board)))        
    
    while True:
        p = remove_square(b, n, m)
        if not p:
            return answer        
        answer += p


def remove_square(b, n, m):
        poped = set()

        for i in range(1, n):
            for j in range(1, m):
                if b[i][j] == b[i][j - 1] == b[i - 1][j] == b[i - 1][j - 1] != '_':
                    poped |= set([(i, j), (i, j-1), (i-1, j), (i-1, j-1)])
                    
        for i, j in poped:
            b[i][j] = 0

        for idx, row in enumerate(b):
            blank = ["_"] * row.count(0)
            b[idx] = blank + [block for block in row if block != 0]

        return len(poped)
                


    
    