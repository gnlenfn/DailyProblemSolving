import sys
input = sys.stdin.readline

a, b = map(int, input().split())

cnt = 1
while b > a:
    if str(b)[-1] == '1':
        b = int(str(b)[:-1])
    elif b % 2 == 0:
        b //= 2
    else:
        break
    
    cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)
