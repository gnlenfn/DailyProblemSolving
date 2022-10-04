n = int(input())
mat = [list(map(int, list(input()))) for _ in range(n)]
check = [[0] * n for _ in range(n)]
# dx[0] dy[0] -> right
# dx[1] dy[1] -> left
# dx[2] dy[2] -> down
# dx[3] dy[3] -> up
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def blob(x, y, c):
    check[x][y] = 1
    global num
    if mat[x][y] == 1:
        num += 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if check[nx][ny] == 0 and mat[nx][ny] == 1:
                blob(nx, ny, c)
                
cnt = 1
numlist = []
num =0

for a in range(n):
    for b in range(n):
        if mat[a][b] == 1 and check[a][b] == 0:
            blob(a, b, cnt)
            numlist.append(num)
            num = 0     
            
print(len(numlist))
for n in sorted(numlist):
    print(n)