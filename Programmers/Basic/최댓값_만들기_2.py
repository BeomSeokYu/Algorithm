def solution(numbers):
    answer = 0
    numbers.sort()
    a = numbers[-1] * numbers[-2]
    b = numbers[0] * numbers[1]
    answer = max(a, b)
    return answer