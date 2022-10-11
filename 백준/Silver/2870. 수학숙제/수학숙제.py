import sys
input = sys.stdin.readline

n = int(input())

alph = []
for _ in range(n):
    word = input()
    tmp = ''
    for w in word:
        if w.isnumeric():
            tmp += w
        else:
            if tmp:
                alph.append(int(tmp))
            tmp = ''
    if tmp:
        alph.append(int(tmp))


for n in sorted(alph):
    print(n)