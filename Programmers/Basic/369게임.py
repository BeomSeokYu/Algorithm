def solution(order):
    answer = 0
    while order != 0:
        t = order % 10
        order = order // 10
        if t in [3, 6, 9]:
            answer += 1
    return answer