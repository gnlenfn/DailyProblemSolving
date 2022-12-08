
def solution(n, k):
    answer = []
    target = [n for n in range(1, n + 1)]
    k -= 1
    
    for num in range(n, 0, -1):
        split_num = fact(num) // num
        answer.append(target[k // split_num])
        target.pop(k // split_num)
        
        k %= split_num

    
    
    return answer

def fact(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    
    return ret