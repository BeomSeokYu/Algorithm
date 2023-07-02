def solution(score):
    answer = [0] * len(score)
    info = []
    for i in range(len(score)):
        info.append([i, sum(score[i]) / 2])
    info.sort(key=lambda x:-x[1])

    rank = 1
    pre_score = -1
    pre_rank = -1
    for idx, avg in info:
        if pre_score != avg:
            pre_score = avg
            answer[idx] = pre_rank = rank
        else :
            answer[idx] = pre_rank
        rank += 1
    return answer