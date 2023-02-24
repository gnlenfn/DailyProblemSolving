import sys
input = sys.stdin.readline

import heapq

n, k = map(int, input().split())
visited = [0] * 100004
queue = []
heapq.heappush(queue, (0, n))
visited[n] = 1

while queue:
    sec, cur = heapq.heappop(queue)
    if cur == k:
        print(sec)
        break

    if cur * 2 <= 100000 and not visited[cur * 2]:
        visited[cur * 2] = 1
        heapq.heappush(queue, (sec, cur * 2))
    
    if cur + 1 <= 100000 and not visited[cur + 1]:
        visited[cur + 1] = 1
        heapq.heappush(queue, (sec + 1, cur + 1))
    
    if cur - 1 >= 0 and not visited[cur - 1]:
        visited[cur - 1] = 1
        heapq.heappush(queue, (sec + 1, cur - 1))
    

