from collections import defaultdict

def solution(n, wires):
    answer = float("inf")
    global tree, cnt
    tree = defaultdict(list)
    
    for x, y in wires:
        tree[x].append(y)
        tree[y].append(x)
    
    for x, y in wires:
        tree[x].remove(y)
        tree[y].remove(x)
        
        cnt = 0
        dfs(1, [])
        
        answer = min(answer, abs(n - 2 * cnt))
        
        tree[x].append(y)
        tree[y].append(x)
    return answer

def dfs(start, visit):
    global cnt
    visit.append(start)
    cnt += 1
    for i in tree[start]:
        if i not in visit:
            dfs(i, visit)