import sys
input = sys.stdin.readline

n = int(input())
string = input()

red, blue = 0, 0
prev = string[0]
if prev == 'R':
    red += 1
else:
    blue += 1
    
for idx in range(1, n):
    cur = string[idx]
    if cur == 'R' and prev != cur:
        red += 1
        prev = 'R'
    
    if cur == 'B' and prev != cur:
        blue += 1
        prev = 'B'

print(min(red, blue) + 1)
