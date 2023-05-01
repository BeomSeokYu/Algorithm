def solution(n, k):
    answer = 0
    service = n // 10
    k -= service
    if k < 0:
        k = 0
    answer = n * 12000 + k * 2000
    return answer