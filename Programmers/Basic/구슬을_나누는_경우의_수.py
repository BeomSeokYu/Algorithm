'''
n개중 r개의 구슬을 고르는 경우의 수 - 조합
nCr = n!/{(n - r)! * r!}
'''
def factorial(n, s):
    result = 1
    for i in range(s, n + 1):
        result *= i
    return result

def solution(balls, share):
    answer = factorial(balls, 2) / (factorial(balls - share, 2) * factorial(share, 2))
    return answer