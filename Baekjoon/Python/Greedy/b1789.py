import sys
input = sys.stdin.readline
'''
s = n * (n + 1) / 2 가 되는 n이 있다면 그것이 최댓값
넘을 경우 n - 1이 될 것
'''
s = int(input())
n = 1
sum = 1
while s > sum:
    n += 1
    sum += n
print(n) if s == sum else print((n - 1))