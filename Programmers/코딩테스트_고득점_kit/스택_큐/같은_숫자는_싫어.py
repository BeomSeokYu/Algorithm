from collections import deque

def solution(arr):
    answer = []
    preNum = -1
    q = deque(arr)
    while q:
        temp = q.popleft()
        if preNum < 0 or preNum != temp:
            answer.append(temp)
        preNum = temp
    return answer