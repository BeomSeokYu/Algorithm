from collections import Counter

def solution(participant, completion):
    answer = ''
    p = Counter(participant)
    c = Counter(completion)
    for i in participant:
        if p[i] != c[i]:
            answer = i
    return answer