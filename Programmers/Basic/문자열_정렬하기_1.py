def solution(my_string):
    num_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = []
    for i in my_string:
        if i in num_str:
            answer.append(int(i))
    return sorted(answer)