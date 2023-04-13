// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/118669

from collections import defaultdict
import heapq 

def solution(n, paths, gates, summits):
    answer = []
    """
    gates 에서 출발하는 다익스트라
    출발지에서 출발한 후 원래 gate로 나와야 함 
      -> 편도만 고려해도 괜찮음, 올라가면서 최소 intensity만 선택하고 그대로 돌아오면 됨
    """
    
    def get_min_intensity():
        pq = []
        visited = [float("inf")] * (n + 1)
        summit_set = set(summits)
        # 출발지 삽입
        for gate in gates:
            heapq.heappush(pq, (0, gate))
            visited[gate] = 0
        
        # djikstra
        while pq:
            intensity, node = heapq.heappop(pq)
            
            if node in summit_set or intensity > visited[node]:
                # 산봉우리 만나면 끝
                continue
            
            for w, nxt in graph[node]:
                # nxt로 이동할 때  기존보다 더 작은 intensity면 큐에 넣음
                new_intensity = max(w, intensity) 
                if new_intensity < visited[nxt]:
                    visited[nxt] = new_intensity
                    heapq.heappush(pq, (new_intensity, nxt))
        
        # 최종 결과 구하기 -> intensity최소값 == visited의 최소값, 봉우리 번호 같이 출력
        min_intensity = [0, float("inf")]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]
        
        return min_intensity
            
        
    graph = defaultdict(list)
    visited = [0] * (n + 1)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    
    
    summits.sort()
    return get_min_intensity()
