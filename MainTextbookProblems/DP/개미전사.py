import sys
input = sys.stdin.readline

'''
1. (i - 1)번째 식량창고를 털기로 결정한 경우 현재의 식량 창고를 털 수 없다
2. (i - 2)번째 식량창고를 털기로 결졍한 경우 현재의 식량 창고를 털 수 있다
'''

n = int(input())
k = list(map(int, input().split()))

d = [0] * n
d[0], d[1] = k[0], max(k[0],k[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + k[i])
print(d[n-1])