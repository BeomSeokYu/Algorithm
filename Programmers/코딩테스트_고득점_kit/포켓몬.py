def solution(nums):
    n = len(nums) // 2
    type_len = len(set(nums))
    answer = min(n, type_len)
    return answer