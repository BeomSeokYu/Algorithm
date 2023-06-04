def solution(spell, dic):
    answer = 2
    for d in dic:
        li = list(d)
        for s in spell:
            try:
                li.remove(s)
            except ValueError:
                li.append(s)
        if (len(li) == 0):
            answer = 1
            break
    return answer