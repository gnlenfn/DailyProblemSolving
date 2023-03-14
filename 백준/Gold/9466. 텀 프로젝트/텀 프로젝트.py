import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
"""_summary_
현재 노드에서 DFS 실행해서 자기 자신으로 돌아올 수 있는 사이클 있으면 True, 없으면 False
answer : (전체 노드 수) - (사이클의 노드 수)
"""

def dfs(node):
    global ret

    visited[node] = 1
    cycle.append(node)
    nxt = adj[node]

    if visited[nxt]:
        if nxt in cycle:
            # 사이클 만들어짐
            ret += cycle[cycle.index(nxt):] # 사이클 이루는 부분만 팀임
        return
    else:
        dfs(nxt)

t = int(input())
for _ in range(t):
    n = int(input())

    adj = [0] + list(map(int, input().strip().split()))
    ret = []
    visited = [0] * (n + 1)
    for idx in range(1, n + 1):
        if not visited[idx]:
            cycle = []
            dfs(idx)    

    print(n - len(ret))  # 중복멤버 제거

    