import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    for j in range(i):
        print(' ', end='')
    for k in range((N * 2) - 1 - (i * 2)):
        print('*', end='')
    print()
for i in range(1, N):
    for j in range(N - i - 1):
        print(' ', end='')
    for k in range(0, i * 2 + 1):
        print('*', end='')
    print()