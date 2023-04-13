// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/176962

from collections import deque

def solution(plans):
    answer = []
    for idx, (name, start, playtime) in enumerate(plans):
        h, m = map(int, start.split(":"))
        plans[idx][1] = h * 60 + m
    
    plans.sort(key=lambda x: x[1])
    plans = deque(plans)
    stop = []  # 도중에 중단된 작업들 저장
    while plans:
        if len(plans) < 2:
            answer.append(plans.popleft()[0])
        else:
            cur, nxt = plans[0], plans[1]
            cur_end = cur[1] + int(cur[2])  # 현재 작업이 끝나는 시간
            nxt_start = nxt[1]  # 다음 작업이 시작할 시간
            
            if cur_end <= nxt_start:  # 다음 작업 시작하기 전에 다 끝내기 가능
                answer.append(cur[0])
                plans.popleft()
                
                # stop 작업
                t = nxt_start - cur_end  # 다음 작업까지 남은 틈새 시간
                while stop:
                    if stop[-1][0] <= t:  # 틈새 시간동안 작업 끝내기 가능
                        poped = stop.pop()
                        t -= poped[0]
                        answer.append(poped[1])
                    
                    else:
                        stop[-1][0] -= t
                        break  # 하던거 멈추고 다음 작업 넘어가야 함
            
            else:
                # 작업 도중에 멈춰야 함
                left_time = cur_end - nxt_start
                stop.append([left_time, cur[0]])
                plans.popleft()
    
    while stop:
        answer.append(stop.pop()[1])  # 중단 됐던 거 남아있으면 가장 최근에 들어온 것 부터 마무리
        
    return answer