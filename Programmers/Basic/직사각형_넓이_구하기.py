def solution(dots):
    answer = 0
    x = set()
    y = set()
    for i, j in dots:
        x.add(i)
        y.add(j)
    x = list(x)
    y = list(y)
    x_len = abs(x[0] - x[1])
    y_len = abs(y[0] - y[1])
    answer = x_len * y_len
    return answer