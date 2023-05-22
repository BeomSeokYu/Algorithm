def solution(my_string):
    answer = ''
    ms_li = list(my_string)
    for i in range(len(ms_li)):
        if 97 > ord(ms_li[i]):
            ms_li[i] = chr(ord(ms_li[i]) + 32)
    ms_li.sort()
    for i in ms_li:
        answer += i
    return answer