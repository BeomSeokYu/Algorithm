# 재귀 PyPy3 제출

import sys
input = sys.stdin.readline

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    cnt = 0
    f = [0] * (n+1)
    for i in range(3, n+1):
        cnt += 1
        f[i] = f[i - 1] + f[i - 2]
    return cnt

n = int(input())

print(fib(n), fibonacci(n))