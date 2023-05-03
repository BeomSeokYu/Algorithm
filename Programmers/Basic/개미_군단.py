def solution(hp):
    answer = 0
    for i in [5, 3, 1]:
        answer += hp // i
        hp %= i
    return answer