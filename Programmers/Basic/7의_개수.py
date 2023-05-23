def solution(array):
    answer = 0
    for i in array:
        while i != 0:
            temp = i % 10
            if temp == 7:
                answer += 1
            i = i // 10
    return answer