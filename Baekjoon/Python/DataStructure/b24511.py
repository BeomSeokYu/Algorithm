import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

q = deque()
for i in range(N):
    if A[N - i - 1] == 0:
        q.appendleft(B[N - i - 1])

for j in C:
    q.appendleft(j)
    print(q.pop(), end=' ')