def solution(keyinput, board):
    answer = [0, 0]
    x_lim, y_lim = board[0] // 2, board[1] // 2
    for i in keyinput:
        if i == "left":
            answer[0] -= 1
            if answer[0] < -x_lim:
                answer[0] = -x_lim
        elif i == "right":
            answer[0] += 1
            if answer[0] > x_lim:
                answer[0] = x_lim
        elif i == "up":
            answer[1] += 1
            if answer[1] > y_lim:
                answer[1] = y_lim
        elif i == "down":
            answer[1] -= 1
            if answer[1] < -y_lim:
                answer[1] = -y_lim
    return answer