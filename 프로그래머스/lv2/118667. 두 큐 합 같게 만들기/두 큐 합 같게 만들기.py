from collections import deque

def solution(queue1, queue2):
    max_pop = max(len(queue1), len(queue2)) * 3
    queue1, queue2 = deque(queue1), deque(queue2)
    answer = 0
    
    sum1, sum2 = sum(queue1), sum(queue2)
    while sum1 != sum2:
        if sum1 > sum2:  # 1합이 더 크므로 1에서 pop
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum2 += tmp
            sum1 -= tmp
            answer += 1

        else:  # 2합이 더 크므로 2에서 pop
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            answer += 1

        if answer >= max_pop:
            return -1
        
    return answer