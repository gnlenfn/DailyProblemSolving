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


for i in range(1, n + 1):
    score = bfs(i)
    ans[i - 1] = score  # 1부터 n까지 사람 번호 매칭하기 때문에 인덱스는 -1 해줘야 함

min_val = min(ans)
print(ans.index(min_val) + 1)  # 인덱스를 찾기 때문에 정답은 +1 해줘야 사람에게 주어진 수 출력
