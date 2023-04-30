def solution(my_string):
    my_string = list(my_string)
    answer = ''
    s = 0
    e = len(my_string) - 1
    while s <= e:
        temp = my_string[s]
        my_string[s] = my_string[e]
        my_string[e] = temp
        s += 1
        e -= 1
    for i in my_string:
        answer += i
    return answer