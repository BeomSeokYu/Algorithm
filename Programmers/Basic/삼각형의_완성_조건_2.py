def solution(sides):
    answer = 0
    _min = max(sides) - min(sides)
    _max = sum(sides)
    answer = _max - _min - 1
    return answer