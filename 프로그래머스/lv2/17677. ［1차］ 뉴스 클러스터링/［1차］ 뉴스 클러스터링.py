from collections import Counter

def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    
    dict1 = Counter([str1[i: i+2] for i in range(len(str1) - 1) if str1[i: i+2].isalpha()])
    dict2 = Counter([str2[i: i+2] for i in range(len(str2) - 1) if str2[i: i+2].isalpha()])

    union = sum((dict1 | dict2).values())
    intersection = sum((dict1 & dict2).values())

    if union == 0:
        answer = 1
    else: 
        answer = (intersection / union) 
        
    return int(answer * 65536)