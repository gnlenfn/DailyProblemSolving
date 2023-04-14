from collections import deque
def solution(order):
    answer = 0
    stack = []
    belt = deque([i for i in range(1, len(order) + 1)])
    order = deque(order)
    
    while belt:
        if order[0] == belt[0]:
            belt.popleft()
            order.popleft()
            answer += 1
        
        elif stack and stack[-1] == order[0]:
            stack.pop()
            order.popleft()
            answer += 1
            
        else:
            stack.append(belt[0])
            belt.popleft()
    
    while stack and stack[-1] == order[0]:
        stack.pop()
        order.popleft()
        answer += 1
        

        
    return answer