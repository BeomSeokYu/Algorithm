'''
어떤 선분과 겹치는지 판단하는 방법
- 해당 선분 범위에 다른 선분의 시작점 또는 끝점이 있음
'''
def solution(lines):
    answer = 0
    a = list(range(lines[0][0]-100, lines[0][1]-100))
    b = list(range(lines[1][0]-100, lines[1][1]-100))
    c = list(range(lines[2][0]-100, lines[2][1]-100))
    temp = [0] * 201
    for li in (a, b, c):
        for i in li:
            temp[i] += 1
    for i in temp:
        if i > 1:
            answer += 1
    return answer