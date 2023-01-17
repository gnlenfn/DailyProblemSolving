import sys
input = sys.stdin.readline

m, n = map(int, input().split())
check = [0] * 1000001

for i in range(2, int(n ** 0.5) + 1):
    start = i * i - m % (i * i)
    if start == i * i:
        start = 0
    
    for idx in range(start, n - m + 1, i * i):
        check[idx] = 1

print(n - m + 1 - sum(check))
