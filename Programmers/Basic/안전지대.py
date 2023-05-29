def setDangerLocation(board, x, y, n):
    loc = [(x-1, y-1), (x, y-1), (x+1, y-1),
          (x-1, y), (x+1, y),
          (x-1, y+1), (x, y+1), (x+1, y+1)]
    for lx, ly in loc:
        if lx < 0 or lx >= n or ly < 0 or ly >= n:
            continue
        if board[lx][ly] != 1:
            board[lx][ly] = 2

def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                setDangerLocation(board, i, j, len(board[0]))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                answer += 1
    return answer