import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return int((a * b) / gcd(max(a, b), min(a, b)))

a, b = map(int, input().split())
print(lcm(a, b))