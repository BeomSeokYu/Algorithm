def solution(numer1, denom1, numer2, denom2):
    answer = []
    p = denom1 * denom2
    c = (numer1 * denom2) + (numer2 * denom1)

    while True:
        g = gcd(max(p, c), min(p, c))
        if g == 1:
            break
        c = c // g
        p = p // g
    answer.append(c)
    answer.append(p)
    return answer

def gcd(a, b):
    if b == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return gcd(b, a%b)