def solution(num, k):
    answer = -1
    num_li = []
    while num != 0:
        num_li.insert(0, num % 10)
        num = num // 10
    for i in range(len(num_li)):
        if num_li[i] == k:
            answer = i + 1
            break
    return answer