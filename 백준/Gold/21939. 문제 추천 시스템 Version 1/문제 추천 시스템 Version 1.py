import sys
input = sys.stdin.readline

import heapq

n = int(input())
max_heap = []
min_heap = []
visited = dict()  # visited[문제번호] = 1 or 0 / 1이면 들어있는 문제, 0이면 해결한 문제

for _ in range(n):  # 이미 추천 리스트에 있는 문제 삽입
    p, l = map(int, input().split())
    heapq.heappush(max_heap, (-l, -p))  # (난이도, 문제번호, 들어온 순서)
    heapq.heappush(min_heap, (l, p))   # 들어온 순서는 최대힙, 최소힙 동기화 시 사용
    # 이떄 난이도가 동일하면
    # 어려운 것 추천은 문제 번호가 큰 순
    # 쉬운 것 추천은 문제 번호가 작은 것 순
    visited[p] = 1

m = int(input())
for _ in range(n, m + n):
    com, *nums = input().split()

    if com == "add":
        p, l = map(int, nums)

        # 동기화 작업
        while not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while not visited[-max_heap[0][1]]:
            heapq.heappop(max_heap)

        heapq.heappush(max_heap, (-l, -p))
        heapq.heappush(min_heap, (l, p))
        visited[p] = 1  # 방문기록을 위해 0 or 문제번호 기록 -> solved 해결 위해 문제번호로 기록
    
    elif com == "recommend":
        # 추천만 했지 아직 푼건 아니기 때문에 추천문제로 출력 후 visited처리 하지는 않음
        l = int(nums[0])
        if l == 1:
            while max_heap and not visited[-max_heap[0][1]]:  # 이미 최소힙에서 삭제된 것 삭제(동기화)
                heapq.heappop(max_heap)
            
            if max_heap:
                print(-max_heap[0][1])  # 추천만 하고 푼건 아니므로 출력만 하고 pop은 안해!!
        
        else:
            while min_heap and not visited[min_heap[0][1]]:  # 이미 최대힙에서 삭제된 것 삭제
                heapq.heappop(min_heap)
            
            if min_heap:
                print(min_heap[0][1])   # 추천만 하고 푼건 아니므로 출력만 하고 pop은 안해!!

    elif com == "solved":
        # 해결한 문제는 visited에서 0으로 처리 (0이면 추천문제 목록에서 삭제된 것)
        p = int(nums[0])
        visited[p] = 0

    