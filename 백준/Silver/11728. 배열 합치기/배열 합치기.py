import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0
ans = []
while i < n and j < m:
    if a[i] < b[j]:
        ans.append(a[i])
        i += 1
    
    else:
        ans.append(b[j])
        j += 1

while i < n:
    ans.append(a[i])
    i += 1

while j < m:
    ans.append(b[j])
    j += 1

for num in ans:
    print(num, end=" ")
