import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n):
    word = sys.stdin.readline().strip()
    words.append(word)
    
words.sort(key=lambda x : (len(x), x))

for idx in range(n):
    if idx == 0 or words[idx] != words[idx - 1]:
        print(words[idx])