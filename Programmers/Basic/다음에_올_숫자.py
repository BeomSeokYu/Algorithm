def solution(common):
    answer = 0
    case1 = common[1] - common[0]
    case2 = common[2] - common[1]
    if case1 == case2:
        # 등차
        answer = common[0] + (case1 * len(common))
    else:
        # 등비
        r = common[1] // common[0]
        answer = common[0]
        for i in range(len(common)):
            answer *= r
    return answer