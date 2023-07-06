def solution(numlist, n):
    answer = []
    slist = []
    for i in numlist:
        slist.append((abs(n - i), i))
    slist.sort(key=lambda x:(x[0],-x[1]))
    for i in slist:
        answer.append(i[1])
    return answer