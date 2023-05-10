def solution(sides):
    answer = 0
    max_idx = 0
    for i in range(1, len(sides)):
        if sides[max_idx] < sides[i]:
            max_idx = i
    if sum(sides) - (sides[max_idx] * 2) < 1:
        answer = 2
    else:
        answer = 1
    return answer