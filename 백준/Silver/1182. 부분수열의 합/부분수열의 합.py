from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

def recur(k, value):
    if k == n:
        global answer
        if value == s:
            answer += 1
    
    else:
        recur(k + 1, value + nums[k])
        recur(k + 1, value)

recur(0, 0)
if s == 0:
    answer -= 1
    
print(answer)