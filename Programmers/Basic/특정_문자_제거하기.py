def solution(my_string, letter):
    answer = ''
    letter_idx = []
    for i in range(len(my_string)):
        if my_string[i] == letter:
            letter_idx.append(i)
    letter_idx.sort(reverse=True)
    my_string = list(my_string)
    for i in letter_idx:
        my_string.pop(i)
    for i in my_string:
        answer += i
    return answer