import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0
while i < n and j < m:
    if a[i] < b[j]:
        print(a[i], end=" ")
        i += 1
    
    else:
        print(b[j], end=" ")
        j += 1

while i < n:
    print(a[i], end=" ")
    i += 1

while j < m:
    print(b[j], end=" ")
    j += 1

