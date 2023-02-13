import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 0
strings = set()

for _ in range(n):
    s = input()
    strings.add(s)

for _ in range(m):
    target = input()
    if target in strings:
        ans += 1

print(ans)
