import sys
input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    queue.append(int(input()))

ans = 0
for idx, tip in enumerate(sorted(queue, reverse=True)):
    if tip - idx < 0:
        continue
    ans += tip - idx

print(ans)
