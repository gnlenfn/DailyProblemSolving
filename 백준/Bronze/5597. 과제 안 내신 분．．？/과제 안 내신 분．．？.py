import sys
input = sys.stdin.readline

students = {x for x in range(1, 31)}    

for _ in range(28):
    n = int(input().strip())
    students.remove(n)

for s in sorted(list(students)):
    print(s)
