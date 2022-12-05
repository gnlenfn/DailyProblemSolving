from collections import defaultdict

def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    dict1, dict2 = defaultdict(int), defaultdict(int)
    
    # 두 글자 단위
    for i in range(len(str1) - 1):
        a, b = str1[i], str1[i+1]
        if not a.isalpha() or not b.isalpha():
            continue

        dict1[a + b] += 1
    
    for i in range(len(str2) - 1):
        a, b = str2[i], str2[i+1]
        if not a.isalpha() or not b.isalpha():
            continue

        dict2[a + b] += 1 
    
    # 교집합
    intersection = 0
    for key in dict1.keys():
        if key in dict2.keys():
            intersection += min(dict1[key], dict2[key])
    
    # 합집합 길이는 전체 길이 - 교집합 길이
    union = sum(dict1.values()) + sum(dict2.values()) - intersection
    
    print(intersection, union)
    print(dict1, dict2)
    if intersection == union == 0:
        answer = 1
    else: 
        answer = (intersection / union) 
        
    return int(answer * 65536)