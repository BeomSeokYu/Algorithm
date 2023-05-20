def solution(n):
    answer = 2
    q_set = []
    for i in range(1, 1001):
        q_set.append(i ** 2)
    q_set = set(q_set)
    if n in q_set:
        answer = 1
    return answer