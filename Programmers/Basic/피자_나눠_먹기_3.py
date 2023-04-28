def solution(slice, n):
    answer = 1
    p = slice
    while p < n:
        p += slice
        answer += 1
    return answer