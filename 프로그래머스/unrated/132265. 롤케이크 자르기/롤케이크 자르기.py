from collections import Counter, defaultdict

def solution(topping):
    answer = 0
    left, right = defaultdict(int), dict(Counter(topping))
    
    for top in topping:
        if len(left) == len(right):
            answer += 1
        
        right[top] -= 1
        if not right[top]:
            del right[top]
            
        left[top] += 1
            
    return answer