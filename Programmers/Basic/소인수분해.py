def solution(n):
    answer = []
    for j in range(2, n + 1):
        while n % j == 0 and j > 1:
            answer.append(j)
            n = n // j
    answer = sorted(list(set(answer)))
    return answer