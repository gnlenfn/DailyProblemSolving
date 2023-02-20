import sys
input = sys.stdin.readline

string = input()

tmp = ""
ret = 0
is_minus = False
for s in string:
    if s.isnumeric():
        tmp += s
    
    elif s == "+" and is_minus:
        ret -= int(tmp)
        tmp = ""
        
    elif s == "+" and not is_minus:
        ret += int(tmp)
        tmp = ""

    elif s == "-" and is_minus:
        ret -= int(tmp)
        tmp = ""

    elif s == "-" and not is_minus:
        ret += int(tmp)
        is_minus = True
        tmp = ""

if is_minus:
    ret -= int(tmp)
else:
    ret += int(tmp)

print(ret)