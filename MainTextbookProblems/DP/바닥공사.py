import sys
input = sys.stdin.readline

'''
1. 왼쪽부터 i - 1까지 길이가 덮개로 이미 채워져 있으면 2 * 1 덮개를 하나 채우는 경우 존재
2. 왼쪽부터 i - 2까지 길이가 덮개로 이미 채워져 있으면 1 * 2 덮개 2개는 넣는 경우, 혹은 2 * 2 덮개 하나를 넣는 경우 2가지 존재
'''

n = int(input())

d = [0] * (n + 1)
d[1], d[2] = 1, 3

if n > 2:
    for i in range(3, n + 1):
        d[i] = d[i - 1] + (d[i - 2] * 2)
print(d[n]%796796)