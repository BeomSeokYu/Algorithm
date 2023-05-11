def solution(array, n):
    answer = 0
    diff = 101
    array.sort()
    for i in array:
        num = abs(n - i)
        if num == diff:
            continue
        elif num < diff:
            diff = num
            answer = i
    return answer