def solution(quiz):
    answer = []
    for i in quiz:
        s, ans = i.split(' = ')
        if eval(s) == int(ans):
            answer.append("O")
        else:
            answer.append("X")
    return answer