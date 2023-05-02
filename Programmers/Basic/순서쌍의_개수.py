'''
    두 수의 곱이 n이기 위한 조건
    1 * n / 1
    2 * n / 2
    3 * n / 3
    4 * n / 4
    ...
    n * 1
'''
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += 1
    return answer