from collections import Counter

def solution(k, tangerine):
    answer = 0
    ret = list(Counter(tangerine).items())
    ret.sort(key=lambda x : x[1], reverse=True)
    for key, val in ret:
        answer += 1
        k -= val

        if k <= 0:
            return answer
    return answer