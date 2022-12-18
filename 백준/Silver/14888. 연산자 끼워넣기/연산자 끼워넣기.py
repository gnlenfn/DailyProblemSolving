n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
min_val = float("inf")
max_val = float("-inf")

def calc(num1, op, num2):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    else:
        if num1 < 0:
            return -(abs(num1) // num2)
        return num1 // num2

def recur(k, val):
    if k == n-1:
        global min_val, max_val
        min_val = min(min_val, val)
        max_val = max(max_val, val)
    
    else:
        global ops
        for i in range(4):
            if ops[i] > 0:
                ops[i] -= 1
                recur(k + 1, calc(val, i, nums[k + 1]))
                ops[i] += 1

recur(0, nums[0])
print(max_val)
print(min_val)