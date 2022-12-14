def solution(rows, columns, queries):    
    mat = [[ i + columns * j for i in range(1, columns + 1)]  for j in range(rows)]
    answer = []
    for x1, y1, x2, y2 in queries:
        answer.append(rot_matrix(x1-1, y1-1, x2-1, y2-1, mat))
        
    return answer

def rot_matrix(x1, y1, x2, y2, arr):
    init = arr[x1][y1]
    min_val = float("inf")
    
    # left
    for k in range(x1, x2):
        arr[k][y1] = arr[k+1][y1]
        min_val = min(arr[k+1][y1], min_val)
        
    # bottom
    for k in range(y1, y2):
        arr[x2][k] = arr[x2][k+1]
        min_val = min(arr[x2][k], min_val)
    
    # right
    for k in range(x2, x1, -1):
        arr[k][y2] = arr[k-1][y2]
        min_val = min(arr[k-1][y2], min_val)
        
    # top
    # init이 들어갈 자리 제외
    for k in range(y2, y1+1, -1):
        arr[x1][k] = arr[x1][k-1]
        min_val = min(arr[x1][k-1], min_val)     
    
    # 왼 - 아래 - 오른쪽 - 위 순서 잘 지켜줘
        
    arr[x1][y1+1] = init
    min_val = min(min_val, init)
    return min_val