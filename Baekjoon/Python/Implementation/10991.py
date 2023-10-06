import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    for j in range(N - i - 1):
        print(' ', end='')
    for k in range(1, i * 2 + 2):
        if k % 2 == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print()