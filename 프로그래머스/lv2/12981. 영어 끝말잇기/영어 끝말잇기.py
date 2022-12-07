from collections import defaultdict

def solution(n, words):
    num = defaultdict(int)
    dic = []
    
    idx = 1
    for word in words:
        idx = idx % n
        if not idx:
            idx = n
        
        if dic and word[0] != dic[-1][-1]:
            return [idx, num[idx] + 1]
        
        if word in dic:
            return [idx, num[idx] + 1]
        
        dic.append(word)
        num[idx] += 1
        idx += 1
        
    return [0, 0]