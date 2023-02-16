import sys
input = sys.stdin.readline

n = int(input())
products = []
for _ in range(n):
    products.append(int(input()))

ans = 0
products.sort(reverse=True)
for idx in range(0, n, 3):
    tmp = products[idx: idx + 3]
    if len(tmp) > 2:
        ans += sum(tmp) - min(tmp)
    else:
        ans += sum(tmp)

print(ans)
