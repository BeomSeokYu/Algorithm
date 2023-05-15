from collections import Counter

def solution(s):
    answer = ''
    answer_li = []
    s_dict = dict(Counter(s))
    for i in s_dict:
        if s_dict[i] == 1:
            answer_li.append(i)
    answer_li.sort()
    for i in answer_li:
        answer += i
    return answer