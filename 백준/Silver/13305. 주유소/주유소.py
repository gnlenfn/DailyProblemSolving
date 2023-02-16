import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
ans = price[0] * dist[0]
for idx in range(1, n-1):
    min_price = min(price[idx - 1], price[idx])
    ans += dist[idx] * min_price

print(ans)
