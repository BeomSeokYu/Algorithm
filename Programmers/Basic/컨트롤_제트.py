def solution(s):
    answer = 0
    s_li = s.split()
    for i in range(len(s_li)):
        if s_li[i] == 'Z':
            answer -= int(s_li[i - 1])
        else:
            answer += int(s_li[i])
    return answer