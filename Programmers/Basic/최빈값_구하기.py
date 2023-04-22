from collections import Counter

def solution(array):
    answer = 0
    d = dict(Counter(array))
    pre = 0
    for i in d:
        if pre < d[i]:
            answer = i
            pre = d[i]
        elif pre == d[i]:
            answer = -1
    return answer