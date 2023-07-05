def solution(num, total):
    answer = []
    target = total // num
    start = target - (num // 2)
    end = target + (num // 2) + 1
    if num % 2 == 0:
        start += 1
    answer = list(range(start, end))
    return answer