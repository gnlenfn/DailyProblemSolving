from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = float("-inf")
for c in combinations(cards, 3):
    if sum(c) <= m and sum(c) > answer:
        answer = sum(c)        
print(answer)