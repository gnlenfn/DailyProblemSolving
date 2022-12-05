import re

def solution(dartResult):
    answer = []
    result = re.findall(r'\d+[A-Z][#*]?', dartResult)
    bonus = {"S": 1, "D": 2, "T": 3}
    option = {"*": 2, "#": -1}
    
    for idx, ret in enumerate(result):
        digit = re.search(r"\d+", ret).group()
        bon = re.search(r"[A-Z]", ret).group()
        is_opt = re.search(r"[#*]", ret)
        opt = is_opt.group() if is_opt else None
        
        score = int(digit) ** bonus[bon]
        answer.append(score)
        if opt:
            if opt == "#":
                answer[idx] *= -1
            else:
                answer[idx] *= 2
                if idx > 0:
                    answer[idx - 1] *= 2

    return sum(answer)