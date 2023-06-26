'''
에라토스테네스의 체
- n 이하의 모든 소수를 구하려고 할 때, 효율적으로 구하기 위해 n의 제곱근( sqrt(n) ) 까지만 확인
'''
import sys
input = sys.stdin.readline

def primeTest(n):
    if n <= 1:
        return False                # 1은 소수가 아님
    if n % 2 == 0:                  # n이 짝수이면 소수에서 제외
        return True if n == 2 else False    # 단, n = 2이면 소수
    for i in range(3, int(n**(0.5))+1, 2): # n이 홀수인 경우 루트(n)까지 나누어 떨어지는 지 확인
        if n % i == 0:              # 나누어 떨어지면 약수에 해당하므로 소수가 아님
            return False
    return True

for i in range(int(input())):
    n = int(input())
    while True:
        if primeTest(n):
            break
        n += 1
    print(n)