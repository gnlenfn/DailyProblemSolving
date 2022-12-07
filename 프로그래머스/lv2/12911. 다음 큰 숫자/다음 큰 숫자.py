def solution(n):
    answer = 0
    num = bin(n).count("1")
    
    for i in range(n + 1, 1_000_001):
        target = bin(i)
        if target.count("1") == num:
            return i
