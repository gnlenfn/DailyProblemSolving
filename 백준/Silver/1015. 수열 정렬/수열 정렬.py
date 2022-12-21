n = int(input())
a = list(map(int, input().split()))

b = [(x, i) for i, x in enumerate(a)]
b.sort()  # 비내림차순으로 정렬 -> [1, 2, 3] 됨
"""
b -> (1, 2) (2, 0) (3, 1)
"""

p = [0] * n 

for i in range(n):
    p[b[i][1]] = i

"""
문제 조건에 따라 b가 [1, 2, 3]이 되어야 하므로 그에따라 p수열 정해짐
b[p[2]] = 1 -> p[2] = 0
b[p[0]] = 2 -> p[0] = 1
b[p[1]] = 3 -> p[1] = 2

p -> [1, 2, 0]
"""

for e in p:
    print(e, end=" ")