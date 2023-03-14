import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return gcd(b, a%b)

c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())
cr, cp = (c1 * p2) + (c2 * p1), p1 * p2

while True:
    gcdNum = gcd(max(cr, cp), min(cr, cp))
    if gcdNum == 1:
        break
    cr, cp = (cr // gcdNum), (cp // gcdNum)
print(cr, cp)