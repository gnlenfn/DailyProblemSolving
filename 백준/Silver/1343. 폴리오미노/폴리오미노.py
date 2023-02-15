import sys
input = sys.stdin.readline

target = input().strip()  # 개행문자가 문제였음

idx = 0
while idx < len(target):
    if target[idx: idx+4] == "XXXX":
        target = target.replace("X", "A", 4)
        idx += 4
    
    elif target[idx: idx+2] == "XX":
        target = target.replace("X", "B", 2)
        idx += 2
    
    elif target[idx] == ".":
        idx += 1
    
    else:
        target = -1
        break


print(target)

