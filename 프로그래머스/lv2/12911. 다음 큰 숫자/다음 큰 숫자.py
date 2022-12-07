def solution(n):
    answer = 0
    num = bin(n).count("1")
    
    for idx in range(n + 1, 1_000_001):
        if bin(idx).count("1") == num:
            return idx
