import sys
input = sys.stdin.readline

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

m.sort(key=lambda x : (x[1], x[0]))
cnt = 0
start, end = 0, 0
for s, e in m:
    if end > s:
        continue
    
    start = s
    end = e
    cnt += 1
    
print(cnt)
