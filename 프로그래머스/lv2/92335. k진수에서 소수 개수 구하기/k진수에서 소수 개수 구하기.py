def notation(n, q):
    rev = ""
    while n > 0:
        n, mod = divmod(n, q)
        rev += str(mod)
        
    return rev[::-1]

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** (1/2)) + 1):
        if num % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    
    trans_num = notation(n, k)
    primes = trans_num.split("0")
    for t in primes:
        if t and is_prime(int(t)):
            answer += 1            
    
    return answer