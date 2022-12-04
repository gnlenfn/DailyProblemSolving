from collections import deque

def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def check_space(p1, p2, mat, dist):
    visited = [[0] * 5 for _ in range(5)]
    q = deque([p1])
    visited[p1[0]][p1[1]] = 1
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            nx, ny = x + dx, y + dy
            
            
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and mat[nx][ny] != 'X':
                if man_dist(p1, (nx, ny)) > dist:
                    continue
                visited[nx][ny] = 1
                q.append((nx, ny))
                
                if (nx, ny) == p2:
                    return True
    
    return False

def solution(places):
    answer = []
    for place in places:
        mat = [list(row) for row in place]
        sit = []
        for row in range(5):
            for col in range(5):
                if mat[row][col] == 'P':
                    sit.append((row, col))
        
        flag = 1
        for i in range(5):
            for j in range(i + 1, len(sit)):
                dist = man_dist(sit[i], sit[j])
                if dist > 2:
                    continue
                
                if check_space(sit[i], sit[j], mat, dist):
                    flag = 0

        answer.append(flag)

    return answer