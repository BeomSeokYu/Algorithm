import sys
input = sys.stdin.readline

for _ in range(int(input())):
    result = [0, 0, 0, 0]
    coin = [25, 10, 5, 1]
    c = int(input())
    for i in range(len(coin)):
        result[i] = c // coin[i]
        c = c % coin[i]
    print(*result, sep=' ')