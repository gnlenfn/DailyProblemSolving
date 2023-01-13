n = int(input())
cows = []
for _ in range(n):
    arr, dur = map(int, input().split())
    cows.append((arr, dur))
    
current = 0
cows.sort()
ans = cows[0][0] + cows[0][1]
for arr, dur in cows[1:]:
    ans = max(ans, arr)
    ans += dur
    
print(ans)