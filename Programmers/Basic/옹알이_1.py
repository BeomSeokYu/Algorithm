def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        idx = 0
        li = list(i)
        while idx < 4:
            if li[:len(can[idx])] == list(can[idx]):
                li = li[len(can[idx]):]
                idx = 0
            else:
                idx += 1
        if li == []:
            answer += 1
    return answer