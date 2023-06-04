def solution(n):
    answer = 0
    while n != 0:
        answer += 1
        if answer % 3 == 0:
            continue
        elif '3' in list(str(answer)):
            continue
        n -= 1
    return answer