def solution(my_string, num1, num2):
    answer = ''
    str_li = list(my_string)
    temp = str_li[num1]
    str_li[num1] = str_li[num2]
    str_li[num2] = temp
    for i in str_li:
        answer += i
    return answer