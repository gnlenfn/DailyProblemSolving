def solution(elements):
    answer = set()
    target = elements + elements
        
    for n in range(1, len(elements) + 1):
        left = 0
        right = left + n
        
        while right < len(target):
            answer.add(sum(target[left: right]))
            left += 1
            right += 1
        
    return len(answer)