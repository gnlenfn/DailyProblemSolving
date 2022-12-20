from itertools import combinations

l, c = map(int, input().split())
alpha = list(input().split())
vowel = set()
constant = set()
for e in alpha:
    if e in 'aeiou':
        vowel.add(e)
    else:
        constant.add(e)

candidates = combinations(alpha, l)
answer = set()

for cand in candidates:
    ret = "".join(sorted(cand))
    if not set(ret) & vowel:
        continue

    if len(set(ret) & constant) < 2:
        continue

    answer.add(ret)

for a in sorted(list(answer)):
    print(a)