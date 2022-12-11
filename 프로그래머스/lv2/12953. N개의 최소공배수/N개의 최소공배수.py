from functools import reduce

def solution(arr):    
    return reduce(lcm , arr, 1)

def euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(x, y):
    return x * y / euclidean(x, y)