import sys

n = int(sys.stdin.readline())

words = []
used = set()
for _ in range(n):
    word = sys.stdin.readline().strip()

    if word not in used:
        words.append((len(word), word))
        used.add(word)

words.sort()

for _, word in words:
    print(word)