def solution(clothes):
    clothes_num = {}
    answer = 1
    for i in clothes:
        if i[1] not in clothes_num:
            clothes_num[i[1]] = 2 # 안 입었을 경우 +1
        else:
            clothes_num[i[1]] += 1
    for i in clothes_num.values():
        answer *= i
    return answer - 1		# 모두 안입었을 경우 하나 빼줌