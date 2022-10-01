from itertools import permutations

def solution(numbers):
    answer = 0
    visit = set()
    for k in range(1, len(numbers) + 1):
        for n in permutations(list(numbers), k):            
            num = int("".join(n))
            
            if num not in visit and prime(num):
                answer += 1
                visit.add(num)

    return answer

def prime(n):
    if n in [0, 1]:
        return False
    
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    
    return True
    