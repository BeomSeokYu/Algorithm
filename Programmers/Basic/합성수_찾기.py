def solution(n):
    answer = 0
    for i in range(2, n + 1):
        cnt = 1
        for j in range(2, n + 1):
            while i % j == 0 and i > 1:
                i = i // j
                cnt += 1
        if cnt > 2:
            answer += 1
    return answer