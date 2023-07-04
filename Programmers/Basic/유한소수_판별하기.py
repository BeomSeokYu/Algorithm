def irreducible(c, p):
    div = min(c, p)
    while div > 1:
        if c % div == 0 and p % div == 0:
            c = c // div
            p = p // div
            div = min(c, p)
        else:
            div -= 1
    return c, p

def isFinite(c, p):
    c, p = irreducible(c, p)
    while True:
        if p % 2 == 0:
            p /= 2
        elif p % 5 == 0:
            p /= 5
        else:
            if p == 1:
                return 1
            else:
                return 2

def solution(a, b):
    return isFinite(a, b)