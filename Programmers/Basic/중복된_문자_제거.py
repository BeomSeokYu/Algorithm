from collections import Counter

def solution(my_string):
    answer = ''
    cnt = dict(Counter(list(my_string)))
    for i in cnt:
        answer += i
    return answer