import sys
n = int(sys.stdin.readline())
col = [0 for _ in range(n)]
answer = 0

def attack(r1, c1, r2,c2):
    # if r1 == r2:
    #     return True  # 어짜피 row별로 진행하기 때문에 체크 불필요
    if c1 == c2:
        return True
    elif (r1 + c1) == (r2 + c2): # 오른쪽 대각선
        return True
    elif (r1 - c1) == (r2 - c2): # 왼쪽 대각선
        return True
    
    return False

def recur(row):
    if row == n: # 보드 마지막까지 잘 도착 (성공)
        global answer
        answer += 1

    else:
        for cand in range(n):
            for i in range(row):
                if attack(row, cand, i, col[i]): # 다른 퀸 공격 가능 (종료)
                    break
            
            else:
                col[row] = cand
                recur(row + 1)
                col[row] = 0

recur(0)
print(answer)

