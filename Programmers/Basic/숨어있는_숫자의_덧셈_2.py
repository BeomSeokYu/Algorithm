def solution(my_string):
    answer = 0
    temp = ''
    num = []
    for i in list(my_string):
        try:
            int(i)
            temp += i
        except ValueError:
            if temp != '':
                num.append(int(temp))
                temp = ''
    if temp != '':
        num.append(int(temp))
    answer = sum(num)
    return answer