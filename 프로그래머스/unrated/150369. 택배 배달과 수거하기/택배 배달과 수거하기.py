def solution(cap, n, deliveries, pickups):
    answer = 0
    deliv = 0
    pick = 0
    idx = n - 1

    for i in range(n - 1, -1, -1):
        # 뒤에서부터 현재까지 delivery, pickup 개수
        deliv += deliveries[i]
        pick += pickups[i]

        while deliv > cap or pick > cap:  # 기록한 택배 수가 cap 보다 많아지면 제거 시작
            deliv -= cap
            pick -= cap
            answer += (idx + 1) * 2  # 수거/배달이 진행되면 현재까지 방문한 가장 먼 집까지 거리 2배만큼 이동
            idx = i
    
    # 남은 것들 처리하려면 남은것들 중 가장 먼 집 까지 갔다오면 됨
    if deliv > 0 or pick > 0:
        answer += (idx + 1) * 2

    return answer
