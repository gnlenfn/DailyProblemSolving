from collections import deque

def solution(x, y, n):
    """
    BFS로 최단거리 찾기
    """
    queue = deque()
    ret = [-1] * (y + 1)
    
    queue.append(x)
    ret[x] = 0
    
    while queue:
        cur = queue.popleft()
        for nxt in [cur + n, cur * 2, cur * 3]:
            if nxt > y:
                continue
            
            if ret[nxt] > 0:
                continue
            
            ret[nxt] = ret[cur] + 1
            queue.append(nxt)
    
    return ret[y]