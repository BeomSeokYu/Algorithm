def solution(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        for s in list(str(n)):
            if s == str(k):
                answer += 1
    return answer