def solution(before, after):
    answer = 0
    after = list(after)
    for i in list(before):
        try:
            after.remove(i)
        except:
            break
    if len(after) == 0:
        answer = 1
    return answer