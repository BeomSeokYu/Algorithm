def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for i in my_string:
        if i in vowel:
            continue
        answer += i
    return answer