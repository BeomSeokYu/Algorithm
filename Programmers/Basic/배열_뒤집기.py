def solution(age):
    answer = 2022
    while age > 1:
        answer -= 1
        age -= 1
    return answer