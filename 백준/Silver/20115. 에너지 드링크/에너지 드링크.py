import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))

drinks.sort()
ans = drinks[-1]
for d in drinks[:-1]:
    ans += d / 2

print(ans)
