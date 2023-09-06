import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = list(map(int, input().split()))
preSum = [0] * (N + 1)
for i in range(N):
    preSum[i + 1] = preSum[i] + li[i]
for x in range(M):
    i, j = map(int, input().split())
    print(preSum[j] - preSum[i - 1])