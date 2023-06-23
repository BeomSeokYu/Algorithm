def calIncl(dot1, dot2):
    x2 = max(dot1[0], dot2[0])
    x1 = min(dot1[0], dot2[0])
    y2 = max(dot1[1], dot2[1])
    y1 = min(dot1[1], dot2[1])
    return (y2 - y1) / (x2 - x1)

def solution(dots):
    case = [(0, 1, 2, 3),
            (0, 2, 1, 3),
            (0, 3, 1, 2),
            (1, 2, 0, 3),
            (1, 3, 0, 2),
            (2, 3, 0, 1)]
    answer = 0
    for d1, d2, d3, d4 in case:
        inc1 = calIncl(dots[d1], dots[d2])
        inc2 = calIncl(dots[d3], dots[d4])
        if(inc1 == inc2):
            answer = 1
            break
    return answer