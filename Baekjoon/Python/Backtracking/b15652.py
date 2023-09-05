import sys

input = sys.stdin.readline

N, M = map(int, input().split())

result = [1] * M
loop = True
while loop:
    print(*result, sep=" ")
    result[-1] += 1
    for i in range(M - 1, -1, -1):
        if i == 0 and result[i] > N:
            loop = False
            break
        if result[i] > N:
            result[i - 1] += 1
            for j in range(i, M):
                result[j] = result[i - 1]