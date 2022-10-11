from collections import defaultdict

n, c = map(int, input().split())
mp = {}
p = 0
for n in map(int, input().split()):
    if n in mp.keys():
        mp[n] = [mp[n][0] + 1, mp[n][1]]
    else:
        mp[n] = [1, p]
        p += 1
        

for key, val in sorted(mp.items(), key=lambda x : (-x[1][0], x[1][1])):
    for _ in range(val[0]):
        print(key, end=" ")
