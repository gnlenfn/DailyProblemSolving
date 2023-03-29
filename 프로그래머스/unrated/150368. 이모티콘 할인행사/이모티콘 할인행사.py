from itertools import product

def solution(users, emoticons):
    plus_ret, profit_ret = 0, 0  # 최종 플러스 가입자 수, 최종 이모티콘 판매 수익
    discounts = product([10, 20, 30, 40], repeat=len(emoticons))  # 모든 할인율 중복 순열
    for dc in discounts:
        plus_users = 0  # 이번 할인 케이스의 플러스 가입자 수
        profit = 0      # 이번 할인 케이스의 총 이모티콘 매출

        for threshold, plus_limit in users:
            # 유저 한 명씩 순회
            paid = 0

            for i in range(len(emoticons)):
                # 이번 할인 상황에 맞게 유저 한 명 구매 결과 확인
                if dc[i] >= threshold:  # 할인율이 원하는 것 이상
                    paid += emoticons[i] * (100 - dc[i]) // 100  # 정수로 쓸라고 
                
            if paid >= plus_limit:  # 기준치 이상 이모티콘 샀음 -> 플러스로 전환
                paid = 0
                plus_users += 1
            else:                   # 그냥 이모티콘 구매
                profit += paid

        if plus_ret < plus_users:  # 이모티콘 플러스 가입자 늘었음!
            plus_ret = plus_users
            profit_ret = profit
        
        elif plus_ret == plus_users and profit_ret < profit:  # 최대 이익 더 큰 경우
            profit_ret = profit

    return [plus_ret, profit_ret]