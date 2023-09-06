import sys
input = sys.stdin.readline

N, K = map(int, input().split())
li = list(map(int, input().split()))
pre_sum = [0] * (N + 1)
for i in range(N):
    pre_sum[i + 1] = pre_sum[i] + li[i]

k_li = []
for i in range(N - K + 1):
    k_li.append(pre_sum[i + K] - pre_sum[i])

print(max(k_li))