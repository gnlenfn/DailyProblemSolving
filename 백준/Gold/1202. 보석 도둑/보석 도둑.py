import sys
input = sys.stdin.readline

import heapq

n, k = map(int, input().split())

jewels = []
for _ in range(n): # 보석 무게 / 가치
    m, v = map(int, input().split())
    jewels.append((m, v))

bags = []
for _ in range(k):  # 가방 허용 무게
    w = int(input())
    bags.append(w)

jewels.sort() # 보석 무게 낮은 것 부터 꺼내기
bags.sort() # 가방 허용 무게 작은 것 부터 채우기

ret = []
ans = 0
idx = 0
for bag in bags:  # 허용 무게가 적은 가방부터 채울거임
    while idx < n and jewels[idx][0] <= bag: # 가방 수용 무게보다 작은 무게를 가진 모든 보석을 heap에 저장
        heapq.heappush(ret, -jewels[idx][1])  # 꺼낼때는 가치가 가장 높은 것 부터 꺼내야 하므로 최대힙 구성
        idx += 1  # 보석 체크할때마다 다음 보석으로 넘어가
    
    if ret:  # heap에 무언가 값이 들어있으면, 
        # 위에서 heap에 추가하지 않았더라도,
        # 혹은 위에서 추가한 것 보다 이전 단계에서 추가한 보석 가치가 더 높을 수도 있음
        # 가방에 최소 하나는 들어가야 하기 때문에 넣을 보석이 있다면 항상 1개 최대값꺼냄
        ans -= ret[0]  # 최대힙 음수로 넣었기 때문에 뺄셈으로 
        heapq.heappop(ret)

print(ans)