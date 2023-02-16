import sys
input = sys.stdin.readline

n = int(input())
t = sorted(list(map(int, input().split())))
ct = [sum(t[:idx]) for idx in range(1, n + 1)]

print(sum(ct))