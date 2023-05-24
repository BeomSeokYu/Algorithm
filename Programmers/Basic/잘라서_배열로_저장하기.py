def solution(my_str, n):
    answer = []
    ms_li = list(my_str)
    temp = ''
    cnt = 0
    for i in ms_li:
        temp += i
        cnt += 1
        if cnt == n:
            answer.append(temp)
            temp = ''
            cnt = 0
    if len(temp) > 0:
        answer.append(temp)
    return answer