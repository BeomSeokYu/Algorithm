def solution(numbers):
    answer = 0
    num_dict = {
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    num_str = ''
    answer_str = ''
    for i in list(numbers):
        num_str += i
        if len(num_str) > 2 and num_str in num_dict.keys():
            answer_str += num_dict[num_str]
            num_str = ''
    answer = int(answer_str)
    return answer