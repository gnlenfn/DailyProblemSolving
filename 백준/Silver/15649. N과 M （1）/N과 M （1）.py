from itertools import permutations
n, m = map(int, input().split())

ret = permutations(range(1, n+1), m)

for r in ret:
    for e in r:
        print(e, end=" ")
    print()