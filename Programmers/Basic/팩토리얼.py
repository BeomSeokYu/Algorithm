def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def solution(n):
    answer = 0
    for i in range(1, 11):
        num = factorial(i)
        if num > n:
            break
        answer = i
    return answer