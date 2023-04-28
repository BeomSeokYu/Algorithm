def solution(price):
    answer = 0
    if price >= 500000:
        answer = int(price - (price / 100 * 20))
    elif price >= 300000:
        answer = int(price - (price / 100 * 10))
    elif price >= 100000:
        answer = int(price - (price / 100 * 5))
    else:
        answer = price
    return answer