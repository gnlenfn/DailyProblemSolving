// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/176962

from collections import deque

def solution(plans):
    answer = []
    # 시간 계산 편하게 하기 위해 모두 분으로 바꾸기
    for idx, (_, start, _) in enumerate(plans):
        h, m = map(int, start.split(":"))
        s = 60 * h + m
        plans[idx][1] = s
    
    # 시작 시간 순서대로 정렬
    plans = sorted(plans, key=lambda x: x[1])
    plans = deque(plans)
    stack = []  # 멈춘 과제들 저장
    while plans:
        if len(plans) > 1:
            cur, nxt = plans[0], plans[1]
            cur_end = cur[1] + int(cur[2])  # 시작시간 + 걸리는 시간 = 끝나는 시간
            
            # 시간 안에 과제 끝낼 수 있어
            if cur_end <= nxt[1]: # 다음 과제의 시작시간보다 끝나는 시간이 작거나 같음
                answer.append(cur[0])
                plans.popleft()
                tmp = nxt[1] - cur_end  # 다음 과제 까지 남은 시간
                while stack: 
                    if stack[-1][0] <= tmp:  # 남은 시간 동안 중단된 것 클리어 가능
                        tmp -= stack[-1][0]
                        answer.append(stack.pop()[1])  # 중단됐던 것 끝내고 answer에 append
                    else:
                        stack[-1][0] -= tmp  # 수행한 시간 만큼 빼고 그대로 보관
                        break
                        
                    
            else:
                # 도중에 새 과제 해야함
                stack.append([cur_end - nxt[1], cur[0]])
                plans.popleft()
            
        else:
            answer.append(plans[0][0])
            plans.popleft()

    while stack:
        answer.append(stack.pop()[1])
        
    return answer
