import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
d = [1] * (n + 1)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j] + 1)
_max = max(d)
print(_max)