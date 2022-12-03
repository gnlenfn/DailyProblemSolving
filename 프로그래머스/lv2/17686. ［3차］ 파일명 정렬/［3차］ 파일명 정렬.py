def solution(files):
    answer = []
    arr = []
    for idx, file in enumerate(files):
        HEAD = ''
        for c in file:
            if c.isnumeric():
                break
            HEAD += c
        
        NUMBER = ''
        for n in file[len(HEAD):]:
            if not n.isnumeric():
                break
            NUMBER += n

        length = len(HEAD) + len(NUMBER)
        TAIL = file[length:]
        
        arr.append([HEAD, NUMBER, TAIL, idx])
        
    arr.sort(key=lambda x : (x[0].lower(), int(x[1]), x[3]))
    
    for parsed in arr:
        answer.append("".join(parsed[:-1]))
    return answer