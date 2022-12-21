"""
input: 이름 국어 영어 수학

국어 내림차순
영어 오름차순
수학 내림차순
이름 사전순

"""
import sys

n = int(input())
grades = []
for _ in range(n):
    student = sys.stdin.readline().split()
    name = student[0]
    korean, english, math = map(int, student[1:])  # 점수 숫자형으로

    grades.append((-korean, english, -math, name)) # 내림차순을 위한 음수화

grades.sort()

for student in grades:
    print(student[3])