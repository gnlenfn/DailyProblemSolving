import sys
input = sys.stdin.readline

def check(year):
    if year % 400 == 0:
        return 1
    
    elif year % 100 == 0:
        return 0
    
    elif year % 4 == 0:
        return 1
    
    return 0


n = int(input().strip())
print(check(n))
