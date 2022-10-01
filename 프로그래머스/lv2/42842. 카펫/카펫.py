def solution(brown, yellow):   
    for i in range(1, int(yellow ** (1/2)) + 1):
        if not yellow % i :
            a, b = i, yellow // i
            
            if (a + 2) * (b + 2) - yellow == brown:
                return [max(a + 2, b + 2), min(a + 2, b + 2)]
