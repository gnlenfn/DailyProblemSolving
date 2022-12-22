from collections import defaultdict

n = int(input())
answer = 0
dots = defaultdict(list)

for _ in range(n):
    num, color = map(int, input().split())
    dots[color].append(num)   # 색깔별로 점 위치 기록

for col in dots.keys():
    target = sorted(dots[col])  # 오름차순 정렬하여 비교할 것
    answer += target[1] - target[0]  # 첫 화살표

    for i in range(1, len(target) - 1):
        answer += min(target[i] - target[i-1], target[i+1] - target[i])
    
    answer += target[-1] - target[-2]  # 마지막 화살표

print(answer)