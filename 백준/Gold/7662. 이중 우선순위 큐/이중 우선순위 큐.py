import sys
input = sys.stdin.readline

import heapq

t = int(input())
for _ in range(t):
    k = int(input())  # 연산의 수
    max_heap = []
    min_heap = []
    visited = [0] * k
    for idx in range(k):
        op, num = input().split()
        num = int(num)
        
        if op == "I":
            heapq.heappush(min_heap, (num, idx))  # 최소힙 삽입
            heapq.heappush(max_heap, (-num, idx))  # 최대힙 삽입 / 삽입 시 인덱스 같이 삽입
            visited[idx] = 1  # 몇 번째로 들어온 값인지 저장 -> 이후 삭제 동기화 시 사용
            # visited[idx] = 1이면 최소힙에 있는 값 -> 최대힙에도 있어야함
            # visited[idx] = 0이면 최대힙에서 모두 삭제해야 동기화 됨
            # idx는 들어온 순서를 나타내고 같은 순서에 들어온 값은 한쪽에 없다면 나머지 한쪽도 삭제해야 동기화 가능
            
        elif num == 1:  # 최대값 삭제
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)  # 동기화 작업 -> 최소힙에 없는 값 삭제

            # 이제 진짜 최대힙에서 최대값 삭제
            if max_heap:
                tmp = heapq.heappop(max_heap)[1]  # 튜플의 1번 인덱스가 들어온 순서
                visited[tmp] = 0
            
        else: # 최소값 삭제
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)

            # 최소힙에서 숫자 삭제
            if min_heap:
                tmp = heapq.heappop(min_heap)[1]
                visited[tmp] = 0
    
    # 마지막 동기화
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap) 

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")