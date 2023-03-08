import sys
input = sys.stdin.readline

from collections import defaultdict
sys.setrecursionlimit(100000)

tree = defaultdict(list)
n = int(input())
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    tree[a].append((w, b))
    tree[b].append((w, a))

visited = [0] * (n + 1)
def dfs(node, weight):  # DFS로 leaf node까지의 거리 모두 구하기
    visited[node] = (weight, node)

    for next_node in tree[node]:
        w, nxt = next_node
        if not visited[nxt]:
            dfs(nxt, weight + w)

dfs(1, 0)
farthest = sorted(visited[1:], reverse=True)[0]  # 가장 먼 노드를 찾았다

visited = [0] * (n + 1)
dfs(farthest[1], 0)  # 가장 먼 노드로부터 다시 DFS 실행

ans = sorted(visited[1:], reverse=True)[0]  # 두 번의 DFS로 지금이 가장 큰 두 노드 구할 수 있고 
print(ans[0])  # 지름 길이도 나옴
