import sys
from collections import defaultdict

lines = sys.stdin.readlines()
forest = defaultdict(int)
total = 0

for line in lines:
    total += 1  # 전체 그루 수 카운트
    forest[line.rstrip()] += 1  # 현재 입력 나무 수 카운트

for tree, cnt in sorted(forest.items()):
    print(f"{tree} {cnt / total * 100:.4f}")  # 나무 이름과 백분율 소수점 4자리까지
    # 만약 100% 여도 소숫점 4자리까지 나와야 함
