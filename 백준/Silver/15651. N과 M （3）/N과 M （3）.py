n, m = map(int, input().split())

selected = [0 for _ in range(m)]

def recur(num):
    if num == m:
        # m개 고름
        for x in selected:
            print(x, end=" ")
        print()
    else:
        for cand in range(1, n+1):
            selected[num] = cand
            recur(num + 1)
            selected[num] = 0

recur(0)