import sys
input = sys.stdin.readline

result = 0

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
for i in range(n):
    result += a[i] * b[i]
print(result)