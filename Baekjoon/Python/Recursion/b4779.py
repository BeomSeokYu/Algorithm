import sys

def cantorian(l, s, e):
    length = (e - s) // 3
    if length < 1:
        return
    mid_start = s + length
    for i in range(mid_start, mid_start + length):
        l[i] = ' '
    cantorian(l, s, s + length)
    cantorian(l, mid_start + length, e)

while True:
    try:
        l = ['-'] * (3 ** int(input()))
        cantorian(l, 0, len(l))

        print(*l, sep='')
    except EOFError:
        break