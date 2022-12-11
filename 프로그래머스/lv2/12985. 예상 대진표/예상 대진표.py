def solution(n,a,b):
    answer = 0
    
    def partner(n):
        if n % 2:
            return n + 1    
        return n - 1
    
    def get_even(n):
        if n % 2:
            return n + 1
        return n

    while True:
        answer += 1
        
        if partner(a) == b:
            return answer
        
        a = get_even(a) // 2
        b = get_even(b) // 2
        

    return answer

