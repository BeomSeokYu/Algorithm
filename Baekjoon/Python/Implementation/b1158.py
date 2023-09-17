import sys
input = sys.stdin.readline

N, K = map(int, input().split())

li = [i for i in range(1, N + 1)]
cur = 0
result = []
while li:
    cur += K - 1
    if cur >= len(li):
        cur %= len(li)
    result.append(li.pop(cur))
print('<', end='')
print(*result, sep=', ', end='')
print('>')