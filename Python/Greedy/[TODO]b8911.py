import sys
input = sys.stdin.readline

def changeDirection(d, direc):
    if d == 'L':
        direc -= 1
        if direc < 0:
            direc = 3
    else:
        direc += 1
        if direc > 3:
            direc = 0
    return direc

def moveAndMemo(x, y, _max, dir):
    if direc == 0:
        y += dir
        _max[0], _max[2] = max(_max[0], y), min(_max[2], y)
    elif direc == 1:
        x += dir
        _max[1], _max[3] = max(_max[1], x), min(_max[3], x)
    elif direc == 2:
        y -= dir
        _max[0], _max[2] = max(_max[0], y), min(_max[2], y)
    elif direc == 3:
        x -= dir
        _max[1], _max[3] = max(_max[1], x), min(_max[3], x)
    return x, y, _max

for i in range(int(input())):

    x, y = 0, 0                  # x, y
    _max = [0, 0, 0, 0]          # y, x, -y, -x
    direc = 0                    # top left bottom right

    for s in input().rstrip():
        if s == 'F':
            x, y, _max = moveAndMemo(x, y, _max, 1)
        elif s == 'B':
            x, y, _max = moveAndMemo(x, y, _max, -1)
        else:
            direc = changeDirection(i, direc)
    print((_max[0]+_max[2])*(_max[1]+_max[3]))