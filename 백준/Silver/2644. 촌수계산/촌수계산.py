from collections import defaultdict

n = int(input())
start, end = map(int, input().split())
tree = defaultdict(list)
visited = [0] * (n + 1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(node, target):
    global cnt
    if node == target:
        return

    for n in tree[node]:
        if not visited[n]:
            visited[n] = visited[node] + 1
            dfs(n, target)

cnt = 0
dfs(start, end)
if visited[end]:
    print(visited[end])
else:
    print(-1)