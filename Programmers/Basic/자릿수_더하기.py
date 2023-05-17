def solution(n):
    answer = 0
    n_li = []
    while n != 0:
        n_li.append(n % 10)
        n = n // 10
    answer = sum(n_li)
    return answer