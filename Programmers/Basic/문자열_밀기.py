from collections import deque

def solution(A, B):
    answer = 0
    aq = deque(A)
    blist = list(B)
    for i in range(len(aq)):
        if list(aq) == blist:
            break
        aq.appendleft(aq.pop())
        answer += 1
    if answer == len(aq):
        answer = -1
    return answer