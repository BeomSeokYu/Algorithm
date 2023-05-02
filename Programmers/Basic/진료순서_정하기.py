def solution(emergency):
    answer = []
    sorted_emer = sorted(emergency, reverse=True)
    pri_dict = {}
    for i in range(len(sorted_emer)):
        pri_dict[sorted_emer[i]] = i + 1
    for i in emergency:
        answer.append(pri_dict[i])
    return answer