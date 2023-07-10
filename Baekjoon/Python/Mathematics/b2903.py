import sys
input = sys.stdin.readline

'''
다음 한 변의 점의 갯수
n' = (2n - 1)^2
'''
x = 2
n = int(input())
for i in range(n):
    x = (x * 2) - 1
print(x ** 2)