import sys
input = sys.stdin.readline

from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(list)
ans = [0] * n  # n 명의 케빈 베이컨 수 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [-1] * (n + 1)
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cur = q.popleft()

        for node in graph[cur]:
            if visited[node] != -1:
                continue
            
            visited[node] = visited[cur] + 1
            q.append(node)

    visited[0] = 0  # 0번 인덱스는 없는걸로 쳐야 하기 때문에 -1 제거
    return sum(visited)  # 케빈 베이컨 수 리턴


min_val, min_idx = bfs(1), 1   # 1번 사람의 케빈 베이컨 수가 가장 작다고 두고 시작
for i in range(2, n + 1):
    val = bfs(i)
    if min_val > val:
        min_val, min_idx = val, i  # 모든 사람의 케빈 베이컨 수를 구하면서 바로바로 최소값을 찾는다

print(min_idx)
