import sys
input = sys.stdin.readline

money = int(input().strip())
price = list(map(int, input().strip().split()))

def bnp():
    cash, stock = money, 0
    for p in price:
        if cash:
            tmp =  cash // p
            cash -= tmp * p
            stock += tmp
        
    return stock * price[-1] + cash


def timing():
    cash, stock = money, 0
    inc, dec = 0, 0
    for idx, p in enumerate(price):
        if not idx:
            continue

        if price[idx - 1] < p:  # 상승
            inc += 1
            dec = 0
        elif price[idx - 1] > p:  # 하락
            dec += 1
            inc = 0
        else:  # 횡보
            inc = 0
            dec = 0

        if inc >= 3 and stock:  # 3일 연속 상승 -> 풀매도
            cash += stock * p
            stock = 0

        if dec >= 3 and cash >= p:  # 3일 연속 하락 -> 풀매수
            stock += cash // p
            cash -= (cash // p) * p

    return stock * price[-1] + cash

jun = bnp()
sung = timing()

if jun > sung:
    print("BNP")
elif jun < sung:
    print("TIMING")
else:
    print("SAMESAME")
