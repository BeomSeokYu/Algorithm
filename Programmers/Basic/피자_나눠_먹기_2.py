import math

def gcd(a, b):
    if b == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b)//gcd(a, b)

def solution(n):
    answer = math.ceil(lcm(max(6, n), min(6, n))/6)
    return answer