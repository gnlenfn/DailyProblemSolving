import sys
input = sys.stdin.readline

import heapq

t = int(input())
for _ in range(t):
    m = int(input())
    nums = []
    for _ in range(m // 10 + 1):
        tmp = list(map(int, input().split()))
        nums += tmp

    upper = []  # 중앙값보다 크거나 같은 수들
    lower = []  # 중앙값보다 작은 수들
    med = []
    # upper의 최소값이 중앙값이 되도록 
    for idx, n in enumerate(nums, 1):
        heapq.heappush(upper, n)  # 먼저 새 값을 upper로 삽입
        heapq.heappush(lower, -heapq.heappop(upper)) # upper의 최소값을 lower로 이동

        if len(upper) < len(lower):  # upper의 최소값이 중앙값이다 -> upper의 길이가 항상 lower보다 길거나 같다
            heapq.heappush(upper, -heapq.heappop(lower))  # lower의 값을 upper로 이동시켜 길이 상태를 유지시킴

        if idx % 2:
            med.append(upper[0])

    print(len(med))  # 중앙값 갯수 출력
    for idx, val in enumerate(med, 1):
        print(val, end=" ")
        if idx % 10 == 0:  # 한 줄에 중앙값 10개 씩 출력
            print()
    print()

