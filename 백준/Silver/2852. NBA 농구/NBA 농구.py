import sys
input = sys.stdin.readline

t = int(input())
score = 0
win_t = [0, 0]

current = 0
for _ in range(t):
    team, tick = input().split()
    team = int(team)
    minute, sec = map(int, tick.split(":"))
    times = 60 * minute + sec
    
    draw = score == 0
    if not draw:
        idx = 0 if score > 0 else 1
        win_t[idx] += (times - current)
    current = times

    if team == 1:
        score += 1
    else:
        score -= 1

if score:
    idx = 0 if score > 0 else 1
    win_t[idx] += 48 * 60 - current

for i in range(2):
    print(f"{win_t[i] // 60:02d}:{win_t[i] % 60:02d}")


