def solution(polynomial):
    answer = ''
    num = polynomial.split(' + ')
    n = []
    x = []
    for i in num:
        try:
            n.append(int(i))
        except ValueError:
            if i == 'x':
                x.append(1)
            else:
                x.append(int(i[:-1]))
    sum_n = sum(n)
    sum_x = sum(x)
    if sum_x != 0:
        answer += 'x' if sum_x == 1 else str(sum_x) + 'x'
    if sum_n != 0:
        if sum_x != 0:
            answer += ' + '
        answer += str(sum_n)
    return answer