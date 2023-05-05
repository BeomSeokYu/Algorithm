def solution(numbers, k):
    answer = 0
    max_len = len(numbers)
    idx = 0
    for i in range(k-1):
        idx += 2
        if idx == max_len:
            idx = 0
        elif idx > max_len:
            idx = 1
    answer = idx + 1
    return answer