import sys
input = sys.stdin.readline

n = int(input())
ans = []

i = 0  # 5원의 갯수
while n >= 5 * i:
    tmp = n - i * 5
    if not tmp % 2:
        ans.append(i + tmp // 2)

    i += 1

if ans:
    print(min(ans))
else:
    print(-1)