import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))

w.sort()
ans = float("-inf")
if len(w) % 2:
    for x, y in zip(w[:-1], reversed(w[:-1])):
        ans = max(ans, x + y)

else:
    for x, y in zip(w, reversed(w)):
        ans = max(ans, x + y)

print(ans)